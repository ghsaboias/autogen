import requests
from bs4 import BeautifulSoup
import random

def get_monkey_info():
    url = "https://en.wikipedia.org/wiki/Monkey"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    
    content = soup.find('div', {'id': 'mw-content-text'})
    paragraphs = content.find_all('p')
    images = content.find_all('img', {'class': 'thumbimage'})
    
    return paragraphs, images

def create_html(paragraphs, images):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>All About Monkeys</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: 0 auto; }
            img { max-width: 100%; height: auto; margin: 10px 0; }
            h1 { color: #333; }
        </style>
    </head>
    <body>
        <h1>All About Monkeys</h1>
    """
    
    for i, paragraph in enumerate(paragraphs):
        html_content += paragraph.prettify()
        if i % 3 == 0 and images:
            img = random.choice(images)
            img_src = "https:" + img['src']
            html_content += f'<img src="{img_src}" alt="Monkey image">'
            images.remove(img)
    
    html_content += """
    </body>
    </html>
    """
    
    return html_content

def save_html(content, filename="monkey_info.html"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"HTML file '{filename}' has been created successfully!")

if __name__ == "__main__":
    paragraphs, images = get_monkey_info()
    html_content = create_html(paragraphs, images)
    save_html(html_content)
