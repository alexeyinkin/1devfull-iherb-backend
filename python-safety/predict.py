import numpy as np
from model import get_model

def get_trained_model():
    model = get_model()
    model.load_weights('weights.ckpt')
    return model
