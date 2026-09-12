import re

import requests
from bs4 import BeautifulSoup


URL = (
    "https://www.banamex.com/es/personas/tarjetas-credito/"
    "tarjeta-de-credito-sin-anualidad-joy.html"
)

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; TdcScraper/1.0)"
}

response = requests.get(URL, headers=headers, timeout=30)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Convertimos todo el HTML a texto para buscar el contenido visible.
text = soup.get_text(" ", strip=True)

pattern = re.compile(
    r"(?:al menos|acumulen|cumplan)\s*"
    r"\$?\s*([\d,]+(?:\.\d{2})?)\s*"
    r"(?:al mes|en todo tipo)",
    re.IGNORECASE,
)

match = pattern.search(text)

if match:
    monto = match.group(1)
    print(f"Monto para exentar la comisión: ${monto} al mes")
else:
    print("No se encontró el monto.")