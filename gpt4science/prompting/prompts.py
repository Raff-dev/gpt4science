from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    PromptTemplate,
)
from langchain.schema import SystemMessage

from gpt4science.prompting.templates import (
    PAPER_STRUCTURE_PROMPT,
    RESEARCH_PAPER_TITLE_PROMPT,
)

research_paper_title_prompt = PromptTemplate(
    template=RESEARCH_PAPER_TITLE_PROMPT,
    input_variables=["topic", "context"],
)

initialize_structure_prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=PAPER_STRUCTURE_PROMPT),
        HumanMessagePromptTemplate.from_template(
            """
            Topic: {topic}
            Context: {context}
            Title: {title}
            """
        ),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ],
    template=PAPER_STRUCTURE_PROMPT,
)
