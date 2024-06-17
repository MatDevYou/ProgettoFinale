# Importa il modulo per interagire con il sistema operativo
import os  
# Importa il modulo per convertire Markdown in HTML
import markdown  
# Importa moduli per gestire i template Jinja2
from jinja2 import Environment, FileSystemLoader  
import stat


# Imposta l'ambiente Jinja2 per caricare i template dalla directory 'templates'
env = Environment(loader=FileSystemLoader('templates'))

def convert_markdown_to_html(markdown_file):
    """Converte un file Markdown in HTML."""
    # Stampa messaggio di debug
    print(f'Convertendo il file Markdown: {markdown_file}')
    # Apre il file Markdown in modalità di lettura
    with open(markdown_file, 'r', encoding='utf-8') as file:
        # Legge il contenuto del file Markdown
        text = file.read()
        # Stampa il contenuto del file Markdown
        print(f'Contenuto del file Markdown:\n{text}')
        # Converte il testo Markdown in HTML
        html = markdown.markdown(text)  
        # Stampa il contenuto convertito in HTML
        print(f'Contenuto convertito in HTML:\n{html}')
    # Ritorna il contenuto HTML convertito
    return html

def generate_html(template_name, context, output_file):
    """Genera un file HTML dal template specificato e contesto."""
    # Stampa messaggio di debug
    print(f'Generando HTML usando il template: {template_name}')
    # Ottiene il template Jinja2
    template = env.get_template(template_name)  
    # Rende il template con il contesto fornito
    html_content = template.render(context)  
    # Stampa il contenuto del file HTML generato
    print(f'Contenuto del file HTML generato:\n{html_content}')
    
    # Apre il file HTML in modalità di scrittura
    with open(output_file, 'w', encoding='utf-8') as file:
        # Scrive il contenuto HTML nel file specificato
        file.write(html_content)  
    # Stampa il percorso del file HTML scritto
    print(f'File HTML scritto: {output_file}')

def main():
    """Funzione principale per generare i siti statici."""
    # Definisce le directory di contenuto e di output
    content_dir = 'content'
    output_dir = 'output'
    # Crea la directory 'output' se non esiste già
    os.makedirs(output_dir, exist_ok=True)  

    # Itera su tutti i file nella directory di contenuto
    for md_file in os.listdir(content_dir):
        # Verifica se il file è un file Markdown
        if md_file.endswith('.md'):  
            # Stampa messaggio di debug
            print(f'Elaborazione del file: {md_file}')
            # Converte il contenuto Markdown in HTML
            html_content = convert_markdown_to_html(os.path.join(content_dir, md_file))
            
            # Definisce il contesto per il template HTML
            context = {
                'title': 'Blog Post',
                'post_title': 'Esempio di Post',
                'post_date': '10 Giugno 2024',
                'post_content': html_content
            }
            
            # Definisce il percorso del file HTML di output
            output_file = os.path.join(output_dir, f'{os.path.splitext(md_file)[0]}.html')
            # Stampa il percorso del file HTML generato
            print(f'Generazione del file HTML: {output_file}')
            # Genera il file HTML usando il template 'post.html'
            generate_html('post.html', context, output_file)  

if __name__ == '__main__':
    # Esegue la funzione main() se lo script viene eseguito direttamente
    main()  
