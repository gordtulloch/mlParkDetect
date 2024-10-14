# mlParkDetect
Telescope Park Detection using machine learning. 

This software will examine images from a camera of a telescope to determine whether it is parked or not.  The software will also detect in what direction the telescope is improperly parked (posDec,posRA,negDec,negRA) and issue corrective commands to the telescope until it is in the correct position, then adjust the INDI park position to the current safe position. For telescopes like mine where the scope needs to be parked for the roof to safely close, this is important. It is critical to a fully automated telescope where the telescope axis might slip or be impeded in some way that changes the encoded position of the axis so 
when the telescope tries to return to the park position it arrives at an unknown position.

Requires Python >= 3.10 if not using Windows executables. Currently does not support INDI 2.10.0 as PyIndiClient is broken.

Releases:
* None, still under active development

## Park detection model
The mlParkDetect program requires a Keras format model file to operate. You will need to train a model before using this software. Use 

https://teachablemachine.withgoogle.com

to create your model. Labels where you should provide data are: negDec,posDec,Parked,negRA,posRA. 

## INI File Parameters
The mlParkDetect.ini file supports the following parameters:

| Parameter | Default | Description |
|-----------|--------------------------------------------------------|---------------------------------------------------------------------|
| KERASMODEL | model/keras_model.h5 | Model file to use/create |
| KERASLABEL | model/labels.txt | Model file to use/create |
| LATESTIFILE | latest.jpg | Latest image of telescope to analyze |

## Installation in Python
To install and run mlParkDetect in Python, create a Python virtual environment (to avoid various package conflicts) and run the application from a terminal window. The following instructions are for Ubuntu. You may need to adjust the package names for other Linux distributions. 

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update 
    sudo apt --assume-yes install python3.10 python3.10-venv g++ libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libncurses5-dev \
        libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev libpng-dev libnova-dev libdbus-1-dev libdbus-glib-1-2 \
        libdbus-glib-1-dev swig cmake libindi-dev git-all wget curl llvm unzip software-properties-common
    git clone https://github.com/gordtulloch/mlParkDetect.git
    cd mlParkDetect
    mkdir model
    python3 -m venv .venv             # Note that if the correct Python version is not the only one installed you should specify the version eg python3.8
    pip3 install git+https://github.com/indilib/pyindi-client.git
    source .venv/bin/activate        # in Linux, do this every time you run the program to set up the virtual environment
    pip3 install -r requirements.txt
    python3 mlParkDetect.py

You need to get a jpg named latest.jpg from your observatory into the mlParkDetect folder or adjust the path of the program to point to it in the ini file.  

## Updating

    cd mlParkDetect
    git pull
    source .venv/bin/activate
    pip3 install -r requirements.txt 

## Release Log
0.0.1 In active development, currently testing Parked,negDec,posDec model.

