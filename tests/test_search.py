from search_engine.search_engine import (
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

    assert index == {
        "I": {"doc1": 0.0752574989159953},
        "can": {"doc1": 0.0752574989159953},
        "t": {"doc1": 0.0, 'doc2': 0.0},
        "shoot": {"doc1": 0.0, 'doc2': 0.0},
        "Don": {"doc2": 0.050171665943996864},
        "at": {"doc2": 0.050171665943996864},
        "me": {"doc2": 0.050171665943996864}
    }


def test_tf_idf():
    docs = []
    doc = {"id": "rabbit_here", "text": ""}
    for _ in range(97):
        doc["text"] += " yes"
    for _ in range(3):
        doc["text"] += " rabbit"
    for i in range(9999):
        docs.append({"id": f"{i}", "text": "no"})
    docs.append(doc)

    index = generate_index_for_docs_collection(docs)

    assert index["rabbit"] == {'rabbit_here': 0.12}


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
