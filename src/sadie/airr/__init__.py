__version__ = "0.2.2"

from .airr import Airr, BadDataSet, BadRequstedFileType, GermlineData
from .airrtable import AirrTable, ScfvAirrTable

__all__ = ["Airr", "AirrTable", "ScfvAirrTable", "BadDataSet", "BadRequstedFileType", "GermlineData"]
