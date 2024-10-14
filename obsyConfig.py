#############################################################################################################
## C O N F I G                                                                                             ##
#############################################################################################################
# Object to retrieve configuration
import configparser
import os

import logging
logger = logging.getLogger('obsyConfig')

class ObsyConfig():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'mlParkDetect.ini')
        # Check if the file exists
        if not os.path.exists(self.file_path):
            logger.info("Config file not found, creating with defaults.")
            self.config['DEFAULT'] = {
                'LATESTFILE'    : '/home/gtulloch/mlParkDetect/latest.jpg',         # What the latest file is called
                'TRAINFOLDER'   : '/home/stellarmate/allskycam', # Folder where training files are
                'KERASMODEL'     : 'mlParkDetect.keras', # Model file to use
            }
            with open(self.file_path, 'w') as configfile:
                self.config.write(configfile)
                return      
    def get(self,keyword):
                self.config = configparser.ConfigParser()
                self.config.read(self.file_path)
                return self.config['DEFAULT'][keyword]

