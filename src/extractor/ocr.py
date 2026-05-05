import pytesseract
import logging

logger = logging.getLogger(__name__)


def ocr_pagina(imagem):
    logger.debug("Executando OCR na página")
    return pytesseract.image_to_data(
        imagem,
        output_type=pytesseract.Output.DICT
    )