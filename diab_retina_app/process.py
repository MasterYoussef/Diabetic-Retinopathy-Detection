import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import os
from skimage import io
import cv2

def process_img(img):
    
    np.set_printoptions(suppress=True)

    # Load the model
    model = tensorflow.keras.models.load_model(os.path.dirname(__file__) + '/my_model.h5')
    #model = tensorflow.keras.models.load_model(os.path.dirname(__file__) + '/keras_model.h5')
    #model = tensorflow.keras.models.load_model(os.path.dirname(__file__) + '/weights.h5')
    data = np.ndarray(shape=(1, 256, 256, 3), dtype=np.float32)
    #data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    image = Image.open(os.path.dirname(__file__) + '/test3/' + img)
    
    size = (256, 256)
    #size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)

    pred_new = prediction[0]
    pred = max(pred_new)

    print(pred_new)
    index = pred_new.tolist().index(pred)

    import matplotlib.pyplot as plt

    left = [0,1, 2, 3, 4]

    # heights of bars
    height = pred_new.tolist()
    new_height = []
    for i in height:
        new_height.append(round(i, 2) * 100)

    print(height)

    print(new_height)
    
    tick_label = ['pas de RD', 'legere', 'moderée', 'severe', 'proliferative']
    
    # plotting a bar chart
    plt.bar(left, new_height, tick_label=tick_label,
            width=0.15, color=['black','red'])


    # plot title
    plt.title('Diabetique detection')

    # function to show the plot
    plt.savefig(os.path.dirname(__file__) + '/output/graph.png')
    plt.show()
    result = []

    if index == 0:
        result.append("pas de RD")
    elif index == 1:
        result.append("legere")
    elif index == 2:
        result.append("modérée")
    elif index == 3:
        result.append("sévere")
    elif index == 4:
        result.append("proliferative")

    accuracy = round(pred, 2)
    result.append("-")
    result.append(accuracy * 100)
    return result
