from pydantic import BaseModel


class Documents(BaseModel):
    tag: str
    documents: list[str]
