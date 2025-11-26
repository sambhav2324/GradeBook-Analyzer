# 📊 GradeBook Analyzer CLI

> A powerful Python-based command-line tool for analyzing student grades, computing statistics, and generating comprehensive academic reports.

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-PEP8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

---

## 🎯 Project Overview

**GradeBook Analyzer** is an intelligent command-line interface (CLI) application designed to help educators and academic administrators efficiently manage and analyze student performance data. Built with Python, this tool automates the tedious process of grade calculation, statistical analysis, and report generation.

### ✨ Key Features

- **📥 Flexible Data Input**: Support for both manual entry and CSV file imports
- **📊 Statistical Analysis**: Automatic calculation of mean, median, min, and max scores
- **🎓 Grade Assignment**: Intelligent letter grade distribution (A-F grading system)
- **✅ Pass/Fail Filtering**: Quick identification of students above/below threshold
- **📈 Visual Distribution**: Grade distribution summary with percentage breakdown
- **💾 Export Functionality**: Save results to CSV format for future reference
- **🔄 Interactive Loop**: Perform multiple analyses in a single session
- **📁 Auto-Discovery**: Automatic detection of CSV files in the current directory

---

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- No external dependencies required (uses only standard library)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ayush-saini8920/gradebook-analyzer-cli.git
   cd gradebook-analyzer-cli
   ```

2. **Run the program**
   ```bash
   python gradebook.py
   ```

That's it! No pip installations needed. 🎉

---

## 📖 Usage Guide

### Option 1: Manual Entry

```bash
$ python gradebook.py

# Select option 1
# Enter student names and marks
# Type 'done' when finished
```

**Example:**
```
Enter student name: Alice
Enter marks for Alice: 92
✓ Added Alice with marks 92.0

Enter student name: Bob
Enter marks for Bob: 85
✓ Added Bob with marks 85.0

Enter student name: done
```

### Option 2: CSV Import

```bash
# The program automatically lists available CSV files
# Simply enter the filename when prompted
```

**CSV Format:**
```csv
Name,Marks
Alice,92
Bob,85
Charlie,78
Diana,65
Eve,45
```

---

## 📊 Sample Output

```
==============================================================
STATISTICAL ANALYSIS
==============================================================
Total Students:     5
Average Marks:      73.00
Median Marks:       78.00
Highest Score:      92.00 (Alice)
Lowest Score:       45.00 (Eve)
==============================================================

==============================================================
GRADE DISTRIBUTION
==============================================================
Grade A:    1 students ( 20.0%)  █
Grade B:    1 students ( 20.0%)  █
Grade C:    1 students ( 20.0%)  █
Grade D:    1 students ( 20.0%)  █
Grade F:    1 students ( 20.0%)  █
==============================================================

==============================================================
FINAL RESULTS TABLE
==============================================================
Name                 Marks      Grade     
------------------------------------------------------------
Alice                92.00      A         
Bob                  85.00      B         
Charlie              78.00      C         
Diana                65.00      D         
Eve                  45.00      F         
==============================================================
```

---

## 🎓 Grading Scale

| Letter Grade | Marks Range | Description |
|--------------|-------------|-------------|
| A            | 90 - 100    | Excellent   |
| B            | 80 - 89     | Good        |
| C            | 70 - 79     | Average     |
| D            | 60 - 69     | Below Average |
| F            | 0 - 59      | Fail        |

**Pass Threshold:** 40 marks

---

## 🗂️ Project Structure

```
gradebook-analyzer-cli/
│
├── gradebook.py          # Main application script
├── README.md             # Project documentation
├── students.csv          # Sample data file (for testing)
├── .gitignore            # Git ignore rules
└── LICENSE               # MIT License
```

---

## 🛠️ Technical Implementation

### Core Functions

| Function | Purpose |
|----------|---------|
| `calculate_average()` | Computes mean of all marks |
| `calculate_median()` | Finds median value |
| `find_max_score()` | Identifies highest scorer |
| `find_min_score()` | Identifies lowest scorer |
| `assign_grade()` | Converts marks to letter grades |
| `filter_pass_fail()` | Uses list comprehension for filtering |
| `save_to_csv()` | Exports results to CSV |

### Design Patterns Used

- **Modular Programming**: Functions are independent and reusable
- **Error Handling**: Try-catch blocks for robust file operations
- **Input Validation**: Ensures data integrity
- **List Comprehensions**: Efficient filtering operations
- **CLI Menu Loop**: Interactive user experience

---

## 📝 Assignment Context

This project was developed as part of the **Programming for Problem Solving using Python** course assignment.

**Assignment Details:**
- **Type:** Individual Project
- **Duration:** 8-10 hours
- **Weightage:** 5 marks
- **Focus Areas:** Data structures, statistical functions, file I/O, CLI design

### Learning Outcomes

✅ Reading and storing data in Python dictionaries  
✅ Implementing statistical analysis functions  
✅ Using control flow for grade assignment  
✅ Applying list comprehensions for filtering  
✅ Modular programming with functions  
✅ Formatted output and CLI design  

---

## 🧪 Testing

### Test Cases

1. **Manual Entry Test** (Minimum 5 students)
   ```bash
   python gradebook.py
   # Select option 1 and enter 5+ students
   ```

2. **CSV Import Test**
   ```bash
   python gradebook.py
   # Select option 2 and load students.csv
   ```

3. **Edge Cases**
   - Empty dataset
   - Single student
   - All students with same marks
   - Boundary values (0, 40, 60, 70, 80, 90, 100)

### Sample Test Data

Create `students.csv`:
```csv
Name,Marks
Alice Johnson,92
Bob Smith,85
Charlie Brown,78
Diana Prince,88
Eve Taylor,45
Frank Miller,95
Grace Lee,72
Henry Wilson,38
Ivy Chen,81
Jack Davis,55
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Enhancement

- [ ] Add GUI using Tkinter
- [ ] Support for Excel files (.xlsx)
- [ ] Graphical charts using matplotlib
- [ ] Database integration (SQLite)
- [ ] Multi-subject support
- [ ] Weighted grade calculation
- [ ] Grade curve adjustment
- [ ] Student comparison reports

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**[Sambhav Agarwal]**
- Email: 2501010191@krmu.edu.in

---
---

## 📸 Screenshots

### Main Menu
```
==============================================================
                   GRADEBOOK ANALYZER
==============================================================
Welcome! This tool helps you analyze student grades.
You can input data manually or load from a CSV file.
==============================================================
```

### Analysis Results
*Detailed statistical analysis with grade distribution and formatted tables*

---

## 🎯 Project Status

✅ **Complete** - All assignment requirements fulfilled  
✅ **Tested** - Manual and CSV input modes verified  
✅ **Documented** - Comprehensive code comments  
✅ **Production Ready** - Error handling implemented  

---

## 📚 Resources

- [Python CSV Module Documentation](https://docs.python.org/3/library/csv.html)
- [Python Statistics Module](https://docs.python.org/3/library/statistics.html)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Git Best Practices](https://git-scm.com/book/en/v2)

---


---

## 📋 Changelog

### Version 1.0.0 (November 2025)
- ✨ Initial release
- ✅ Manual entry mode
- ✅ CSV import functionality
- ✅ Statistical analysis
- ✅ Grade assignment system
- ✅ Pass/fail filtering
- ✅ Results export to CSV
- ✅ Auto-discovery of CSV files

---

**Happy Coding! 🚀**
