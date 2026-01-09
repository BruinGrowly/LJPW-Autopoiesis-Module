import ast

code = """
def mixed_tabs_and_spaces():
	x = 1
    y = 2
	return x + y
"""

try:
    ast.parse(code)
except SyntaxError as e:
    print(f"Type: {type(e).__name__}")
    print(f"Message: {e.msg}")
    print(f"Line: {e.lineno}")