from pydantic.v1 import BaseModel


class SubSection(BaseModel):
    title: str


class Chapter(BaseModel):
    title: str
    subsections: list[SubSection]


class PaperStructure(BaseModel):
    topic: str
    context: str
    title: str
    chapters: list[Chapter]


class InitializePaperStructureArgs(BaseModel):
    paper_structure: PaperStructure
