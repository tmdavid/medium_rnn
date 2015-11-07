__author__ = 'David'
import numpy as np

class DataModel:

    filename = ''
    file = ''

    def __init__(self):
        pass

    def open_file(self, filename):
        self.filename = filename
        self.file = open(filename, 'r').read().lower()
        print len(self.file)
        return self.file

    def prepare_dataset(self, text):
        chars = set(text)

        print chars

        print('total chars:', len(chars))
        char_indices = dict((c, i) for i, c in enumerate(chars))
        indices_char = dict((i, c) for i, c in enumerate(chars))
        print char_indices
        print indices_char
        maxlen = 20
        step = 3
        sentences = []
        next_chars = []
        for i in range(0, len(text) - maxlen, step):
            sentences.append(text[i: i + maxlen])
            next_chars.append(text[i + maxlen])
        print('nb sequences:', len(sentences))
        print('Vectorization...')
        X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
        y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
        for i, sentence in enumerate(sentences):
            for t, char in enumerate(sentence):
                X[i, t, char_indices[char]] = 1
            y[i, char_indices[next_chars[i]]] = 1

        return X, y, chars, char_indices, indices_char






