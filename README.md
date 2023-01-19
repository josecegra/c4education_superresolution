# Enhancing low-resolution images - C4education

Change the directory to the `model-api` folder of this repository and build the docker image:

`docker build . --no-cache`

If successful, a docker image should be created with a certain id. To see the id of all your docker images run `docker images`.

Create a directory called `data` for instance containing the target images. Run the container mounting th `data` directory previously created as a volume, and mapping the port 8888

`docker run -p 0.0.0.0:8888:8888/tcp -v /home/user/data:/data <your_docker_image_id_here>`

The model api should run now in `http://localhost:8888/srapi`, and it accepts POST requests with a json body `{'input':'path/to/input','output':'path/to/output'}` containing the input path for the low-resolution image and the output path for the enhanced version. We can call the api with the client command line tool, which takes the input and output paths as arguments. 

`python client.py --input ../data/[ph]117[ph]HKMS000005_km003abz.jpg --output ../data/high_resolution_img.jpg` 


