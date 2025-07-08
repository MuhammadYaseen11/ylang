# YLang — A Domain-Specific Language for Learning Data Structures & Algorithms (DSA)

**Author:** Muhammad Yaseen  

---

## Project Overview

YLang is a lightweight, interpreted programming language designed specifically to help learners understand and practice core Data Structures and Algorithms concepts easily. 

Traditional programming languages often require boilerplate or complex syntax when working with data structures like arrays, linked lists, and trees. YLang abstracts these complexities with simple, human-readable commands and built-in support for essential data structures and algorithms.

This project demonstrates my ability to:

- Design and implement a custom programming language interpreter from scratch.
- Apply core computer science concepts including data structures and algorithms.
- Build clean, modular Python code that can be extended and maintained.
- Provide educational tools that facilitate learning and practicing technical skills.

---

## Features

### Language Constructs

- **Variables and Basic Types:** Declare and use integer variables.
- **Arrays:** Create arrays with intuitive syntax; supports insertion, deletion, sorting, and searching.
- **Linked Lists:** Create singly linked lists with insertion, deletion, and traversal.
- **Binary Trees:** Create binary search trees with insertion and inorder traversal.
- **Control Structures:** Supports simple repetition (`repeat n times`) and arithmetic operations (`add x to y`).
- **Input/Output:** Use `say` command to print variables or strings.

### Supported Commands Examples

```plaintext

let x = 10
say x

array nums = [5,3,8,1]
nums.insert(2, 9)
nums.sort()
say nums

linkedlist list
list.insert(10)
list.insert(20)
list.delete(10)
say list

tree t
t.insert(15)
t.insert(10)
t.insert(20)
say t

repeat 3 times say "Practice DSA daily!"
add 5 to 7
```
### Why YLang?
Educational Focus: Designed to reduce complexity in practicing DSA, helping beginners focus on concepts without syntax distractions.

Custom Data Structures: Native implementations of arrays, linked lists, and trees with useful methods.

Extendable Interpreter: Written in Python with clear structure, easily extensible to add more data structures or language features.

Command-Line Interface: Simple script-based usage for quick testing and learning.

### Technical Details
Language Interpreter: Built from scratch in Python using procedural parsing for simplicity.

Data Structures Implemented:

Dynamic arrays with insertion, deletion, sorting, and searching.

Singly linked lists with insertion, deletion, and traversal.

Binary Search Trees with insertion and inorder traversal.

Algorithms: Sorting and searching are natively supported as array methods.

Error Handling: Basic error reporting for invalid commands and out-of-bound operations.

Modular Design: Object-oriented data structure classes and command interpreter functions separated for clarity.

### Skills Demonstrated
Language Design & Implementation

Data Structures & Algorithms

Python Programming & OOP

Parsing & Interpretation

Command-line Tool Development

Software Documentation & Clean Code Practices

### Future Improvements
Add more complex control flow (if-else, loops).

Implement more algorithms (graph traversals, advanced sorts).

Add user-defined functions and variables of different types.

Create an interactive REPL for instant command execution.

Build visualization tools for data structures to enhance learning.
