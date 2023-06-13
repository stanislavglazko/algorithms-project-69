import math
import re
from collections import defaultdict


def search(documents: list[dict], target_string: str) -> list[str]:
    index = generate_index(documents)
    docs_with_target_words = find_docs_with_target_words(
        target_string, index
    )
    if docs_with_target_words:
        return get_docs_names_in_relevant_order(docs_with_target_words)
    return []


def generate_index(documents: list[dict]) -> dict[str, dict]:
    index = defaultdict(dict)
    number_of_words_in_documents = defaultdict(int)
    number_of_documents = len(documents)
    for document in documents:
        generate_index_for_doc(document, index, number_of_words_in_documents)
    calculate_tf_idf(index, number_of_documents, number_of_words_in_documents)
    return index


def generate_index_for_doc(
    document: dict[str, str],
    index: defaultdict,
    number_of_words_in_documents: dict[str, int],
) -> None:
    document_id, document_text = document["id"], document["text"]
    words = re.findall(r'\w+', document_text)
    number_of_words_in_documents[document_id] = len(words)
    for word in words:
        if document_id not in index[word]:
            index[word][document_id] = 1
        else:
            index[word][document_id] += 1


def calculate_tf_idf(
    index: defaultdict,
    number_of_documents: defaultdict,
    number_of_words_in_documents: int,
) -> None:
    for word, docs_with_word in index.items():
        idf = math.log10(number_of_documents / len(docs_with_word))
        for document, number_of_target_word_in_doc in docs_with_word.items():
            tf = number_of_target_word_in_doc / number_of_words_in_documents[
                document
            ]
            index[word][document] = tf * idf


def find_docs_with_target_words(
    target_string: str,
    index: dict[str, dict],
) -> dict[str, list]:
    target_words = target_string.split()
    docs_with_target_words = defaultdict(list)
    for target_word in target_words:
        if target_word not in index:
            continue
        for doc_id, tf_idf in index[target_word].items():
            if doc_id in docs_with_target_words:
                docs_with_target_words[doc_id][0] += 1
                docs_with_target_words[doc_id][1] *= tf_idf
            else:
                docs_with_target_words[doc_id].append(1)
                docs_with_target_words[doc_id].append(tf_idf)
    return docs_with_target_words


def get_docs_names_in_relevant_order(
    target_dict: dict[str, list],
) -> list[str]:
    return [
        document_name for document_name, _ in sorted(
            target_dict.items(), key=lambda item: item[1], reverse=True
        )
    ]
