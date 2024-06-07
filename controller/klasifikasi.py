import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the saved model
model = tf.keras.models.load_model('cnn_model.h5')

# Define class labels
class_labels = {
    0: 'Daun Sehat',
    1: 'Penyakit Ceratoma trifurcata',
    2: 'Penyakit Cercospora',
    3: 'Penyakit Daun Bintik',
    4: 'Penyakit Malformasi'
}

def classify_image(img_path):
    img_height, img_width = 150, 150  # Ukuran gambar sesuai dengan yang digunakan saat training

    img = image.load_img(img_path, target_size=(img_height, img_width))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the image

    # Predict the class
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)[0]
    confidence = np.max(predictions)

    # Get the label of the predicted class
    predicted_label = class_labels[predicted_class]

    return predicted_label, confidence
