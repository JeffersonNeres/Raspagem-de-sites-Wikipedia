from requests import get
from bs4 import BeautifulSoup
from nome_segundarios import raspagem
import pytest

site_intro = input("Cole o link Wikipedia que deseja fazer a raspagem aqui: ")
site = get(site_intro)
tags = BeautifulSoup(site.text, "html5lib")
title = tags.find("title")
title
print("Página Principal:", title.text)

subtitles = tags.find_all("a", attrs = {"class" : "mw-redirect"})
[h2.text for h2 in subtitles]
paginas = [site_intro + h2["href"] for h2 in subtitles]

numero_da_pagina = 1
for pagina in paginas:
    numero_da_pagina += 1
    print(f"{numero_da_pagina}° Página, {raspagem(pagina)} \n link: {pagina}")

assert len(paginas) == numero_da_pagina - 1
