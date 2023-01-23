import os
import tqdm
import fire
import numpy as np
from PIL import Image
from pathlib import Path
from ISR.models import RDN, RRDN

def main(*args):
    input_path = args[0]
    output_path = args[1]
    output_path, input_path = Path(output_path), Path(input_path)
    output_path.mkdir(parents=True,exist_ok=True)
    image_list = list(input_path.iterdir())
    print(f'Enhancing {len(image_list)} images')
    
    model = RDN(weights='noise-cancel')

    for img_path in tqdm.tqdm(image_list):
        img = Image.open(img_path)
        sr_img = model.predict(np.array(img))
        sr_img = Image.fromarray(sr_img)
        sr_img.save(output_path.joinpath(img_path.name))

    print('Finished')
     

if __name__=="__main__":
    fire.Fire(main)

