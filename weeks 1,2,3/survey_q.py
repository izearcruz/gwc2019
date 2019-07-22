import json
f = open("answers2.json", "r")
x = json.load(f)

sum_ages = 0
lst_ages = []
for i in x:
    temp = i["How old are you?"]
    if temp.isnumeric():
        age = int(temp)
        sum_ages += age
        lst_ages.append(age)
avg = sum_ages / len(x)
print(avg)
print(lst_ages)
