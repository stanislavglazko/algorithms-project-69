import re
from collections import defaultdict


def search(documents: list[dict], target_word: str) -> list[str]:
    docs_with_target_word = get_docs_with_target_word(
        documents, target_word,
    )
    return get_reverse_sorted_by_item_list_from_dict(docs_with_target_word)


def get_docs_with_target_word(documents: list[dict], target_word: str) -> dict:
    docs_with_target_word = {}
    for document in documents:
        number_of_repetitions_target_word = count_target_word_in_document(
            document["text"], target_word,
        )
        if number_of_repetitions_target_word:
            docs_with_target_word[
                document["id"]
            ] = number_of_repetitions_target_word
    return docs_with_target_word


def count_target_word_in_document(document_text: str, target_word) -> bool:
    number_of_repetitions_target_word = 0
    splited_text = document_text.split()
    for word in splited_text:
        if get_processed_word(word) == target_word:
            number_of_repetitions_target_word += 1
    return number_of_repetitions_target_word


def get_processed_word(word: str) -> str:
    return "".join(re.findall(r'\w+', word))


def get_reverse_sorted_by_item_list_from_dict(target_dict: dict):
    return [
        k for k, _ in sorted(
            target_dict.items(), key=lambda item: item[1], reverse=True
            )
        ]


def fuzzy_search(documents: list[dict], target_string: str) -> list[str]:
    target_words = target_string.split()
    docs_with_target_words = {}
    for target_word in target_words:
        docs_with_target_word = get_docs_with_target_word(
            documents, target_word
        )
        for doc_id, word_repetition in docs_with_target_word.items():
            if doc_id in docs_with_target_words:
                docs_with_target_words[doc_id][0] += 1
                docs_with_target_words[doc_id][1] += word_repetition
            else:
                docs_with_target_words[doc_id] = []
                docs_with_target_words[doc_id].append(1)
                docs_with_target_words[doc_id].append(word_repetition)
    return get_reverse_sorted_by_item_list_from_dict(docs_with_target_words)


def generate_index_for_docs_collection(documents: list[dict]) -> dict:
    index = defaultdict(list)
    for document in documents:
        generate_index_for_doc(document, index)
    return index


def generate_index_for_doc(document: dict, index: defaultdict) -> dict:
    splited_text = document["text"].split()
    for word in splited_text:
        processed_word = get_processed_word(word)
        if document["id"] not in index[processed_word]:
            index[processed_word].append(document["id"])


if __name__ == '__main__':
    search()
