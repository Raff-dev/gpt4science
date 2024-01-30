from typing import Any

from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate


class PydanticPromptTemplate(PromptTemplate):
    def __init__(self, *args, parser: PydanticOutputParser, **kwargs: Any) -> None:
        format_instructions = parser.get_format_instructions()
        kwargs["template"] += "\n\n{format_instructions}"
        kwargs["partial_variables"]["format_instructions"] = format_instructions
        super().__init__(*args, **kwargs)
