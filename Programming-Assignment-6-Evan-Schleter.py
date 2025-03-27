class Array():
    def __init__(self):
        self.__a=[]
        self.__nItems=0

    def __str__(self):
        return str(self.__a)

    def insert(self,item):
        self.__a.append(item)
        self.__nItems += 1

    def get(self,n):
        if (0 <= n < self.__nItems):
            return self.__a[n]
        return None 
    
    def find(self,n):
        for i in range(self.__nItems):
            if (self.__a[i] == n):
                return i
        return -1
    
    def delete(self,n):
        item = self.find(n)
        if item >= 0:
            self.__a.pop(item)
            self.__nItems -= 1

arr = Array()

arr.insert(10)
arr.insert(20)
arr.insert(30)
print(arr)

print(arr.get(1))
print(arr.find(30))
print(arr.find(50))

arr.delete(20)
print(arr)