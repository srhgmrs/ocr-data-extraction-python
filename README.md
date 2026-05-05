# 📄 PDF OCR Extractor — Data Extraction Tool

Transforme PDFs não estruturados em dados utilizáveis com Python e OCR.

## Sobre o projeto

Este projeto resolve um problema comum em ambientes corporativos:
**extrair dados estruturados de PDFs escaneados automaticamente.**

Utilizando OCR com Tesseract, o sistema identifica padrões de layout e converte documentos em dados organizados (Excel), prontos para análise ou integração com pipelines de dados.

---

## Tecnologias utilizadas

* Python
* Tesseract OCR
* pdf2image
* OpenPyXL

---

## Funcionalidades

* ✔️ Extração automática de dados via OCR
* ✔️ Detecção inteligente de colunas (Cod, Nome, Matrícula)
* ✔️ Processamento de múltiplas páginas
* ✔️ Exportação para Excel
* ✔️ Interface via linha de comando (CLI)
* ✔️ Configuração flexível (Tesseract / Poppler)

---

## Caso de uso real

Ideal para:

* Automação de processos administrativos
* Digitalização de documentos
* Pipelines de dados
* Integração com Power Automate / RPA

---

## ▶️ Como usar

```bash
pip install -r requirements.txt
```

```bash
python main.py arquivo.pdf
```

### Com configurações customizadas:

```bash
python main.py arquivo.pdf \
  --output resultado.xlsx \
  --tesseract "C:/Program Files/Tesseract-OCR/tesseract.exe" \
  --poppler "C:/poppler/bin"
```

---

## Pré-requisitos

### Tesseract OCR

https://github.com/tesseract-ocr/tesseract

### Poppler

https://github.com/oschwartz10612/poppler-windows

---

## Output

Arquivo Excel com estrutura:

| Pagina | Cod | Nome | Matrícula |
| ------ | --- | ---- | --------- |

---

## Arquitetura

O projeto segue uma estrutura modular:

* `ocr.py` → leitura OCR
* `parser.py` → interpretação dos dados
* `core.py` → pipeline principal
* `exporter.py` → saída em Excel

---

## Possíveis melhorias

* Suporte a múltiplos layouts de documentos
* API REST (FastAPI)
* Integração com cloud (Azure / AWS)
* Pipeline automatizado (Airflow / Power Automate)

---

## Autor

Projeto desenvolvido como parte de portfólio para atuação em:

* Engenharia de Dados
* Automação
* Desenvolvimento Python

---

## Destaque técnico

Este projeto demonstra:

* Manipulação de dados não estruturados
* Uso de OCR em produção
* Design modular em Python
* Automação de processos reais

---

Se esse projeto te ajudou, considere dar um star!
