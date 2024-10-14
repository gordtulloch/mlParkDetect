import keras
import sys
import argparse
from pathlib import Path
import time
from datetime import datetime
from datetime import timedelta
import numpy as np
import cv2
import PIL
from PIL import Image
import logging
import sqlite3
import os

from obsyConfig import ObsyConfig
config=ObsyConfig()

logger = logging.getLogger("obsyPark")

# Suppress Tensorflow warnings
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

logger.setLevel(logging.INFO)

sys.path.append(str(Path(__file__).parent.absolute().parent))

class ObsyPark(object):
    CLASS_NAMES = (
        'Parked',
        'posDec',
        'posRA',
        'negDec',
        'negRA',
    )
    
    def __init__(self):
        self.config = config
        logger.info('Using keras model: %s', config.get("KERASMODEL"))
        self.model = keras.models.load_model(config.get("KERASMODEL"), compile=False)

    def isParked(self):
        # Grab the image file from whereever 
        image_file = config.get("LATESTFILE")
        logger.info('Loading image: %s', image_file)

        result=self.detect(image_file)

        return (result != 'Parked',result.replace('\n', ''))

    def detect(self, imagePath):
        # Load and preprocess the image
        image = Image.open(imagePath)
        image = image.resize((256, 256))
        image_array = np.array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)
        detect_start = time.time()

        # Predicts the model
        prediction = self.model.predict(image_array,verbose=0)
        idx = np.argmax(prediction)
        class_name = self.CLASS_NAMES[idx]
        confidence_score = (prediction[0][idx]).astype(np.float32)

        detect_elapsed_s = time.time() - detect_start
        logger.info('Park detection in %0.4f s', detect_elapsed_s)
        logger.info('Rating: %s, Confidence %0.3f', class_name, confidence_score)
        
        return(class_name)

