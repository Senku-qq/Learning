import csv
# file = open(file='C:/Users/manyt/Documents/text_documents/konspekt.txt', mode="r+", encoding='utf-8')
# file = open(file='zadania/kartinka.jpg', mode="rb")
# print(file.name)
# print(file.read())
# file.close  

# with open(file='text.txt', mode='r', encoding='UTF-8') as file:
#         # file.write("Процерка цикла\n")
  
#     file_ = file.seek(10)
#     file_ = file.read()
#     print(file_)
# print("Информация сохранена ")
# users = [
#     ["Tom", 28],
#     ["Alice", 23],
#     ["Bob", 34]
# ]
File_name = 'users2.csv'
# # with open(File_name, "w", newline="") as file:
# #     writer = csv.writer(file)
# #     writer.writerows(users)
# # with open(File_name, "a", newline="") as file:
# #     user = ['Fill', 34]
# #     writer = csv.writer(file)
# #     writer.writerow(user)
# with open(File_name,"r", newline="") as file:
#     reader = csv.reader(file)
#     for i in reader:
#         print(i[0], " - ", i[1])

users = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34}
]

with open(File_name, "w", newline="") as file: 
    columns = ['name', 'age']
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()

    writer.writerows(users)
    user = {"name" : "Sam", "age": 41}
    writer.writerow(user)
with open(File_name,"r", newline="") as file:
    reader = csv.DictReader(file)
    for i in reader:
        print(i['name'], " - ", i['age'])