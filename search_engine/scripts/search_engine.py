import re
from collections import defaultdict


def search(documents: list[dict], target_word: str) -> list[str]:
    index = generate_index_for_docs_collection(documents)
    if target_word in index:
        return get_reverse_sorted_by_item_list_from_dict(index[target_word])
    return []


def generate_index_for_docs_collection(documents: list[dict]) -> dict:
    index = defaultdict(dict)
    for document in documents:
        generate_index_for_doc(document, index)
    return index


def generate_index_for_doc(document: dict, index: defaultdict) -> dict:
    splited_text = document["text"].split()
    for word in splited_text:
        processed_word = get_processed_word(word)
        if document["id"] not in index[processed_word]:
            index[processed_word][document["id"]] = 1
        else:
            index[processed_word][document["id"]] += 1


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
    index = generate_index_for_docs_collection(documents)
    for target_word in target_words:
        if target_word not in index:
            continue
        docs_with_target_word = index[target_word]
        for doc_id, word_repetition in docs_with_target_word.items():
            if doc_id in docs_with_target_words:
                docs_with_target_words[doc_id][0] += 1
                docs_with_target_words[doc_id][1] += word_repetition
            else:
                docs_with_target_words[doc_id] = []
                docs_with_target_words[doc_id].append(1)
                docs_with_target_words[doc_id].append(word_repetition)
    if docs_with_target_words:
        return get_reverse_sorted_by_item_list_from_dict(docs_with_target_words)
    return []


if __name__ == '__main__':
    search()
