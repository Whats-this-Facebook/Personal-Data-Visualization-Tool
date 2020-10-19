import argparse
import json

def Main():
        path = input('Enter your folder path:')
        myFB = Facebook(path)
        all_Comments = myFB.comments()
        print(all_Comments)
        print(comments_str(all_Comments))

def comments_str(comments):
    """Pick the content from comments dictionary and combine all of them into one string.

    Args:
      An array of comments. All the info are in dictioanry format.

    Returns:
      A string.
    """
    comments_str = ""
    for aComments in comments:
        if "data" in aComments: # Ensure comment has data attached
            datas = aComments["data"]
            for data in datas:
                str = data["comment"]["comment"]
                comments_str = comments_str + " " + str
    return comments_str

class Facebook:
    """A Facebook instance provides data including comments, apps.

    Args:
      The path of the folder user downloaded from Facebook.

    Returns:
      All the returns are arrays of dictionaries.
    """
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


if __name__ == "__main__":
    Main()
