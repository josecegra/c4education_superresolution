# C4education Superresolution

Change the directory to the `model-api` folder of this repository and build the docker image:

`sudo docker build . --no-cache`

If successful, a docker image should be created with a certain id. To see the id of all your docker images run `sudo docker images`. Run the container mounting the `superresolution_data` directory previously created as a volume, and mapping the port 5050

`sudo docker run -p 127.0.0.1:5050:5050/tcp -v /home/jcejudo/superresolution_data:/superresolution_data <your_docker_image_id_here>`

The model api should run now in `http://0.0.0.0:5050/srapi`, and it accepts POST requests with a json body `{'input':'path/to/input','output':'path/to/output'}` containing the input path for the low-resolution image and the output path for the enhanced version. We can call the api with the client command line tool, which takes the input and output paths as arguments. 

`python client.py --input ../superresolution_data/low_resolution_img.jpg --output ../superresolution_data/low_resolution_img.jpg` 
