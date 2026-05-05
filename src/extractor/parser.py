
import logging

logger = logging.getLogger(__name__)

def normalizar(texto):
    return texto.strip().lower()

def detectar_faixas(dados):
    faixas = {}

    for i, texto in enumerate(dados["text"]):
        # lógica...

        if len(faixas) != 3:
            logger.warning("Não foi possível detectar todas as colunas esperadas")
            return None

    logger.debug(f"Faixas detectadas: {faixas}")
    return faixas

def extrair_linhas(dados, faixas):
    resultado = []

    # simplificado para clareza
    cod = []
    nome = []
    mat = []

    for i, texto in enumerate(dados["text"]):
        x = dados["left"][i]
        y = dados["top"][i]

        if not texto.strip():
            continue

        if faixas["cod"][0] <= x <= faixas["cod"][1]:
            cod.append(texto)
        elif faixas["nome"][0] <= x <= faixas["nome"][1]:
            nome.append(texto)
        elif faixas["matricula"][0] <= x <= faixas["matricula"][1]:
            mat.append(texto)

    tamanho = min(len(cod), len(nome), len(mat))

    for i in range(tamanho):
        resultado.append([cod[i], nome[i], mat[i]])

    return resultado