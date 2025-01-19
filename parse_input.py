import os
import re

# Path to the 'Album' folder
album_dir = 'Albums'
output_file = 'input.txt'

# Collect content from all .txt files
collated_content = []

# Define the regex pattern to remove the unwanted characters
embed_pattern = re.compile(r'\??\d*Embed$')
bracket_line_pattern = re.compile(r'^\[\s*.*?\s*\]$')

# Walk through the directory
for root, _, files in os.walk(album_dir):
    print(root)
    print(files)
    for file in files:
        if file.endswith('.txt'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                cleaned_lines = []
                for line in lines[1:]:  # Omit the first line
                    # Remove lines that are just [text]
                    if not bracket_line_pattern.match(line.strip()):
                        # Remove trailing '?', digits, and 'Embed'
                        line = re.sub(embed_pattern, '', line).strip()
                        cleaned_lines.append(line)
                content = '\n'.join(cleaned_lines).strip()
                collated_content.append(content)

# Write the collated content to 'input.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(collated_content))

print(f"Collated text written to {output_file}")
