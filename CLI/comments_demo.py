import json
import os

# get all .json from folders under main folder
def getAllJsonFromMainFolder(mainPath):
        subFolders = mainFolders(mainPath)
        for subFolder in subFolders:
            path = mainPath + "/" + subFolder
            insideFolders(path)

# get all folders' name under main folder
def mainFolders(path):
    try:
        subFolders = [pos_json for pos_json in os.listdir(path)]
        return subFolders
    except:
        print("get subFolders' name fail")

# .json files
def insideFolders(path):
    try:
        jsonFiles = [pos_json for pos_json in os.listdir(path) if pos_json.endswith('.json')]
        return jsonFiles
    except:
        print("get all json files fail")

def readJSON(path):
    try:
        with open(path) as f:
            d = json.load(f)
            print(d)
    except:
        print("read json fail")

def getAllComments(path):
    try:
        if '/comments/comments.json' not in path:
            path = path + '/comments/comments.json'

        comments_str = ''
        with open(path) as f:
            d = json.load(f)
            allComments = d["comments"]
            for aComments in allComments:
                datas = aComments["data"]
                for data in datas:
                    str = data["comment"]["comment"]
                    comments_str = comments_str + " " + str
        return comments_str            

    except:
            print('read comments fail: some data without comment....')

def Main():
        path = input('Enter your folder path:')
        comments_path = path + '/comments/comments.json'
        
        # allC is all comments combined in one string.
        allC = getAllComments(comments_path)
        print(allC)
        
if __name__ == "__main__":
    Main()