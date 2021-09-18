from os import system
from calcupy import settings
from calcupy import commands
from calcupy import evaluator
from calcupy.variables import NumberVariables, FunctionVariables
from math import sqrt, sin, cos, tan
from math import pi, e


class Calculator:
    DEFAULT_NUMBER_VARIABLES = {"pi": pi, "e": e}
    DEFAULT_FUNCTION_VARIABLES = {"sqrt": sqrt, "sin": sin, "cos": cos, "tan": tan}

    def __init__(
        self,
        number_variables: dict = None,
        function_variables: dict = None,
        title: str = settings.DEFAULT_TITLE,
        bullet: str = settings.DEFAULT_BULLET,
    ):
        self._number_variables = NumberVariables()
        self._function_variables = FunctionVariables()
        self._title = title
        self._bullet = bullet
        self._command_handler = commands.CommandHandler()
        self._set_default_number_variables()
        self._set_default_function_variables()
        if number_variables:
            self._set_number_variables(number_variables)
        if function_variables:
            self._set_function_variables(function_variables)

    def _set_default_number_variables(self) -> None:
        for identifier, value in self.DEFAULT_NUMBER_VARIABLES.items():
            self._number_variables.add_variable(identifier, value)

    def _set_default_function_variables(self) -> None:
        for identifier, function in self.DEFAULT_FUNCTION_VARIABLES.items():
            self._function_variables.add_builtins(identifier, function)

    def _set_number_variables(self, number_variables: dict) -> None:
        for identifier, value in number_variables.items():
            self._number_variables.add_variable(identifier, value)

    def _set_function_variables(self, function_variables: dict) -> None:
        for identifier, function in function_variables.items():
            self._function_variables.add_variable(identifier, function)

    def _update_ans(self, value) -> None:
        self._number_variables.add_variable("ans", value)

    def _setting_commands(self, input_) -> None:
        if not input_:
            return True

        if input_.lower() == "clear" or input_.lower() == "cls":
            system("cls")
            print(self._title)
            return True

        if input_.lower() == "exit" or input_.lower() == "stop":
            exit()

        return None

    def start(self):
        system("cls")
        print(self._title)
        while True:
            input_ = input(f"\n{self._bullet} ").strip()

            if self._setting_commands(input_):
                continue

            try:
                command = self._command_handler.get_command(
                    input_, self._function_variables
                )
                if command:
                    command.handle(self._number_variables)
                    continue

                result = evaluator.evaluate(
                    input_, self._number_variables, self._function_variables
                )
                self._update_ans(result)
                print(result)

            except Exception as exception:
                print(f"Error: {exception}")
