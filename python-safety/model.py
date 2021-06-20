import tensorflow as tf
from constants import feature_count, substance_count

input_count = feature_count + substance_count

def get_model():
    # Создаём нейронную сеть из трёх слоёв.
    # TODO: Определить количество нейронов в промежуточном слое после получения реальных данных
    #       и замера эффективности обучения.
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(input_count),
        tf.keras.layers.Dense(input_count * 2, activation='relu'),
        tf.keras.layers.Dense(1),
    ])
    model.compile(loss = tf.losses.MeanSquaredError(), optimizer = tf.optimizers.Adam())
    return model
