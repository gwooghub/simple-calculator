# Simple Calculator

A small command-line calculator written in Python. It adds, subtracts, multiplies, and divides two numbers at a time.

## Requirements

- Python 3.6 or newer
- No extra packages are needed

## Running the calculator

Save the calculator code as `calculator.py`. Open a terminal in the folder containing that file and run:

```bash
python calculator.py
```

If your system uses `python3` instead, run:

```bash
python3 calculator.py
```

## How to use it

1. Choose an operation: `+`, `-`, `*`, or `/`.
2. Enter the first number.
3. Enter the second number.
4. Read the result. The calculator then asks for another operation.

Whole numbers, decimals, and negative numbers are supported.

To exit, enter `q` at the operation prompt. Uppercase `Q` works too. The quit command is not available at the number prompts.

## Example

```text
Simple Calculator

Choose an operation (+, -, *, /) or q to quit: *
First number: 6
Second number: 2.5
Result: 15.0

Choose an operation (+, -, *, /) or q to quit: q
Goodbye!
```

## Input errors

The calculator checks for a few common mistakes:

- **Unknown operation:** It asks you to choose one of the four supported symbols.
- **Invalid number:** It displays `That wasn't a valid number. Try again.` and returns to the operation prompt.
- **Division by zero:** It displays `You can't divide by zero.` and returns to the operation prompt.

## A couple of limitations

This calculator performs one operation at a time. Enter the numbers separately; expressions such as `2 + 3 * 4` are not supported.

Numbers are stored as Python floating-point values. Whole-number results may appear with `.0`, and some decimal calculations can show small rounding differences. For example, adding `0.1` and `0.2` produces `0.30000000000000004`.
