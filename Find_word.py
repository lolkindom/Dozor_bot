import requests
import re
def find_word(ask):
    a = 'https://anagram.poncy.ru/mask.html?inword='
    b = '&answer_type=4&nouns=true'

    c = requests.get(a + ask + b)
# print(s)
#     print(c.text)

    find = r'">(\w+)</a>'
    d = re.findall(find, c.text)
    return '\n'.join(d[:-1])
    # for each in d[:-1]:
    #     return each
# find_word(input())

