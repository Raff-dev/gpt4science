from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    PromptTemplate,
)
from langchain.schema import SystemMessage

from gpt4science.prompting.templates import (
    RESEARCH_PAPER_TITLE_PROMPT,
    TABLE_OF_CONTENTS_PROMPT,
)

research_paper_title_prompt = PromptTemplate(
    template=RESEARCH_PAPER_TITLE_PROMPT,
    input_variables=["topic", "context"],
)

initialize_structure_prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=TABLE_OF_CONTENTS_PROMPT),
        HumanMessagePromptTemplate.from_template(
            """
            Topic: {topic}
            Context: {context}
            Title: {title}
            """
        ),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ],
    template=TABLE_OF_CONTENTS_PROMPT,
)
