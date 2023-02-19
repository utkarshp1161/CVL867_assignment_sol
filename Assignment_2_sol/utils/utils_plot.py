import matplotlib.pyplot as plt
import numpy as np


plt.rcParams.update(
    {
        'font.family': 'sans-serif',
        'font.sans-serif': 'Helvetica',
        'font.size': 20,
    }
)

def plot(rand_walk, c = "bo", label="label", dim = 1):
    """Plot rand walk
    """
    plt.figure(figsize=(8.5,7))
    if dim == 1 :
        plot_, = plt.plot(rand_walk[0], c)
        plot_.set_label(label)
        return plot_

    if dim == 2 :
        plot_, = plt.plot(rand_walk[0], rand_walk[1])
        plot_.set_label(label)
        return plot_