# codecademy-school-project

## What

Codecademy School Catalog Project in Dataclass syntax with Enum.

## Documentation

Enum requires at least Python 3.4 to run the file. Here is the link to documentation: [enum — Support for enumerations](https://docs.python.org/3/library/enum.html)

Dataclasses were first introduced in Python 3.7. They can be backported to Python 3.6 by running **`pip install dataclasses`**.

Here is list of links with more info:

- Official documentation: [dataclasses — Data Classes](https://docs.python.org/3/library/dataclasses.html#module-dataclasses)
- Backport: [dataclasses 0.8](https://pypi.org/project/dataclasses/)
- Real Python article: [Data Classes in Python 3.7+ (Guide)](https://realpython.com/python-data-classes/)

The use of `slots=True` declaration in the `@dataclass` decorator requires Python 3.10. Also, if you are using any Python version less than 3.9, you need to have this import: `from typing import List` and this line `list[str] = field(default_factory=list)` needs to be changed to `List[str] = field(default_factory=list)`.
