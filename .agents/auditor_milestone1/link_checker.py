import os
import re
from pathlib import Path

def find_md_files(root_dir):
    return list(Path(root_dir).rglob("*.md"))

def check_links_in_file(file_path, root_dir):
    content = file_path.read_text(encoding="utf-8")
    # regex for markdown links: [text](link)
    # ignore links starting with http, https, mailto, or just fragment identifiers starting with #
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    broken_links = []
    
    for match in link_pattern.finditer(content):
        text, link = match.groups()
        # Clean up link from anchors if any
        clean_link = link.split('#')[0]
        
        # Skip absolute web links and empty links
        if not clean_link or clean_link.startswith(('http://', 'https://', 'mailto:', 'tel:')):
            continue
            
        # Check if it's a relative path
        link_path = (file_path.parent / clean_link).resolve()
        
        # Verify if link_path exists
        if not link_path.exists():
            broken_links.append((link, str(link_path)))
            
    return broken_links

def main():
    root_dir = Path(r"C:\Users\svhon\.gemini\antigravity\scratch\god-repo")
    all_files = find_md_files(root_dir)
    total_broken = 0
    
    print(f"Scanning {len(all_files)} markdown files for relative links...")
    
    for file_path in all_files:
        # Skip files inside .agents/
        if ".agents" in file_path.parts:
            continue
            
        broken = check_links_in_file(file_path, root_dir)
        if broken:
            print(f"\nIn file: {file_path.relative_to(root_dir)}")
            for link, target in broken:
                print(f"  Broken link: '{link}' -> resolved to: '{target}'")
                total_broken += 1
                
    if total_broken == 0:
        print("\nAll relative links are VALID!")
    else:
        print(f"\nFound {total_broken} broken relative links.")

if __name__ == "__main__":
    main()
