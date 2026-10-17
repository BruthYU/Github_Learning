import numpy as np
import matplotlib.pyplot as aaa_plt

def plot_data(x, y):
    aaa_plt.scatter(x, y)
    aaa_plt.show()

def main():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([1, 2, 3, 4, 5])
    plot_data(x, y)

if __name__ == "__main__":
    main()