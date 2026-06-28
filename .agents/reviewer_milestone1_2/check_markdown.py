import os
import re
import sys

# Reconfigure stdout to use UTF-8 to avoid encoding errors on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

modified_files = [
    r"developers/ai-editors-ide-extensions/README.md",
    r"developers/devops-cicd-ai-tools/README.md",
    r"developers/llm-gateways-routers/README.md",
    r"developers/prompt-engineering-observability/README.md",
    r"developers/rag-vector-databases/README.md",
    r"developers/starters-boilerplates/README.md",
    r"discover/model-comparisons-benchmarks/README.md",
    r"discover/open-source-alternatives/README.md",
    r"everyone/ai-mobile-apps/README.md",
    r"meta/ai-hardware-guide/README.md",
    r"meta/ai-news-staying-updated/README.md",
    r"developers/cli-agents/README.md",
]

repo_root = r"C:\Users\svhon\.gemini\antigravity\scratch\god-repo"

def check_file(file_rel_path):
    abs_path = os.path.join(repo_root, file_rel_path)
    if not os.path.exists(abs_path):
        return [f"File does not exist: {abs_path}"]
    
    with open(abs_path, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.splitlines()

    errors = []
    
    # 1. Code blocks matching
    code_block_count = content.count("```")
    if code_block_count % 2 != 0:
        errors.append(f"Mismatched triple backticks (``` count: {code_block_count})")

    # 2. Track inside/outside code block
    in_code_block = False
    
    # 3. Line by line validation
    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        
        # Toggle code block
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
            
        if in_code_block:
            continue  # Ignore markdown rules inside code block
            
        # 3.1 Check headers
        if stripped.startswith("#"):
            # Check space after #
            match = re.match(r'^(#+)(.*)', stripped)
            if match:
                hashes = match.group(1)
                after = match.group(2)
                if after and not after.startswith(" "):
                    errors.append(f"Line {idx}: Heading misses space after '#': '{stripped}'")
                    
        # 3.3 Check for placeholders
        # We look for explicit placeholders
        placeholders = ["TODO", "FIXME", "TBD", "PLACEHOLDER", "INSERT HERE", "[insert", "<insert"]
        for p in placeholders:
            if re.search(r'\b' + re.escape(p) + r'\b', line.upper()):
                if "N/A" in line and p == "TBD":
                    continue
                # For meta/ai-hardware-guide/README.md, TBD is for unannounced/unavailable specs.
                # Let's still report it but flag it contextually.
                errors.append(f"Line {idx}: Potential placeholder '{p}' found: {stripped}")

        # 3.4 Check inline code backticks balance
        inline_backticks = stripped.count("`")
        if inline_backticks % 2 != 0:
            errors.append(f"Line {idx}: Mismatched inline backticks (count: {inline_backticks})")

        # 3.5 Check link brackets balance
        open_brackets = stripped.count('[')
        close_brackets = stripped.count(']')
        if open_brackets != close_brackets:
            errors.append(f"Line {idx}: Mismatched square brackets: {stripped}")
            
        if "](" in stripped:
            link_matches = re.finditer(r'\]\(([^)]*)', stripped)
            for m in link_matches:
                content_after = m.group(1)
                # If there's a space in the URL, that's invalid markdown link syntax (needs to be URL-encoded or wrapped)
                if " " in content_after and not content_after.startswith("<"):
                    errors.append(f"Line {idx}: Space in link URL: {stripped}")

    # 4. Table column consistency across adjacent lines
    # Find tables
    in_table = False
    in_code_block = False
    table_pipes_count = 0
    table_start_line = 0
    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        # Toggle code block
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
            
        # Detect table rows
        # Table rows typically contain pipes. A separator row looks like |---|---|
        is_table_row = "|" in line
        if is_table_row:
            pipes = len(re.findall(r'(?<!\\)\|', line))
            if not in_table:
                in_table = True
                table_pipes_count = pipes
                table_start_line = idx
            else:
                if pipes != table_pipes_count:
                    errors.append(f"Line {idx}: Table column pipe count mismatch (expected {table_pipes_count} pipes from line {table_start_line}, got {pipes}): {stripped}")
        else:
            in_table = False

    return errors

all_ok = True
for f in modified_files:
    print(f"Checking {f}...")
    errors = check_file(f)
    if errors:
        all_ok = False
        print(f"  [FAIL] Errors in {f}:")
        for err in errors:
            # print characters safely
            try:
                print(f"    - {err}")
            except Exception:
                print(f"    - {err.encode('ascii', errors='replace').decode('ascii')}")
    else:
        print(f"  [PASS] {f} is clean.")

if all_ok:
    print("\nAll files successfully verified.")
else:
    print("\nSome files failed verification.")
