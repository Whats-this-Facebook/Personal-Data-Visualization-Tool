import argparse
import json

class Facebook:
    def __init__(self, folder):
        self.folder = folder
    
    def comments(self):
        path = str(self.folder + "/comments/comments.json")
        try:
            with open(path) as f:
              d = json.load(f)
              return d["comments"]
        except:
            print("read comments' json fail") 
    
    def apps(self):
        path = str(self.folder + "/apps_and_websites/apps_and_websites.json")
        try:
            with open(path) as f:
              d = json.load(f)
              return d["installed_apps"]
        except:
            print("read apps' json fail") 


def Main():
        path = input('Enter your folder path:')
        myFB = Facebook(path)
        for app in myFB.apps():
            print(app['name'])



if __name__ == "__main__":
    Main()