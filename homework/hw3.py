from typing import List, Any


class CountVectorizer:
    """
    Convert a collection of text documents to a matrix of token counts.
    """

    def __init__(self):
        self._vocabulary = []

    @staticmethod
    def get_words(corpus: List[str]) -> List[str]:
        words: List[Any] = []
        for sentence in corpus:
            for word in sentence.lower().split(' '):
                if word not in words:
                    words.append(word)
        return words

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        self._vocabulary = self.get_words(corpus)
        count_matrix: List[List[int]] = []
        for sentence in corpus:
            count_words = dict.fromkeys(self._vocabulary, 0)
            for word in sentence.lower().split(' '):
                count_words[word] += 1
            count_matrix.append(list(count_words.values()))
        return count_matrix

    @property
    def get_feature_names(self):
        return self._vocabulary


if __name__ == '__main__':
    corp = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(corp)
    print(vectorizer.get_feature_names)
    print(matrix)
