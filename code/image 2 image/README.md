# Image to image Modification Using ControlNet

## Overview

This repository contains a Python script that leverages the [ControlNet](https://replicate.com/jagilley/controlnet) API to modify images based on a variety of control parameters. ControlNet is a powerful tool that can transform images in a creative and controlled way.

## Requirements

Before using this script, make sure you have the following requirements in place:

- Python 3.x
- The `replicate` library
- An image file that you want to modify (referenced as "path to file" in the code)
- An API key or access to the ControlNet API, which you can obtain from [Replicate](https://replicate.com)

## Getting Started

Follow these steps to get started with image modification using ControlNet:

1. Clone or download this repository to your local machine.

2. Make sure you have the necessary Python packages installed. You can install the required packages using pip:

    ```bash
    pip install replicate requests
    ```

3. Open the `image2image.py` file and update the following parameters:

   - `image`: Replace "path to file" with the path to the image you want to modify.
   - `model_type`: Choose one of the available models ("canny," "depth," "hed," "normal," "mlsd," "scribble," "seg," "openpose") to define the image modification style.
   - `prompt`: Set the text prompt for the image modification.
   - `num_sample`: Specify the number of samples to generate (1 or 4).
   - `res`: Define the image resolution (256, 512, 768).
   - `ddim_steps`: Adjust the number of steps for ddim transformation (e.g., 20).
   - `scale`: Set the scale for image transformation (0.1 - 30).
   - `a_prompt`: Add any additional prompts (if needed).
   - `n_prompt`: Define a list of negative prompts to influence the modification.
   - `low_threshold` and `high_threshold`: Specify thresholds for the Canny model (1 - 255).
   - `bg_threshold`: Set the background threshold for the normal model (0 - 1).
   - `value_threshold` and `distance_threshold`: Define thresholds for the MLS (Multi-Level Style Disentanglement) model.
   - `detect_resolution`: Set the resolution for detection (128 - 1024).

4. Save your changes.

5. Execute the `image2image.py` script.

## Output

The modified image will be saved as "sample_image.png" in the same directory where the script is located.

## Additional Information

- You can find more details about the ControlNet API [here](https://replicate.com/jagilley/controlnet/api).

## Acknowledgments

- Thanks to [Replicate](https://replicate.com) for providing access to the ControlNet API.

Feel free to explore and experiment with the ControlNet API to create unique and intriguing image modifications!
