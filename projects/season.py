def season(s):
    if s > 0 and s < 3 and s == 12: return "Your season time is winter"
    if s > 2 and s < 6: return "Your season time is spring"
    if s > 5 and s < 9: return "Your season time is summer"
    if s > 8 and s < 12: return "Your season time is autumn"

print(season(int(input("введите ваш месяц:"))))
    