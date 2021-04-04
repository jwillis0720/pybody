import os
from pathlib import Path
from sadie.utility import SadieIO


def get_file(file):
    """Helper method for test execution."""
    _file = os.path.join(os.path.abspath(os.path.dirname(__file__)), f"fixtures/{file}")
    if not os.path.exists(_file):
        raise FileNotFoundError(_file)
    return _file


def test_io_single_files():
    # infer filetypes of non compressed
    input_file = get_file("multiple.fasta")
    io = SadieIO(input_file)
    assert io.input == Path(input_file)
    assert io.infer_input
    assert not io.input_compressed
    assert io.input_file_type == "fasta"
    assert not io.isdir

    input_file = get_file("multiple.fastq")
    io = SadieIO(input_file)
    assert io.input == Path(input_file)
    assert io.infer_input
    assert not io.input_compressed
    assert io.input_file_type == "fastq"
    assert not io.isdir

    input_file = get_file("ab1_files/file1.ab1")
    io = SadieIO(input_file)
    assert io.input == Path(input_file)
    assert io.infer_input
    assert not io.input_compressed
    assert io.input_file_type == "abi"
    assert not io.isdir

    # infer filetypes of non compressed
    input_file = get_file("multiple.fasta.gz")
    io = SadieIO(input_file)
    assert io.input == Path(input_file)
    assert io.infer_input
    assert io.input_compressed == "gzip"
    assert io.input_file_type == "fasta"
    assert not io.isdir

    input_file = get_file("multiple.fastq.gz")
    io = SadieIO(input_file)
    assert io.input == Path(input_file)
    assert io.infer_input
    assert io.input_compressed == "gzip"
    assert io.input_file_type == "fastq"
    assert not io.isdir

    input_file = get_file("ab1_files/file1.ab1.gz")
    io = SadieIO(input_file)
    assert io.input == Path(input_file)
    assert io.infer_input
    assert io.input_compressed == "gzip"
    assert io.input_file_type == "abi"
    assert not io.isdir


def test_io_folders():
    # infer filetypes of non compressed
    input_file = get_file("fasta_folder")
    io = SadieIO(input_file)
    assert io.input == Path(input_file)
    assert io.infer_input
    assert not io.input_compressed
    assert io.input_file_type == "fasta"
    assert io.isdir

    input_file = get_file("fastq_folder")
    io = SadieIO(input_file)
    assert io.input == Path(input_file)
    assert io.infer_input
    assert not io.input_compressed
    assert io.input_file_type == "fastq"
    assert io.isdir

    input_file = get_file("ab1_files")
    io = SadieIO(input_file)
    assert io.input == Path(input_file)
    assert io.infer_input
    assert not io.input_compressed
    assert io.input_file_type == "abi"
    assert io.isdir
