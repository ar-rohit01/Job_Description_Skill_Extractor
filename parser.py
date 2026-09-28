from typing import List

from pydantic import BaseModel, Field


class JobDescriptionOutput(BaseModel):
    skills: List[str] = Field(default_factory=list)
    experience: str = "not_available"
    education: str = "not_available"