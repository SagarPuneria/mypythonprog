# Python Learning Series

A comprehensive Python learning repository containing practical examples and concepts for beginners to intermediate learners.

## 📁 Project Structure

```
mypythonprog/
├── README.md                    # Project documentation
├── sample.py                    # Basic Python script with path manipulation
├── class_test/                  # Object-Oriented Programming examples
│   ├── c1.py                   # Basic class definition
│   ├── c2.py                   # Class with constructor (__init__)
│   ├── c3.py                   # Class with methods
│   ├── c4.py                   # Self parameter variations
│   ├── c5.py                   # Class attributes and built-in functions
│   ├── c6.py                   # Class documentation and introspection
│   ├── c7.py                   # Object lifecycle and destructor
│   ├── c8.py                   # Inheritance and class relationships
│   ├── c9.py                   # Operator overloading
│   ├── c10.py                  # Private attributes and name mangling
│   ├── c11.py                  # Iterator protocol
│   ├── c12.py                  # Exception handling basics
│   └── c13.py                  # File handling with exception handling
├── module_test/                 # Module and import system examples
│   ├── p1.py                   # Module importing and path manipulation
│   ├── support2.py             # Simple module with function
│   └── spt/
│       └── support.py          # Nested module structure
├── package_test/                # Python package examples
│   ├── phe.py                  # Package usage example
│   └── Phone/                  # Sample package
│       ├── __init__.py         # Package initialization
│       ├── G3.py               # G3 phone module
│       ├── Isdn.py             # ISDN phone module
│       └── Pots.py             # POTS phone module
└── sampleCode/                  # Data structure examples
    ├── dictionary.py           # Dictionary operations
    ├── list.py                 # List operations
    ├── sets.py                 # Set operations
    └── tuple.py                # Tuple operations
```

## 🚀 Getting Started

### Prerequisites
- Python 2.7+ (Note: This project uses Python 2 syntax)
- Basic understanding of command line/terminal

### Running the Examples

#### 1. Basic Script Execution
```bash
# Navigate to the project directory
cd "mypythonprog"

# Run the main sample script
python sample.py
```

#### 2. Data Structures Examples
```bash
# Navigate to sampleCode directory
cd sampleCode

# Run list examples
python list.py

# Run tuple examples  
python tuple.py

# Run set examples
python sets.py

# Run dictionary examples
python dictionary.py
```

#### 3. Object-Oriented Programming Examples
```bash
# Navigate to class_test directory
cd class_test

# Basic class example
python c1.py

# Class with constructor
python c2.py

# Class with methods
python c3.py

# Inheritance example
python c8.py

# Operator overloading
python c9.py

# Exception handling
python c12.py
```

#### 4. Module and Package Examples
```bash
# Test module importing
cd module_test
python p1.py

# Test package usage
cd ../package_test
python phe.py
```

## 📚 Learning Topics Covered

### 1. Data Structures (`sampleCode/`)
- **Lists**: Ordered, mutable collections with duplicate support
- **Tuples**: Ordered, immutable collections
- **Sets**: Unordered collections with no duplicates
- **Dictionaries**: Key-value pairs, unordered and mutable

### 2. Object-Oriented Programming (`class_test/`)
- **Basic Classes**: Class definition and instantiation
- **Constructors**: `__init__` method usage
- **Methods**: Instance and class methods
- **Inheritance**: Single inheritance and method overriding
- **Special Methods**: `__str__`, `__add__`, `__del__`
- **Access Control**: Private attributes and name mangling
- **Exception Handling**: try/except/finally blocks
- **File Operations**: Safe file handling with exceptions

### 3. Modules and Packages (`module_test/`, `package_test/`)
- **Module Creation**: Creating reusable code modules
- **Import System**: Different ways to import modules
- **Path Manipulation**: Adding custom paths to sys.path
- **Package Structure**: Creating and using Python packages
- **`__init__.py`**: Package initialization files

## 🔧 Commands to Create This Structure

Here are the terminal commands that could be used to create this project structure:

```bash
# Create main project directory
mkdir mypythonprog
cd mypythonprog

# Create subdirectories
mkdir class_test module_test package_test sampleCode
mkdir module_test/spt
mkdir package_test/Phone

# Create the main files
touch README.md sample.py

# Create class test files
touch class_test/c{1..13}.py

# Create module test files
touch module_test/p1.py module_test/support2.py
touch module_test/spt/support.py

# Create package test files
touch package_test/phe.py
touch package_test/Phone/__init__.py
touch package_test/Phone/{G3,Isdn,Pots}.py

# Create sample code files
touch sampleCode/{dictionary,list,sets,tuple}.py
```

## 📖 Example Usage

### Working with Lists
```python
# From sampleCode/list.py
list1 = ['physics', 'chemistry', 1997, 2000, 2000]
print list1  # ['physics', 'chemistry', 1997, 2000, 2000]
del list1[2]
print list1  # ['physics', 'chemistry', 2000, 2000]
```

### Creating Classes
```python
# From class_test/c2.py
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print("Name: " + p1.name)
print("Age: " + str(p1.age))
```

### Using Packages
```python
# From package_test/phe.py
import Phone

Phone.pots()   # I'm Pots Phone
Phone.isdn()   # I'm Isdn Phone  
Phone.g33()    # I'm G3 Phone
```

## 🎯 Learning Path Recommendation

1. **Start with Data Structures** (`sampleCode/`)
   - Understand lists, tuples, sets, and dictionaries
   - Practice with the provided examples

2. **Learn Basic OOP** (`class_test/c1.py` to `c6.py`)
   - Class definition and instantiation
   - Constructors and methods
   - Class attributes

3. **Advance in OOP** (`class_test/c7.py` to `c11.py`)
   - Inheritance and polymorphism
   - Special methods and operator overloading
   - Access control

4. **Error Handling** (`class_test/c12.py`, `c13.py`)
   - Exception handling patterns
   - File operations with proper error handling

5. **Modules and Packages** (`module_test/`, `package_test/`)
   - Creating reusable code
   - Understanding Python's import system

## 📝 Notes

- This project uses Python 2 syntax (note the `print` statements without parentheses)
- To modernize for Python 3, update print statements: `print "text"` → `print("text")`
- The examples demonstrate fundamental Python concepts with practical, runnable code

## 🤝 Contributing

Feel free to add more examples or improve existing ones. Each example should be:
- Self-contained and runnable
- Well-commented
- Focused on a specific concept
- Following consistent naming conventions

---

Happy Learning! 🐍
