from search_engine.scripts.search_engine import search


def test_search():
    checking_documents = create_docs()

    result = search(checking_documents, "shoot")

    assert result == ["doc1", "doc2"]


def test_search_with_empty_docs():
    result = search([], "shoot")

    assert result == []


def create_docs() -> list[dict]:
    doc1 = {
        "id": "doc1",
        "text": "I can't shoot straight unless I've had a pint!",
    }
    doc2 = {
        "id": "doc2",
        "text": "Don't shoot shoot shoot that thing at me.",
    }
    doc3 = {"id": "doc3", "text": "I'm your shooter."}
    return [doc1, doc2, doc3]
