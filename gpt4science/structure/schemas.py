from pydantic.v1 import BaseModel


class Section(BaseModel):
    section_name: str


class Chapter(BaseModel):
    chapter_name: str
    sections: list[Section]


class PaperStructure(BaseModel):
    paper_title: str
    topic: str
    context: str
    chapters: list[Chapter]


class InitializePaperStructureArgs(BaseModel):
    paper_structure: PaperStructure
