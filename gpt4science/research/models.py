from pydantic.v1 import BaseModel


class SearchToolArgsSchema(BaseModel):
    queries: list[str]
