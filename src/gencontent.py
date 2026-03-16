import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    markdown_lines = markdown.split('\n')
    for line in markdown_lines:
        if line.startswith("# "):
            return line[2:].strip()
    
    raise Exception("Not a header.")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    
    markdown_file = open(from_path, "r")
    markdown_content = markdown_file.read()
    markdown_file.close()
    
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()
    
    html = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', 'href="' + basepath)
    template = template.replace('src="/', 'src="' + basepath)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)
    to_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for file in os.listdir(dir_path_content):
        path = os.path.join(dir_path_content, file)
        if os.path.isfile(path):
            dest_path = os.path.join(dest_dir_path, file)
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(path, template_path, dest_path, basepath)
        else:
            dest_path = os.path.join(dest_dir_path, file)
            generate_pages_recursive(path, template_path, dest_path, basepath)