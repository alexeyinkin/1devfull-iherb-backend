import pandas as pd
import numpy as np

from model import get_model
from constants import feature_count, substance_count

#def get_fit_model(filename: str):
def get_fit_model(filename):
    model = get_model()
    names = []

    for n in range(0, feature_count):
        names.append('f' + str(n + 1))

    for n in range(0, substance_count):
        names.append('s' + str(n + 1))

    names.append('o1')

    df_source = pd.read_csv(filename, sep='\t', names=names)

    labels = df_source.pop('o1')
    inputs = np.array(df_source)

    model.fit(inputs, labels, epochs=30)

    return model


#def fit_and_dump(data_filename: str, weights_filename: str):
def fit_and_dump(data_filename, weights_filename):
    model = get_fit_model(data_filename)
    model.save_weights(weights_filename)

fit_and_dump('random.tsv', 'weights.ckpt')
