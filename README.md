Quicksort Algorithm: Deterministic and Randomized Versions
Overview
This repository contains the implementation of both deterministic and randomized versions of the Quicksort algorithm. The purpose of this assignment is to compare the performance of these two versions and analyze their time complexity under different input scenarios.

Contents:
quicksort_deterministic.py: Python script implementing deterministic Quicksort.
quicksort_randomized.py: Python script implementing randomized Quicksort.
analysis_report.pdf: Detailed report discussing the algorithm's performance, complexity, and the impact of randomization.
README.md: This file with instructions on how to run the code and a summary of the findings.
Quicksort Algorithms
Deterministic Quicksort
The deterministic version of Quicksort always selects a fixed pivot (in this case, the last element) for partitioning. This version works well on average but may suffer from 
𝑂
(
𝑛
2
)
O(n 
2
 ) time complexity when sorting already sorted or reverse-sorted arrays.

Randomized Quicksort
The randomized version of Quicksort selects a random pivot from the subarray to be sorted, reducing the likelihood of encountering the worst-case time complexity. On average, this version performs better than the deterministic one, particularly on ordered inputs.

How to Run the Code
Prerequisites
Python 3.x installed on your system.
Steps to Run
Clone the repository:

bash
Copy code
git clone https://github.com/your-repo/quicksort-algorithm.git
cd quicksort-algorithm
Run the deterministic version of Quicksort:

bash
Copy code
python code.py
Run the randomized version of Quicksort:

bash
Copy code
python code.py
Running Time Comparison
You can modify the input arrays inside the respective Python scripts to test with different array sizes or distributions (random, sorted, reverse-sorted).
The script contains example input arrays. To use different input sizes or array types, you can edit the arr variable and observe the differences in performance.
