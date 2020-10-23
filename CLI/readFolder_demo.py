import argparse
import json

def Main():
  parser = argparse.ArgumentParser()
  parser.add_argument("filepath", help = "path to folder downloaded from facebook")
  args = parser.parse_args()

  myFB = Facebook(args.filepath)
  choose = input('Please choose a visualization:\n1. What are my top 10 most used words? \n2. Who have I pokde most? \n3.Who are the friends I interact with the most? \n4. What facebook knows about my off-facebook activity? \n5. What facebook knows about my installed aoos?\nYour choice: ')
  
  if int(choose):
    user_operation(myFB, int(choose))
  else:
    print('invalid input: enter a number')

def user_operation(fb, choose):
    """Show something based on users' choice.

    Args:
      A Facebook instance, the number user entered.

    Returns:
      No return.
    """

    if choose == 1:
      all_Comments = fb.comments()

    elif choose == 2:
      print('poked most')

    elif choose == 3:
      print('friends')

    elif choose == 4:
      offFB_activites = fb.offFB_activities()
      for activity in offFB_activites:
        if activity['name']:
          print(activity['name'])

    elif choose == 5:
      print('installed apps')

    else:
        print('???')

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
            return []

    def apps(self):
        path = str(self.folder + "/apps_and_websites/apps_and_websites.json")
        try:
            with open(path) as f:
              d = json.load(f)
              return d["installed_apps"]
        except:
            print("read apps' json fail")
            return[]

    def offFB_activities(self):
        path = str(self.folder + "/ads_and_businesses/your_off-facebook_activity.json")
        try:
            with open(path) as f:
              d = json.load(f)
              return d["off_facebook_activity"]
        except:
            print("read offFB' json fail")
            return []

if __name__ == "__main__":
    Main()
