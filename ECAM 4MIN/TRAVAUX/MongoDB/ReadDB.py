from time import sleep
from pymongo import MongoClient

client = MongoClient()
db = client['SaveFiles']
posts = db.posts
bill_posts = posts.find()

print('Elements in posts:\n')
i = 1
for elem in bill_posts:
    print(elem, '\n\n')

print('My DB:', bill_posts)
print('\n\nCollection', db.test_collection)

while True:
    sleep(10)
