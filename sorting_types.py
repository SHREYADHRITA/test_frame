# this is a basic code to perform different types of sorting using OOPs concept

class Sorting:

    def __init__(self):
        # this is the constructor class executed when the class Sorting is called
        self.unsorted = []
        self.num = int(input("enter a number of elements in the list"))
        for i in range(0, self.num):
            n = int(input("enter a number"))
            self.unsorted.append(n)
        self.min = 0

    def selection_sort(self):
        n = len(self.unsorted)
        for i in range(0, n):
            current_min = self.unsorted[i]  # initialise with first value
            self.min = i  # min initialiser
            # iterate over remaining unsorted items
            for j in range(i, n):
                # check if jth value is less than current min
                if self.unsorted[j] < current_min:
                    # update minimum value and index
                    current_min = self.unsorted[j]
                    self.min = j
                    temp = self.unsorted[i]
                    self.unsorted[i] = self.unsorted[self.min]
                    self.unsorted[self.min] = temp

        return self.unsorted

    def bubble_sort(self):
        """ bubble sort algorithm """
        n = len(self.unsorted)
        # iterate over unsorted array up until second last element
        for i in range(0, n - 1):

            # swapped conditions monitors for finalised list
            swapped = False

            # iterate over remaining unsorted items
            for j in range(0, n - 1 - i):

                # compare adjacent elements
                if self.unsorted[j] > self.unsorted[j + 1]:
                    # swap elements
                    temp = self.unsorted[j]
                    self.unsorted[j] = self.unsorted[j + 1]
                    self.unsorted[j + 1] = temp
                    swapped = True

            if not swapped:
                break
        return self.unsorted


sort = Sorting()

print("1-selection sort, \n 2-bubble sort")
o = int(input("enter the type of sort you want to perform"))

if o == 1:
    print(sort.selection_sort())
if o == 2:
    print(sort.bubble_sort())
