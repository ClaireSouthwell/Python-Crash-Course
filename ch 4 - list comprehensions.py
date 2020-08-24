#SUMMING NUMBERS BETWEEN 1 AND 1 MILLION
#for loop 
total = 0
for number in range (1, 1000001):
    total += number
print(total)
#yields 500000500000

#list comprehension
total = [sum(range(1, 1000001))]
print(total)
#yields [500000500000]

#CUBES 1 TO 10
#for loop
cube_list = []
for number in range(1, 11):
    cube = number**3
    cube_list.append(cube)
print(cube_list)
#yields [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

#list comprehension
cube_list = [number**3 for number in range(1, 11)]
print(cube_list)
#yields [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

