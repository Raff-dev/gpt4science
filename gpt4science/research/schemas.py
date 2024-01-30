from pydantic.v1 import BaseModel


class ScholarSearch(BaseModel):
    queries: list[str]
