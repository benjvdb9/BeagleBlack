import json
from isodate import duration_isoformat
from datetime import timedelta
from pymongo import MongoClient

class SaveData():
    def __init__(self, info, stats, equiped):
        self.name = info[0]
        self.type = 'save'
        self.player_level = info[1];
        self.insight = info[2];
        self.location = info[3];
        self.playtime = info[4];
        self.stats = SaveData.stats_init(stats)
        self.equiped_items = SaveData.equiped_init(equiped)

    def stats_init(stats):
        stats_list = {'VIT': stats[0], 'END': stats[1], 'STR': stats[2],
                      'SKL': stats[3], 'BLT': stats[4], 'ARC': stats[5]}

        return stats_list

    def equiped_init(equiped):
        default = {'right1': equiped[0], 'right2': equiped[1], 'left1': equiped[2],
                   'left2': equiped[3], 'head': equiped[4], 'torso': equiped[5],
                   'arms': equiped[6], 'legs': equiped[7]}

        return default

    def to_dict(self):
        dictio = {'name': self.name, 'type':self.type, 'player level': self.player_level,
                  'insight': self.insight, 'location': self.location,
                  'playtime': duration_isoformat(self.playtime), 'stats': self.stats,
                  'equipment': self.equiped_items}
        return dictio

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

class ConfigFile():
    def __init__(self):
        self.type = 'config'
        self.luminosity = 5
        self.window_size = (800, 600)

    def to_dict(self):
        dictio = {'type': self.type, 'luminosity': self.luminosity, 'window_size': self.window_size}
        return dictio

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

class SaveDB():
    def __init__(self):
        self.savefiles = []
        
    def addSaveFile(self, *savedata):
        for save in savedata:
            self.savefiles.append(save.to_dict())

    def createJSON(self):
        return json.dumps(self.savefiles, indent=4)

    def exportToJSON(self):
        file = open('db.json', 'w')
        file.write(self.createJSON())
        file.close()

class MongoManager():
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['SaveFiles']
        self.posts = self.db.posts

    def addOnePost(self, post):
        result = self.posts.insert_one(post)
        print('Single post: {}\n\n'.format(result.inserted_id))

    def addManyPosts(self, posts):
        result = self.posts.insert_many(posts)
        print('Multiple posts: {}\n\n'.format(result.inserted_ids))

    def updateOnePost(self, typ, field, value):
        self.posts.update_one({'type': typ}, {'$set': {field : value}})

    def getSaves(self):
        posts = self.posts.find({'type': 'save'})
        return posts

    def getSpecificSave(self, player_name):
        posts = self.posts.find({'type': 'save', 'name': player_name})
        return posts

    def readDataBase(self):
        posts = self.posts.find()

        print('Elements in database:\n')
        for post in posts:
            print(post, '\n\n')

    def resetDataBase(self):
        self.db.posts.drop()
