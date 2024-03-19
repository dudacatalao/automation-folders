import os
from tkinter.filedialog import askdirectory

# solicita que você selecione uma pasta
caminho = askdirectory(title='Selecione uma pasta')

# pega todos os arquivos da pasta selecionada
lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".png", ".jpg"],
    "planilhas": [".xlsx", ".csv"],
    "pdfs": [".pdf"],
    "power points": [".pptx"],
    "bd": [".brM3"],
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")

    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.makedirs(f"{caminho}/{pasta}")
            os.rename(f"caminho/{arquivo}", f"caminho/{pasta}/{arquivo}")