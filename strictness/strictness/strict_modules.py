"""
We have an idea: strict modules.

Strict modules are a new Python module type marked with __strict__ = True at the top of the module, and implemented by leveraging many of the low-level extensibility mechanisms already provided by Python. A custom module loader parses the code using the ast module, performs abstract interpretation on the loaded code to analyze it, applies various transformations to the AST, and then compiles the modified AST back into Python byte code using the built-in compile function.

"""
