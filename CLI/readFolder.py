import argparse
import json
import os

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
  
def messages_str(messages, name):
    """Pick the content from messages and combine all of them into one string.

    Args:
      An array of messages. All the info are in dictioanry format.

    Returns:
      A string.
    """
    message_str = ''
    for message in messages:
      for i in message['messages']:
        try:
          if i['sender_name'] == name and i['type'] == 'Generic':
            message_str += ' ' + i['content']
        except:
          continue
    
    return message_str

def posts_str(posts):
    """Pick the content from posts and combine all of them into one string.

    Args:
      An array of posts. All the info are in dictioanry format.

    Returns:
      A string.
    """
    posts_str = ''
    for p in posts:
        for post in p:
          try:
            posts_str += ' ' + post['data'][0]['post']
          except:
            continue
    
    return posts_str 


class Facebook:
    """A Facebook instance provides data including comments, apps.

    Args:
      The path of the folder user downloaded from Facebook.

    Returns:
      All the returns are arrays of dictionaries.
    """

    def __init__(self, folder):
        self.folder = folder

    def profile(self):
        path = os.path.join(self.folder, "profile_information", "profile_information.json")
        try:
            with open(path) as f:
              d = json.load(f)
              return d["profile"]
        except:
            print("read profile info json fail")
            return []

    def comments(self):
        path = os.path.join(self.folder, "comments", "comments.json")
        try:
            with open(path) as f:
              d = json.load(f)
              return d["comments"]
        except:
            print("read comments' json fail")
            return []

    def messages(self):
        path = os.path.join(self.folder, "messages", "inbox")
        messages = []
        try:
            folders = os.scandir(path)
            for f in folders:
              if os.path.isdir(os.path.join(path, f)):
                folder = os.scandir(os.path.join(path, f))
                for file in folder:
                  if os.path.isfile(os.path.join(path, file)):
                    messages.append(json.load(open(os.path.join(path, file))))
        except:
            print("read messages json fail")
        return messages

    def posts(self):
        path = os.path.join(self.folder, "posts")
        posts = []
        try:
            folders = os.scandir(path)
            for f in folders:
              if os.path.isfile(os.path.join(path, f)) and ('your_posts' in f.name):
                    posts.append(json.load(open(os.path.join(path, f))))
        except:
            print("read posts json fail")
        return posts

    def apps(self):
        path = os.path.join(self.folder, "apps_and_websites", "apps_and_websites.json")
        try:
            with open(path) as f:
              d = json.load(f)
              return d["installed_apps"]
        except:
            #print("read apps' json fail")
            return[]

    def offFB_activities(self):
        path = os.path.join(self.folder, "ads_and_businesses", "your_off-facebook_activity.json")
        try:
            with open(path) as f:
              d = json.load(f)
              return d["off_facebook_activity"]
        except:
            print("read offFB' json fail")
            return []

    def offFB_activities_list(self):
        activityList = []
        activity_dict = self.offFB_activities()
        for act in activity_dict:
                activityList.append(act['name'])

        return activityList

    def account_activity(self):
        path = os.path.join(self.folder, "security_and_login_information", "account_activity.json")
        try:
            with open(path) as f:
              d = json.load(f)
              return d["account_activity"]
        except:
            print("read account_activity' json fail")
            return []


if __name__ == "__main__":
    Main()
