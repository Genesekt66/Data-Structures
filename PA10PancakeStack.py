import random

class PancakeStack(): #pancake class
    def __init__(self):
        self.stack = [] #empty list
    
    def is_empty(self):
        if (len(self.stack) < 1): #checks if empty
            return True
        else:
            return False
    def push(self, pancake): #adds new pancake to top of stack
        self.stack.insert(0, pancake)

    def pop(self):
        if self.is_empty(): #catches if empty
            return "Caught exception: This stack is empty!"
            
        else:  #removes and returns pop
            popped = self.stack[0]
            self.stack.remove(popped)
            return popped

    def peek(self): #returns top of stack without removing
        if (self.is_empty()): 
            return "IndexError detected. This stack is empty"
        else:
            return self.stack[0]
    
    def size(self): #gets size
        return len(self.stack)
    
    def _visualize_stack(self):#little helper to print the stack
        print("Current stack:", self.stack)


class demonstrate_pancake_stack():  #simulates creating a stack, pushing 4 pancakes onto the stack, then removing the pancakes from the stack
    simulation = PancakeStack()
    pushes = 0

    print("\n\nInitial stack: ", simulation.stack)
    
    print("\n\nPushing pancakes onto the stack:")
    
    i = 0
    while i < 4: #pushes 4 pancakes
        simulation.push(random.randint(1,10))
        pushes += 1
        print("\n\nPush: Added a pancake with size", simulation.peek())
        simulation._visualize_stack()
        print("Peek: Top pancake has size", simulation.peek())
        print("The current size of the pancake stack is", simulation.size())
        i+=1

    print("\n\nPopping pancakes from stack:")
    while i < 8: #pops 4 pancakes
        print("Removed a pancake with size",simulation.pop())
        simulation._visualize_stack()
        i+=1

    print("\n\nTrying to pop from empty stack:")
    print(simulation.pop()) #tries to pop another pancake, exception thrown

    print(f"\n\nTotal number of pushes is {pushes}")
    print(f"Final size {simulation.size()}")

demonstrate = demonstrate_pancake_stack()