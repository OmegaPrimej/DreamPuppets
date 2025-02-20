import torch
from torch import nn
from diffusers import StableDiffusionPipeline
from transformers import AutoFeatureExtractor

class StableDiffusionV1_4(nn.Module):
    def __init__(self):
        super(StableDiffusionV1_4, self).__init__()
        self.model_name = "CompVis/stable-diffusion-v1-4"
        self.feature_extractor = AutoFeatureExtractor.from_pretrained(self.model_name)
        self.pipeline = StableDiffusionPipeline.from_pretrained(self.model_name, torch_dtype=torch.float16)

    def generate_image(self, prompt):
        images = self.pipeline(prompt).images
        return images

Example usage:
model = StableDiffusionV1_4()
prompt = "A beautiful landscape with rolling hills and a sunset"
images = model.generate_image(prompt)
print(images)
