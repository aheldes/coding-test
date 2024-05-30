from fastapi import FastAPI, Query, Depends

from dependencies import get_documents_by_tag
from schemas import Documents

app = FastAPI()


@app.get("/")
async def status():
    return {"Status": "OK"}


@app.get("/taggedContent", response_model=Documents, response_model_exclude_none=True)
def tagged_content(
        tag: str = Query(..., title="Tag", description="Tag to search for", min_length=1, max_length=50,
                         regex="^[a-zA-Z ]+$"),
        documents=Depends(get_documents_by_tag)):
    return documents
