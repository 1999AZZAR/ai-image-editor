# Image Creation Using Text Prompts

## Overview

This repository contains a Python script that utilizes the [Replicate Image Creation API](https://replicate.com) to generate images from text prompts. You can create unique and imaginative visuals using descriptive text as input.

## Requirements

Before using this script, ensure you have the following requirements in place:

- Python 3.x
- The `replicate` library
- An API key or access to the Replicate Image Creation API, which you can obtain from [Replicate](https://replicate.com)
- Optionally, you can choose one of the provided models (uncomment the desired model in the code).

## Getting Started

Follow these steps to get started with image creation from text prompts:

1. Clone or download this repository to your local machine.

2. Make sure you have the necessary Python packages installed. You can install the required packages using pip:

    ```bash
    pip install replicate requests
    ```

3. Open the `text2image.py` file and update the following parameters:

   - `prompt`: Define a descriptive text prompt to generate the image.
   - `n_prompt`: Specify any negative prompts that influence the image generation.
   - `height` and `width`: Set the dimensions of the generated image (default is 1024x1024).
   - `prompt_w`: Adjust the prompt strength (-1 to 1).
   - `refine`: Choose the refining method ("no_refiner," "expert_ensemble_refiner," or "base_image_refiner").
   - `scale`: Define the guidance scale (default is 7.5, max 20).
   - `lora_source`: Set the source for the LoRA model.
   - `inference`: Define the number of inference steps (default is 8, max 50).
   - `h_noise`: Specify the high noise fraction (default is 0.8).
   - `s_lora`: Set the LoRA scale (default is 0.6).

4. Save your changes.

5. Execute the `text2image.py` script.

## Output

The generated image will be saved as "sample_image.png" in the same directory where the script is located.

## Additional Information

You can find more details about the models and the Replicate Image Creation API on the respective links:

- [Alex Genovese's SDXL-LoRA](https://replicate.com/alexgenovese/sdxl-lora)
- [Stability AI's SDXL](https://replicate.com/stability-ai/sdxl)
- [Alex Genovese's SDXL](https://replicate.com/alexgenovese/sdxl)
- [Luosiallen's Latent Consistency Model](https://replicate.com/luosiallen/latent-consistency-model)

## Acknowledgments

- Thanks to [Replicate](https://replicate.com) for providing access to the Replicate Image Creation API.

Explore the various models and prompts to unleash your creativity and generate captivating images from text descriptions!

---

## support

You can support me by buy me a coffee if u like to.
<div align="left">
  <a href="https://www.buymeacoffee.com/azzar" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 42px !important;width: 151.9px !important; margin-top: 50px !important;">
  </a>
</div>
