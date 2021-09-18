from calcupy.variables import NumberVariables, FunctionVariables
from calcupy import evaluator
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def handle(self, number_variables: NumberVariables) -> None:
        pass


class AddCommand(Command):
    def __init__(
        self, identifier: str, expression: str, function_variables: FunctionVariables
    ):
        self.identifier = identifier
        self.expression = expression
        self.function_variables = function_variables

    def handle(self, number_variables) -> None:
        if not self.expression:
            raise SyntaxError("Invalid syntax for add command")

        value = evaluator.evaluate(
            self.expression, number_variables, self.function_variables
        )
        number_variables.add_variable(self.identifier, value)


class RemoveCommand(Command):
    def __init__(self, identifier: str):
        self.identifier = identifier

    def handle(self, number_variables: NumberVariables) -> None:
        number_variables.remove_variable(self.identifier)


class CommandHandler:
    VALID_INSTRUCTIONS = ("add", "remove")

    def _is_command(self, operation) -> bool:
        """
        Returns True if the operation contains a command,
        else returns False.
        """
        instruction = operation.split(" ")[0]
        if instruction in self.VALID_INSTRUCTIONS:
            return True
        return False

    def get_command(
        self, operation: str, function_variables: FunctionVariables
    ) -> Command:
        if not self._is_command(operation):
            return None

        operation_list = operation.split(" ")
        instruction = operation_list[0]

        if instruction == "add":
            identifier = operation_list[1]
            expression = "".join(operation_list[2::])
            return AddCommand(identifier, expression, function_variables)

        if instruction == "remove":
            identifier = operation_list[1]
            return RemoveCommand(identifier)
