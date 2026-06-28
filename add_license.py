import os
import sys

# File extensions to target
TARGET_EXTENSIONS = {'.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.rs'}
HEADER_FILE = 'HEADER.txt'

def add_header_to_file(filepath, header_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Skip if header already exists
    if "Sayanox License" in content:
        return

    # Determine comment style based on extension
    ext = os.path.splitext(filepath)[1]
    if ext in ['.html', '.css']:
        formatted_header = f"<!--\n{header_text}\n-->\n\n"
    elif ext in ['.c', '.cpp', '.java', '.js', '.rs']:
        formatted_header = f"/*\n{header_text}\n*/\n\n"
    else: # Python, etc.
        formatted_header = '\n'.join([f"# {line}" for line in header_text.splitlines()]) + "\n\n"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(formatted_header + content)
    print(f"Added header to: {filepath}")

def main(directory):
    if not os.path.exists(HEADER_FILE):
        print(f"Error: {HEADER_FILE} not found in the current directory.")
        sys.exit(1)

    with open(HEADER_FILE, 'r', encoding='utf-8') as f:
        header_text = f.read()

    for root, _, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1] in TARGET_EXTENSIONS:
                add_header_to_file(os.path.join(root, file), header_text)

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    main(target_dir)
    print("License headers added successfully!")
