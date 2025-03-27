def CalcTime(speed, distance):
    return round(float(distance/speed*60),1)
def menu():
    print("Wecome to the pizza delivery time calculator!")
def inputspeed():
    return input("What is the average speed the delivery vehicle will be driving in miles per hour?")
def inputdistance():
    return input("How far away are we delivering to in miles?")

menu()
speed = float(inputspeed())
distance = float(inputdistance())
print(f'It will take {CalcTime(speed, distance)} minutes to deliver this pizza')