1
add = lambda a, b: a + b
print("Yig‘indi:", add(5, 3))


#2
square = lambda x: x * x
print("Kvadrat:", square(4))


#3
even_odd = lambda x: "Juft" if x % 2 == 0 else "Toq"
print("Natija:", even_odd(7))


#4
numbers = [1, 2, 3, 4, 5]
squared_list = list(map(lambda x: x**2, numbers))
print("Kvadratlar:", squared_list)


#5
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Juft sonlar:", even_numbers)


#5
max_num = lambda a, b: a if a > b else b
print("Eng katta:", max_num(10, 25))


#6
average = lambda a, b, c: (a + b + c) / 3
print("O‘rtacha:", average(5, 10, 15))
