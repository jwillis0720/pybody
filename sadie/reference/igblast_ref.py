import logging
import os
import json
import itertools
import gzip

# third party
import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# module
from .settings import BLAST_CONVENTION
from .blast import write_blast_db

logger = logging.getLogger(__file__)


def write_out_fasta(sequences, outpath):
    logger = logging.getLogger(__file__)
    output_fasta = outpath + ".fasta"
    logger.debug("output fasta {}".format(output_fasta))

    # Im sure this will come back to haunt me, but if, we've seen the name, save that
    seen_short_names = []
    with open(output_fasta, "w") as f:
        for sequence in sequences:
            name = sequence.name
            if "|" not in name:
                # we may have preparsed this if its coming from database
                short_name = name
            else:
                short_name = name.split("|")[1]
            if short_name in seen_short_names:
                logger.warning(
                    "DANGER!!! DANGER!! We have already seen this gene name once, probably a duplicate species {}!!".format(
                        short_name
                    )
                )
                continue
            seq = str(sequence.seq).replace(".", "")
            f.write(">{}\n{}\n".format(short_name, seq))
            seen_short_names.append(short_name)

    return output_fasta


def get_databases_types(database_json):
    return list(set(map(lambda x: x["source"], database_json)))


def get_species_from_database(database_json):
    return list(set(map(lambda x: x["common"], database_json)))


def get_filtered_data(database_json, source, common, receptor, segment):
    return list(
        filter(
            lambda x: x["source"] == source
            and x["common"] == common
            and x["gene_segment"] == segment
            and x["receptor"] == receptor,
            database_json,
        )
    )


def make_igblast_ref_database(database, outdir, only_functional):
    """[summary]

    Parameters
    ----------
    engine : [type]
        [description]
    blast_dir : [type]
        [description]
    only_functional : [type]
        [description]
    """
    # The blast DB groups by V,D and J
    ig_database = json.load(gzip.open(database, "rt"))

    for receptor, common, source in itertools.product(
        ["Ig", "TCR"], get_species_from_database(ig_database), get_databases_types(ig_database)
    ):
        receptor_blast_dir = os.path.join(outdir, f"{source}/{receptor}/blastdb/")
        if not os.path.exists(receptor_blast_dir):
            logger.info("Creating %s", receptor_blast_dir)
            os.makedirs(receptor_blast_dir)
        for segment in list("VDJ"):
            filtered_df = get_filtered_data(ig_database, source, common, receptor, segment)
            if not filtered_df:
                logger.info(f"No entries for {common}-{source}-{receptor}")
                continue
            # recptor_translate_name = BLAST_CONVENTION[receptor]
            out_segment = os.path.join(receptor_blast_dir, f"{common}_{segment}")
            genes = list(map(lambda x: x["gene"], filtered_df))
            seqs = list(map(lambda x: x["imgt"][f"{segment.lower()}_gene_nt"], filtered_df))
            joined_seqs = [SeqRecord(Seq(seq), name=v, id=v) for v, seq in zip(genes, seqs)]
            fasta_file = write_out_fasta(joined_seqs, out_segment)
            write_blast_db(fasta_file, fasta_file.split(".fasta")[0])
            logger.info(f"Wrote blast for {fasta_file}")