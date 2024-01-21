from __future__ import annotations

import pprint

from langchain.tools import Tool
from pydantic.v1 import BaseModel


class SubSection(BaseModel):
    title: str


class Chapter(BaseModel):
    title: str
    SubSection: list[SubSection]


class PaperStructure(BaseModel):
    topic: str
    context: str
    title: str
    chapters: list[Chapter]


class InitializeStructureArgs(BaseModel):
    paper_structure: PaperStructure


def initialize_structure(paper_structure: PaperStructure) -> None:
    pprint.pprint(paper_structure.json(), indent=4)


initialize_structure_tool = Tool.from_function(
    name="initialize_structure",
    description="Given topic, context, and paper title, create a paper structure.",
    func=initialize_structure,
    args_schema=InitializeStructureArgs,
)
