import os
from pathlib import Path
from typing import Any, List, Union
from pandas.core.indexes.base import Index


class Error(Exception):
    """Base class for exceptions in this module."""


class MissingAirrColumns(Error):
    """Exception raised for not finiding the igblast module

    Attributes:
    """

    def __init__(self, missing_columns: Union[Index, List[Union[str, int]]]):
        super().__init__()
        self.missing_columns = missing_columns

    def __str__(self):
        return "Must have all AIRR columns defined, missing {}".format(self.missing_columns)


class EmtpyFileError(Error):
    """Exception raised for a file passed to igblast being empty

    this is needed because blasts accepts empty files but we will not

    """

    def __init__(self, file: Union[str, Path]):
        super().__init__()
        self.passed_arguments = file

    def __str__(self):
        return "{} is empty".format(self.passed_arguments)


class BadIgBLASTExe(Error):
    """Exception raised for not finiding the igblastn executable

    Attributes:
    """

    def __init__(self, passed_executable: Union[str, Path], msg: str):
        super().__init__()
        self.passed_arguments = passed_executable
        self.msg = msg

    def __str__(self) -> str:
        _env = os.environ["PATH"]
        return f"Cant find IgBLAST {self.passed_arguments}. Check {_env}\n {self.msg}"


class MissingIgBLASTArgument(Error):
    """Missing a required IgBLAST command argument

    If a required command is missing

    """

    def __init__(self, msg: str):
        super().__init__()
        self.msg = msg

    def __str__(self) -> str:
        return self.msg


class BadIgBLASTArgument(Error):
    """Exception raised for passing incorrect params to an igblast arguments"""

    def __init__(
        self,
        passed_arguments: Any,
        accepted_arguments: Union[
            str,
            type,
            Union[Path, str],
            List[str],
        ],
    ):
        super().__init__()
        self.passed_arguments = passed_arguments
        self.accepted_arguments = accepted_arguments

    def __str__(self) -> str:
        return "Passed argument {}. Only accepts {}".format(self.passed_arguments, self.accepted_arguments)


class BadIgDATA(Error):
    """Exception raised for IgData path (which is crucial) not being found

    Attributes:
    """

    def __init__(self, passed_arguments: Any):
        super().__init__()
        self.passed_arguments = passed_arguments

    def __str__(self):
        return f"Bad IgDAta path {self.passed_arguments} - please provide where IgDATA is located"


class IgBLASTRunTimeError(Error):
    """Exception raised for Igblast runtime error"""

    def __init__(self, stderr: bytes):
        super().__init__()
        self.stderr = stderr

    def __str__(self):
        return "Runtime Error with Blast {}".format(self.stderr.decode("utf-8"))


class BadDataSet(Error):
    """Exception raised for annotating a bad species

    Attributes:
    """

    def __init__(self, requested_type: str, accepted_types: List[str]):
        super().__init__()
        self.requested_type = requested_type
        self.accepted_types = accepted_types

    def __str__(self):
        return "{} dataset, avail datasets{}".format(self.requested_type, sorted(self.accepted_types))


class BadRequstedFileType(Error):
    """Exception raised for unsupported file types

    Attributes:
    """

    def __init__(self, requested_type: str, accepted_types: List[str]):
        super().__init__()
        self.requested_type = requested_type
        self.accepted_types = accepted_types

    def __str__(self):
        return "{} file passed, only accepts {}".format(self.requested_type, self.accepted_types)
