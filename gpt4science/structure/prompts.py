from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    PromptTemplate,
)
from langchain.schema import SystemMessage

RELEVANCE_CATEGORIES = ["irrelevant", "somewhat relevant", "relevant", "very relevant"]

RELEVANCE_ESTIMATION_PROMPT = f"""
Your estimates should be based on the following relevance categories:
Use notation of {RELEVANCE_CATEGORIES} to estimate the relevance of the source material.
"""


SOURECE_RELEVANCE_ESTIMATION_PROMPT = """
You're a research scientist supervisor tasked with estimating the relevance of source material for a research paper.
Given a topic and context, you need to estimate the relevance of the contents of the source material.
{ESTIMATION}

topic: {topic}
context: {context}
source_material: {source_material}
"""

CHAPTER_RELEVANCE_ESTIMATION_PROMPT = """
Given the chapter title of a research paper, you need to estimate the relevance of the chapter to the topic of the research paper.
{ESTIMATION}
"""


IMAGE_RELEVANCE_PROMPT = """
Find images. Function call to image ask and find relevance.
"""


REFERENCE_SEARCH_PROMPT = """
Given a paragraph of text, describe a question that it answers.
"""


research_paper_title_prompt = PromptTemplate(
    template="""
    You're a research scientist supervisor.
    Based on the topic and context, you need to come up with a research paper title.

    topic: {topic}
    context: {context}
    """,
    input_variables=["topic", "context"],
)


initialize_structure_prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(
            content="""
            You're a research scientist.
            Based on the topic, context, and paper title, your job is to come up with chapters and subchapters as a general structure in the form of a table of contents.
            Use tools available to create the table of contents.
            """
        ),
        HumanMessagePromptTemplate.from_template(
            """
            Topic: {topic}
            Context: {context}
            Title: {title}
            """
        ),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ],
)
