import math
import re
from collections import defaultdict


def search(documents: list[dict], target_string: str) -> list[str]:
    index = generate_index_for_docs_collection(documents)
    docs_with_target_words = generate_docs_with_target_words(
        target_string, index
    )
    print(docs_with_target_words, "HHHHHHH")
    if docs_with_target_words:
        return convert_docs_with_target_words_to_sorted_list_of_docs(
            docs_with_target_words
        )
    return []


def generate_index_for_docs_collection(
    documents: list[dict],
) -> dict[str, dict]:
    index = defaultdict(dict)
    lengths_of_docs = defaultdict(int)
    length_of_docs_collection = len(documents)
    for document in documents:
        generate_index_for_doc(document, index, lengths_of_docs)
    calculate_tf_idf(index, length_of_docs_collection, lengths_of_docs)
    return index


def generate_index_for_doc(
    document: dict[str, str],
    index: defaultdict,
    lengths_of_docs: dict[str, int],
) -> None:
    document_id, document_text = document["id"], document["text"]
    splited_text = document_text.split()
    lengths_of_docs[document_id] = len(splited_text)
    for word in splited_text:
        processed_word = get_processed_word(word)
        if document_id not in index[processed_word]:
            index[processed_word][document_id] = 1
        else:
            index[processed_word][document_id] += 1


def get_processed_word(word: str) -> str:
    return "".join(re.findall(r'\w+', word))


def calculate_tf_idf(
    index: defaultdict,
    length_of_docs_collection: defaultdict,
    lengths_of_docs: int,
) -> None:
    for word, docs_with_word in index.items():
        idf = math.log10(length_of_docs_collection / len(docs_with_word))
        for doc, number in docs_with_word.items():
            tf = number / lengths_of_docs[doc]
            index[word][doc] = tf * idf


def generate_docs_with_target_words(
    target_string: str,
    index: dict[str, dict],
) -> dict[str, list]:
    target_words = target_string.split()
    docs_with_target_words = {}
    for target_word in target_words:
        if target_word not in index:
            continue
        for doc_id, word_repetition in index[target_word].items():
            if doc_id in docs_with_target_words:
                docs_with_target_words[doc_id] += word_repetition
            else:
                docs_with_target_words[doc_id] = word_repetition
    return docs_with_target_words


def convert_docs_with_target_words_to_sorted_list_of_docs(
    target_dict: dict[str, list],
) -> list[str]:
    return [
        k for k, _ in sorted(
            target_dict.items(), key=lambda item: item, reverse=True
            )
        ]
