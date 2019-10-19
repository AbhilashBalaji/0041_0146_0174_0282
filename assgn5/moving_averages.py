import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = open("temperatures.csv", "r")

x = dataset.readline()
x = dataset.readlines()

dates = list()
snos = list()
temps = list()

for i in range(len(x)):
	a, b = x[i].strip().split(",")
	if b[0] == "?":
		b = b[1:]
	dates.append(a)
	temps.append(float(b))
	snos.append(i)

plt.plot(snos, temps)

