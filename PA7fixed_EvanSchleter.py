class OrderedArray:
    def __init__(self):
        self.__a = []
        self.__nItems = 0

    def insertMultiple(self, size):
        for i in range(size):
            item = int(input(f"Enter item to insert {i+1}: "))
            self.insert(item)
        
    def insert(self, item):
        pos = self.Binary_Search_Insertion(item)
        
        if self.__nItems == 0 or pos == self.__nItems:
            self.__a.append(item)
        else:
            self.__a.append(None)
            for i in range(self.__nItems, pos, -1):
                self.__a[i] = self.__a[i-1]
            self.__a[pos] = item
        self.__nItems += 1
    
    def Binary_Search_Insertion(self, item):
        left = 0
        right = self.__nItems - 1

        while left <= right:
            mid = (left + right) // 2
            if self.__a[mid] == item:
                return mid
            elif self.__a[mid] < item:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def Binary_Search_Value(self, item):
        left = 0
        right = self.__nItems - 1

        while left <= right:
            mid = (left + right) // 2
            if self.__a[mid] == item:
                return mid
            elif self.__a[mid] < item:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def Binary_Search_By_Index(self, index):
        if 0 <= index < self.__nItems:
            return self.__a[index]
        return "Index out of bounds"

    def delete(self, item): #item, not index
        index = self.Binary_Search_Value(item)
        if index != -1:
            self.__a.pop(index)
            self.__nItems -= 1

    def printArray(self):
        for item in self.__a:
            print(item)

class UnorderedArray:
    def __init__(self):
        self.__a = []
        self.__nItems = 0
        
    def insert(self, size):
        for i in range(size):
            item = input(f"Enter item to insert: {i+1}: ")
            self.__a.append(item)
            self.__nItems += 1

    def insertHC(self, size):
        a = [10, 22, 33]
        for i in range(size):
            item = a[i]
            self.__a.append(item)
            self.__nItems += 1

    def getValue(self, index): #returns value from index
        if index < 0 or index >= self.__nItems:
            print("Index out of bounds")
        else:
            print(self.__a[index])
            return self.__a[index]

    def LinearSearch(self, item):
        for i in range(self.__nItems):
            if self.__a[i] == item:
                return i
        return -1

    def delete1(self, item):
        i = 0
        while i < self.__nItems:
            if self.__a[i] == item:
                self.__a.pop(i)
                self.__nItems -= 1
            else:
                i += 1

    def delete2(self, item):
        index = self.LinearSearch(item)
        if index != -1:
            self.__a[index] = self.__a[self.__nItems - 1]
            self.__a[self.__nItems - 1] = None
            self.__nItems -= 1
            return True
        return False

    def printArray(self):
        for item in self.__a:
            print(item)
    
def test_ordered_array():
    arr = OrderedArray()
    while True:
        print("\nOrdered Array Menu:")
        print("1. Insert Multiple Items")
        print("2. Insert Single Item")
        print("3. Search by Value")
        print("4. Search by Index")
        print("5. Delete an Item")
        print("6. Print Array")
        print("7. Return to Main Menu")
        op = input("Enter your choice: ")
        
        if op == "1":
            size = int(input("Enter number of items to insert: "))
            arr.insertMultiple(size)
        elif op == "2":
            item = int(input("Enter item to insert: "))
            arr.insert(item)
        elif op == "3":
            value = int(input("Enter value to search: "))
            result = arr.Binary_Search_Value(value)
            print(f"Search result: {result}")
        elif op == "4":
            index = int(input("Enter index to search: "))
            result = arr.Binary_Search_By_Index(index)
            print(f"Search result: {result}")
        elif op == "5":
            item = int(input("Enter item to delete: "))
            arr.delete(item)
        elif op == "6":
            print("Ordered Array Contents:")
            arr.printArray()
        elif op == "7":
            break
        else:
            print("Invalid option. Try again.")


def test_unordered_array():
    arr = UnorderedArray()
    while True:
        print("\nUnordered Array Menu:")
        print("1. Insert Items Manually")
        print("2. Insert Hard-Coded Items (HC)")
        print("3. Linear Search")
        print("4. Get Value by Index")
        print("5. Delete an Item (delete1)")
        print("6. Print Array")
        print("7. Return to Main Menu")
        op = input("Enter your choice: ")
        
        if op == "1":
            size = int(input("Enter number of items to insert: "))
            arr.insert(size)
        elif op == "2":
            size = int(input("Enter number of hard-coded items to insert: "))
            arr.insertHC(size)
        elif op == "3":
            item = input("Enter item to search for: ")
            result = arr.LinearSearch(item)
            print(f"Search result: {result}")
        elif op == "4":
            index = int(input("Enter index: "))
            result = arr.getValue(index)
            print(f"Value at index {index}: {result}")
        elif op == "5":
            item = int(input("Enter item to delete (using delete1): "))
            arr.delete1(item)
        elif op == "6":
            print("Unordered Array Contents:")
            arr.printArray()
        elif op == "7":
            break
        else:
            print("Invalid option. Try again.")


def main():
    while True:
        print("\nMain Menu:")
        print("1. Test Ordered Array")
        print("2. Test Unordered Array")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            test_ordered_array()
        elif choice == "2":
            test_unordered_array()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()