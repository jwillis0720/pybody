from pydantic import BaseModel, validator
from typing import Optional, List


class Species(BaseModel):
    species: str


class GeneEntry(BaseModel):
    """V,D or J Gene Entry with validation"""

    sub_species: Optional[str]
    species: str
    gene: str
    database: str

    @validator("sub_species")
    def check_sub_species(cls, v):
        # pylint: disable=no-self-argument
        return Species(**{"species": v}).species

    @validator("species")
    def check_species(cls, v, values):
        # pylint: disable=no-self-argument
        if values["sub_species"] is None:
            values["sub_species"] = Species(**{"species": v}).species
        return Species(**{"species": v}).species

    @validator("gene")
    def check_vgene(cls, v, values):
        # pylint: disable=no-self-argument
        if v[3] not in ["V", "D", "J"]:
            raise ValueError(f"gene must contain V,D or J at 3rd index, current have {v[3]} in {v} ")
        return v

    @validator("database")
    def check_database(cls, v):
        # pylint: disable=no-self-argument
        if v not in ["imgt", "custom"]:
            raise ValueError(f"{v} is not a valid database, chocies are 'imgt' or 'custom'")
        return v


class GeneEntries(BaseModel):
    """V,D or J Gene Entry with validation"""

    sub_species: Optional[str]
    species: str
    gene: List[str]
    database: str

    @validator("sub_species")
    def check_sub_species(cls, v):
        # pylint: disable=no-self-argument
        return Species(**{"species": v}).species

    @validator("species")
    def check_species(cls, v, values):
        # pylint: disable=no-self-argument
        if values["sub_species"] is None:
            values["sub_species"] = Species(**{"species": v}).species
        return Species(**{"species": v}).species

    @validator("gene", each_item=True)
    def check_vgene(cls, v, values):
        # pylint: disable=no-self-argument
        if v[3] not in ["V", "D", "J"]:
            raise ValueError(f"gene must contain V,D or J at 3rd index, current have {v[3]} in {v} ")
        return v

    @validator("database")
    def check_database(cls, v):
        # pylint: disable=no-self-argument
        if v not in ["imgt", "custom"]:
            raise ValueError(f"{v} is not a valid database, chocies are 'imgt' or 'custom'")
        return v
