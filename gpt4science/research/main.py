from __future__ import annotations

from langchain.output_parsers import PydanticOutputParser
from langchain_openai.chat_models import ChatOpenAI

from gpt4science.research.schemas import ScholarSearch
from gpt4science.settings import (
    DATA_PATH,
    GPT4_TURBO,
    NUMBER_SEARCH_QUERIES,
    OPENAI_API_KEY,
)
from gpt4science.structure.schemas import PaperStructure
from gpt4science.utils.prompt_templates import PydanticPromptTemplate

data_file = DATA_PATH / "creatine.json"


PRE_RESEARCH_PROMPT = f"""
You're a prompt engineer tasked with creating search prompts for Google Scholar for research paper source gathering.
You need to create search queries that will return the most relevant results.
Use notation available in the Google Scholar search bar to create the most accurate search queries.

number of queries: {NUMBER_SEARCH_QUERIES}
"""


def main():
    paper = PaperStructure.parse_file(data_file)
    model = ChatOpenAI(api_key=OPENAI_API_KEY, model=GPT4_TURBO)

    parser = PydanticOutputParser(pydantic_object=ScholarSearch)
    prompt = PydanticPromptTemplate(
        parser=parser,
        template="""
        {pre_research_prompt}
        title: {title}
        chapter: {chapter}
        sections: {sections}
        number of queries: {n_queries}
        """,
        input_variables=["title", "chapter", "sections"],
        partial_variables={
            "pre_research_prompt": PRE_RESEARCH_PROMPT,
            "n_queries": NUMBER_SEARCH_QUERIES,
        },
    )

    chain = prompt | model | parser

    result = chain.batch(
        [
            {
                "title": paper.paper_title,
                "chapter": chapter.chapter_name,
                "sections": str([section.section_name for section in chapter.sections]),
            }
            for chapter in paper.chapters
        ]
    )

    for scholar_search in result:
        print(scholar_search.queries)
