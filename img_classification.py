# import the necessary packages
import numpy as np
import argparse
import cv2
from keras.preprocessing.image import img_to_array
from keras.models import model_from_json
from keras.preprocessing import image
# from keras.models import model

# construct the argument parse and parse the arguments
"""
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])
orig = image.copy()
"""

# dimensions of our images
# img_width, img_height = 150, 150 # 1st
# img_width, img_height = 1356, 694 # 2nd
img_width, img_height = 500, 150 #3rd

"""
# load the model we saved
# model = load_model('first_try1.h5')
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
"""

# load weights and model JSON
json_file = open('final.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)

# load weights into new model
model.load_weights("final.h5")

# predicting images
img = image.load_img('wrong2.png', target_size=(img_width, img_height))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

images = np.vstack([x])
classes = model.predict_classes(images, batch_size=10)
# print classes

"""
# predicting multiple images at once
img = image.load_img('test2.jpg', target_size=(img_width, img_height))
y = image.img_to_array(img)
y = np.expand_dims(y, axis=0)
"""

# pass the list of multiple images np.vstack()
# images = np.vstack([x, y])
classes = model.predict_classes(images, batch_size=10)

# classes_withinfo = model.predict_proba(images, batch_size=10)
# print(classes_withinfo)

if classes == 0:
    print "Img - Yes"
else:
    print "Img - No"

# print the classes, the images belong to
# print classes
