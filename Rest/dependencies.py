import json
import os

from fastapi.exceptions import HTTPException

from schemas import Documents


def find_tag_data(data, tag):
    if isinstance(data, dict):
        if tag in data:
            return data[tag]
        else:
            for subkey in data:
                result = find_tag_data(data[subkey], tag)
                if result is not None:
                    return result
    return None


def get_all_documents(data):
    documents = []
    if "tags" not in data:
        return data['documents']
    else:
        documents.extend(data['documents'])
        for child_data in data['tags'].values():
            documents.extend(get_all_documents(child_data))
    return documents


def get_documents_uris(document_data, documents):
    for key, value in document_data.items():
        if key in documents:
            yield value


def get_documents_by_tag(tag: str):
    file_path = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    tag_data = find_tag_data(data['tags'], tag)
    if not tag_data:
        raise HTTPException(status_code=404, detail="No documents found for the given tag")
    return Documents(tag=tag, documents=list(get_all_documents(tag_data)))
