import re


def search(documents: list[dict], target_word: str) -> list[str]:
    names_of_docs_with_target_string = []
    for document in documents:
        if is_target_string_in_document(document["text"], target_word):
            names_of_docs_with_target_string.append(document["id"])
    return names_of_docs_with_target_string


def is_target_string_in_document(document_text: str, target_word) -> bool:
    splited_text = document_text.split()
    for word in splited_text:
        processed_word = "".join(re.findall(r'\w+', word))
        if processed_word == target_word:
            return True
    return False


if __name__ == '__main__':
    search()
