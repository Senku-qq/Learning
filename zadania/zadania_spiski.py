# name = ["misha","maks,","artem"]
# name.extend(["gurgen","chmo"])
# name.pop(-1)
# print(name)
#  mat = [
#      [10, 20, 30],
#      [40, 50, 60],
#      [70, 80, 90]
#  ]
# print(mat)

# for i in mat:
#     print(i)
# for i in range(len(mat)):
#     for j in range(len(mat)):
#         print(mat[i][j])
# mat = [
#      [10, 20, 30],
#      [40, 50, 60],
#      [70, 80, 90]
#  ]
# for i in range(len(mat)):
#     # for j in mat:
#     print(end="\n")
#     for j in range(len(mat)):
#         print(mat[i][j],end = " ")
# num =  [10, 20, 10, 20, 30, 40, 30, 50]
# numb = []
# for i in num:
#     if i in numb:
#         continue    
#     numb.append(i)
# print(numb)
# num = []
# def square(number): return number *number
# def cubes(number): return number **3
# for i in range(1,11):
#     num.append(i)
# print(f"Начальный список\n{num}")

# result = map(square,num)
# resultc = map(cubes,num)
# print("squares")
# for i in result: print(i, end = " ")

# print("\ncubes")

# for i in resultc: print(i, end = " ")
# num = [10, 20, 30, 40, 50]
# num2 = num[::-1]
# print(num2)
# num = [11, 22, 33, 44, 55]
# print(f"Начальный список{num}")
# for i in num: 
#     if i % 2 == 0: num.remove(i)
# print(f"Список с нечетными числами{num}")
# num = [1, 2, 3, 4]
 #num2 = [5, 6, 7, 8]
 #num3 = []
# print(f"Первый список: {num}")
# print(f"Второй список: {num2}")
# # for i in range(len(num)):
# #     if i == 0:
# #         for j in range(len(num2)):
# #             if j in num2 == 0:
# #                 num3.append(num[i]+num2[j])
# #     if i == 1:
# #         for j in range(len(num2)):
# #             if j in num2 == 1:
# #                 num3.append(num[i]+num2[j])
# #     if i == 2:
# #         for j in range(len(num2)):
# #             if j in num2 == 2:
# #                 num3.append(num[i]+num2[j])
# #     if i == 3:
# #         for j in range(len(num2)):
# #             if j in num2 == 3:
# #                 num3.append(num[i]+num2[j])
#num3.append(min(num) + min(num2)) ; num.remove(min(num)) ; num2.remove(min(num2))
 #num3.append(min(num) + min(num2)) ; num.remove(min(num)) ; num2.remove(min(num2))
# num3.append(min(num) + min(num2)) ; num.remove(min(num)) ; num2.remove(min(num2))
# num3.append(min(num) + min(num2)) ; num.remove(min(num)) ; num2.remove(min(num2))

# print(f"Результат сложения :{num3}")

# def summm(num,num2):
#      result = []
#      for a, b in zip(num,num2):
#          result.append(a * b)
#      return result
#     num = [1, 2, 3, 4]
#     num2 = [5, 6, 7, 8]
#     num3 = summm(num,num2)
#     print(f"Первый список: {num}")
#     print(f"Второй список: {num2 }")
#     print(f"Результат сложения: {num3}")
#     all_result = 0
#     for i in num3:
#         all_result += i
    # print(all_result)
# list1 = [10, 20, 30, 40, 50]
# list2 = [20, 25, 30, 35, 40]
# new_list = set(list1)
# new_list2 = set(list2)
# new_list3 = new_list.difference(new_list2)
# print(new_list3)
#
# students = {"Tom", "Bob", "Sam"}
# employees = {"Tom", "Bob", "Alex", "Mike"}
# people = students.union(employees)
# print(f"Все люди в обеих группах {people}")
# workers = employees.intersection(students)
# print(workers)
# studying = students.difference(employees)
# print(studying)
# only_one_thing = students.symmetric_difference(employees)
# print(only_one_thing)
for i in range(5):
    print('i')