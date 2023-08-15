# Basic Examples in Python

This section introduces the fundamental concepts and operations in Python, tailored for marine scientists and those interested in data analysis. Each topic includes a brief introduction, Python code examples, and an explanation of why things work the way they do.

## Python Basics

### Variables and Data Types

```python
# Defining variables
name = "Dolphin"
age = 5
weight = 150.5
is_mammal = True
```

**Why?**  
Variables are used to store information that can be referenced and manipulated in a program. Different data types (like strings, integers, floats, and booleans) allow us to represent different kinds of information.

### Lists, Tuples, and Dictionaries

```python
# Lists
species = ["Dolphin", "Whale", "Shark"]

# Tuples
location = (25.7617, -80.1918)  # Latitude, Longitude

# Dictionaries
dolphin_info = {"name": "Daisy", "age": 8, "type": "Bottlenose"}
```

**Why?**  
- Lists are ordered collections that are mutable (can be changed).
- Tuples are ordered collections that are immutable (cannot be changed).
- Dictionaries store data in key-value pairs, allowing for quick data retrieval.

### Control Structures

```python
# If-else statement
if age > 10:
    print("This is an adult dolphin.")
else:
    print("This is a young dolphin.")

# For loop
for specie in species:
    print(specie)
```

**Why?**  
Control structures allow us to introduce logic and repetition in our programs. They enable us to execute specific blocks of code based on conditions or repeatedly.

### Functions and Modules

```python
# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Using a function
message = greet("Daisy")
print(message)
```

**Why?**  
Functions help in modularizing and reusing code. They allow us to group a set of statements together to perform a specific task.

---

## Data Handling with Pandas

### Reading and Writing Data

```python
import pandas as pd

# Reading data from a CSV file
data = pd.read_csv("marine_data.csv")

# Writing data to an Excel file
data.to_excel("marine_data.xlsx", index=False)
```

**Why?**  
Pandas provides powerful tools for reading and writing data in various formats. This allows us to easily import and export data for analysis.

### Basic Data Exploration

```python
# Viewing the first few rows of the dataset
print(data.head())

# Getting a summary of the dataset
print(data.describe())
```

**Why?**  
Before diving into data analysis, it's essential to understand the structure and basic statistics of our data. This helps in identifying trends, anomalies, or areas that might need cleaning.

## Advanced Python Concepts

### **List Comprehensions**

A concise way to create lists using a single line of code.

```python
# Example: Squaring numbers in a list
squared_numbers = [x**2 for x in range(10)]
```

**Why?**  
List comprehensions provide a more syntactically elegant and readable way to create lists, reducing the need for multi-line loops.

### **Lambda Functions**

Short, anonymous functions without a name.

```python
# Example: Doubling a number
double = lambda x: x * 2
```

**Why?**  
Lambda functions are useful when you need a small function for a short period and don't want to formally define it using the def keyword.

### **Error Handling**

Using `try` and `except` to handle potential errors in code.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

**Why?**  
Error handling ensures that the program can continue to run and provide useful feedback even if an unexpected event occurs.

## Working with Date and Time

### **Datetime Module**

Handling dates and times.

```python
from datetime import datetime

# Current date and time
now = datetime.now()
```

**Why?**  
Date and time operations are crucial, especially when dealing with time-series marine data, like tide levels or seasonal variations.

## File Operations

### **Reading and Writing Files**

Basic operations to read from and write to files.

```python
# Writing to a file
with open('sample.txt', 'w') as file:
    file.write('Hello, Sea++!')

# Reading from a file
with open('sample.txt', 'r') as file:
    content = file.read()
```

**Why?**  
File operations are fundamental when working with datasets, logs, or any data stored in files.

## Object-Oriented Programming (OOP)

### **Classes and Objects**

Defining custom data types and methods.

```python
class Fish:
    def __init__(self, species):
        self.species = species

    def swim(self):
        print(f"The {self.species} is swimming!")

# Creating an object
salmon = Fish("Salmon")
salmon.swim()
```

**Why?**  
OOP allows for structuring the program in a way that real-world entities can be modeled, making the code more modular and organized.

## External Libraries

### **Installing and Using Libraries**

How to install and use external Python libraries.

```bash
pip install numpy
```

```python
import numpy as np
```

**Why?**  
External libraries expand Python's capabilities, providing tools and functions that aren't available in the standard library. For marine scientists, libraries like `numpy`, `pandas`, `matplotlib`, and `scipy` can be invaluable.

---

# Important Libraries

## Pandas: Data Manipulation and Analysis

**Pandas** is a powerful library that provides data structures and functions needed to efficiently manipulate large datasets.

### Reading and Writing Data

```python
import pandas as pd

# Reading data from a CSV file
data = pd.read_csv("marine_data.csv")

# Writing data to an Excel file
data.to_excel("marine_data.xlsx", index=False)
```

### Data Exploration and Cleaning

```python
# Viewing the first few rows of the dataset
print(data.head())

# Handling missing values
data.fillna(0, inplace=True)
```

1. **Read CSV**: `pd.read_csv('filename.csv')`
   - Reads a comma-separated values (CSV) file into a Pandas DataFrame. The file's path is specified as the argument.

2. **Write to CSV**: `dataframe.to_csv('filename.csv')`
   - Writes the contents of a DataFrame to a CSV file. The desired file name/path is specified as the argument.

3. **Select Column**: `dataframe['column_name']`
   - Selects and returns a specific column from the DataFrame based on the column's name.

4. **Select Row**: `dataframe.iloc[row_index]`
   - Selects and returns a specific row from the DataFrame based on its integer index.

5. **Filter Data**: `dataframe[dataframe['column'] > value]`
   - Filters and returns rows from the DataFrame where the values in the specified column meet the condition (in this case, greater than a specified value).

6. **Handle Missing Data**: `dataframe.dropna()`
   - Removes rows with missing values (NaN) from the DataFrame.

7. **Replace Missing Data**: `dataframe.fillna(value)`
   - Replaces missing values (NaN) in the DataFrame with a specified value.

8. **Group Data**: `dataframe.groupby('column_name')`
   - Groups the DataFrame based on unique values in the specified column. This is often used in conjunction with aggregation functions like `sum()`, `mean()`, etc.

9. **Merge DataFrames**: `pd.merge(df1, df2, on='common_column')`
   - Merges two DataFrames (`df1` and `df2`) based on a common column. The resulting DataFrame will have rows where the values in the 'common_column' match in both `df1` and `df2`.

10. **Pivot Table**: `pd.pivot_table(dataframe, values='D', index=['A', 'B'], columns=['C'])`
   - Creates a pivot table from the DataFrame. The values in column 'D' are aggregated (default is mean) based on unique combinations of values in columns 'A' and 'B'. The unique values in column 'C' become the new columns in the pivot table.

11. **Sort Values**: `dataframe.sort_values(by='column_name')`
   - Sorts the DataFrame based on the values in the specified column.

12. **Rename Columns**: `dataframe.rename(columns={'old_name': 'new_name'})`
   - Renames columns in the DataFrame. The old and new column names are provided as a dictionary.

13. **Set Index**: `dataframe.set_index('column_name')`
   - Sets a specific column as the index for the DataFrame.

14. **Reset Index**: `dataframe.reset_index()`
   - Resets the index of the DataFrame to the default integer index.

15. **Describe Data**: `dataframe.describe()`
   - Provides a statistical summary of the DataFrame's columns, including count, mean, standard deviation, minimum, 25th percentile, median (50th percentile), 75th percentile, and maximum.

---

## Matplotlib: Data Visualization

**Matplotlib** is a plotting library that provides a wide array of graphics and visualization tools.

### Basic Plotting

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.show()
```

1. **Basic Plot**: `plt.plot(x, y)`
   - Plots y versus x as lines (or markers) on a graph. This is the most basic type of plot.

2. **Show Plot**: `plt.show()`
   - Displays the plot. This command is typically used at the end to render the visualization.

3. **Title**: `plt.title('Title Here')`
   - Adds a title to the plot.

4. **X and Y Labels**: `plt.xlabel('X Label')`, `plt.ylabel('Y Label')`
   - Adds labels to the x-axis and y-axis, respectively.

5. **Scatter Plot**: `plt.scatter(x, y)`
   - Creates a scatter plot of y versus x using dots.

6. **Histogram**: `plt.hist(data)`
   - Plots a histogram. It groups data into bins and shows the frequency of data points in each bin.

7. **Bar Chart**: `plt.bar(x, y)`
   - Creates a bar chart. Bars represent the y-values at corresponding x-values.

8. **Pie Chart**: `plt.pie(data, labels=labels)`
   - Creates a pie chart. The data values are represented as slices of the pie, and the labels correspond to each slice.

9. **Save Figure**: `plt.savefig('filename.png')`
   - Saves the current figure to a file. You can specify the file format (e.g., PNG, JPG, SVG).

10. **Subplots**: `fig, ax = plt.subplots()`
   - Creates a new figure and a set of subplots. This is useful when you want to have multiple plots in a single figure.

11. **Legend**: `plt.legend()`
   - Adds a legend to the plot. It's used to identify the different datasets or categories in your plot.

12. **Grid**: `plt.grid(True)`
   - Adds a grid to the plot, which can help in reading the plot values.

13. **Axis Range**: `plt.xlim(start, end)`, `plt.ylim(start, end)`
   - Sets the limits of the x-axis and y-axis, respectively.

14. **Error Bars**: `plt.errorbar(x, y, yerr=y_error)`
   - Plots y versus x with error deltas (y_error) represented as vertical lines.

15. **Log Scale**: `plt.yscale('log')`
   - Sets the y-axis to a logarithmic scale. This is useful when dealing with exponential data or when there's a large range of y-values.

---

## Numpy: Numerical Operations

**Numpy** offers support for arrays (including multidimensional arrays) and an assortment of mathematical functions to operate on these arrays.

### Array Operations

```python
import numpy as np

# Creating an array
arr = np.array([1, 2, 3, 4, 5])

# Basic operations
print(arr + 10)
```

1. **Create Array**: `np.array([1, 2, 3])`
   - Creates a 1-dimensional array with the specified values.

2. **Range of Values**: `np.arange(start, stop, step)`
   - Creates an array of values starting from `start`, stopping before `stop`, and incrementing by `step`.

3. **Zeros Array**: `np.zeros(shape)`
   - Creates an array filled with zeros. The shape can be a single integer (for 1D) or a tuple (for 2D or higher dimensions).

4. **Ones Array**: `np.ones(shape)`
   - Creates an array filled with ones. The shape is specified similarly to the zeros array.

5. **Reshape Array**: `array.reshape(shape)`
   - Reshapes the array to the specified shape without changing its data.

6. **Array Dimensions**: `array.shape`
   - Returns a tuple representing the dimensions (shape) of the array.

7. **Array Data Type**: `array.dtype`
   - Returns the data type of the array's elements.

8. **Math Operations**: `np.add(array1, array2)`, `np.subtract(array1, array2)`
   - Performs element-wise addition and subtraction on two arrays, respectively.

9. **Dot Product**: `np.dot(vector1, vector2)`
   - Computes the dot product of two vectors.

10. **Matrix Multiplication**: `np.matmul(matrix1, matrix2)`
   - Multiplies two matrices together.

11. **Transpose**: `array.T`
   - Returns the transpose of the array. For a 2D matrix, this swaps rows with columns.

12. **Inverse**: `np.linalg.inv(matrix)`
   - Computes the inverse of a matrix. The matrix must be square and invertible.

13. **Sum**: `np.sum(array)`
   - Computes the sum of all elements in the array.

14. **Mean**: `np.mean(array)`
   - Computes the arithmetic mean of the array's elements.

15. **Standard Deviation**: `np.std(array)`
   - Computes the standard deviation of the array's elements.

---

## Seaborn: Advanced Data Visualization

**Seaborn** is built on top of Matplotlib and provides a higher-level interface for creating visually appealing graphics.

### Statistical Plots

```python
import seaborn as sns

# Boxplot
sns.boxplot(data=data, x='Category', y='Value')
plt.show()
```

1. **Distribution Plot**: `sns.distplot(data)`
   - Visualizes the distribution of a dataset. It combines a histogram with a kernel density estimate (KDE).

2. **Box Plot**: `sns.boxplot(x=data['X'], y=data['Y'])`
   - Displays the distribution of data based on a five-number summary: minimum, first quartile, median, third quartile, and maximum.

3. **Violin Plot**: `sns.violinplot(x=data['X'], y=data['Y'])`
   - Combines aspects of a box plot with a KDE, showing the distribution of data across different categories.

4. **Pair Plot**: `sns.pairplot(data)`
   - Plots pairwise relationships in a dataset. By using pair plots, we can immediately see the distributions of single variables and relationships between two variables.

5. **Heatmap**: `sns.heatmap(data.corr())`
   - Visualizes data as a color-encoded matrix. Commonly used for displaying correlation matrices.

6. **Bar Plot**: `sns.barplot(x='X', y='Y', data=data)`
   - Displays the average of a numerical variable per category.

7. **Count Plot**: `sns.countplot(x='X', data=data)`
   - Shows the counts of occurrences in a categorical bin.

8. **Joint Plot**: `sns.jointplot(x='X', y='Y', data=data)`
   - Displays a relationship between two variables (bivariate) as well as one-dimensional profiles (univariate) in the margins.

9. **Regression Plot**: `sns.regplot(x='X', y='Y', data=data)`
   - Plots data and a linear regression model fit.

10. **Swarm Plot**: `sns.swarmplot(x=data['X'], y=data['Y'])`
   - Displays all observations along with some representation of the underlying distribution.

11. **Facet Grid**: `g = sns.FacetGrid(data, col='Column_Name')`
   - Creates a grid of subplots based on column and row-wise variable.

12. **Set Style**: `sns.set_style('whitegrid')`
   - Sets the aesthetic style of the plots. This affects things like the color of the axes, whether a grid is enabled by default, and other aesthetic elements.

13. **Color Palette**: `sns.set_palette('husl')`
   - Sets the default color palette.

14. **Despine**: `sns.despine()`
   - Removes the top and right spines from plots.

15. **KDE Plot**: `sns.kdeplot(data)`
   - Plots a kernel density estimate to visualize the probability density of a continuous variable.

---

## OS: Operating System Interaction

The **os** library provides a way of using operating system-dependent functionality like reading or writing to the file system.

### Directory Operations

```python
import os

# Get current directory
print(os.getcwd())

# List files and directories
print(os.listdir('.'))
```

1. **Current Directory**: `os.getcwd()`
   - Returns the current working directory.

2. **Change Directory**: `os.chdir('path/to/directory')`
   - Changes the current working directory to the specified path.

3. **List Files**: `os.listdir('path/to/directory')`
   - Returns a list of files and directories in the specified directory.

4. **Create Directory**: `os.mkdir('directory_name')`
   - Creates a new directory with the specified name.

5. **Remove Directory**: `os.rmdir('directory_name')`
   - Removes the specified directory. The directory must be empty.

6. **Rename File/Directory**: `os.rename('old_name', 'new_name')`
   - Renames a file or directory from `old_name` to `new_name`.

7. **Check Path Exists**: `os.path.exists('path/to/file_or_directory')`
   - Returns `True` if the specified file or directory exists, otherwise `False`.

8. **Join Paths**: `os.path.join('path', 'filename')`
   - Joins one or more path components together into a single path.

9. **Get File Size**: `os.path.getsize('path/to/file')`
   - Returns the size of the specified file in bytes.

10. **Split Path**: `os.path.split('path/to/file')`
   - Splits the pathname into a tuple containing the directory and filename.

11. **File Extension**: `os.path.splitext('filename.ext')`
   - Splits the pathname into a tuple containing the root and extension.

12. **Check if Directory**: `os.path.isdir('path/to/directory')`
   - Returns `True` if the specified path is a directory, otherwise `False`.

13. **Check if File**: `os.path.isfile('path/to/file')`
   - Returns `True` if the specified path is a regular file, otherwise `False`.

14. **Absolute Path**: `os.path.abspath('path')`
   - Returns the absolute path of the specified path.

15. **Create Directories**: `os.makedirs('path/to/directory')`
   - Creates a directory recursively, meaning it creates any intermediate directories in the path that don't exist yet.

---

## Shutil: idk what it's called 

The `shutil` module in Python provides a higher-level interface for file operations. Here are 15 important commands from the `shutil` library along with their descriptions:

1. **copy(src, dst)**
   - **Description**: Copies the file `src` to the file or directory `dst`.
   
2. **copy2(src, dst)**
   - **Description**: Similar to `copy()`, but metadata is also copied.

3. **copyfile(src, dst)**
   - **Description**: Copies the contents of the source file to the destination file.

4. **copytree(src, dst)**
   - **Description**: Recursively copies an entire directory tree rooted at `src` to the destination directory.

5. **rmtree(path)**
   - **Description**: Recursively deletes a directory tree.

6. **move(src, dst)**
   - **Description**: Moves a file or directory (`src`) to another location (`dst`).

7. **disk_usage(path)**
   - **Description**: Returns disk usage statistics about the given path as a named tuple with the attributes `total`, `used`, and `free`.

8. **chown(path, user, group)**
   - **Description**: Change the owner and group id of the given path to the numeric `user` and `group`.

9. **which(cmd)**
   - **Description**: Returns the path to an executable which would be run if the given `cmd` was called.

10. **make_archive(base_name, format, root_dir=None, base_dir=None)**
   - **Description**: Creates an archive file (such as zip or tar) and returns its name.

11. **unpack_archive(filename, extract_dir=None, format=None)**
   - **Description**: Unpacks an archive file.

12. **get_archive_formats()**
   - **Description**: Returns a list of supported formats for archiving.

13. **get_unpack_formats()**
   - **Description**: Returns a list of supported formats for unpacking.

14. **get_terminal_size(fallback=(columns, lines))**
   - **Description**: Returns the size of the terminal window as a named tuple of `columns` and `lines`.

15. **ignore_patterns(*patterns)**
   - **Description**: Returns a function that can be used as `copytree`'s `ignore` callback function, ignoring files and directories that match one of the glob-style patterns.


These headings and brief introductions provide a structured way to introduce each library and its primary functionalities. You can expand upon each section by adding more detailed examples and explanations as needed.