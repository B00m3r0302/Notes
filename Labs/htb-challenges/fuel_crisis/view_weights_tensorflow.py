import tensorflow as tf

# Load the model
model = tf.keras.models.load_model('ai_ml_fuel_crisis/challenge/application/models/model.h5')

# View the model summary (this shows the layers and their shapes)
model.summary()
