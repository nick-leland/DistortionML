import re
import numpy as np
import math
from sympy import symbols, limit, sympify

def latex_to_python_function(latex_string):
    # Check if it's a limit expression
    limit_match = re.match(r'\\lim_{(\w+)\\to(\w+|\+?\\infty|-?\\infty)}\s*(.+)', latex_string)
    if limit_match:
        var, approach, expression = limit_match.groups()
        # Convert LaTeX infinity to SymPy infinity
        if approach in ['+\\infty', '\\infty']:
            approach = 'oo'
        elif approach == '-\\infty':
            approach = '-oo'
        
        # Replace LaTeX operations with SymPy equivalents
        replacements = [
            (r'\\sqrt{([^}]+)}', r'sqrt(\1)'),
            (r'(\w+)\^(\w+)', r'\1**\2'),
            (r'\\sin', 'sin'),
            (r'\\cos', 'cos'),
            (r'\\tan', 'tan'),
            (r'\\exp', 'exp'),
            (r'\\log', 'log'),
            (r'\\pi', 'pi'),
            (r'\\frac{([^}]+)}{([^}]+)}', r'(\1)/(\2)')
        ]
        
        for old, new in replacements:
            expression = re.sub(old, new, expression)
        
        # Create a SymPy expression
        x = symbols(var)
        sympy_expr = sympify(expression)
        
        # Define the limit function
        def limit_function():
            return float(limit(sympy_expr, x, approach))
        
        return limit_function

    # If not a limit, proceed with the original function conversion
    match = re.match(r'(\w+)\(([\w,\s]+)\)\s*=\s*(.+)', latex_string)
    if not match:
        raise ValueError("Invalid LaTeX function format")
    
    func_name, vars_string, expression = match.groups()
    variables = [v.strip() for v in vars_string.split(',')]
    
    # Replace LaTeX operations with Python equivalents
    replacements = [
        (r'\\sqrt{([^}]+)}', r'np.sqrt(\1)'),
        (r'(\w+)\^(\d+)', r'\1**\2'),
        (r'\\sin', 'np.sin'),
        (r'\\cos', 'np.cos'),
        (r'\\tan', 'np.tan'),
        (r'\\exp', 'np.exp'),
        (r'\\log', 'np.log'),
        (r'\\pi', 'np.pi'),
        (r'\\frac{([^}]+)}{([^}]+)}', r'(\1)/(\2)')
    ]
    
    for old, new in replacements:
        expression = re.sub(old, new, expression)
    
    # Create and return the function
    function_def = f"def {func_name}({', '.join(variables)}):\n    return {expression}"
    exec(function_def, globals())
    return globals()[func_name]

# Example usage
regular_function = "f(x, y) = -\\sqrt{x^2 + y^2}"
python_function = latex_to_python_function(regular_function)
print(python_function(3, 4))  # Should output -5.0

limit_function = "\\lim_{x\\to\\infty} \\frac{x^2 + 2x + 1}{x^2 + 1}"
limit_result = latex_to_python_function(limit_function)
print(limit_result())  # Should output 1.0


# Let's talk about inverting the function.  
def original_function(x, y):
    return -np.sqrt(x**2 + y**2)

def inverse_function(f, a, b, c, d, theta):
