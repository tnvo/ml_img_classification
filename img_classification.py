# import the necessary packages
import numpy as np
import argparse
# import cv2
from keras.preprocessing.image import img_to_array
from keras.models import model_from_json
from keras.preprocessing import image

def run():
    # dimensions of our images
    img_width, img_height = 500, 150 #3rd


    # load weights and model JSON
    json_file = open('final.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)

    # load weights into new model
    model.load_weights("final.h5")

    # predicting images
    img = image.load_img('phish.png', target_size=(img_width, img_height))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict_classes(images, batch_size=10)

    # pass the list of multiple images np.vstack()
    # images = np.vstack([x, y])
    classes = model.predict_classes(images, batch_size=10)

    if classes == 0:
        return "Class 1 - Yes"
    else:
        return "Class 2 - No"

    # print the classes, the images belong to
    # print classes
