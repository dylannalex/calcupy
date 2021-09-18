from abc import ABC, abstractmethod
from calcupy.check_types import is_float, is_int
from types import FunctionType


class Variables(ABC):
    def __init__(self):
        self._variables = {}

    @abstractmethod
    def add_variable(self, identifier: str, value: str) -> None:
        pass

    def remove_variable(self, identifier: str) -> None:
        self._variables.pop(identifier, None)

    def get_value(self, identifier: str) -> str:
        return self._variables[identifier]

    def get_identifiers(self) -> tuple:
        return tuple(self._variables.keys())

    def _verify_identifier(self, identifier) -> None:
        if not identifier.isidentifier():
            raise SyntaxError(f"{identifier} is not a valid identifier.")


class NumberVariables(Variables):
    def add_variable(self, identifier: str, value: str) -> None:
        self._verify_identifier(identifier)

        if not is_int(value) and not is_float(value):
            raise ValueError("Variable value must be an integer or a float.")

        if identifier in self._variables:
            self.remove_variable(identifier)

        self._variables[identifier] = value


class FunctionVariables(Variables):
    def add_variable(self, identifier: str, function: FunctionType) -> None:
        self._verify_identifier(identifier)

        if not isinstance(function, FunctionType):
            raise ValueError(f"{identifier} value must be a function.")

        if identifier in self._variables:
            self.remove_variable(identifier)

        self._variables[identifier] = function

    def add_builtins(self, identifier: str, builtin_function):
        self._variables[identifier] = builtin_function
