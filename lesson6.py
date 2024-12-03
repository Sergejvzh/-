immutable_var = 1
immutable_var2 = ('bobr')
immutable_var3 = ([1,2,'a','b'])
print(immutable_var)
print(immutable_var2)
print(immutable_var3)
print(immutable_var3 [1]) # если взять индекс [1] кортежа, выдаст элемент "2"
immutable_var3[1] = 5 # если заменить элемент на число "5" выдаст ошибку
print(immutable_var3)

# mutable_list = [1, 2, 'a', 'b', 'Sergej']
# print(mutable_list)
# mutable_list [4] = 9 # если заменить [Sergej] кортежа на число 9, ошибки нет
# print(mutable_list)
