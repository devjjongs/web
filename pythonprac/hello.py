print('hello sparta!!')

a = 2
b = 3
print(a + b)

a = '백'
b = '종석'
print(a + b)

a_list = ['사과', '배', '감']
print(a_list[0])


def is_adult (age):
    if age > 20:
        print("성인입니다")
    else:
        print("성인입니다")


is_adult(21)

fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']

count = 0
for aaa in fruits:
    if aaa == "사과":
        count += 1

print(count)

people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:
    if person['age'] > 20:
        print(person['name'])
