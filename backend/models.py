from pydantic import BaseModel, Field
from typing import Optional

#I defined pixel class here
class PixelModel(BaseModel):
    x: int
    y: int
    color: str
    userId: Optional[str] = None
    lastUpdatedAt: None
    id: Optional[str] = Field(alias="_id")
