import time


class Sortings:
    # Insertion Sort
    def insertionSort(self, arr, drawData, timeTick):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            drawData(arr, ['red' if x == i else 'white' for x in range(len(arr))])
            time.sleep(timeTick)
            while j >= 0 and key < arr[j]:
                drawData(arr, ['yellow' if x == j + 1 else 'white' for x in range(len(arr))])
                time.sleep(timeTick)
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key
            drawData(arr, ['green' if x == j + 1 else 'white' for x in range(len(arr))])
            time.sleep(timeTick)

    # BUBBLE SORT
    def bubble_sort(self, data, drawData, timeTick):
        for _ in range(len(data) - 1):
            for j in range(len(data) - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    drawData(data, ['green' if x == j or x == j + 1 else 'white' for x in range(len(data))])
                    time.sleep(0.2)

        drawData(data, ['green' for x in range(len(data))])

    def heapify(self, arr, N, i, drawData, timeTick):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        drawData(arr, ['green' if x >= l and x <= r else 'white' for x in range(len(arr))])
        time.sleep(timeTick)
        if l < N and arr[largest] < arr[l]:
            largest = l
            drawData(arr, ['yellow' if x == l else 'white' for x in range(len(arr))])
            time.sleep(timeTick)

        if r < N and arr[largest] < arr[r]:
            largest = r
            drawData(arr, ['yellow' if x == r else 'white' for x in range(len(arr))])
            time.sleep(timeTick)

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            drawData(arr, ['red' if x == i else 'white' for x in range(len(arr))])
            time.sleep(timeTick)
            self.heapify(arr, N, largest, drawData, timeTick)


    def heapSort(self, arr, drawData, timeTick):
        N = len(arr)

        for i in range(N // 2 - 1, -1, -1):
            self.heapify(arr, N, i, drawData, timeTick)

        for i in range(N - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0, drawData, timeTick)

    # SELECTION SORT
    def selection_sort(self, data, drawData, timeTick):
        for i in range(len(data) - 1):

            min_idx = i
            for j in range(i + 1, len(data)):
                if data[min_idx] > data[j]:
                    min_idx = j

            data[i], data[min_idx] = data[min_idx], data[i]
            drawData(data, ['green' if x == min_idx or x == i else 'red' for x in range(len(data))])
            time.sleep(timeTick)

        drawData(data, ['green' for x in range(len(data))])

    # QUICK SORT
    def partition(self, data, left, right, drawData, timeTick):
        border = left
        pivot = data[right]

        drawData(data, self.getColorArray(len(data), left, right, border, border))
        time.sleep(timeTick)

        for j in range(left, right):
            if data[j] < pivot:
                drawData(data, self.getColorArray(
                    len(data), left, right, border, j, True))
                time.sleep(timeTick)

                data[border], data[j] = data[j], data[border]
                border += 1

            drawData(data, self.getColorArray(len(data), left, right, border, j))
            time.sleep(timeTick)

        drawData(data, self.getColorArray(len(data), left, right, border, right, True))
        time.sleep(timeTick)

        data[border], data[right] = data[right], data[border]

        return border

    def quick_sort(self, data, left, right, drawData, timeTick):
        if left < right:
            partitionIdx = self.partition(data, left, right, drawData, timeTick)

            # LEFT PARTITION
            self.quick_sort(data, left, partitionIdx - 1, drawData, timeTick)

            # RIGHT PARTITION
            self.quick_sort(data, partitionIdx + 1, right, drawData, timeTick)

    def getColorArray(self, dataLen, left, right, border, currIdx, isSwaping=False):
        colorArray = []
        for i in range(dataLen):
            # base coloring
            if i >= left and i <= right:
                colorArray.append('gray')
            else:
                colorArray.append('white')

            if i == right:
                colorArray[i] = 'yellow'
            elif i == border:
                colorArray[i] = 'yellow'
            elif i == currIdx:
                colorArray[i] = 'yellow'

            if isSwaping:
                if i == border or i == currIdx:
                    colorArray[i] = 'green'

        return colorArray

    # MERGE SORT
    def merge_sort(self, data, drawData, timeTick):
        self.merge_sort_alg(data, 0, len(data) - 1, drawData, timeTick)


    def merge_sort_alg(self, data, left, right, drawData, timeTick):
        if left < right:
            middle = (left + right) // 2
            self.merge_sort_alg(data, left, middle, drawData, timeTick)
            self.merge_sort_alg(data, middle + 1, right, drawData, timeTick)
            self.merge(data, left, middle, right, drawData, timeTick)

    def merge(self, data, left, middle, right, drawData, timeTick):

        leftPart = data[left:middle + 1]
        rightPart = data[middle + 1: right + 1]

        leftIdx = rightIdx = 0

        for dataIdx in range(left, right + 1):
            if leftIdx < len(leftPart) and rightIdx < len(rightPart):
                if leftPart[leftIdx] <= rightPart[rightIdx]:
                    data[dataIdx] = leftPart[leftIdx]
                    leftIdx += 1
                else:
                    data[dataIdx] = rightPart[rightIdx]
                    rightIdx += 1

            elif leftIdx < len(leftPart):
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1

        drawData(data, ["green" if left <= x <= right else "white" for x in range(len(data))])
        time.sleep(timeTick)

    # RADIX SORT
    def countingSort(self, arr, exp1, drawData, timeTick):

        n = len(arr)
        output = [0] * (n)
        count = [0] * (10)

        for i in range(0, n):
            index = arr[i] // exp1
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] // exp1
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
            drawData(arr, ["yellow" if x == index or x == i else "white" for x in range(len(arr))])
            time.sleep(timeTick)

        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]
            drawData(arr, ["red" if x == i else "white" for x in range(len(arr))])
            time.sleep(timeTick)

    # Method to do Radix Sort
    def radixSort(self, arr, drawData, timeTick):

        max1 = max(arr)
        exp = 1
        while max1 / exp >= 1:
            self.countingSort(arr, exp, drawData, timeTick)
            exp *= 10

    # COUNT SORT
    def count_sort(self, arr, drawData, timeTick):
        max_element = int(max(arr))
        min_element = int(min(arr))
        range_of_elements = max_element - min_element + 1
        count_arr = [0 for _ in range(range_of_elements)]
        output_arr = [0 for _ in range(len(arr))]

        for i in range(0, len(arr)):
            count_arr[arr[i] - min_element] += 1
            drawData(arr, ["green" if x == i else "white" for x in range(len(arr))])
            time.sleep(timeTick)

        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i - 1]

        for i in range(len(arr) - 1, -1, -1):
            output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
            count_arr[arr[i] - min_element] -= 1

        for i in range(0, len(arr)):
            arr[i] = output_arr[i]
            drawData(arr, ["red" if x == i else "white" for x in range(len(arr))])
            time.sleep(timeTick)

    # BUCKET SORT
    def IS(self, b, drawData, timeTick):
        for i in range(1, len(b)):
            up = b[i]
            j = i - 1
            while j >= 0 and b[j] > up:
                b[j + 1] = b[j]
                j -= 1
            b[j + 1] = up
        return b

    def bucketSort(self, x, drawData, timeTick):
        arr = []
        slot_num = 10
        for i in range(slot_num):
            arr.append([])

        for j in x:
            index_b = int(slot_num * j)
            arr[index_b].append(j)

        for i in range(slot_num):
            drawData(x, ["red" if v == i else "white" for v in range(len(x))])
            time.sleep(timeTick)
            arr[i] = self.IS(arr[i], drawData, timeTick)

        k = 0
        for i in range(slot_num):
            for j in range(len(arr[i])):
                x[k] = arr[i][j]
                k += 1
                drawData(x, ["green" if v == j or v == j + 1 else "white" for v in range(len(x))])
                time.sleep(timeTick)
