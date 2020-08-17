import time
import math

def time_it(fn, *args, repetitions= 1, **kwargs):
    if repetitions <= 0:
        raise ValueError("Number of Repetitions should be greater than zero")
    start_time = time.time()
    for i in range(repetitions):
        fn(*args,**kwargs)
    end_time = time.time()
    avg_runtime = (end_time - start_time) / (repetitions)
    print(f'The average run time taken for {repetitions} repetitions are {avg_runtime}')
    return avg_runtime

def squared_power_list(pow_of=1, *args, start=0, end=5):
    l = []
    if pow_of <= 0:
        raise ValueError('Negative values & Zero are not allowed!')
    elif start >= end:
        raise ValueError('End Value should be greater than start value')
    elif start < 0 or end < 0:
        raise ValueError('Negative start or end is not acceptable')
    else:
        for i in range(start, end+1):
            power_of = pow_of ** i
            l.append(power_of)
    print(l)

    return l

def polygon_area(side_length, sides=3):
    if side_length <= 0:
        raise ValueError("Input Valid length of polygon")
    elif sides >= 3 and sides <= 6:
        area = sides * (side_length ** 2) * (1 / (math.tan(math.pi / sides))) / 4
        print(f'Area of polygon is {area}')
    else:
        raise ValueError("Cannot find an area of specified side - can compute area for a minimum of Trigon to maximum Hexagon")

    return area

def temp_converter(temp, temp_given_in='f'):
    temp_given_in = str(temp_given_in)
    if temp_given_in.lower() not in ('c', 'f'):
        raise ValueError("please provide the unit as c or f")
    if temp_given_in.lower() == 'f' and temp > 0:
        temp_cel = (temp - 32) * 5/9
        print(f'{temp} in Farenheit is {temp_cel} in Celcius scale')
        return temp_cel
    elif temp_given_in.lower() == 'c' and temp > 0:
        temp_far = (temp * 1.8) + 32
        print(f'{temp} in Celcius is {temp_far} in Farenheit scale')
        return temp_far
    else:
        raise ValueError("Temperature should be either in C°:'c' or F°: 'f' and it cannot be zero or negative")

def speed_converter(speed, dist, time):
    if dist not in ('km', 'm', 'ft', 'yrd'):
        raise ValueError("Distance units can be only in - km, m, ft, yrd")
    if time not in ('ms', 's', 'min', 'hr', 'day'):
        raise ValueError("Time units can be only in - ms, s, min, hr, day")
    if speed<0:
        raise ValueError("Speed cannot be negative")
    if dist == 'km':
        if time == 'ms':
            result = speed/3600000
        if time == 's':
            result = speed/3600
        if time == 'min':
            result = speed/60
        if time == 'hr':
            result = speed
        if time == 'day':
            result = speed*24

    if dist == 'm':
        if time == 'ms':
            result = speed/3600
        if time == 's':
            result = speed/3.6
        if time == 'min':
            result = speed/.06
        if time == 'hr':
            result = speed*1000
        if time == 'day':
            result = speed*24000

    if dist == 'ft':
        if time == 'ms':
            result = speed*3280.84/3600000
        if time == 's':
            result = speed*3280.84/3600
        if time == 'min':
            result = speed*3280.84/60
        if time == 'hr':
            result = speed*3280.84
        if time == 'day':
            result = speed*3280.84*24

    if dist == 'yrd':
        if time == 'ms':
            result = speed*1093.6132/3600000
        if time == 's':
            result = speed*1093.6132/3600
        if time == 'min':
            result = speed*1093.6132/60
        if time == 'hr':
            result = speed*1093.6132
        if time == 'day':
            result = speed*1093.6132*24

    print(result)
    return result