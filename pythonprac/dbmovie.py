from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.zuy17.mongodb.net/Cluster0?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db = client.dbsparta

# Q1. 영화제목 '가버나움' 평점 가져오기
movie = db.movies.find_one({'title': '가버나움'})
# print(movie['star'])

# Q2. '가버나움'의 평점과 같은 평점의 영화 제목 가져오기
movie = db.movies.find_one({'title': '가버나움'})
star = movie['star']

all_movies = list(db.movies.find({'star': star}, {'_id': False}))

for same_star in all_movies:
    print(same_star['title'])

# Q3. '가버나움' 영화의 평점을 0으로 만들기
db.movies.update_one({'title': '가버나움'}, {'$set': {'star': '0'}})
