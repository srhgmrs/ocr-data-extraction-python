from pdf2image import convert_from_path
from .ocr import ocr_pagina
from .parser import detectar_faixas, extrair_linhas
import logging

logger = logging.getLogger(__name__)


def processar_pdf(pdf_path, poppler_path=None, dpi=300):
    logger.info(f"Iniciando processamento do PDF: {pdf_path}")

    paginas = convert_from_path(pdf_path, dpi=dpi, poppler_path=poppler_path)
    logger.info(f"{len(paginas)} páginas carregadas")

    resultados = []

    for i, pagina in enumerate(paginas, 1):
        logger.info(f"Processando página {i}")

        dados = ocr_pagina(pagina)
        faixas = detectar_faixas(dados)

        if not faixas:
            logger.warning(f"Cabeçalho não encontrado na página {i}")
            continue

        linhas = extrair_linhas(dados, faixas)
        logger.info(f"{len(linhas)} registros extraídos da página {i}")

        for linha in linhas:
            resultados.append([i] + linha)

    logger.info(f"Processamento finalizado. Total de registros: {len(resultados)}")

    return resultados