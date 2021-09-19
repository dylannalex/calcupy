# CalcuPy :books:

<p align="center">
  <img width="450" height="450" src="../media/calcupy-demo.gif?raw=true">
</p>

Create console-based calculators in a few lines of code.

## :pushpin: Creating a calculator

### :round_pushpin: Add predefined numeric variables:

```
GRAVITY = 9.8
SPEED = 20

number_variables = {"g": GRAVITY, "v": SPEED}
calculator = Calculator(number_variables)
calculator.start()
```

If we run the calculator:

```
$ g
9.8

$ v
20

$ v + g * 0.01
20.098
```

### :round_pushpin: Add predefined functions:

```
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def y(x1, x2):
    return (x1 + 2) * x2


function_variables = {"y": y, "fac": factorial}
calculator = Calculator(None, function_variables)
calculator.start()
```

If we run the calculator:

```
$ fac(4)
24

$ y(2.4, 5.1)
22.44

$ fac(3) + y(2.4, 5.1)
28.44
```

### :round_pushpin: Basic example:

```
def foo(x, y):
    return x * y ** 2


title = "MY CALCULATOR"
bullet = "->"
number_variables = {"x": 2, "y": 3}
function_variables = {"foo": foo}
calculator = Calculator(number_variables, function_variables, title, bullet)
calculator.start()
```

If we run the calculator:

```
MY CALCULATOR

-> foo(2, 3)
18

-> foo(x, y) * 2
36

-> x / 8 * y
0.75
```

## :pushpin: Commands

### :round_pushpin: ADD

#### Description:

ADD command let you dynamically add new numeric variables.

#### Syntax:

```
add identifier expression
```

#### Example:

```
$ add x 4

$ add y 3

$ x * y
12
```

You can also assign an arithmetic expression to a variable. This
expression is solved and the result is stored in the specified
identifier.

```
$ add x sqrt(5) * tan(8 * 2) / 5

$ x
0.1344468258787234
```

### :round_pushpin: REMOVE

#### Description:

REMOVE command let you dynamically remove numeric variables.

#### Syntax:

```
remove identifier
```

#### Example:

```
$ add x 4.2

$ x
4.2

$ remove x

$ x
Error: 'NoneType' object is not subscriptable
```
