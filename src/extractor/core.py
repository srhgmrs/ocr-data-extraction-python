from pdf2image import convert_from_path
from .ocr import ocr_pagina
from .parser import detectar_faixas, extrair_linhas


def processar_pdf(pdf_path, poppler_path=None, dpi=300):
    paginas = convert_from_path(pdf_path, dpi=dpi, poppler_path=poppler_path)

    resultados = []
    faixas_salvas = None

    for i, pagina in enumerate(paginas, 1):
        dados = ocr_pagina(pagina)
        faixas = detectar_faixas(dados) or faixas_salvas

        if not faixas:
            continue

        faixas_salvas = faixas
        linhas = extrair_linhas(dados, faixas)

        for linha in linhas:
            resultados.append([i] + linha)

    return resultados