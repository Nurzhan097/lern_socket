import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # for render 3d

matplotlib.rc("font", size=18)  # font size large

houses = pd.read_csv("houses.csv")
houses.head(7)

fig = plt.figure(figsize=(10, 10))  # create image
ax = plt.axes()


