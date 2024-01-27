from pydantic.v1 import BaseModel


class Section(BaseModel):
    title: str


class Chapter(BaseModel):
    title: str
    sections: list[Section]


class Paper(BaseModel):
    topic: str
    context: str
    title: str
    chapters: list[Chapter]


class InitializePaperArgs(BaseModel):
    paper_structure: Paper
