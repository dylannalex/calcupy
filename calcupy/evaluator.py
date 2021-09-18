from calcupy.variables import NumberVariables, FunctionVariables


def _replace_number_variables(expression: str, number_variables: NumberVariables):
    """
    Given an expression, all NumberVariables identifiers are
    replaced with their respective value.

    Example:
    number_variables = NumberVariables()
    number_variables.add_variable("x", 2)
    number_variables.add_variable("y", 4)
    expression = "x * y"

    _replace_number_variables(expression, number_variables)
    >>> "2 * 4"
    """
    for identifier in number_variables.get_identifiers():
        if identifier in expression:
            expression = expression.replace(
                identifier, str(number_variables.get_value(identifier))
            )
    return expression


def _replace_function_variables(expression: str, function_variables: FunctionVariables):
    """
    Given an expression (without any NumberVariables identifiers),
    it is replaced with a _run_function call so eval() can
    successfully execute FunctionVariables functions.

    Example:
    function_variables = FunctionVariables()
    function_variables.add_variable("foo", foo)
    expression = "2 * foo(1, 2)"

    _replace_function_variables(expression, function_variables)
    >>> "2 * _run_function(function_variables.get_value("foo"), 1, 2)"
    """
    for identifier in function_variables.get_identifiers():
        if identifier in expression:
            expression = expression.replace(
                f"{identifier}(",
                f"_run_function(function_variables.get_value('{identifier}'), ",
            )
    return expression


def _run_function(function, *args):
    """
    Since eval() function only evaluates functions written in the
    source code, _run_function is at eval() scope and makes it
    possible to run FunctionVariables functions.
    """
    return function(*args)


def evaluate(
    expression: str,
    number_variables: NumberVariables,
    function_variables: FunctionVariables,
):
    """
    Evaluates a given expression and returns its value.

    It first replaces all number_variables with their respective value.
    Then it replaces the function_variables identifier with a _run_function
    call. Finally it evaluates the expression with the built in eval
    function.
    """
    return eval(
        _replace_function_variables(
            _replace_number_variables(expression, number_variables), function_variables
        ),
        {"__builtins__": None},
        {"_run_function": _run_function, "function_variables": function_variables},
    )
