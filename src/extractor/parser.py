def normalizar(texto):
    return texto.strip().lower()


def detectar_faixas(dados):
    faixas = {}

    for i, texto in enumerate(dados["text"]):
        t = normalizar(texto)

        if t == "cod":
            label = "cod"
        elif t == "nome":
            label = "nome"
        elif "matr" in t:
            label = "matricula"
        else:
            continue

        if label not in faixas:
            x = dados["left"][i]
            w = dados["width"][i]
            y = dados["top"][i]

            faixas[label] = (x - 80, x + w + 80, y)

    return faixas if len(faixas) == 3 else None


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