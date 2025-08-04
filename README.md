# Python Learning Series 🐍

A comprehensive Python learning repository containing practical examples and progressive concepts for beginners to intermediate learners. This project demonstrates modern Python 3 programming with type hints, proper documentation, and best practices.

## 📁 Project Structure

```
mypythonprog/
├── README.md                    # Project documentation
├── sample.py                    # Basic Python script with path manipulation & type hints
├── class_test/                  # Object-Oriented Programming examples (13 files)
│   ├── c1.py                   # Basic class definition
│   ├── c2.py                   # Class with constructor (__init__) and type hints
│   ├── c3.py                   # Class with methods
│   ├── c4.py                   # Self parameter variations
│   ├── c5.py                   # Class attributes and built-in functions
│   ├── c6.py                   # Class documentation and introspection
│   ├── c7.py                   # Object lifecycle and destructor (__del__)
│   ├── c8.py                   # Inheritance and class relationships
│   ├── c8-2.py                 # Advanced inheritance examples
│   ├── c9.py                   # Operator overloading (__add__, __str__)
│   ├── c10.py                  # Private attributes and name mangling
│   ├── c11.py                  # Iterator protocol (__iter__, __next__)
│   ├── c12.py                  # Exception handling (try/except/finally)
│   └── c13.py                  # File handling with exception handling
├── module_test/                 # Module and import system examples
│   ├── p1.py                   # Module importing and sys.path manipulation
│   ├── Support2.py             # Simple module with function
│   ├── __pycache__/            # Python bytecode cache
│   └── spt/                    # Nested module package
│       ├── support.py          # Nested module structure
│       └── __pycache__/        # Python bytecode cache
├── package_test/                # Python package examples
│   ├── phe.py                  # Package usage demonstration
│   └── Phone/                  # Sample Phone package
│       ├── __init__.py         # Package initialization with relative imports
│       ├── G3.py               # G3 phone module
│       ├── Isdn.py             # ISDN phone module
│       ├── Pots.py             # POTS phone module
│       └── __pycache__/        # Python bytecode cache
└── sampleCode/                  # Data structure examples with type hints
    ├── dictionary.py           # Dictionary operations and methods
    ├── list.py                 # List operations (ordered, mutable)
    ├── sets.py                 # Set operations (unordered, no duplicates)
    └── tuple.py                # Tuple operations (ordered, immutable)
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7+ (This project uses modern Python 3 syntax with type hints)
- Basic understanding of command line/terminal
- Optional: Virtual environment for isolated development

### Setting Up Virtual Environment (Recommended)
```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate

# Deactivate when done
deactivate
```

### Running the Examples

#### 1. Basic Script Execution
```bash
# Navigate to the project directory
cd mypythonprog

# Run the main sample script (demonstrates path manipulation and type hints)
python3 sample.py

# Expected output shows sys.path manipulation and function with type annotations
```

#### 2. Data Structures Examples
```bash
# Navigate to sampleCode directory
cd sampleCode

# Run list examples (ordered, mutable collections)
python3 list.py
# Shows: list operations, indexing, modification, append

# Run tuple examples (ordered, immutable collections)  
python3 tuple.py
# Shows: tuple creation, immutability, concatenation

# Run set examples (unordered, no duplicates)
python3 sets.py
# Shows: set operations, duplicate removal, no indexing

# Run dictionary examples (key-value pairs)
python3 dictionary.py
# Shows: dict operations, key-value access, modification
```

#### 3. Object-Oriented Programming Examples
```bash
# Navigate to class_test directory
cd class_test

# Basic class example
python3 c1.py
# Output: Basic class definition and instantiation

# Class with constructor and type hints
python3 c2.py
# Output: Constructor with typed parameters and default values

# Inheritance example
python3 c8.py
# Output: Parent-child class relationships and method overriding

# Exception handling
python3 c12.py
# Output: try/except/finally blocks with proper error handling

# File handling with exceptions
python3 c13.py
# Output: Safe file operations with exception handling
```

#### 4. Module and Package Examples
```bash
# Test module importing and path manipulation
cd module_test
python3 p1.py
# Shows: sys.path manipulation and custom module imports

# Test package usage
cd ../package_test
python3 phe.py
# Shows: Package importing and function calls from package modules
```

## 📚 Learning Topics Covered

### 1. Data Structures (`sampleCode/`)
- **Lists** (`list.py`): Ordered, mutable collections with duplicate support
  ```python
  list1 = ["physics", "chemistry", 1997, 2000, 2000]
  del list1[2]          # Remove by index
  list1[0] = "biology"  # Modify existing item
  list1.append("math")  # Add new item
  ```

- **Tuples** (`tuple.py`): Ordered, immutable collections
  ```python
  tup1 = (12, 12, 34.56, "wow")
  tup2 = ("abc", "xyz", 123)
  tup3 = tup1 + tup2  # Concatenation (creates new tuple)
  # tup1[0] = 99  # TypeError: immutable
  ```

- **Sets** (`sets.py`): Unordered collections with no duplicates
  ```python
  thisset = {"apple", "banana", "cherry", 123, 123}
  # Automatically removes duplicates: {123, 'apple', 'banana', 'cherry'}
  # thisset[0] = "wow"  # TypeError: no indexing
  ```

- **Dictionaries** (`dictionary.py`): Key-value pairs, unordered and mutable
  ```python
  thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
  thisdict["brand"] = "Ferrari"  # Modify value
  # {'brand': 'Ferrari', 'model': 'Mustang', 'year': 1964}
  ```

### 2. Object-Oriented Programming (`class_test/`)
- **Basic Classes** (`c1.py`): Class definition and instantiation
  ```python
  class MyClass:
      x = 5
  
  p1 = MyClass()
  print(p1.x)  # 5
  ```

- **Constructors** (`c2.py`): `__init__` method with type hints
  ```python
  class Person:
      def __init__(self, name: str, age: int, city: str = "Hyderabad") -> None:
          self.name = name
          self.age = age  
          self.city = city
  
  p1 = Person("John", 36)
  ```

- **Inheritance** (`c8.py`): Single inheritance and method overriding
  ```python
  class Parent:
      parentAttr = 100
      def parentMethod(self):
          print("Calling parent method")
  
  class Child(Parent):
      def childMethod(self):
          print("Calling child method")
  ```

- **Exception Handling** (`c12.py`, `c13.py`): try/except/finally blocks
  ```python
  try:
      print(x)  # NameError if x not defined
  except NameError:
      print("Variable x is not defined")
  except:
      print("Something else went wrong")
  finally:
      print("The 'try except' is finished")
  ```

### 3. Modules and Packages (`module_test/`, `package_test/`)
- **Module Creation**: Creating reusable code modules
  ```python
  # Support2.py
  def print_func(message):
      print("Hello:", message)
  
  # p1.py
  import Support2
  Support2.print_func("Zara 2")
  ```

- **Package Structure**: Creating and using Python packages
  ```python
  # Phone/__init__.py
  from .Pots import potss
  from .Isdn import isdnn  
  from .G3 import g33
  
  # phe.py
  import Phone
  Phone.potss()  # "I'm Pots Phone"
  ```

- **Path Manipulation**: Adding custom paths to sys.path
  ```python
  import sys, os
  currentPath = os.path.dirname(os.path.realpath(__file__))
  sys.path.insert(0, os.path.join(currentPath, ".."))
  ```

## 🔧 Commands to Create This Structure

Here are the complete terminal commands to recreate this project structure from scratch:

### Basic Directory Structure
```bash
# Create main project directory
mkdir mypythonprog
cd mypythonprog

# Create subdirectories
mkdir class_test module_test package_test sampleCode
mkdir module_test/spt module_test/__pycache__ module_test/spt/__pycache__
mkdir package_test/Phone package_test/Phone/__pycache__

# Create the main files
touch README.md sample.py
```

### Create All Class Test Files (13 files)
```bash
# Create class test files (c1 through c13, plus c8-2)
touch class_test/c{1..13}.py
touch class_test/c8-2.py

# Alternative one-liner for all class files:
# for i in {1..13}; do touch class_test/c$i.py; done && touch class_test/c8-2.py
```

### Create Module Test Files
```bash
# Create module test files
touch module_test/p1.py
touch module_test/Support2.py
touch module_test/spt/support.py

# Create __pycache__ directories (these are auto-generated by Python)
# mkdir -p module_test/__pycache__ module_test/spt/__pycache__
```

### Create Package Test Files
```bash
# Create package test files
touch package_test/phe.py

# Create Phone package files
touch package_test/Phone/__init__.py
touch package_test/Phone/G3.py
touch package_test/Phone/Isdn.py  
touch package_test/Phone/Pots.py

# Create __pycache__ directories (auto-generated)
# mkdir -p package_test/Phone/__pycache__
```

### Create Sample Code Files
```bash
# Create data structure example files
touch sampleCode/dictionary.py
touch sampleCode/list.py
touch sampleCode/sets.py
touch sampleCode/tuple.py
```

### Complete One-Line Structure Creation
```bash
# Complete project structure in one command block
mkdir -p mypythonprog/{class_test,module_test/{spt,__pycache__,spt/__pycache__},package_test/Phone/__pycache__,sampleCode} && \
cd mypythonprog && \
touch README.md sample.py && \
touch class_test/c{1..13}.py class_test/c8-2.py && \
touch module_test/{p1.py,Support2.py} module_test/spt/support.py && \
touch package_test/phe.py package_test/Phone/{__init__.py,G3.py,Isdn.py,Pots.py} && \
touch sampleCode/{dictionary.py,list.py,sets.py,tuple.py}
```

### File Permissions (Make Scripts Executable)
```bash
# Make Python files executable (optional)
chmod +x sampleCode/*.py
chmod +x class_test/*.py
chmod +x module_test/*.py package_test/*.py
chmod +x package_test/Phone/*.py
```

### Verification Commands
```bash
# Verify the structure
tree mypythonprog/
# or use ls -la for each directory

# Count files
find mypythonprog -name "*.py" | wc -l  # Should show 27 Python files

# Show directory structure
ls -la mypythonprog/
ls -la mypythonprog/class_test/
ls -la mypythonprog/sampleCode/
ls -la mypythonprog/package_test/Phone/
```

## 📖 Example Usage & Code Snippets

### Working with Data Structures

#### Lists (Ordered, Mutable)
```python
# From sampleCode/list.py
list1 = ["physics", "chemistry", 1997, 2000, 2000]
print(list1)  # ['physics', 'chemistry', 1997, 2000, 2000]

del list1[2]  # Remove element at index 2
print(list1)  # ['physics', 'chemistry', 2000, 2000]

list1[0] = "biology"  # Change existing item
print(list1)  # ['biology', 'chemistry', 2000, 2000]

list1.append("math")  # Add new item
print(list1)  # ['biology', 'chemistry', 2000, 2000, 'math']
```

#### Tuples (Ordered, Immutable)
```python
# From sampleCode/tuple.py
tup1 = (12, 12, 34.56, "wow")
tup2 = ("abc", "xyz", 123)

# Concatenation creates new tuple
tup3 = tup1 + tup2
print(tup3)  # (12, 12, 34.56, 'wow', 'abc', 'xyz', 123)

# Following would raise TypeError (immutable)
# tup1[0] = 99  # TypeError: 'tuple' object does not support item assignment
```

#### Sets (Unordered, No Duplicates)
```python
# From sampleCode/sets.py
thisset = {"apple", "banana", "cherry", 123, 123}
print(thisset)  # {123, 'apple', 'banana', 'cherry'} - duplicates removed

# Following would raise TypeError (no indexing)
# thisset[0] = "wow"  # TypeError: 'set' object does not support item assignment
```

#### Dictionaries (Key-Value Pairs)
```python
# From sampleCode/dictionary.py
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

thisdict["brand"] = "Ferrari"  # Modify value
print(thisdict)  # {'brand': 'Ferrari', 'model': 'Mustang', 'year': 1964}
```

### Object-Oriented Programming

#### Basic Class with Type Hints
```python
# From class_test/c2.py
class Person:
    def __init__(self, name: str, age: int, city: str = "Hyderabad") -> None:
        self.name = name
        self.age = age
        self.city = city

# Efficient way - create object once
p1 = Person("John", 36)
print("Name:", p1.name)   # Name: John
print("Age:", p1.age)     # Age: 36
print("City:", p1.city)   # City: Hyderabad

# With custom city
p2 = Person("Jane", 28, "Bangalore")
print("City:", p2.city)   # City: Bangalore
```

#### Inheritance Example
```python
# From class_test/c8.py
class Parent:
    parentAttr = 100
    
    def __init__(self):
        self.name = "Parent"
        print("Calling parent constructor")
    
    def parentMethod(self):
        print("Calling parent method")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Call parent constructor
        self.name = "Child"
        print("Calling child constructor")
    
    def childMethod(self):
        print("Calling child method")

# Usage
c = Child()
c.parentMethod()  # Inherited method
c.childMethod()   # Own method
```

#### Exception Handling
```python
# From class_test/c12.py
try:
    print(x)  # NameError if x not defined
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")
```

#### File Handling with Exceptions
```python
# From class_test/c13.py
f = None
try:
    f = open("demofile.txt", "w")
    f.write("Lorem Ipsum")
except IOError as emsg:
    print("Something went wrong when writing to the file:", emsg)
finally:
    print("Closing file:")
    if f is not None:
        print("File is open, now closing...")
        f.close()
```

### Modules and Packages

#### Module Usage
```python
# module_test/Support2.py
def print_func(message):
    print("Hello:", message)

# module_test/p1.py
import Support2
Support2.print_func("Zara 2")  # Output: Hello: Zara 2
```

#### Package Structure and Usage
```python
# package_test/Phone/__init__.py
from .Pots import potss
from .Isdn import isdnn
from .G3 import g33

# package_test/Phone/Pots.py
def potss():
    print("I'm Pots Phone")

# package_test/phe.py
import Phone
Phone.potss()   # Output: I'm Pots Phone
Phone.isdnn()   # Output: I'm Isdn Phone
Phone.g33()     # Output: I'm G3 Phone
```

#### Path Manipulation
```python
# From sample.py
import os
import sys

currentPath = os.path.dirname(os.path.realpath(__file__))
print("Current path:", currentPath)

# Add custom paths to sys.path for module discovery
sys.path.insert(0, os.path.join(currentPath, ".."))
sys.path.insert(0, os.path.join(currentPath, "../backup"))
```

## 🎯 Learning Path Recommendation

### Phase 1: Foundations (Beginner)
1. **Start with Basic Script** (`sample.py`)
   - Understand Python file structure
   - Learn about path manipulation and imports
   - Introduction to type hints and docstrings

2. **Master Data Structures** (`sampleCode/`)
   - Start with Lists (`list.py`) - ordered, mutable
   - Move to Tuples (`tuple.py`) - ordered, immutable  
   - Explore Sets (`sets.py`) - unordered, unique elements
   - Finish with Dictionaries (`dictionary.py`) - key-value pairs
   - **Practice**: Experiment with each data type's methods

### Phase 2: Object-Oriented Programming (Intermediate)
3. **Basic OOP Concepts** (`class_test/c1.py` to `c6.py`)
   - Class definition and instantiation (`c1.py`)
   - Constructors with type hints (`c2.py`)
   - Instance methods (`c3.py`)
   - Self parameter variations (`c4.py`)
   - Class attributes and built-ins (`c5.py`)
   - Documentation and introspection (`c6.py`)

4. **Advanced OOP** (`class_test/c7.py` to `c11.py`)
   - Object lifecycle and destructors (`c7.py`)
   - Inheritance and relationships (`c8.py`, `c8-2.py`)
   - Operator overloading (`c9.py`)
   - Private attributes and name mangling (`c10.py`)
   - Iterator protocol (`c11.py`)

### Phase 3: Error Handling & File Operations (Intermediate)
5. **Exception Management** (`class_test/c12.py`, `c13.py`)
   - Basic try/except/finally patterns (`c12.py`)
   - File operations with proper error handling (`c13.py`)
   - **Practice**: Implement robust error handling in your code

### Phase 4: Modular Programming (Advanced)
6. **Modules and Packages** (`module_test/`, `package_test/`)
   - Module creation and importing (`module_test/`)
   - Path manipulation and sys.path (`p1.py`)
   - Package structure and `__init__.py` (`package_test/`)
   - Relative imports and package organization
   - **Practice**: Create your own reusable modules

### 🏆 Progressive Challenges

#### Beginner Challenges
- [ ] Create a program using all four data structures
- [ ] Build a simple calculator class with basic operations
- [ ] Implement exception handling for user input validation

#### Intermediate Challenges  
- [ ] Create a package for mathematical operations (add, subtract, etc.)
- [ ] Build a class hierarchy (Animal -> Dog/Cat with specific behaviors)
- [ ] Implement a file processing system with proper error handling

#### Advanced Challenges
- [ ] Create a module that dynamically imports other modules
- [ ] Build a custom iterator class for a specific data structure
- [ ] Design a package with sub-packages and complex import relationships

### 📋 Study Checklist

**Data Structures Mastery:**
- [ ] Can create and manipulate lists effectively
- [ ] Understand tuple immutability and use cases
- [ ] Know when to use sets vs lists
- [ ] Comfortable with dictionary operations and methods

**OOP Proficiency:**
- [ ] Can design classes with proper constructors
- [ ] Understand inheritance and method overriding
- [ ] Know how to handle object lifecycle
- [ ] Can implement custom operators and iterators

**Error Handling:**
- [ ] Write code with appropriate exception handling
- [ ] Understand try/except/else/finally flow
- [ ] Can handle file operations safely

**Modular Programming:**
- [ ] Can create and organize modules
- [ ] Understand Python's import system
- [ ] Know how to structure packages properly
- [ ] Can manipulate sys.path when needed

## �️ Development Setup & Tools

### Code Quality Tools
```bash
# Install Python linting and formatting tools
pip3 install pylint black mypy

# Run pylint for code analysis
python3 -m pylint sample.py

# Format code with black
python3 -m black sampleCode/

# Type checking with mypy
python3 -m mypy class_test/c2.py
```

### Project Statistics
- **Total Python Files**: 27 files
- **Lines of Code**: ~500+ lines
- **Concepts Covered**: 15+ Python concepts
- **Difficulty Levels**: Beginner to Intermediate

### File Organization Summary
```
📁 sampleCode/     - 4 files  (Data Structures)
📁 class_test/     - 14 files (OOP Concepts) 
📁 module_test/    - 3 files  (Module System)
📁 package_test/   - 5 files  (Package System)
📄 sample.py       - 1 file   (Basic Concepts)
```

## 📝 Notes & Best Practices

### Modern Python Features Used
- **Type Hints**: Function parameters and return types annotated
- **Docstrings**: Proper documentation for modules and functions  
- **F-strings**: Modern string formatting (where applicable)
- **Pathlib**: Modern path handling (in some examples)
- **Context Managers**: Proper file handling patterns

### Code Style Guidelines
- Follow PEP 8 Python style guide
- Use meaningful variable and function names
- Include type hints for better code documentation
- Write docstrings for modules, classes, and functions
- Handle exceptions appropriately

### Common Patterns Demonstrated
1. **Constructor Patterns**: Default parameters, type hints
2. **Error Handling**: try/except/finally blocks
3. **Import Patterns**: Absolute and relative imports
4. **File Operations**: Safe file handling with context managers
5. **Class Design**: Inheritance, encapsulation, polymorphism

### Migration from Python 2 to Python 3
This project demonstrates modern Python 3 practices. Key differences from older Python 2 code:
- `print()` function instead of print statement
- Type hints for better code documentation
- Modern exception handling syntax
- Unicode strings by default

## 🤝 Contributing

### How to Contribute
1. **Add New Examples**: Create new Python files demonstrating specific concepts
2. **Improve Documentation**: Enhance code comments and docstrings
3. **Fix Issues**: Report and fix any bugs or inconsistencies
4. **Add Tests**: Create unit tests for the examples

### Contribution Guidelines
- Each example should be **self-contained** and runnable
- Include **comprehensive comments** explaining the concept
- Follow **consistent naming conventions**
- Add **type hints** where appropriate
- Update **README.md** when adding new files or concepts

### File Naming Convention
- `c*.py` - Class-related examples (numbered sequentially)
- Descriptive names for data structure files (`list.py`, `dictionary.py`)
- Package files follow the concept they demonstrate

## 🚀 Next Steps & Extensions

### Potential Additions
- **Advanced Topics**: Decorators, generators, context managers
- **Standard Library**: Collections, itertools, functools examples
- **Testing**: Unit tests using unittest or pytest
- **Documentation**: Sphinx documentation generation
- **Type Checking**: More comprehensive mypy configuration

---

Happy Learning! 🐍
