from typing import List, Optional
import math


class CountVectorizer:
    def __init__(self):
        self.feature_names = None

    def get_feature_names(self) -> Optional[List[str]]:
        return self.feature_names

    def fit_transform(self, text: List[str]) -> List[List[int]]:
        words_set = set()
        words_list = []
        doc_term_matrix = []

        # Building words set
        for sent in text:
            for word in sent.lower().split():
                if word not in words_set:
                    words_list.append(word)
                    words_set.add(word)

        self.feature_names = words_list

        # Building document term matrix
        for sent in text:
            counter = dict.fromkeys(words_list, 0)
            for word in sent.lower().split():
                counter[word] += 1

            doc_term_matrix.append(list(counter.values()))

        return doc_term_matrix


class TfidfTransformer:
    @staticmethod
    def tf_transform(count_matrix: List[List[int]]) -> List[List[float]]:
        if len(count_matrix) == 0:
            return []

        freq_mat = []

        for count_row in count_matrix:
            k_words = sum(count_row)
            freq_mat.append([count / k_words for count in count_row])
            # freq_mat.append(
            #     list(map(lambda count: count / k_words, count_row)))

        return freq_mat

    @staticmethod
    def idf_transform(count_matrix: List[List[int]]) -> List[float]:
        if len(count_matrix) == 0:
            return []

        idf_mat = []
        k_documents = len(count_matrix)
        k_tokens = len(count_matrix[0])

        for i in range(k_tokens):
            k_docs_with_ith_token = sum(
                count_matrix[j][i] > 0 for j in range(k_documents))
            idf = math.log((1 + k_documents) / (1 + k_docs_with_ith_token)) + 1
            idf_mat.append(round(idf, 1))

        return idf_mat

    def fit_transform(self, count_matrix: List[List[int]]) -> List[List[float]]:
        tf_matrix = TfidfTransformer.tf_transform(count_matrix)
        idf_matrix = TfidfTransformer.idf_transform(count_matrix)

        tf_idf_mat = []

        for tf_row in tf_matrix:
            tf_idf_row = [tf_row[i] * idf_matrix[i] for i in range(len(tf_row))]
            tf_idf_mat.append(list(map(lambda x: round(x, 3), tf_idf_row)))

        return tf_idf_mat


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self.transformer = TfidfTransformer()

    def fit_transform(self, text: List[str]) -> List[List[float]]:
        count_matrix = super().fit_transform(text)
        tf_idf_mat = self.transformer.fit_transform(count_matrix)

        return tf_idf_mat
