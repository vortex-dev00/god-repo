import os
import re
from pathlib import Path

def main():
    root_dir = Path(r"C:\Users\svhon\.gemini\antigravity\scratch\god-repo")
    modified_files = [
        "developers/ai-editors-ide-extensions/README.md",
        "developers/devops-cicd-ai-tools/README.md",
        "developers/llm-gateways-routers/README.md",
        "developers/prompt-engineering-observability/README.md",
        "developers/rag-vector-databases/README.md",
        "developers/starters-boilerplates/README.md",
        "discover/model-comparisons-benchmarks/README.md",
        "discover/open-source-alternatives/README.md",
        "everyone/ai-mobile-apps/README.md",
        "meta/ai-hardware-guide/README.md",
        "meta/ai-news-staying-updated/README.md",
        "developers/cli-agents/README.md"
    ]
    
    suspicious_patterns = [
        r"(?i)TODO",
        r"(?i)placeholder",
        r"(?i)insert here",
        r"(?i)tbd",
        r"(?i)coming soon",
        r"pass",
        r"fail",
        r"(?i)cheating",
        r"(?i)integrity",
        r"(?i)facade",
    ]
    
    compiled_patterns = [re.compile(pat) for pat in suspicious_patterns]
    
    for rel_path in modified_files:
        file_path = root_dir / rel_path
        if not file_path.exists():
            print(f"File does not exist: {rel_path}")
            continue
            
        content = file_path.read_text(encoding="utf-8")
        
        # Check for empty sections
        lines = content.splitlines()
        for idx, line in enumerate(lines):
            for pat in compiled_patterns:
                if pat.search(line):
                    print(f"Found suspicious pattern '{pat.pattern}' in {rel_path}:{idx+1}: {line}")
                    
if __name__ == "__main__":
    main()
