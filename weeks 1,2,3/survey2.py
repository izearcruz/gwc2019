import json
json_data = '{"a": 1, "b"": 2, "c": 3, "d": 4, "e": 5}'

[
  {
    "What's your name?": 'Yiyang',
    'What is your favorite food?': 'pizza',
    "what's your favorite color?": 'blue',
    'What is your favorite band?': 'BTS',
    "What's your favorite tv show?": 'Criminal Minds',
    "What's your favorite animal?": 'whale',
    'Do you  like spicy food?': 'kind of',
    'What do you think of Izear?': 'nice!'
  },
  {
    "What's your name?": 'izear',
    'What is your favorite food?': 'pizza',
    "what's your favorite color?": 'red',
    'What is your favorite band?': 'bts',
    "What's your favorite tv show?": 'the office',
    "What's your favorite animal?": 'cat',
    'Do you  like spicy food?': 'yes',
    'What do you think of Izear?': 'oof!!'
  },
  {
    "What's your name?": 'fatou',
    'What is your favorite food?': 'grilled cheese',
    "what's your favorite color?": 'blue',
    'What is your favorite band?': '5sos',
    "What's your favorite tv show?": 'On My Block',
    "What's your favorite animal?": 'Monkey',
    'Do you  like spicy food?': 'yeah',
    'What do you think of Izear?': 'She dresses nice'
  },
  {
    "What's your name?": 'Amelia',
    'What is your favorite food?': 'chocolate lava cake',
    "what's your favorite color?": 'black',
    'What is your favorite band?': 'Bastille',
    "What's your favorite tv show?": 'Jeopardy!',
    "What's your favorite animal?": 'humans???',
    'Do you  like spicy food?': 'sometimes. occasionally.',
    'What do you think of Izear?': 'very good'
  }
]
print(json.loads(json_data)
loaded_json = json.loads(json_data)
for x in loaded_json:
	print("%s: %d" % (x, loaded_json[x]))

with open('distros.json', 'r') as f:
    distros_dict = json.load(f)

for distro in distros_dict:
    print(distro['Name'])
