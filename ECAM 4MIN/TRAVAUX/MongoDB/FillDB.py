from CreateDB import *

container = SaveDB()
traf = SaveData(('Trafalgar', 137, 99, "Hunter's Dream", timedelta(hours= 45, minutes= 44, seconds = 27)),
                [51, 45, 14, 50, 20, 7],
                ['Chikage', 'Blade of Marcy', 'Evelyn', "Hunter's Torch", 'Bone Ash Mask',
                 'Bone Ash Armor', 'Bone Ash Gauntlets', 'Bone Ash Leggings'])

meta = SaveData(('Metasticia', 122, 65, "Hunter's Dream", timedelta(hours= 17, minutes= 00, seconds = 24)),
                [50, 39, 11, 35, 30, 7],
                ['Reiterpallasch', 'Burial Blade', 'Evelyn', "Hunter's Torch", "Henryk's Hunter Cap",
                 "Henryk's Hunter Garb", "Henryk's Hunter Gloves", "Henryk's Hunter Trousers"])

chrl = SaveData(('Charlie Sun', 146, 94, "Hunter's Dream", timedelta(hours= 39, minutes= 35, seconds = 27)),
                [50, 30, 20, 50, 16, 30],
                ['Burial Blade', 'Rakuyo', "Hunter Pistol", "Repeating Pistol", 'Old Hunter Cap',
                 "Gehrman's Hunter Garb", "Knight's Gloves", "Gascoigne's Trousers"])

conf = ConfigFile()
container.addSaveFile(traf, meta, chrl, conf)
container.exportToJSON()

MM = MongoManager()
MM.resetDataBase()
MM.addManyPosts(container.savefiles)
MM.readDataBase()
