from langchain.prompts import PromptTemplate

from gpt4science.prompting.templates import (
    PAPER_STRUCTURE_PROMPT,
    RESEARCH_PAPER_TITLE_PROMPT,
)

research_paper_title_prompt = PromptTemplate(
    template=RESEARCH_PAPER_TITLE_PROMPT,
    input_variables=["topic", "context"],
)

initialize_structure_prompt = PromptTemplate(
    template=PAPER_STRUCTURE_PROMPT,
    input_variables=["topic", "context", "title"],
)
