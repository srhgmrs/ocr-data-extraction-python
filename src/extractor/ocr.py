import pytesseract


def ocr_pagina(imagem):
    return pytesseract.image_to_data(
        imagem,
        output_type=pytesseract.Output.DICT
    )