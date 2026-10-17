import numpy as np
import matplotlib.pyplot as aaa_plt

def main():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    aaa_plt.plot(x, y)
    aaa_plt.show()

if __name__ == "__main__":
    main()