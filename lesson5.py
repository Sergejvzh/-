# my_string = input(" Меня зовут: ")
# print(type("my_string"))
# print (len(my_string))
# print("my_string".upper())
# print("my_string".lower())
# print('привет, я Сергей'.replace(' ' , ''))
# print(my_string[0])
# print(my_string[-1])

immutable_var = 1
immutable_var2 = ('bobr')
immutable_var3 = (1,2,'a','b')
print(immutable_var)
print(immutable_var2)
print(immutable_var3)
print(immutable_var3 [1]) # если взять индекс [1] кортежа, выдаст элемент "2"
immutable_var3[1] = 5 # если заменить элемент на число "5" выдаст ошибку
print(immutable_var)

# mutable_list = [1, 2, 'a', 'b', 'Sergej']
# print(mutable_list)
# mutable_list [4] = 9 # если заменить [Sergej] кортежа на число 9, ошибки нет
# print(mutable_list)



