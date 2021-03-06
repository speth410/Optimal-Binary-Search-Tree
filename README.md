
# Instructions

You are to implement the dynamic programming algorithm we discussed in class for the optimal binary search tree problem.

 

>- You must provide a feature to store the three matrices e, w, and r, and also the optimal binary search tree in files. Use appropriate file names.  No GUI is required for displaying the tree.  A textual structure (display) is sufficient.
>- You may use the algorithms provided in the class (and in Chapter 15); however, you must not reuse the implementations from other sources. The implementation must be yours. You cannot use code written by others, including seeking free and/or paid services from others (e.g., Course Hero). It is an individual assignment, and no group work is expected or will be accepted.
>- There is no specific programming-language requirement for this assignment.
>- You must chart the performance of the algorithm for n=10, 100, 1000, 10000, and 100000 randomly generated input keys (then sorted) and their probabilities. Remember you would need n+1 dummy keys and the sum of probabilities of real and dummy keys is one. You may reuse the code from Assignment 01.
>- Compare the recorded performances (time measurements) with their theoretical growth rates, i.e., “Big-oh” complexities.
>- If you run out of resources for a specific configuration (e.g., out of memory for 1,000,000 keys), it should be noted and submitted.
>- Provide a README file explaining the structure of your implementation, decision designs, and how to execute your program.

## Requirements


```bash
python3
numpy
pandas
```

## Usage

```bash
python3 OptimalBinarySearchTree.py
```

## Structure
#### main()
> Carries out the main execution of the program
#### optimalBST()
> Performs the Optimal Binary Search Tree Algorithm given an array of key probabilities (p), array of dummy key probabilities (q), and the number of keys (n).
#### generateProbabilities()
> Generates n number of pseudo-random key probabilities that add up to 1.
#### ouput()
> Ouputs the results of the optimalBST() algorithm to a csv file.
