# zoho_link_crawler.py

import requests
from bs4 import BeautifulSoup

# List of URLs to crawl
urls = [
    "https://flyexpresssssss.zohodesk.com/portal/en/kb/articles/copa-chile-telefono-c%C3%B3mo-llamar-a-copa-airlines-en-chile-24-horas",
    "https://flyexpresssssss.zohodesk.com/portal/en/kb/articles/copa-chile-cl-c%C3%B3mo-llamar-a-copa-airlines-en-chile-24x7",
    "https://flyexpresssssss.zohodesk.com/portal/en/kb/articles/copa-atencion-c%C3%B3mo-llamar-a-copa-airlines-en-chile",
    "https://flyexpresssssss.zohodesk.com/portal/en/kb/articles/copa-argentina-telefono-c%C3%B3mo-llamar-a-copa-airlines-en-argentina-24-horas",
    "https://flyexpresssssss.zohodesk.com/portal/en/kb/articles/cm-ar-telefono-c%C3%B3mo-llamar-a-copa-airlines-en-argentina-24horas",
    "https://flyexpresssssss.zohodesk.com/portal/en/kb/articles/habla-directo-c%C3%B3mo-llamar-a-copa-airlines-en-argentina",
    "https://flyexpresssssss.zohodesk.com/portal/en/kb/articles/copa-airlines-mexico-telefono-c%C3%B3mo-llamar-a-copa-airlines-en-mexico-24-horas",
    "https://flyexpresssssss.zohodesk.com/portal/en/kb/articles/cm-mx-telefono-c%C3%B3mo-llamar-a-copa-airlines-en-mexico-llama-ahora",
    "https://flyexpresssssss.zohodesk.com/portal/en/kb/articles/copaairlines-costa-rica-telefono-c%C3%B3mo-llamar-a-copa-airlines-en-costa-rica-24-horas",
    "https://flyexpresssssss.zohodesk.com/portal/en/kb/articles/copa-24x7-asistencia-c%C3%B3mo-puedo-hablar-con-una-persona-real-en-copa",
    "https://flyexpresssssss.zohodesk.com/portal/en/kb/articles/copa-ayuda-inmediata-c%C3%B3mo-puedo-cambiar-un-pasaje-de-copa-airlines-24horas",
    "https://flyexpresssssss.zohodesk.com/portal/en/kb/articles/copa-airliness-espa%C3%B1a-telefono-c%C3%B3mo-llamar-a-copa-airlines-en-espa%C3%B1a-24-horas-servico",
    "https://flyexpresssssss.zohodesk.com/portal/en/kb/articles/copa-airlines-24x7-soporte-cu%C3%A1l-es-el-horario-de-atenci%C3%B3n-de-copa-airlines-24-horas",
    "https://flyexpresssssss.zohodesk.com/portal/en/kb/articles/copa-airliness-colombia-telefono-c%C3%B3mo-llamar-a-copa-airlines-en-colombia-24-horas",
    "https://flyexpresssssss.zohodesk.com/portal/en/kb/articles/copa-persona-directo-c%C3%B3mo-hablar-con-una-persona-viva-en-copa-airlines-ayuda",
    "https://flyexpresssssss.zohodesk.com/portal/en/kb/articles/copa-airlines-peru-telefono-c%C3%B3mo-llamar-a-copa-airlines-en-peru-24-horas",
    "https://flyexpresssssss.zohodesk.com/portal/en/kb/articles/c%C3%B3mo-llamar-a-booking-com-en-espanol-24-horas"
]

# Crawl and extract titles
for url in urls:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string.strip() if soup.title else 'No Title'
            print(f"[✔] {url} - {title}")
        else:
            print(f"[✘] {url} - HTTP {response.status_code}")
    except Exception as e:
        print(f"[✘] {url} - ERROR: {e}")
