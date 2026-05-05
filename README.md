# 📄 OCR Data Extraction Pipeline (Python)

Transforme PDFs não estruturados em dados prontos para análise com um pipeline modular de OCR.

---

## 🚀 Overview

Este projeto implementa um **pipeline completo de extração de dados** capaz de transformar documentos PDF escaneados em dados estruturados (Excel), utilizando OCR com Tesseract.

Ele resolve um problema comum em ambientes corporativos:
➡️ **converter documentos não estruturados em dados utilizáveis automaticamente**

---

## 💡 Problema

Muitos processos empresariais ainda dependem de:

* PDFs escaneados
* documentos não estruturados
* extração manual de dados

Isso gera:

* retrabalho
* erros humanos
* baixa escalabilidade

---

## ✅ Solução

Este projeto automatiza esse processo através de:

* 🔍 OCR (reconhecimento de texto)
* 🧠 Detecção de estrutura (colunas: Cod, Nome, Matrícula)
* 🔄 Processamento de múltiplas páginas
* 📊 Exportação para Excel

---

## 🧱 Arquitetura

O projeto segue uma arquitetura modular:

```
src/
 └── extractor/
     ├── core.py        # Pipeline principal
     ├── ocr.py         # Extração OCR
     ├── parser.py      # Interpretação dos dados
     └── exporter.py    # Exportação para Excel
```

---

## ⚙️ Tecnologias

* Python
* Tesseract OCR
* pdf2image
* OpenPyXL

---

## ▶️ Como executar

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 2. Executar o script

```bash
python main.py arquivo.pdf
```

---

### 3. Parâmetros opcionais

```bash
python main.py arquivo.pdf \
  --output resultado.xlsx \
  --tesseract "C:/Program Files/Tesseract-OCR/tesseract.exe" \
  --poppler "C:/poppler/bin"
```

---

## 📊 Output

O sistema gera um arquivo Excel estruturado:

| Página | Cod | Nome | Matrícula |
| ------ | --- | ---- | --------- |

---

## 💼 Aplicações reais

Este projeto pode ser utilizado em:

* Automação de processos administrativos
* Digitalização de documentos
* Integração com RPA (Power Automate)
* Pipelines de dados (ETL)
* Sistemas internos corporativos

---

## 📈 Evoluções futuras

* API REST (FastAPI)
* Suporte a múltiplos layouts de PDF
* Integração com cloud (Azure / AWS)
* Processamento em lote (pipeline)

---

## 🧠 Destaques técnicos

* Processamento de dados não estruturados
* Uso de OCR em pipeline automatizado
* Arquitetura modular e escalável
* Separação clara de responsabilidades

---

## 👩‍💻 Autor

Projeto desenvolvido como parte de portfólio voltado para:

* Engenharia de Dados
* Automação
* Desenvolvimento Python

---

⭐ Se este projeto te ajudou, considere dar um star!
