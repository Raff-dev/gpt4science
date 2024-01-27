from __future__ import annotations

import pprint

from langchain.tools import Tool

from gpt4science.structure.models import InitializePaperArgs, Paper


def create_table_of_contents(table_of_contents: Paper) -> None:
    toc_json = table_of_contents.json()
    pprint.pprint(toc_json, indent=4)
    return toc_json


initialize_structure_tool = Tool.from_function(
    name="create_table_of_contents",
    description="Given topic, context, and paper title, create table of contents.",
    func=create_table_of_contents,
    args_schema=InitializePaperArgs,
)
