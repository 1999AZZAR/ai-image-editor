# image to prompt

import replicate

image = open("path to file", "rb")

class i2t:
    response = replicate.run(
        "methexis-inc/img2prompt:50adaf2d3ad20a6f911a8a9e3ccf777b263b8596fbd2c8fc26e8888f8a0edbb5", 
        input={
            "image": image
            }
    )
    print(response)

i2t_instance = i2t()

# link : https://replicate.com/methexis-inc/img2prompt
