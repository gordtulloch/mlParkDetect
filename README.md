# mlParkDetect
Telescope Park Detection using machine learning. 

This software will examine images from a camera of a telescope to determine whether it is parked or not.  The software will also detect in what direction the telescope is improperly parked (posDec,posRA,negDec,negRA) and issue corrective commands to the telescope until it is in the correct position, then adjust the INDI park position to the current safe position. For telescopes like mine where the scope needs to be parked for the roof to safely close, this is important. It is critical to a fully automated telescope where the telescope axis might slip or be impeded in some way that changes the encoded position of the axis so 
when the telescope tries to return to the park position it arrives at an unknown position.

Requires Python >= 3.10 if not using Windows executables. Currently does not support INDI 2.10.0 as PyIndiClient is broken.

Releases:
* None, still under active development

## Park detection model
The mlParkDetect program requires a Keras format model file to operate. You will need to train a model before using this software. Complete instructions TODO.

## INI File Parameters
The mlParkDetect.ini file supports the following parameters:

| Parameter | Default | Description |
|-----------|--------------------------------------------------------|---------------------------------------------------------------------|
| TRAINFOLDER | /home/$USER/mlParkDetect/train | Folder where training files are |
| KERASMODEL | mlParkDetect.keras | Model file to use/create |
| LATESTIMAGE | latest.jpg | Latest image of telescope to analyze |


## Installation in Python
To install and run mlParkDetect in Python, create a Python virtual environment (to avoid various package conflicts) and run the application from a terminal window.

    git clone https://github.com/gordtulloch/mlParkDetect.git
    cd mlParkDetect
    python3 -m venv .venv           
    source .venv/bin/activate        # in Linux
    .venv\scripts\activate.bat        # in Windows

    pip3 install -r requirements.txt
    python3 mlParkDetect.py

You need to get a jpg named latest.jpg from your observatory into the mlParkDetect folder or adjust the path of the program to point to it in the ini file. 

## Updating in Python

    cd mlParkDetect
    git pull

## Release Log
0.0.1 In active development

