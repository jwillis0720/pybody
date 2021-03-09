__version__ = "0.1.18"

from .airr import Airr, BadDataSet, BadRequstedFileType, GermlineData
from .airrtable import AirrTable, ScfvAirrTable

__all__ = ["Airr", "AirrTable", "ScfvAirrTable", "BadDataSet", "BadRequstedFileType", "GermlineData"]
