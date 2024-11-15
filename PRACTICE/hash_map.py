voted = {}

def proverka_na_golos(name):
    if voted.get(name):
        print("kick them")
    else:
        voted[name] = True
        print("let them vote")
proverka_na_golos("tom")
proverka_na_golos("tom")
proverka_na_golos("vika")