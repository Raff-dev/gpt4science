from __future__ import annotations

import pprint

from langchain.tools import Tool
from pydantic.v1 import BaseModel


class SubSection(BaseModel):
    title: str


class Chapter(BaseModel):
    title: str
    SubSection: list[SubSection]


class TableOfContents(BaseModel):
    topic: str
    context: str
    title: str
    chapters: list[Chapter]


class InitializeStructureArgs(BaseModel):
    paper_structure: TableOfContents


def create_table_of_contents(table_of_contents: TableOfContents) -> None:
    pprint.pprint(table_of_contents.json(), indent=4)


initialize_structure_tool = Tool.from_function(
    name="create_table_of_contents",
    description="Given topic, context, and paper title, create table of contents.",
    func=create_table_of_contents,
    args_schema=InitializeStructureArgs,
)
