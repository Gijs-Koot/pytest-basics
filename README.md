# Using `pytest`

## Basic Usage

- Using the assert statement
- Pytest discovery and using `setup.py`

### Integration with Visual Studio Code

- Use "Python: discover tests" to setup the integration with VSC

### Pytest helpers

- If you want to use a temporary folder use `tempdir`
- Use `pytest.approx` for float comparisons

### Exercise 1

Write a test for the writefile function in `funcs.py`

## Write testable code

### Mock and patch

- You can use `unittest.mock.patch` to "rewire" a function to an object that you control in the test
- This object is a `unittest.mock.MagicMock`
    - For example, to set a return value, use `mock.return_value = True`
    - This is a method for dealing with external dependencies

### Dependency injection

### Exercise 2

Write a test for `funcs.py::get_buildings` that mocks the connection.

## Recap

## Using fixtures

## Mocking exercise

## Integration with VS Code / workflow

## Discussion

- Testing implementation vs. interface
- Test driven development
