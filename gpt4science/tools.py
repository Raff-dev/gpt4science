from __future__ import annotations

import os
import pprint

from dotenv import load_dotenv
from langchain.tools import StructuredTool
from pydantic import BaseModel

load_dotenv()


SERP_API_KEY = os.getenv("SERP_API_KEY")


class Chapter(BaseModel):
    title: str
    chapters: list[Chapter] | None = None


class PaperStructure(BaseModel):
    topic: str
    context: str
    title: str
    chapters: list[Chapter]


def initialize_structure(paper_structure: PaperStructure) -> None:
    pprint.pprint(paper_structure.model_dump())


initialize_structure_tool = StructuredTool.from_function(
    name="initialize_structure",
    description="Given topic, context, and paper title, create a paper structure.",
    func=initialize_structure,
    input_schema=PaperStructure,
)
