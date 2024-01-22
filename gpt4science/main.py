from __future__ import annotations

from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.chains import LLMChain, SequentialChain
from langchain_openai.chat_models import ChatOpenAI

from gpt4science.prompting.prompts import (
    initialize_structure_prompt,
    research_paper_title_prompt,
)
from gpt4science.settings import GPT4_TURBO, OPENAI_API_KEY
from gpt4science.tools import initialize_structure_tool


def main():
    llm = ChatOpenAI(api_key=OPENAI_API_KEY, model=GPT4_TURBO)

    tools = [initialize_structure_tool]
    agent = create_openai_functions_agent(
        llm=llm, tools=tools, prompt=initialize_structure_prompt
    )
    structure_executor_chain = AgentExecutor(agent=agent, verbose=True, tools=tools)

    title_chain = LLMChain(
        llm=llm, prompt=research_paper_title_prompt, output_key="title"
    )

    chain = SequentialChain(
        chains=[title_chain, structure_executor_chain],
        input_variables=["topic", "context"],
        verbose=True,
    )

    chain(
        {
            "topic": "quantum computing",
            "context": (
                "Quantum computing is a field that applies the laws of quantum "
                "mechanics to computational ability."
            ),
        }
    )


if __name__ == "__main__":
    main()
