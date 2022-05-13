from collections import UserString

from pydantic.fields import ModelField

CHAINS = {'L', 'H', 'K', 'A', 'B', 'G'}


class Chain(UserString):
    
    chains = CHAINS
    
    @classmethod
    def __get_validators__(cls):    
        yield cls.validate

    @classmethod
    def validate(cls, value: str, field: ModelField) -> str:
        if not isinstance(value, str):
            raise ValueError(f"{field} [{value}] must be a string")
        value = value.strip().upper()
        if value not in CHAINS:
            raise ValueError(f"{field} [{value}] must be in {CHAINS}")
        
        return value