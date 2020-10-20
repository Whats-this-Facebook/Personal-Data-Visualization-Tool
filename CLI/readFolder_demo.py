import argparse
import json

def Main():
  parser = argparse.ArgumentParser()
  parser.add_argument("filepath", help = "path to folder downloaded from facebook")
  args = parser.parse_args()

  myFB = Facebook(args.filepath)
  choose = input('Please choose a visualization:\n1. What are my top 10 most used words? \n2. Who have I pokde most? \n3.Who are the friends I interact with the most? \n4. What facebook knows about my off-facebook activity? \n5. What facebook knows about my installed aoos?\nYour choice: ')
  
  try:
    user_choose = int(choose)
  except ValueError:
    print("Invalid input")

  if user_choose == 1:
    all_Comments = myFB.comments()
  elif user_choose == 2:
    print('poked most')
  elif user_choose == 3:
    print('friends')
  elif user_choose == 4:
    print('off-facebook')
  elif user_choose == 5:
    print('installed apps')
  else:
    print('Invalid option.')


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
