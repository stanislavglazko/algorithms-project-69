from search_engine.scripts.search_engine import fuzzy_search, search


def test_relevant_search():
    checking_documents = create_docs()

    result = search(checking_documents, "shoot")

    assert result == ["doc2", "doc1"]


def test_fuzzy_search():
    checking_documents = create_docs_for_fyzzy_search()

    result = fuzzy_search(checking_documents, "shoot at me")

    assert result == ["doc2", "doc4", "doc1"]


def test_search_with_empty_docs():
    result = search([], "shoot")

    assert result == []


def create_docs() -> list[dict]:
    doc1 = {
        "id": "doc1",
        "text": "I can't shoot! straight unless I've had a pint!",
    }
    doc2 = {
        "id": "doc2",
        "text": "Don't shoot shoot shoot that thing at me.",
    }
    doc3 = {"id": "doc3", "text": "I'm your shooter."}
    return [doc1, doc2, doc3]


def create_docs_for_fyzzy_search() -> list[dict]:
    checking_documents = create_docs()
    new_doc = {
        "id": "doc4",
        "text": "Don't shoot that thing at me.",
    }
    return [*checking_documents, new_doc]
