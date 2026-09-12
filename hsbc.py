import re

import requests
from bs4 import BeautifulSoup


URL = (
    "https://www.hsbc.com.mx/tarjetas-de-credito/productos/zero/"
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
    r"(?:una\s+compra|compras?)\s+de\s+\$?\s*"
    r"([\d,]+(?:\.\d{2})?)\s*"
    r"(?:M\.?\s*N\.?)?\s+al\s+mes",
    re.IGNORECASE,
)

match = pattern.search(text)

if match:
    monto = match.group(1)
    print(f"Monto para exentar la comisión: ${monto} al mes")
else:
    print("No se encontró el monto.")