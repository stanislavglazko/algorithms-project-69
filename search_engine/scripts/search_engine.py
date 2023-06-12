import re


def search(documents: list[dict], target_word: str) -> list[str]:
    docs_with_target_word = {}
    for document in documents:
        number_of_repetitions_target_word = count_target_word_in_document(
            document["text"], target_word,
        )
        if number_of_repetitions_target_word:
            docs_with_target_word[
                document["id"]
            ] = number_of_repetitions_target_word
    return sorted(docs_with_target_word, reverse=True)


def count_target_word_in_document(document_text: str, target_word) -> bool:
    number_of_repetitions_target_word = 0
    splited_text = document_text.split()
    for word in splited_text:
        processed_word = "".join(re.findall(r'\w+', word))
        if processed_word == target_word:
            number_of_repetitions_target_word += 1
    return number_of_repetitions_target_word


if __name__ == '__main__':
    search()
