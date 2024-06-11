import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from OpenFolders import openFolder, getDownloadsFolders

def generatorByPromot(promp):
    model_id = "stabilityai/stable-diffusion-2-1"

    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    pipe = pipe.to("cuda")

    prompt = "a photo of an astronaut riding a horse on mars"
    image = pipe(prompt).images[0]

    folder = getDownloadsFolders();
    file   = "image_ia"
    index  = 0

    while os.path.isfile(folder / (file+".png")):
        index+= 1
        file = file+"_"+str(index)

    file = file+".png"
    image.save(folder / file)

    openFolder(folder)

if __name__ == "__main__":
    promp = input("Escribe tu promot de imagen")
    generatorByPromot(promp)