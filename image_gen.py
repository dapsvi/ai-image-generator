import replicate
import requests
import os

os.environ["REPLICATE_API_TOKEN"] = "YOUR_API_TOKEN"

def prompt_link(p):
    output = replicate.run(
      "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
      input={"prompt": p}
    )
    return output[0]

def prompt(p, file_name):
    link = prompt_link(p)
    img_data = requests.get(link).content
    with open('./' + file_name + '.png', 'wb') as handler:
        handler.write(img_data)

if __name__ == "__main__":
    prompt("Beautiful night sky with lots of stars", "night-sky-stars")