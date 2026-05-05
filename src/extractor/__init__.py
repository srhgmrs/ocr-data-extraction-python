__version__ = "1.0.0"
__author__ = "Sarah Guimarães"

from .core import processar_pdf
from .exporter import salvar_xlsx

__all__ = ["processar_pdf", "salvar_xlsx"]