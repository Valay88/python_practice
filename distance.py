'''
    distance = speed * time
'''
speed = int(input('Enter your vehicle speed:'))
time = float(input('Enter time  duraction to reach:'))
def distance(speed,time):
    distance = speed * time
    print(f'your vehicle speed is{speed} and time to reach is{time} you have cutted distance is :{distance} km')

## function calling
distance(speed,time)