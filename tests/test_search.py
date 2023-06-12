from search_engine.scripts.search_engine import (
    generate_index_for_docs_collection,
    search,
)


def test_relevant_search():
    checking_documents = create_docs()

    result = search(checking_documents, "shoot")

    assert result == ["doc2", "doc1"]


def test_fuzzy_search():
    checking_documents = create_docs_for_fuzzy_search()

    result = search(checking_documents, "shoot at me")

    assert result == ["doc2", "doc4", "doc1"]


def test_search_with_empty_docs():
    result = search([], "shoot")

    assert result == []


def test_generating_index():
    checking_documents = create_docs_to_test_index()

    index = generate_index_for_docs_collection(checking_documents)

    # assert index == {
    #     "I": {"doc1": 1},
    #     "cant": {"doc1": 1},
    #     "shoot": {"doc1": 1, "doc2": 2},
    #     "Dont": {"doc2": 1},
    #     "at": {"doc2": 1},
    #     "me": {"doc2": 1},
    # }
    assert index == {
        'I': {'doc1': 0.23104906018664842},
        'cant': {'doc1': 0.23104906018664842},
        'shoot': {'doc1': 0.0, 'doc2': 0.0},
        'Dont': {'doc2': 0.13862943611198905},
        'at': {'doc2': 0.13862943611198905},
        'me': {'doc2': 0.13862943611198905}
        }


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


def create_docs_to_test_index() -> list[dict]:
    doc1 = {
        "id": "doc1",
        "text": "I can't shoot!",
    }
    doc2 = {
        "id": "doc2",
        "text": "Don't shoot shoot at me.",
    }
    return [doc1, doc2]


def create_docs_for_fuzzy_search() -> list[dict]:
    checking_documents = create_docs()
    new_doc = {
        "id": "doc4",
        "text": "Don't shoot that thing at me.",
    }
    return [*checking_documents, new_doc]
