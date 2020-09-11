#file:///C:/Users/dstrube3/Documents/GitHub/test/masters/Deep-Learning-with-PyTorch.pdf
#https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html
#torchStuff.py
#pip3 install torch --user


#import numpy
#print("I can import numpy: " + numpy.__version__)

import torch
print("I can import torch: " + torch.__version__)

import torchvision
print("I can import torchvision: " + torchvision.__version__)

import torchaudio
print("I can import torchaudio: " + torchaudio.__version__)

#https://pytorch.org/mobile/android/
"""print("doing torchvision stuff...")
model = torchvision.models.resnet18(pretrained=True)
model.eval()
example = torch.rand(1, 3, 224, 224)
traced_script_module = torch.jit.trace(model, example)
traced_script_module.save("model.pt")
print("done")
"""

#https://pytorch.org/audio/
#https://pytorch.org/tutorials/beginner/audio_preprocessing_tutorial.html
import matplotlib.pyplot as plt

import os

maxX = 2
for x in range(1,maxX):
	filename = "torchStuff/"+str(x)+".wav"
	waveform, sample_rate = torchaudio.load(filename)
	os.system("afplay " + filename)
	print("Shape of waveform: {}".format(waveform.size()))
	print("Sample rate of waveform: {}".format(sample_rate))

	plt.figure()
	plt.plot(waveform.t().numpy())
	plt.show()
	if (x < maxX-1):
		input("Hit enter for next")