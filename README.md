# File-System
This project simulates two different file allocation strategies: Contiguous Allocation and Linked Allocation. It helps to understand how these strategies manage disk space and allocate files in a given number of blocks.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

- ## Introduction
- File allocation strategies are crucial for efficient disk space mamagement. This project provides a simulation of Contiguous Allocation and Linked Allocation strategies, visualizing how files are stored in disk blocks and comparing their efficiency.

- ## Features
- **Contiguous Allocation**: Allocates a sequance of contiguous blocks for each file.
- **Linked Allocation**: Allocates blocks non-contiguously with each blocks pointing to the next block in the sequence.
- **Visualization**: Displays the allocation table and the state of the disk blocks for each strategy.

- ## Installation
- To run this project, ensure you have Python and numpy installed on your system. You can download python from [python.org](https://www.python.org/downloads/). You can install numpy using pip:

- ```bash
  pip intall numpy

  #Clone this repository:
  ```bash
  git clone https://github.com/ayoushka/File-System.git
  cd File-System

  ## Usage
  python main.py

  ## Examples
  Enter the total number of disk blocks: 10
  Enter the number of files: 2
  Enter size of file 1 (in blocks): 3
  Enter size of file 2 (in blocks): 4
  
## Contribution
Contributions are welcome!
Feel free to open issues or subnit pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for mor details.
Feel free to customize this README file according to your project's specific details and requirements! If you have any additional questions or need further assistance, let me know.
