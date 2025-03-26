
import random
import time

class CircularQueue():
    def __init__(self,size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
    
    def is_empty(self): #check if empty
        return self.front == -1
    
    def is_full(self): #check  if full
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item): #add item to the queue
        if(self.is_full()):
            return "Queue is full!"
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
    
    def dequeue(self): #remove item from the queue
        if self.is_empty():
            return "Queue is empty!"
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return item
        
    def peek(self): #look at next item in queue
        if self.is_empty():
            print("Queue is empty")
        return f"{self.queue[self.__front]}"

    def sizeo(self): #sizeo, the size function that returns size and also does nopt conflict with CircularQueue().size
        if self.is_empty():
            return 0
        if self.rear >= self.front:
            return self.rear - self.front + 1
        return self.size - (self.front - self.rear - 1)

class Customer(): #customer class
    def __init__(self, customer_id, arrival_time, items):
        self.customer_id = customer_id
        self.arrival_time = arrival_time
        self.items = items
    def __str__(self): #string customer
        return f"Customer: {self.customer_id}, Arrived at: {self.arrival_time}, Number of Items: {self.items}"
    
def simulate_checkout(simulation_time=20):
    checkout = CircularQueue(10)

    curr_time = 0
    curr_customer = None
    processing_time = 0
    total_wait_time = 0
    processed_customers = 0
    max_queue_length = 0
    cust_id = 0

    print("\n\nSimulation begining")

    while curr_time < simulation_time:
        if random.random() < 0.45: #random 45% chance of customer
            customer = Customer(cust_id, curr_time, random.randint(1,20))
            cust_id += 1
            checkout.enqueue(customer)
            print(f"New customer arrived: {customer}") #customer created and printed

        max_queue_length = max(max_queue_length, checkout.sizeo()) #keeps track of max queue length
        
        if curr_customer is None and not checkout.is_empty():
            curr_customer = checkout.dequeue()
            processing_time = curr_customer.items #sets how long it takes to process items
            print(f"Customer {curr_customer.customer_id} starts checkout.") #if checkout is empty and there is no current customer, start checkout of 

        if curr_customer is not None:
            processing_time -= 1 #changes processing time eveery increment
            if processing_time == 0:
                processed_customers += 1 #incremenets # of procesed customers
                total_wait_time += (curr_time - curr_customer.arrival_time)
                print(f"Customer {curr_customer.customer_id} finished checkout.") #finishes checkout process
                curr_customer = None 
                
        curr_time += 1
        time.sleep(0.5)

    if processed_customers > 0: #incase no customers are processed
        average_wait_time = total_wait_time / processed_customers
    else:
        average_wait_time = 0
        
    print("\nSimulation complete!") #print results
    print(f"Total customers processed: {processed_customers}")
    print(f"Average waiting time: {average_wait_time:.2f}")
    print(f"Maximum queue length: {max_queue_length}")

simulate_checkout()