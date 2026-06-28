from markdown_it import MarkdownIt

def main():
    md = MarkdownIt()
    content = """
# Header 1
[link text](relative/path/file.md#anchor)
![image alt](images/pic.png)
    """
    tokens = md.parse(content)
    for token in tokens:
        print("Token:", token.type)
        if token.type == "inline" and token.children:
            for child in token.children:
                print("  Child Token:", child.type, getattr(child, "attrs", None), getattr(child, "content", None))

if __name__ == "__main__":
    main()
