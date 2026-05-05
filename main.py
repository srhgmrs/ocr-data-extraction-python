import argparse
import pytesseract
from src.extractor.core import processar_pdf
from src.extractor.exporter import salvar_xlsx


def main():
    parser = argparse.ArgumentParser(description="PDF OCR Extractor")

    parser.add_argument("pdf", help="Caminho do PDF")
    parser.add_argument("-o", "--output", default="saida.xlsx")
    parser.add_argument("--tesseract", help="Caminho do executável do Tesseract")
    parser.add_argument("--poppler", help="Caminho do Poppler")

    args = parser.parse_args()

    if args.tesseract:
        pytesseract.pytesseract.tesseract_cmd = args.tesseract

    dados = processar_pdf(args.pdf, args.poppler)

    if not dados:
        print("Nenhum dado encontrado.")
        return

    salvar_xlsx(dados, args.output)
    print(f"Arquivo salvo em: {args.output}")


if __name__ == "__main__":
    main()