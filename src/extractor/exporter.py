from openpyxl import Workbook


def salvar_xlsx(dados, output):
    wb = Workbook()
    ws = wb.active

    ws.append(["Pagina", "Cod", "Nome", "Matricula"])

    for row in dados:
        ws.append(row)

    wb.save(output)