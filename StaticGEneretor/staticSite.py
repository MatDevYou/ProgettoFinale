import os
import markdown
from jinja2 import Environment, FileSystemLoader

# Imposta l'ambiente Jinja2
env = Environment(loader=FileSystemLoader('templates'))

def convert_markdown_to_html(markdown_file):
    with open(markdown_file, 'r', encoding='utf-8') as file:
        text = file.read()
        html = markdown.markdown(text)
    return html

def generate_html(template_name, context, output_file):
    template = env.get_template(template_name)
    html_content = template.render(context)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

def main():
    content_dir = 'content'
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)

    for md_file in os.listdir(content_dir):
        if md_file.endswith('.md'):
            html_content = convert_markdown_to_html(os.path.join(content_dir, md_file))
            
            context = {
                'title': 'Blog Post',
                'post_title': 'Esempio di Post',
                'post_date': '10 Giugno 2024',
                'post_content': html_content
            }
            
            output_file = os.path.join(output_dir, f'{os.path.splitext(md_file)[0]}.html')
            generate_html('post.html', context, output_file)

if __name__ == '__main__':
    main()
