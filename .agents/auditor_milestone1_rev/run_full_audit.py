import os
import re
import subprocess
import sys
import urllib.parse
from markdown_it import MarkdownIt

REPO_ROOT = r"C:\Users\svhon\.gemini\antigravity\scratch\god-repo"

def make_anchor(header_text):
    anchor = header_text.lower().strip()
    cleaned = []
    for c in anchor:
        if c.isalnum() or c in (' ', '-', '_'):
            cleaned.append(c)
    anchor = "".join(cleaned)
    anchor = anchor.replace(' ', '-')
    return anchor

def get_modified_files():
    # Run git status / diff to get modified and untracked files
    modified = []
    try:
        # Check modified files in index / working tree
        out1 = subprocess.check_output(["git", "diff", "--name-only"], cwd=REPO_ROOT, text=True)
        modified.extend(out1.splitlines())
        
        # Check cached modified files (staged)
        out2 = subprocess.check_output(["git", "diff", "--cached", "--name-only"], cwd=REPO_ROOT, text=True)
        modified.extend(out2.splitlines())
        
        # Check untracked files
        out3 = subprocess.check_output(["git", "status", "--porcelain"], cwd=REPO_ROOT, text=True)
        for line in out3.splitlines():
            if line.startswith("?? "):
                path = line[3:]
                # If path is a directory (ends with /), list files inside it
                full_path = os.path.join(REPO_ROOT, path)
                if os.path.isdir(full_path):
                    for r, d, fs in os.walk(full_path):
                        for f in fs:
                            rel_f = os.path.relpath(os.path.join(r, f), REPO_ROOT)
                            modified.append(rel_f)
                else:
                    modified.append(path)
    except Exception as e:
        print(f"Error running git: {e}")
    
    # Filter unique, normalize, and exclude .agents, .git, ORIGINAL_REQUEST.md, PROJECT.md
    filtered = []
    for f in set(modified):
        f_norm = f.replace('/', os.sep)
        parts = f_norm.split(os.sep)
        if '.git' in parts or '.agents' in parts:
            continue
        if parts[-1] in ('ORIGINAL_REQUEST.md', 'PROJECT.md'):
            continue
        filtered.append(os.path.abspath(os.path.join(REPO_ROOT, f_norm)))
    return filtered

def find_all_markdown_files():
    md_files = []
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        parts = dirpath.split(os.sep)
        if '.git' in parts or '.agents' in parts:
            continue
        for f in filenames:
            if f.endswith('.md'):
                # Also filter out ORIGINAL_REQUEST.md and PROJECT.md
                if f not in ('ORIGINAL_REQUEST.md', 'PROJECT.md'):
                    md_files.append(os.path.abspath(os.path.join(dirpath, f)))
    return md_files

def get_anchors_and_links(file_path):
    md = MarkdownIt()
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    tokens = md.parse(content)
    
    anchors = set()
    links = []
    
    for token in tokens:
        if token.type == "heading_open":
            # The next token is usually the inline heading text
            # Let's find it in the sequence
            pass
        # To get heading text accurately, we can extract headers via regex or scan tokens
        if token.type == "inline" and token.children:
            # Check if parent is a heading
            # markdown-it headings: heading_open -> inline -> heading_close
            # Let's find headers by looking at markdown tokens
            pass

    # A simpler way to get headers is using regex since it matches markdown headings precisely
    # and generates their anchors:
    # E.g. lines starting with #
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            level = 0
            for c in line:
                if c == '#':
                    level += 1
                else:
                    break
            header_text = line[level:].strip()
            if header_text:
                # Remove markdown links if present in header, e.g. [some text](...) -> some text
                header_text_clean = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', header_text)
                anchors.add(make_anchor(header_text_clean))

    # Extract links from markdown-it tokens
    for token in tokens:
        if token.type == "inline" and token.children:
            in_link = False
            href = None
            text = []
            for child in token.children:
                if child.type == "link_open":
                    in_link = True
                    href = child.attrs.get("href", "")
                elif child.type == "link_close":
                    in_link = False
                    if href:
                        links.append(("".join(text), href))
                    text = []
                    href = None
                elif in_link:
                    if child.content:
                        text.append(child.content)
                elif child.type == "image":
                    src = child.attrs.get("src", "")
                    links.append((child.content or "image", src))
                    
    return anchors, links

def main():
    print("--- FORENSIC INTEGRITY AUDIT ---")
    modified_files = get_modified_files()
    all_files = find_all_markdown_files()
    
    print(f"Total markdown files in repository: {len(all_files)}")
    print(f"Modified/added markdown files: {len(modified_files)}")
    for f in modified_files:
        print(f"  - {os.path.relpath(f, REPO_ROOT)}")
        
    print("\n--- PHASE 1: Markdown Compilation Check ---")
    compile_failures = []
    for f in modified_files:
        try:
            md = MarkdownIt()
            with open(f, "r", encoding="utf-8") as file_obj:
                content = file_obj.read()
            md.parse(content)
            print(f"[PASS] {os.path.relpath(f, REPO_ROOT)} parses cleanly.")
        except Exception as e:
            print(f"[FAIL] {os.path.relpath(f, REPO_ROOT)} failed to parse: {e}")
            compile_failures.append((f, str(e)))
            
    print("\n--- PHASE 2: Relative Link and Anchor Check ---")
    # Gather anchors for all files in the repo
    all_anchors = {}
    all_links = {}
    for f in all_files:
        try:
            anchors, links = get_anchors_and_links(f)
            all_anchors[f] = anchors
            all_links[f] = links
        except Exception as e:
            print(f"Error parsing {f}: {e}")
            all_anchors[f] = set()
            all_links[f] = []
            
    broken_links = []
    for f, links in all_links.items():
        rel_f = os.path.relpath(f, REPO_ROOT)
        for text, url in links:
            if url.startswith(('http://', 'https://', 'mailto:', 'ftp://')):
                continue
            
            # Pure anchor link
            if url.startswith('#'):
                anchor = url[1:]
                if anchor not in all_anchors[f]:
                    broken_links.append({
                        'source': rel_f,
                        'text': text,
                        'url': url,
                        'reason': f"Anchor '{anchor}' not found in current file."
                    })
                continue
                
            parts = url.split('#')
            link_path = parts[0]
            link_anchor = parts[1] if len(parts) > 1 else None
            
            decoded_link_path = urllib.parse.unquote(link_path)
            target_dir = os.path.dirname(f)
            target_abs = os.path.abspath(os.path.join(target_dir, decoded_link_path))
            
            if not os.path.exists(target_abs):
                broken_links.append({
                    'source': rel_f,
                    'text': text,
                    'url': url,
                    'reason': f"Target file '{decoded_link_path}' does not exist."
                })
                continue
                
            if link_anchor and target_abs.endswith('.md'):
                if target_abs in all_anchors:
                    if link_anchor not in all_anchors[target_abs]:
                        broken_links.append({
                            'source': rel_f,
                            'text': text,
                            'url': url,
                            'reason': f"Anchor '{link_anchor}' not found in target file '{decoded_link_path}'."
                        })
                else:
                    broken_links.append({
                        'source': rel_f,
                        'text': text,
                        'url': url,
                        'reason': f"Target file '{decoded_link_path}' was not indexed."
                    })
                    
    if broken_links:
        print(f"[FAIL] Found {len(broken_links)} broken relative link(s):")
        for idx, bl in enumerate(broken_links, 1):
            print(f"  {idx}. File: {bl['source']}")
            print(f"     Text: {bl['text']}")
            print(f"     URL: {bl['url']}")
            print(f"     Reason: {bl['reason']}")
    else:
        print("[PASS] All relative links and anchors are fully resolved.")
        
    print("\n--- PHASE 3: Integrity Violation Check (Genuine Content vs Facades/Hardcoded Flags) ---")
    integrity_issues = []
    # Search for suspicious patterns or placeholder tags
    placeholder_patterns = [
        r'\[\s*TODO\s*\]',
        r'\[\s*PLACEHOLDER\s*\]',
        r'lorem\s+ipsum',
        r'test\s+passed',
        r'validation\s+ok',
        r'check\s+passed',
        r'success\s*=\s*true',
    ]
    
    # Also check if any modified file has empty or extremely small size
    for f in modified_files:
        rel_f = os.path.relpath(f, REPO_ROOT)
        size = os.path.getsize(f)
        if size == 0:
            integrity_issues.append((rel_f, "File is empty (size 0 bytes)"))
            continue
            
        with open(f, "r", encoding="utf-8") as file_obj:
            content = file_obj.read()
            
        # Check patterns
        for pattern in placeholder_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                integrity_issues.append((rel_f, f"Suspicious pattern '{pattern}' matched {len(matches)} time(s): {matches}"))
                
    if integrity_issues:
        print("[FAIL] Found potential integrity issues:")
        for file, issue in integrity_issues:
            print(f"  - File: {file} | Issue: {issue}")
    else:
        print("[PASS] No integrity violations or facade implementations detected.")
        
    print("\n--- SUMMARY OF RESULTS ---")
    verdict = "CLEAN"
    if compile_failures or broken_links or integrity_issues:
        verdict = "INTEGRITY VIOLATION"
        
    print(f"Verdict: {verdict}")
    sys.exit(0 if verdict == "CLEAN" else 1)

if __name__ == "__main__":
    main()
