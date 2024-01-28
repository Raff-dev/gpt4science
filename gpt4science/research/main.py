from __future__ import annotations

from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    PromptTemplate,
)
from langchain.schema import SystemMessage
from langchain.tools import tool
from langchain_openai.chat_models import ChatOpenAI

from gpt4science.research.models import SearchToolArgsSchema
from gpt4science.settings import (
    DATA_PATH,
    GPT4_TURBO,
    NUMBER_SEARCH_QUERIES,
    OPENAI_API_KEY,
)
from gpt4science.structure.schemas import PaperStructure

data_file = DATA_PATH / "test_paper.json"


@tool(args_schema=SearchToolArgsSchema, return_direct=True)
def gather_google_scholar_sources(queries: list[str]) -> str:
    """Search Google Scholar for sources related to the paper's topic."""
    return "\n".join(queries)


tools = [gather_google_scholar_sources]
paper = PaperStructure.parse_file(data_file)
llm = ChatOpenAI(api_key=OPENAI_API_KEY, model=GPT4_TURBO)


PRE_RESEARCH_PROMPT = f"""
You're a prompt engineer tasked with creating search prompts for Google Scholar for research paper source gathering.
You need to create search queries that will return the most relevant results.
Use notation available in the Google Scholar search bar to create the most accurate search queries.

number of queries: {NUMBER_SEARCH_QUERIES}
"""


def gather_pre_research():
    prompt = PromptTemplate(
        template="""
        {pre_research_prompt}
        topic: {topic}
        context: {context}
        number of queries: {n_queries}
        """,
        input_variables=["topic", "context", "n_queries"],
    ).partial(pre_research_prompt=PRE_RESEARCH_PROMPT, n_queries=NUMBER_SEARCH_QUERIES)

    agent = create_openai_functions_agent(llm=llm, tools=tools, prompt=prompt)
    chain = AgentExecutor(agent=agent, verbose=True, tools=tools)

    chain.invoke(
        {
            "topic": paper.topic,
            "context": paper.context,
        }
    )


def main():
    prompt = ChatPromptTemplate(
        messages=[
            SystemMessage(content=PRE_RESEARCH_PROMPT),
            HumanMessagePromptTemplate.from_template(
                template="""
                Make sure the search terms are not too specific or too broad.

                title: {title}
                chapter: {chapter}
                sections: {sections}
                """
            ),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ],
    )
    agent = create_openai_functions_agent(llm=llm, tools=tools, prompt=prompt)
    chain = AgentExecutor(agent=agent, verbose=True, tools=tools)

    chain.batch(
        [
            {
                "title": paper.title,
                "chapter": chapter.title,
                "sections": str([section.title for section in chapter.sections]),
            }
            for chapter in paper.chapters
        ]
    )


if __name__ == "__main__":
    main()
