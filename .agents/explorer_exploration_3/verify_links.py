import os
import re
import sys

def find_markdown_files(root_dir):
    md_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        # Skip git and agent folders if needed, but here we scan everything
        if '.git' in dirpath or '.agents' in dirpath:
            continue
        for filename in filenames:
            if filename.lower().endswith('.md'):
                md_files.append(os.path.join(dirpath, filename))
    return md_files

def extract_links(file_path):
    links = []
    # Match markdown links: [text](url)
    link_regex = re.compile(r'\[.*?\]\((.*?)\)')
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line_num, line in enumerate(f, 1):
            for match in link_regex.finditer(line):
                url = match.group(1).strip()
                links.append((line_num, url))
    return links

def is_relative_link(url):
    # Ignore absolute links, anchors in the same file, and mailto
    if url.startswith(('http://', 'https://', 'mailto:', '#')):
        return False
    return True

def verify_link(source_file, link):
    # Separate file path from potential anchor
    parts = link.split('#', 1)
    target_path = parts[0]
    
    if not target_path:
        # Just an anchor link in the same file, already filtered by is_relative_link
        return True
        
    source_dir = os.path.dirname(source_file)
    # Resolve relative path
    resolved_path = os.path.normpath(os.path.join(source_dir, target_path))
    
    if not os.path.exists(resolved_path):
        return False
        
    # If the target exists and is a directory, check if it contains a README.md file
    if os.path.isdir(resolved_path):
        readme_path = os.path.join(resolved_path, 'README.md')
        if not os.path.exists(readme_path):
            return False
            
    return True

def main():
    # Use current working directory as repo root
    repo_root = os.getcwd()
    print(f"Scanning repository for markdown links starting from: {repo_root}")
    
    md_files = find_markdown_files(repo_root)
    broken_links_count = 0
    checked_links_count = 0
    
    for md_file in md_files:
        rel_src = os.path.relpath(md_file, repo_root)
        links = extract_links(md_file)
        for line_num, url in links:
            if is_relative_link(url):
                checked_links_count += 1
                if not verify_link(md_file, url):
                    broken_links_count += 1
                    print(f"Error: Broken relative link found in '{rel_src}' at line {line_num}:")
                    print(f"  Link: '{url}'")
                    print(f"  Attempted resolve path: '{os.path.normpath(os.path.join(os.path.dirname(md_file), url))}'")
                    print()
                    
    print(f"Verification summary:")
    print(f"  Markdown files scanned: {len(md_files)}")
    print(f"  Relative links checked: {checked_links_count}")
    print(f"  Broken links found:     {broken_links_count}")
    
    if broken_links_count > 0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()
