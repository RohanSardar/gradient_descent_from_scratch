# Gradient Descent from Scratch

This Python project demonstrates gradient descent on a univariate function using `NumPy` and `Matplotlib`. Two different starting points are used to show how the optimization paths converge to local or global minima.

It visualizes gradient descent on the function:

$$
f(x) = x^4 - 10x^2 + 9
$$

Two points with different initial values are optimized using gradient descent, and their paths are animated using Matplotlib.

### Features
- Gradient descent visualization from two starting points
- Live visualization over 500 iterations
- Final positions highlighted on the graph

### How to run ?
```
python gradient_descent_visualization_2d.py
```

### Customizations
- Starting points: Change `current_x0` and `current_x1`
- Learning rate: Modify `learning_rate`
- Iterations: Adjust the loop count
- More points: You can add as many points as you wish
