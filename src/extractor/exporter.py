from openpyxl import Workbook
import logging

logger = logging.getLogger(__name__)


def salvar_xlsx(dados, output):
    logger.info(f"Salvando arquivo Excel em: {output}")

    wb = Workbook()
    ws = wb.active

    for row in dados:
        ws.append(row)

    wb.save(output)

    logger.info("Arquivo salvo com sucesso")
