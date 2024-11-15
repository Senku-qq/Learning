dogy_name = "Artem"
dogy_race = "bulldog"
def create_pet(dogy_name):
    print(f"Имя и расса вашего питомца:{dogy_name}")
    question = input("Вы хотите поменять свое имя? Yes/No: ")
    if "Yes" in question:
        print(smena())
def smena():
    global dogy_name
    dogy_name = (input("Введите новое имя питомца:"))

create_pet(dogy_name)