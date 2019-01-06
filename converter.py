from trijoint import im2recipe
import torch

model = im2recipe()
model.visionMLP = torch.nn.DataParallel(model.visionMLP)
checkpoint = torch.load("data/model_e220_v-4.700.pth.tar")
model.load_state_dict(checkpoint['state_dict'])
# torch.save(model.state_dict(), "data/model_3.pth")