from pydantic import BaseModel, Field


class DataValidation(BaseModel):
    """
    Data validation class to ensure the integrity of data.
    """

    t: int = Field(
        ..., description="Timestamp"
    )
    o: float = Field(
        ..., gt=0, description="Opening price must be greater than 0"
    )
    h: float = Field(
        ..., gt=0, description="High price must be greater than 0"
    )
    l: float = Field(
        ..., gt=0, description="Low price must be greater than 0"
    )
    c: float = Field(
        ..., gt=0, description="Closing price must be greater than 0"
    )
    v: float = Field(
        ..., gt=0, description="Volume must be greater than 0"
    )
