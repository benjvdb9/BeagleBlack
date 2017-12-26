from isodate import parse_duration
from CreateDB import MongoManager

class SaveManager():
    def __init__(self):
        self.manager = MongoManager()

    #Simple request
    def changeLuminosity(self, lum):
        self.manager.updateOnePost('config', 'luminosity', lum)

    #Medium request
    def getTotalPlaytime(self):
        saves = self.manager.getSaves()
        playtimes = parse_duration(saves[0]['playtime'])

        for save in saves[1:]:
            playtime = parse_duration(save['playtime'])
            playtimes += playtime

        print(playtimes)
        return playtimes

    #Hard request
    def getStatDiff(self, P1, P2):
        save1 = self.manager.getSpecificSave(P1)
        save2 = self.manager.getSpecificSave(P2)

        for stat1, stat2 in zip(save1, save2):
            stats1 = stat1['stats']
            stats2 = stat2['stats']

        stats_diff = self.dictDiff(stats1, stats2)

    #Sum function, was supposed to be used in getTotalPlaytime but scapped
    #due to not working well with non-ints, kept as reference
    def genericSum(self):
        pipe = [{'$group': {'_id': 'None', 'total': {'$sum': '$insight'}}}]
        result = self.manager.posts.aggregate(pipeline=pipe)

        for elm in result:
            print(elm)
        return result

    def dictDiff(self, dic1, dic2):
        dic_diff = {}
        attributes = ['VIT', 'END', 'STR', 'SKL', 'BLT', 'ARC']

        for attribute in attributes:
            dic_diff[attribute] = dic1[attribute] - dic2[attribute]

        print(dic_diff)
        return dic_diff
    
test = SaveManager()

#Use ReadDB.py to analyse database
#test.changeLuminosity(9)

#test.getTotalPlaytime()

#test.getStatDiff('Trafalgar', 'Metasticia')

#test.genericSum()
