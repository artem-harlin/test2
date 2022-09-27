years = int(input())
month = int(input())
years_now = int(input())
month_now = int(input())
s = years_now - years
month_age = month + month_now
if month_age >= 12:
    s -= 1
    print(s)



