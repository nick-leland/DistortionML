import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    """Original Function"""
    return x**2 + y**2

def gradient_f(x, y):
    """Manually takes the derivative of the function"""
    return 2*x, 2*y

x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)

U, V = gradient_f(X, Y)

plt.figure(figsize=(10, 8))
plt.quiver(X, Y, U, V, color='b', alpha=0.8)
plt.title("Gradient Vector Field of f(x,y) = x^2 + y^2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

# Save the plot as a PNG file instead of displaying it
plt.savefig('gradient_vector_field.png')
print("Plot saved as 'gradient_vector_field.png'")
