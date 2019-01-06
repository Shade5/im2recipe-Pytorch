from trijoint import im2recipe
import torch

model = im2recipe()
model.visionMLP = torch.nn.DataParallel(model.visionMLP)
checkpoint = torch.load("data/model_3.pth")
model.load_state_dict(checkpoint)
print(model)