# image creation

import replicate
import requests

prompt      = "a woman in lingerie posing on a city street, a comic book panel by Jason Felix, trending on cg society, art nouveau, ornate, fantasy, steampunk"
n_prompt    = "tiling, 2 heads, 2 faces, cropped image, out of frame, draft, deformed hands, signatures, twisted fingers, double image, long neck, malformed hands, multiple heads, extra limb, ugly, poorly drawn hands, missing limb, disfigured, cut-off, ugly, grain, low-res, Deformed, blurry, bad anatomy, disfigured, poorly drawn face, mutation, mutated, floating limbs, disconnected limbs, long body, disgusting, poorly drawn, mutilated, mangled, surreal, extra fingers, duplicate artefacts, morbid, gross proportions, missing arms, mutated hands, mutilated hands, cloned face, malformed"
height      = 720 # default 1024
width       = 1024 # default 1024
prompt_w    = 0.55 # -1 to 1
refine      = "expert_ensemble_refiner" # no_refiner, expert_ensemble_refiner, base_image_refiner
scale       = 10 # default 7.5 max 20
lora_source = "https://pbxt.replicate.delivery/dgeTJ4xBtfqZj0wGnbsoIMSm9sPI5lDzzeyxeQTmCtIeI17LC/trained_model.tar"
inference   = 8 # max 50 default 8
h_noise     = 0.8 # default 0.8 
s_lora      = 0.6 # default 0.6

class t2i:
    _instance = None  # Singleton instance
    
    output = replicate.run(
        # "alexgenovese/sdxl-lora:423422aecd2567600cd6456fdcaef85f21a772e9fa1512311be1eeb4aa0bb0d5",
        # "stability-ai/sdxl:2b017d9b67edd2ee1401238df49d75da53c523f36e363881e057f5dc3ed3c5b2", 
        "alexgenovese/sdxl:4b017dc7f7e71d1be25569c854897a433bb4a2bc285b6e1009fce5287d62806c",
        # "luosiallen/latent-consistency-model:553803fd018b3cf875a8bc774c99da9b33f36647badfd88a6eec90d61c5f62fc",
        input={
            "prompt": prompt,
            "negative_prompt" : n_prompt,
            "height": height,
            "width": width,
            "prompt_strength" : prompt_w,
            "refine": refine,
            "guidance_scale" : scale,
            "lora_url": lora_source,
            "lora_scale": s_lora,
            "num_inference_steps" : inference,
            "high_noise_frac" : h_noise
            },
    )

    output = output[0]

    print(output)

    response = requests.get(output)

    file = open("sample_image.png", "wb")
    file.write(response.content)
    file.close()

t2i_instance = t2i()
