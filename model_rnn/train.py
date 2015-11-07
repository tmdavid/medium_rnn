__author__ = 'David'

import keras
from data_model import DataModel as DM
from model import Model as M
import random
import numpy as np
import sys

data = DM()

data_input = data.open_file('..\posts_files\posts_Culture.txt')
X, y, chars, char_indices, indices_char = data.prepare_dataset(data_input)
model_class = M()

maxlen = 20
step = 3
sentences = []
next_chars = []

model = model_class.generate_model(data_input, maxlen)

for iteration in range(1, 60):
    print()
    print('-' * 50)
    print('Iteration', iteration)
    model.fit(X, y, batch_size=16, nb_epoch=1)

    start_index = random.randint(0, len(data_input) - maxlen - 1)

    for diversity in [0.2, 0.5, 1.0, 1.2]:
        print()
        print('----- diversity:', diversity)

        generated = ''
        sentence = data_input[start_index: start_index + maxlen]
        generated += sentence
        print('----- Generating with seed: "' + sentence + '"')
        sys.stdout.write(generated)

        for iteration in range(400):
            x = np.zeros((1, maxlen, len(chars)))
            for t, char in enumerate(sentence):
                x[0, t, char_indices[char]] = 1.

            preds = model.predict(x, verbose=0)[0]
            next_index = M.sample(preds, diversity)
            next_char = indices_char[next_index]

            generated += next_char
            sentence = sentence[1:] + next_char

            sys.stdout.write(next_char)
            sys.stdout.flush()
        print()







