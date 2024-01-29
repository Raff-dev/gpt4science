from invoke import Context, task

from gpt4science.research.main import main as research_main
from gpt4science.structure.main import main as structure_main


@task
def research(_: Context):
    research_main()


@task
def structure(_: Context):
    structure_main()
