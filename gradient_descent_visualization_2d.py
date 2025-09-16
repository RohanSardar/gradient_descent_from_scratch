import numpy as np
import matplotlib.pyplot as plt

def y_function(x):
    return x**4 - 10*x**2 + 9

def y_derivative(x):
    return 4*x**3 - 20*x

x = np.linspace(-4, 4, 1000)
y = y_function(x)
min_y = min(y)

current_x0 = 3.8
current_x1 = 0.2

learning_rate = 0.0004

path_x0 = []
path_y0 = []

path_x1 = []
path_y1 = []

plt.ion()  

for i in range(500):
    current_y0 = y_function(current_x0)
    current_y1 = y_function(current_x1)

    path_x0.append(current_x0)
    path_y0.append(current_y0)

    path_x1.append(current_x1)
    path_y1.append(current_y1)

    plt.plot(x, y, label="f(x) = x^4 + 10x^2 + 9", color='lime')

    plt.plot(path_x0, path_y0, '-.', color='brown', label="Descent Path (Point 1)")
    plt.scatter(current_x0, current_y0, color='brown', s=100, label='Point 1')

    plt.plot(path_x1, path_y1, '-.', color='deeppink', label="Descent Path (Point 2)")
    plt.scatter(current_x1, current_y1, color='deeppink', s=100, label='Point 2')

    plt.title(f"Gradient Descent - Iteration {i}")
    plt.xlabel("x")
    plt.ylabel("y = f(x)")
    plt.ylim(min_y-5, 100)
    plt.grid(True, color='wheat')
    plt.legend()
    plt.pause(0.01)
    plt.clf()

    current_x0 -= learning_rate * y_derivative(current_x0)
    current_x1 -= learning_rate * y_derivative(current_x1)

plt.ioff()
plt.plot(x, y, label="f(x) = x^4 + 10x^2 + 9", color='lime')

plt.plot(path_x0, path_y0, '--', color='brown', label="Descent Path (Point 1)")
plt.scatter(current_x0, y_function(current_x0), color='brown', s=100, label="Final Position (Point 1)")

plt.plot(path_x1, path_y1, '--', color='deeppink', label="Descent Path (Point 2)")
plt.scatter(current_x1, y_function(current_x1), color='deeppink', s=100, label="Final Position (Point 2)")

plt.ylim(min_y-5, 100)
plt.xlabel("x")
plt.ylabel("y = f(x)")
plt.title("Final Result after Gradient Descent")
plt.legend()
plt.grid(True, color='wheat')
plt.show()
