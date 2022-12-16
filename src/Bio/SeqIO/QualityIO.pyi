from collections.abc import Generator
from typing import Any

from Bio import BiopythonParserWarning as BiopythonParserWarning
from Bio import BiopythonWarning as BiopythonWarning
from Bio import StreamModeError as StreamModeError
from Bio.File import as_handle as as_handle
from Bio.Seq import Seq as Seq
from Bio.SeqRecord import SeqRecord as SeqRecord

from .Interfaces import SequenceIterator as SequenceIterator
from .Interfaces import SequenceWriter as SequenceWriter

SANGER_SCORE_OFFSET: int
SOLEXA_SCORE_OFFSET: int

def solexa_quality_from_phred(phred_quality): ...
def phred_quality_from_solexa(solexa_quality): ...
def FastqGeneralIterator(source) -> Generator[Any, None, None]: ...

class FastqPhredIterator(SequenceIterator):
    title2ids: Any
    def __init__(self, source, alphabet: Any | None = ..., title2ids: Any | None = ...) -> None: ...
    def parse(self, handle): ...
    def iterate(self, handle) -> Generator[Any, None, None]: ...

def FastqSolexaIterator(
    source, alphabet: Any | None = ..., title2ids: Any | None = ...
) -> Generator[Any, None, None]: ...
def FastqIlluminaIterator(
    source, alphabet: Any | None = ..., title2ids: Any | None = ...
) -> Generator[Any, None, None]: ...

class QualPhredIterator(SequenceIterator):
    title2ids: Any
    def __init__(self, source, alphabet: Any | None = ..., title2ids: Any | None = ...) -> None: ...
    def parse(self, handle): ...
    def iterate(self, handle) -> Generator[Any, None, None]: ...

class FastqPhredWriter(SequenceWriter):
    def write_record(self, record) -> None: ...

def as_fastq(record): ...

class QualPhredWriter(SequenceWriter):
    wrap: Any
    record2title: Any
    def __init__(self, handle, wrap: int = ..., record2title: Any | None = ...) -> None: ...
    def write_record(self, record) -> None: ...

def as_qual(record): ...

class FastqSolexaWriter(SequenceWriter):
    def write_record(self, record) -> None: ...

def as_fastq_solexa(record): ...

class FastqIlluminaWriter(SequenceWriter):
    def write_record(self, record) -> None: ...

def as_fastq_illumina(record): ...
def PairedFastaQualIterator(
    fasta_source, qual_source, alphabet: Any | None = ..., title2ids: Any | None = ...
) -> Generator[Any, None, None]: ...