import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from collections import Counter
from datetime import datetime

def bubble(lst):
    tempo=lst
    x = np.arange(0, len(tempo), 1)
    n = len(tempo)
    for i in range(n):
        for j in range(0, n - i - 1):
            plt.bar(x, tempo)
            plt.pause(0.001)
            plt.clf()
            if tempo[j] > tempo[j + 1]:
                tempo[j], tempo[j + 1] = tempo[j + 1], tempo[j]

    plt.show()


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2
        x = np.arange(0, len(arr), 1)

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        plt.bar(x, arr)
        plt.pause(0.001)
        plt.clf()
        merge(arr, l, m, r)
        plt.bar(x, arr)
        plt.pause(0.001)
        plt.clf()

def secondscreen(lstt,original_list):

    root = Tk()
    root.geometry("400x400")
    root.title("Sorting Algos")
    print(original_list)
    mybutton=Button(root,text='Bubble sort',command=lambda: bubble(lstt))
    mybutton.pack()
    mybutton2 = Button(root, text='Merge sort', command=lambda: mergeSort(original_list,0,len(original_list)-1))
    mybutton2.pack()
    print(original_list)
    root.mainloop()


root = Tk()
root.geometry("400x400")
root.title("Sorting Algos")

infofile = open("input1.txt", "r")
lst = []
for y in infofile:
    lst.append(int(y))

infofile2 = open("input2.txt", "r")
lst1 = []
for y in infofile2:
    lst1.append(int(y))

l=Label(text='text file 1',bg='yellow')
l.pack()
listbox = Listbox(root,width=20,height=1)
listbox.insert(0,lst)
listbox.pack()
l=Label(text='text file 2',bg='yellow')
l.pack()
listbox = Listbox(root,width=20,height=1)
listbox.insert(0,lst1)
listbox.pack()
l=Label(text='Please choose the text file u want to sort',bg='yellow')
l.pack()
mainbut = Button(root, text='list1', command=lambda: secondscreen(lst,lst))
mainbut.pack()
mainbut2 = Button(root, text='list2', command=lambda: secondscreen(lst1,lst1))
mainbut2.pack()
root.mainloop()