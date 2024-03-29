from __future__ import annotations

from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.chains import LLMChain, SequentialChain
from langchain_openai.chat_models import ChatOpenAI

from gpt4science.settings import GPT4_TURBO, OPENAI_API_KEY
from gpt4science.structure.prompts import (
    initialize_structure_prompt,
    research_paper_title_prompt,
)
from gpt4science.structure.tools import initialize_structure_tool


def main():
    llm = ChatOpenAI(api_key=OPENAI_API_KEY, model=GPT4_TURBO)

    title_chain = LLMChain(
        llm=llm, prompt=research_paper_title_prompt, output_key="title", verbose=True
    )

    tools = [initialize_structure_tool]
    agent = create_openai_functions_agent(
        llm=llm, tools=tools, prompt=initialize_structure_prompt
    )
    structure_executor_chain = AgentExecutor(agent=agent, verbose=True, tools=tools)

    chain = SequentialChain(
        chains=[title_chain, structure_executor_chain],
        input_variables=["topic", "context"],
        verbose=True,
    )

    chain.invoke(
        {
            "topic": "creatine",
            "context": (
                "strength training, muscle protein synthesis, hypertrophy, performance,"
                "resistance training"
            ),
        }
    )
    # title = (
    #     "Enhancing Muscle Hypertrophy and Performance through Creatine"
    #     "Supplementation: Implications for Resistance Training Regimens"
    # )
