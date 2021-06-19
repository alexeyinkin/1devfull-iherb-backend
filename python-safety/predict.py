import numpy as np
from model import get_model

def get_trained_model():
    model = get_model()
    model.load_weights('weights.ckpt')
    return model

#model = get_fit_model('random.tsv')
#inputs_raw = [[0,0,0,0,0]]
#inputs_np = np.array(inputs_raw)

#print(model.predict(inputs_np))
