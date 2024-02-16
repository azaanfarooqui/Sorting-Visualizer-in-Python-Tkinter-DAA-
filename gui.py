from tkinter import *
from tkinter import ttk
from sorting import Sortings

global choice
Sortings = Sortings()

global speedScale
speedScale = 0.1


def SECONDSCREEN(choice):
    root = Tk()
    root.title('Sorting Algorithm Visualiser')
    root.maxsize(900, 600)
    root.config(bg='black')

    # variables
    selected_alg = StringVar()

    # function
    def drawData(data, colorArray):
        canvas.delete("all")
        c_height = 380
        c_width = 600
        x_width = c_width / (len(data) + 1)
        offset = 30
        spacing = 10
        normalizedData = [i / max(data) for i in data]
        for i, height in enumerate(normalizedData):
            # top left
            x0 = i * x_width + offset + spacing
            y0 = c_height - height * 350
            # bottom right
            x1 = (i + 1) * x_width + offset
            y1 = c_height

            canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
            canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]), fill='white')

        root.update_idletasks()

    def Generate():
        global data
        if choice == 1:
            infofile2 = open("input1.txt", "r")
            data = []
            for y in infofile2:
                data.append(float(y))
        elif choice == 2:
            infofile2 = open("input2.txt", "r")
            data = []
            for y in infofile2:
                data.append(int(y))

        elif choice == 3:
            infofile2 = open("input3.txt", "r")
            data = []
            for y in infofile2:
                data.append(int(y))

        drawData(data, ['white' for x in range(len(data))])

    def StartAlgorithm():
        global data
        if not data: return

        if algMenu.get() == 'Quick Sort':
            Sortings.quick_sort(data, 0, len(data) - 1, drawData, speedScale)
            Label(UI_frame, text="---Time Complexity: O(nlog(n)) ---", bg='black', fg='white').grid(row=1, column=0, padx=5,
                                                                                              pady=5, )

        elif algMenu.get() == 'Bubble Sort':
            Sortings.bubble_sort(data, drawData, speedScale)
            Label(UI_frame, text="---Time Complexity: O(n^2)---", bg='black', fg='white').grid(row=1, column=0, padx=5,
                                                                                          pady=5)

        elif algMenu.get() == 'Selection Sort':
            Sortings.selection_sort(data, drawData, speedScale)
            Label(UI_frame, text="----Time Complexity: O(n^2)--- ", bg='black', fg='white').grid(row=1, column=0, padx=5,
                                                                                          pady=5)

        elif algMenu.get() == 'Merge Sort':
            Sortings.merge_sort(data, drawData, speedScale)
            Label(UI_frame, text="---Time Complexity: O(nlog(n))---", bg='black', fg='white').grid(row=1, column=0, padx=5,
                                                                                              pady=5)

        elif algMenu.get() == 'Insertion Sort':
            Sortings.insertionSort(data, drawData, speedScale)
            Label(UI_frame, text="--Time Complexity: O(nlog(n)) --", bg='black', fg='white').grid(row=1, column=0, padx=5,
                                                                                              pady=5)

        elif algMenu.get() == 'Heap Sort':
            Sortings.heapSort(data, drawData, speedScale)
            Label(UI_frame, text="----Time Complexity: O(nlog(n)) --", bg='black', fg='white').grid(row=1, column=0, padx=5,
                                                                                              pady=5)

        elif algMenu.get() == 'Radix Sort':
            if choice == 2 or choice == 3:
                Sortings.count_sort(data, drawData, speedScale)
                Label(UI_frame, text="----Time Complexity: O(nd) --", bg='black', fg='white').grid(row=1, column=0, padx=5,
                                                                                              pady=5)
            else:
                Label(UI_frame, text="----NOT COMPATIBLE------- ", bg='black', fg='white').grid(row=1, column=0, padx=5,
                                                                                                pady=5)

        elif algMenu.get() == 'Count Sort':
            if choice == 2 or choice == 3:
                Sortings.count_sort(data, drawData, speedScale)
                Label(UI_frame, text="---Time Complexity: O(n+k) ", bg='black', fg='white').grid(row=1, column=0, padx=5,
                                                                                          pady=5)
            else:
                Label(UI_frame, text="----NOT COMPATIBLE------- ", bg='black', fg='white').grid(row=1, column=0, padx=5,
                                                                                              pady=5)

        elif algMenu.get() == 'Bucket Sort':
            if choice == 1:
                Sortings.bucketSort(data, drawData, speedScale)
                Label(UI_frame, text="----Time Complexity: O(n+k)----", bg='black', fg='white').grid(row=1, column=0, padx=5,
                                                                                              pady=5)
            else:
                Label(UI_frame, text="----NOT COMPATIBLE-------", bg='black', fg='white').grid(row=1, column=0, padx=5,
                                                                                     pady=5)

        drawData(data, ['yellow' for x in range(len(data))])

    # frame / base lauout
    UI_frame = Frame(root, width=700, height=300, bg='red')
    UI_frame.grid(row=0, column=0, padx=0, pady=0)

    canvas = Canvas(root, width=700, height=380, bg='black')
    canvas.grid(row=1, column=0, padx=0, pady=0)
    # User Interface Area
    # Row[0]

    Label(UI_frame, text="Algorithm: ", bg='black', fg='white').grid(row=0, column=0, padx=5, pady=5, sticky=W)
    algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg,
                           values=['Bubble Sort', 'Selection Sort', 'Quick Sort', 'Merge Sort', 'Radix Sort',
                                   'Insertion Sort', 'Heap Sort', 'Count Sort', 'Bucket Sort'])
    algMenu.grid(row=0, column=1, padx=5, pady=5)
    algMenu.current(0)

    Button(UI_frame, text="Start", command=StartAlgorithm, bg='green').grid(row=1, column=3, padx=5, pady=5)

    Button(UI_frame, text="Generate", command=Generate, bg='grey').grid(row=0, column=3, padx=5, pady=5)

    root.mainloop()


root = Tk()
root.geometry("400x400")
root.title("Sorting Algos")
root.config(bg='black')
infofile = open("input1.txt", "r")
lst = []
for y in infofile:
    lst.append(float(y))

infofile2 = open("input2.txt", "r")
lst1 = []
for y in infofile2:
    lst1.append(int(y))

infofile3 = open("input3.txt", "r")
lst2 = []
for y in infofile3:
    lst2.append(int(y))

l = Label(text='text file 1', bg='yellow')
l.pack()
listbox = Listbox(root, width=40, height=1)
listbox.insert(0, lst)
listbox.pack()
l = Label(text='text file 2', bg='yellow')
l.pack()
listbox = Listbox(root, width=40, height=1)
listbox.insert(0, lst1)
listbox.pack()
l = Label(text='text file 3', bg='yellow')
l.pack()
listbox = Listbox(root, width=50, height=1)
listbox.insert(0, lst2)
listbox.pack()
l = Label(text='Please choose the text file u want to sort', bg='yellow')
l.pack()
mainbut = Button(root, text='File1', command=lambda: SECONDSCREEN(1))
mainbut.pack()
mainbut2 = Button(root, text='File2', command=lambda: SECONDSCREEN(2))
mainbut2.pack()
mainbut3 = Button(root, text='File3', command=lambda: SECONDSCREEN(3))
mainbut3.pack()
root.mainloop()
