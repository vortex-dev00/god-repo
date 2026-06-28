import os
from markdown_it import MarkdownIt

REPO_ROOT = r"C:\Users\svhon\.gemini\antigravity\scratch\god-repo"

def main():
    md = MarkdownIt()
    
    # Try parsing a sample file
    sample_file = os.path.join(REPO_ROOT, "README.md")
    with open(sample_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    try:
        tokens = md.parse(content)
        print(f"Successfully parsed README.md. Tokens count: {len(tokens)}")
    except Exception as e:
        print(f"Failed to parse README.md: {e}")

if __name__ == "__main__":
    main()
