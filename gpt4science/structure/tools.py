from __future__ import annotations

import os
import pprint

from langchain.tools import Tool

from gpt4science.settings import DATA_PATH
from gpt4science.structure.schemas import InitializePaperStructureArgs, PaperStructure


def create_paper_structure(paper_structure: PaperStructure) -> None:
    toc_json = paper_structure.json()
    pprint.pprint(toc_json, indent=4)

    data_path = os.path.join(DATA_PATH, paper_structure.title.lower().replace(" ", "_"))
    with open(data_path, "w", encoding="utf-8") as file:
        file.write(str(toc_json))

    return toc_json


initialize_structure_tool = Tool.from_function(
    name="create_paper_structure",
    description="Given topic, context, and title, create table of contents.",
    func=create_paper_structure,
    args_schema=InitializePaperStructureArgs,
)
