## Command Line Interface

Create and activate a virtual environment

`python3 -m venv virtualenv`

`source virtualenv/bin/activate`


Install dependencies

`python3 -m pip install --upgrade pip`

`python3 -m pip install --upgrade Pillow`

`pip install git+https://github.com/josecegra/image-super-resolution.git`

`pip install fire`

Prepare a folder containing the images to be enhanced. Run the `cli.py` script including the input folder followed by output folder as arguments

`python3 cli.py ../../data/low_resolution ../../data/high_resolution`