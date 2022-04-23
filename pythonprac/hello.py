# print('hello sparta!!')
#
# a = 2
# b = 3
# print(a + b)
#
# a = '백'
# b = '종석'
# print(a + b)
#
# a_list = ['사과', '배', '감']
# print(a_list[0])
#
#
# def is_adult (age):
#     if age > 20:
#         print("성인입니다")
#     else:
#         print("성인입니다")
#
#
# is_adult(21)
#
# fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']
#
# count = 0
# for aaa in fruits:
#     if aaa == "사과":
#         count += 1
#
# print(count)
#
# people = [{'name': 'bob', 'age': 20},
#           {'name': 'carry', 'age': 38},
#           {'name': 'john', 'age': 7},
#           {'name': 'smith', 'age': 17},
#           {'name': 'ben', 'age': 27}]
#
# for person in people:
#     if person['age'] > 20:
#         print(person['name'])

# import requests  # requests 라이브러리 설치 필요
#
# r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
# rjson = r.json()
#
# rows = rjson['RealtimeCityAir']['row']
#
# for row in rows:
#     gu_name = row['MSRSTE_NM']
#     gu_mise = row['IDEX_MVL']
#     # print(gu_name, gu_mise)
#     if gu_mise < 60:
#         print(gu_name)

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
# print(soup)
# #old_content > table > tbody > tr:nth-child(3) > td.title > div > a
# #old_content > table > tbody > tr:nth-child(4) > td.title > div > a
# #old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
# #old_content > table > tbody > tr:nth-child(2) > td.point

movies = soup.select('#old_content > table > tbody > tr')
# print(movies)

for movie in movies:
    rank = movie.select_one('td:nth-child(1) > img')
    # print(rank['alt'])
    title = movie.select_one('td.title > div > a')
    # print(title.text)
    star = movie.select_one('td.point')
    # print(star.text)
    if title is not None:
        print(rank['alt'], title.text, star.text)
