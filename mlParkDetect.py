#!/usr/bin/env python3
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import time
from pysolar.solar import *
import datetime
import os

import warnings
warnings.filterwarnings("ignore")

VERSION="1.0.0"

from obsyPark import ObsyPark
park=ObsyPark()
from obsyConfig import ObsyConfig
config=ObsyConfig()

# Set up logging
import logging
logFilename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'mlParkDetect.log')
logger = logging.getLogger()
fhandler = logging.FileHandler(filename=logFilename, mode='a')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.info("Program Start - mlParkDetect"+VERSION)
logger.setLevel(logging.DEBUG)

if os.name == 'nt':
	_ = os.system('cls')
else:
	_ = os.system('clear')
print ("mlParkDetect "+VERSION+" by Gord Tulloch report issues at https://github.com/gordtulloch/mlParkDetect ")

#######################################################################################
## DO NOT EDIT FROM HERE ON
#######################################################################################
while True:
	# Call the park object to determine if it's cloudy
	result,text=park.isParked()
	if result:
		logger.info("Parked: "+text)
	else:
		logger.info("Not Parked: "+text)
	# Wait for the next image
	time.sleep(60)
# End of program
