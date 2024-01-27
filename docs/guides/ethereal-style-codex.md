> # <p align="center">Ethereal Codex for Ghostly Code Weaving</p>

![Ethereal Codex GIF](../images/Ethereal-Codex.gif)

> ## Ethereal Introduction

Embark on a spectral journey through the realms of the Coding Style Guide, a sacred manuscript meticulously crafted for the ethereal projects within the [Ghost-Hackers](https://github.com/Ghost-Hackers) organization. These ghostly pages weave an enchanting spell of consistency, summoning a harmonious coding environment across our spectral endeavors. Embrace this otherworldly approach, for it transcends mere code formatting—it is a manifestation of our collective essence.

As spectral beings of Ghost-Hackers, we believe in the power of a well-maintained and consistent coding style—a ghostly sigil symbolizing our unwavering commitment to excellence. Whether you traverse the shadows as a seasoned contributor or embark on your first spectral steps, these spectral guidelines will not only guide your coding endeavors but also contribute to the spectral elegance and professionalism that defines our ghostly projects.

Together, let us embark on this spectral coding journey, dancing with the whispers of shared values and aspirations that echo through the corridors of the Ghost-Hackers community.

### Attention: Contributors

This guide is a work in progress. We welcome your contributions to enhance the ethereal experience. Feel free to submit a [pull request](https://github.com/Ghost-Hackers/Ghost-Hackers.bot/pulls) with your suggestions. Together, let us expand the Codices, creating a spectral guide for all to enjoy. Please refer to the [Contributing Guidelines](..\..\CONTRIBUTING.md) for more details on how to contribute and the [Code of Conduct](..\..\CODE_OF_CONDUCT.md) for our community standards.

> ## Table of Shadows

- [Ethereal Codex for Ghostly Code Weaving](#ethereal-codex-for-ghostly-code-weaving)
  - [Ethereal Introduction](#ethereal-introduction)
    - [Attention: Contributors](#attention-contributors)
  - [Table of Shadows](#table-of-shadows)
  - [Formatting](#formatting)
    - [Indentation](#indentation)
    - [Spacing](#spacing)
    - [Line Length](#line-length)
  - [Naming Enchantments](#naming-enchantments)
    - [Variables](#variables)
    - [Functions](#functions)
    - [Classes](#classes)
  - [Whispers of Comments](#whispers-of-comments)
  - [Spectral Documentation](#spectral-documentation)
  - [Best Conjuring Practices](#best-conjuring-practices)
  - [Version Control Rituals](#version-control-rituals)
  - [Testing Seances](#testing-seances)
  - [Error Haunting](#error-haunting)
  - [Dependency Incantations](#dependency-incantations)
  - [Styling for Python](#styling-for-python)
    - [PEP 8 Compliance](#pep-8-compliance)
    - [Type Hints](#type-hints)
  - [Styling for JavaScript](#styling-for-javascript)
    - [StandardJS](#standardjs)
  - [Styling for HTML](#styling-for-html)
    - [HTML5 Best Practices](#html5-best-practices)
  - [Styling for CSS](#styling-for-css)
    - [BEM Methodology](#bem-methodology)
  - [Styling for Shell Scripting](#styling-for-shell-scripting)
    - [ShellCheck](#shellcheck)
  - [Styling for Java](#styling-for-java)
    - [Google Java Style Guide](#google-java-style-guide)
  - [Styling for C++](#styling-for-c)
    - [Google C++ Style Guide](#google-c-style-guide)
  - [Ethereal Documentation Codex](#ethereal-documentation-codex)
    - [Guiding Spirits](#guiding-spirits)

> ## Formatting

### Indentation

Use four spaces for indentation. Avoid using tabs.

```python
def example_function():
    if condition:
        print("Indented ethereal block")
```

### Spacing

- Use a single space after commas in function arguments and list elements.
- Avoid extraneous whitespace.

```python
# Good
example_list = [1, 2, 3]

# Bad
example_list = [ 1 , 2 , 3 ]
```

### Line Length

Limit lines to a maximum of 80 characters.

```python
# Good
def example_function(arg1, arg2, arg3):
    ...

# Bad
def example_function(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    ...
```

> ## Naming Enchantments

### Variables

Use descriptive, lowercase variable names. Separate words with underscores.

```python
spirit_name = "John"
```

### Functions

Follow the same conventions as variables. Use a verb for function names.

```python
def conjure_total(items):
    ...
```

### Classes

Use CamelCase for class names.

```python
class EtherealClass:
    ...
```

> ## Whispers of Comments

- Use comments sparingly, focusing on why rather than what.
- Keep comments up-to-date with the code.

```python
# Good
def conjure_total(items):
    # Sum the values of the items
    total = sum(items)
    return total

# Bad
def conjure_total(items):
    total = sum(items)  # Calculate total
    return total
```

> ## Spectral Documentation

- Include a docstring for every module, class, and function.
- Follow the [Google Python Docstring Style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) conventions.

```python
def ethereal_function(arg1, arg2):
    """This is a brief description of the function.

    More detailed information about the function and its parameters.

    Args:
        arg1 (int): Description of arg1.
        arg2 (str): Description of arg2.

    Returns:
        bool: Description of the return value.
    """
    ...
```

> ## Best Conjuring Practices

- Write modular and reusable code.
- Avoid unnecessary global variables.
- Ensure code follows the Single Responsibility Principle.

> ## Version Control Rituals

- Commit messages should be concise and descriptive.
- Branch names should reflect the feature or bug being addressed.

> ## Testing Seances

- Write unit tests for functions and methods.
- Use meaningful test function names.

> ## Error Haunting

- Use try-except blocks for exception handling.
- Provide informative error messages.

> ## Dependency Incantations

- Clearly document external dependencies.
- Include version numbers for reproducibility.

> ## Styling for Python

### PEP 8 Compliance

Follow the guidelines outlined in [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.

### Type Hints

Consider using [type hints](https://docs.python.org/3/library/typing.html) to enhance code clarity and assist with static analysis.

```python
def example_function(arg1: int, arg2: str) -> bool:
    ...
```

> ## Styling for JavaScript

### StandardJS

Adhere to the [StandardJS](https://standardjs.com/) for JavaScript code.

```javascript
// Good
const exampleArray = [1, 2, 3];

// Bad
var exampleArray = new Array(1, 2, 3);
```

> ## Styling for HTML

### HTML5 Best Practices

Follow the best practices for HTML5 outlined by the [HTML Living Standard](https://html.spec.whatwg.org/multipage/).

```html
<!-- Good -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ghostly Project</title>
</head>
<body>
    <h1>Welcome to the Ghostly Realm</h1>
</body>
</html>

<!-- Bad -->
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ghostly Project</title>
  </head>
  <body>
    <h1>Welcome to the Ghostly Realm</h1>
  </body>
</html>
```

> ## Styling for CSS

### BEM Methodology

Follow the [Block Element Modifier (BEM)](http://getbem.com/) methodology for writing CSS.

```css
/* Good */
.block {
    background-color: #fff;
}

.block__element {
    color: #000;
}

.block--modifier {
    font-size: 16px;
}

/* Bad */
#element {
    background-color: #fff;
}

#element strong {
    color: #000;
}

#element.big {
    font-size: 16px;
}
```

> ## Styling for Shell Scripting

### ShellCheck

Use [ShellCheck](https://www.shellcheck.net/) to analyze and improve your shell scripts.

```bash
# Good
#!/bin/bash

echo "Hello, spectral world!"

# Bad
#!/bin/bash

Echo "Hello, spectral world!"
```

> ## Styling for Java

### Google Java Style Guide

Follow the [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html) for Java code.

```java
// Good
public class GhostlyClass {
    private int spectralNumber;

    public GhostlyClass(int spectralNumber) {
        this.spectralNumber = spectralNumber;
    }

    public void enchant() {
        // Ethereal enchantment
    }
}

// Bad
public class ghostly_class {
    private int spectral_number;

    public ghostly_class(int spectral_number) {
        this.spectral_number = spectral_number;
    }

    public void enchant() {
        // Non-ethereal enchantment
    }
}
```

> ## Styling for C++

### Google C++ Style Guide

Follow the [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html) for C++ code.

```cpp
// Good
class EtherealClass {
private:
    int spectral_number;

public:
    EtherealClass(int spectral_number) : spectral_number(spectral_number) {}

    void enchant() {
        // Ethereal enchantment
    }
};

// Bad
class ghostly_class {
private:
    int spectral_number;

public:
    ghostly_class(int spectral_number) : spectral_number(spectral_number) {}

    void enchant() {
        // Non-ethereal enchantment
    }
}
```

> ## Ethereal Documentation Codex

### Guiding Spirits

Feel the pulse of the spectral community by inviting fellow seekers to contribute their wisdom. Let their voices resonate through the corridors of your documentation. Gain the knowledge of the [Ethereal Documentation Codex](ethereal-documentation-codex.md) and allow it to guide your spectral journey.

---
*May the expanded Ethereal Codex be your guide through ever-shifting mists of knowledge.*

[Back to Top](#ethereal-codex-for-ghostly-code-weaving)