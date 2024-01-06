
########
# Definining classes
from typing import List
from pydantic import BaseModel

class StoryLine(BaseModel):
    role: str
    line: str

class Story(BaseModel):
    story_lines: List[StoryLine]

########