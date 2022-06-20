input_list = []
matrix = []
a = True
while a:
    input_list = [str(i) for i in input().split()]
    if input_list != ['end']:
        matrix.append(input_list)
    else:
        a = False
        for i in matrix:
            print(*i)  #Ввод матрицы до преобразования в числовой формат со стопом по end
