RESEARCH_PAPER_TITLE_PROMPT = """
You're a research scientist supervisor.
Based on the topic and context, you need to come up with a research paper title.

topic: {topic}
context: {context}
"""

PAPER_STRUCTURE_PROMPT = """
You're a research scientist.
Based on the topic, context, and paper title, your job is to come up with chapters and a general structure in the form of a table of contents.
Use initialize_structure to create the paper structure.

topic: {topic}
context: {context}
title: {title}
"""

RELEVANCE_CATEGORIES = ["irrelevant", "somewhat relevant", "relevant", "very relevant"]

RELEVANCE_ESTIMATION_PROMPT = f"""
Your estimates should be based on the following relevance categories:
Use notation of {RELEVANCE_CATEGORIES} to estimate the relevance of the source material.
"""

SEARCH_PROMPT = """
You're a prompt engineer tasked with creating search prompts for Google Scholar for research paper source gathering.
Given a topic and context, you need to create n search queries that will return the most relevant results.
Use notation available in the Google Scholar search bar to create the most accurate search queries.
Respond only with the search queries separated by newlines.

topic: {topic}
context: {context}
n: {n}

Search queries:
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
