import os
import re
import sys

REPO_ROOT = r"C:\Users\svhon\.gemini\antigravity\scratch\god-repo"

def make_anchor(header_text):
    # Strip leading/trailing whitespaces and lower case
    anchor = header_text.lower().strip()
    # Remove characters that are not alphanumeric, spaces, hyphens, or underscores
    # Note: GitHub markdown removes emojis and most punctuation
    cleaned = []
    for c in anchor:
        if c.isalnum() or c in (' ', '-', '_'):
            cleaned.append(c)
    anchor = "".join(cleaned)
    # Replace spaces with hyphens
    anchor = anchor.replace(' ', '-')
    return anchor

def get_headers_and_anchors(file_path):
    headers = []
    anchors = set()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#'):
                # Count the level
                level = 0
                for c in line:
                    if c == '#':
                        level += 1
                    else:
                        break
                header_text = line[level:].strip()
                if header_text:
                    headers.append((level, header_text))
                    anchor = make_anchor(header_text)
                    anchors.add(anchor)
    return headers, anchors

def find_markdown_files(root_dir):
    md_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Exclude .git and .agents
        if '.git' in dirpath.split(os.sep) or '.agents' in dirpath.split(os.sep):
            continue
        for f in filenames:
            if f.endswith('.md'):
                md_files.append(os.path.join(dirpath, f))
    return md_files

def extract_links(content):
    # Extract inline links [text](url)
    inline_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    # Extract reference links [label]: url
    ref_links = re.findall(r'^\[([^\]]+)\]:\s*(\S+)', content, re.MULTILINE)
    
    links = []
    for text, url in inline_links:
        links.append((text, url.strip()))
    for label, url in ref_links:
        links.append((label, url.strip()))
    return links

def main():
    print(f"Scanning repository at: {REPO_ROOT}")
    md_files = find_markdown_files(REPO_ROOT)
    print(f"Found {len(md_files)} markdown files.")
    
    # First, collect all files, headers, and anchors
    file_anchors = {}
    file_paths_set = set(os.path.abspath(f) for f in md_files)
    
    for f in md_files:
        abs_path = os.path.abspath(f)
        headers, anchors = get_headers_and_anchors(abs_path)
        file_anchors[abs_path] = anchors
        
    broken_links = []
    total_links_checked = 0
    
    for f in md_files:
        abs_path = os.path.abspath(f)
        rel_to_root = os.path.relpath(abs_path, REPO_ROOT)
        
        with open(abs_path, 'r', encoding='utf-8') as file_obj:
            content = file_obj.read()
            
        links = extract_links(content)
        for text, url in links:
            # Skip external links, mailto, etc.
            if url.startswith(('http://', 'https://', 'mailto:', 'ftp://')):
                continue
            
            # Skip pure anchor links if they check out in the same file
            if url.startswith('#'):
                anchor = url[1:]
                total_links_checked += 1
                if anchor not in file_anchors[abs_path]:
                    broken_links.append({
                        'file': rel_to_root,
                        'text': text,
                        'url': url,
                        'reason': f"Anchor '{anchor}' not found in current file."
                    })
                continue
                
            # Split file path and anchor
            parts = url.split('#')
            link_path = parts[0]
            link_anchor = parts[1] if len(parts) > 1 else None
            
            # Resolve target path relative to the file containing the link
            target_dir = os.path.dirname(abs_path)
            # URL decoding (e.g., %20 to space)
            import urllib.parse
            decoded_link_path = urllib.parse.unquote(link_path)
            
            target_abs_path = os.path.abspath(os.path.join(target_dir, decoded_link_path))
            
            total_links_checked += 1
            
            # Check if target file/directory exists
            if not os.path.exists(target_abs_path):
                broken_links.append({
                    'file': rel_to_root,
                    'text': text,
                    'url': url,
                    'reason': f"Target path '{decoded_link_path}' (resolved: '{target_abs_path}') does not exist."
                })
                continue
                
            # If target exists and there is an anchor, check the anchor in the target file
            if link_anchor:
                # If target is a directory, anchors don't make sense unless it has an index file,
                # but let's see. If target is a directory, it might resolve to its README.md or not.
                # Usually link should be to the markdown file directly.
                if os.path.isdir(target_abs_path):
                    broken_links.append({
                        'file': rel_to_root,
                        'text': text,
                        'url': url,
                        'reason': f"Link points to a directory '{decoded_link_path}' with an anchor '{link_anchor}'."
                    })
                elif target_abs_path.endswith('.md'):
                    if target_abs_path in file_anchors:
                        if link_anchor not in file_anchors[target_abs_path]:
                            # Try to generate potential anchor variants if it's slightly off
                            # e.g., github vs generic anchor
                            broken_links.append({
                                'file': rel_to_root,
                                'text': text,
                                'url': url,
                                'reason': f"Anchor '{link_anchor}' not found in target file '{decoded_link_path}'."
                            })
                    else:
                        # Should have been loaded, but check just in case
                        broken_links.append({
                            'file': rel_to_root,
                            'text': text,
                            'url': url,
                            'reason': f"Target file '{decoded_link_path}' is not indexed or read."
                        })

    print(f"\nChecked {total_links_checked} internal links.")
    if broken_links:
        print(f"FOUND {len(broken_links)} BROKEN LINKS:")
        for idx, bl in enumerate(broken_links, 1):
            print(f"{idx}. File: {bl['file']}")
            print(f"   Text: {bl['text']}")
            print(f"   URL: {bl['url']}")
            print(f"   Reason: {bl['reason']}")
            print()
    else:
        print("All internal links are valid!")

if __name__ == '__main__':
    main()
