import json

answers = []

quenstions = ["What's your name?", "What is your favorite food?", "what's your favorite color?", "What is your favorite band?", "What's your favorite tv show?","What's your favorite animal?", "Do you  like spicy food?", "Where do you live?","How old are you?"]

for i in range(5):
    answer = {}
    for q in quenstions:
        answer[q] = input(q)
    print(answer)
    answers.append(answer)
    print(answers)



#json.dumps(a)
f = open("answers2.json", "w") #f if file object
f.write(json.dumps(answers))
f.close()

# sum_ages = 0
# lst_ages = []
# for i in x:
#     if tempt.isnumeric():
#         age = int(temp)
#         sum_ages += lst_ages
#         lst_ages.append(age)
# avg = sum_ages / len(x)
# print(avg)
# print(lst_ages)
#
# favorite_band = 0
# lst_band = []
# for b in y:
#     if tempt.isalpha():
#         band =
