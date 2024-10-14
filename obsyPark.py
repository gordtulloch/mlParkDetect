import keras
import sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageOps  # Install pillow instead of PIL


from obsyConfig import ObsyConfig
config=ObsyConfig()

import logging
logger = logging.getLogger("obsyPark")

sys.path.append(str(Path(__file__).parent.absolute().parent))

class ObsyPark(object):  
    def __init__(self):
        self.config = config
        logger.info('Using keras model: %s', config.get("KERASMODEL"))
        self.model = keras.models.load_model(config.get("KERASMODEL"), compile=False)

    def isParked(self):
        # Grab the image file from whereever 
        image_file = config.get("LATESTFILE")
        logger.info('Loading image: %s', image_file)

        result=self.detect(image_file)

        return (result.replace('\n', '') == 'Parked',result.replace('\n', ''))

    def detect(self, imagePath):
        # Load the labels
        class_names = open(config.get("KERASLABEL"), "r").readlines()

        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # Replace this with the path to your image
        image = Image.open(config.get("LATESTFILE")).convert("RGB")

        # resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

        # turn the image into a numpy array
        image_array = np.asarray(image)

        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

        # Load the image into the array
        data[0] = normalized_image_array

        # Predicts the model
        prediction = self.model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        # Print prediction and confidence score
        logger.info("Class:"+str(class_name[2:]))
        logger.info("Confidence Score:"+str(confidence_score))

        return(class_name[2:])

