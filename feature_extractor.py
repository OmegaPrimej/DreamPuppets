import torch
from transformers import AutoFeatureExtractor

class FeatureExtractor:
    def __init__(self):
        self.model_name = "CompVis/stable-diffusion-v1-4"
        self.feature_extractor = AutoFeatureExtractor.from_pretrained(self.model_name)

    def extract_features(self, images):
        inputs = self.feature_extractor(images, return_tensors="pt")
        return inputs

Example usage:
extractor = FeatureExtractor()
images = [...]  # input images
features = extractor.extract_features(images)
print(features)
