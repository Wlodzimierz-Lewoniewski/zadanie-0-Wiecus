import string

def get_documents_and_queries():
    n = int(input("Podaj liczbę dokumentów: "))
    documents = [input(f"Dokument {i + 1}: ") for i in range(n)]

    m = int(input("Podaj liczbę zapytań: "))
    queries = [input(f"Zapytanie {j + 1}: ").strip().lower() for j in range(m)]

    return documents, queries

def word_count_in_document(word, document):
    cleaned_doc = document.translate(str.maketrans('', '', string.punctuation)).lower()
    return cleaned_doc.split().count(word)

def process_queries(documents, queries):
    results = []

    for query in queries:
        cleaned_query = query.translate(str.maketrans('', '', string.punctuation))

        doc_occurrences = [(index, word_count_in_document(cleaned_query, doc))
                           for index, doc in enumerate(documents)]

        filtered_occurrences = [item for item in doc_occurrences if item[1] > 0]

        sorted_occurrences = sorted(filtered_occurrences, key=lambda x: (-x[1], x[0]))

        sorted_indexes = [index for index, _ in sorted_occurrences]

        results.append(sorted_indexes)


    return results

def main():
    documents, queries = get_documents_and_queries()
    results = process_queries(documents, queries)

    print("\nWyniki dla zapytań:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
