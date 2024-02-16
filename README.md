# Sorting-Visualizer-in-Python-Tkinter-DAA-
Sorting Algorithms Visualization is a Python project that provides a GUI for visualizing and comparing sorting algorithms, allowing users to interactively observe the sorting process of two lists read from text files.

Description:
This Python script provides a graphical user interface (GUI) to visualize and compare the sorting algorithms. It reads data from two text files (input1.txt and input2.txt), displays the unsorted lists, and allows the user to select a list for sorting using either Bubble Sort or Merge Sort.

Features:

Bubble Sort Visualization: The bubble function visualizes the Bubble Sort algorithm by animating the sorting process using matplotlib.
Merge Sort Visualization: The mergeSort and merge functions visualize the Merge Sort algorithm by animating the sorting process using matplotlib.
GUI Interface: The script uses tkinter to create a simple GUI with buttons to select and sort the lists.
Dependencies:

matplotlib: For visualization of sorting algorithms.
tkinter: For creating the GUI.
Usage:

Ensure that the text files input1.txt and input2.txt contain the unsorted lists.
Run the script to open the GUI window.
Select a list to sort by clicking the corresponding button (list1 or list2).
Choose the sorting algorithm by clicking the respective button.

Insertion Sort: Iterates over the list, moving elements that are greater than the current key to one position ahead of their current position.
Heap Sort: Utilizes a heap data structure to sort elements. It first converts the array into a heap, then repeatedly extracts the maximum element and rebuilds the heap.
Selection Sort: Selects the minimum element from the unsorted portion of the array and swaps it with the element at the current position.
Quick Sort: Chooses a pivot element and partitions the array such that all elements less than the pivot are on its left, and all elements greater are on its right. Recursively applies this operation to sub-arrays.
Merge Sort: Divides the array into two halves, recursively sorts the two halves, and then merges the sorted halves.
Radix Sort: Sorts numbers by processing individual digits. It sorts the numbers from the least significant digit to the most significant digit.
Count Sort: Sorts elements based on their count occurrences in the input array.
Bucket Sort: Distributes elements into a number of buckets, then sorts the elements in each bucket and merges them back.

These algorithms are visualized step-by-step using graphical elements to help users understand their workings better.
