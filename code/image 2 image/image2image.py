# modify image using control net

import replicate
import requests

image     = open("path to file", "rb")
model_type  = "canny" # canny, depth, hed, normal, mlsd, scribble, seg, openpose
prompt      = "beautiful flower"
num_sample  = "1" # 1 or 4
res         = "512" # 256, 512, 768
ddim_steps  = 20
scale       = 8 # (0.1-30)
a_prompt    = "" # additional prompt
n_prompt    = "tiling, 2 heads, 2 faces, cropped image, out of frame, draft, deformed hands, signatures, twisted fingers, double image, long neck, malformed hands, multiple heads, extra limb, ugly, poorly drawn hands, missing limb, disfigured, cut-off, ugly, grain, low-res, Deformed, blurry, bad anatomy, disfigured, poorly drawn face, mutation, mutated, floating limbs, disconnected limbs, long body, disgusting, poorly drawn, mutilated, mangled, surreal, extra fingers, duplicate artefacts, morbid, gross proportions, missing arms, mutated hands, mutilated hands, cloned face, malformed"
low_threshold   = 100 # canny model only (1-255)
high_threshold  = 200 #canny model only (1-255)
bg_threshold    = 0 # normal model only (0-1)
value_threshold = 0.1 # mlsd only (0.1-2)
distance_threshold  = 0.1 #mlsd only (0.1-20)
detect_resolution   = 512 # 128 - 1024

class i2m:
    output = replicate.run(
        "jagilley/controlnet:8ebda4c70b3ea2a2bf86e44595afb562a2cdf85525c620f1671a78113c9f325b",
        input={
            "image": image,
            "model_type": model_type,
            "prompt": prompt,
            "num_samples": num_sample,
            "image_resolution" : res,
            "ddim_steps": ddim_steps,
            "scale": scale,
            "a_prompt": a_prompt,
            "n_prompt": n_prompt,
            "detect_resolution": detect_resolution,
            "low_threshold": low_threshold,
            "high_threshold": high_threshold,
            "bg_threshold": bg_threshold,
            "value_threshold": value_threshold,
            "distance_threshold": distance_threshold
            }
    )

    my_list = output
    output = my_list[1]
    print(output)

    response = requests.get(output)

    file = open("sample_image.png", "wb")
    file.write(response.content)
    file.close()

i2m.instance = i2m()

# link : https://replicate.com/jagilley/controlnet/api