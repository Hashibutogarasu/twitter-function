#!/usr/bin/env python
# -*- coding: utf-8 -*-


###########################
#coding utf-8
#2021/06/06
#made by Columba_Karasu
#Dependent libraries:tweepy
###########################


def timeline(api,count=20,limits_output=False):
  try:
    for status in api.home_timeline(count=count):
    
      if (("RT" in status.text) == False):

        print("-"*42)

        if status.user.verified == True:
          print(status.user.name + " ✔︎" + " @" + status.user.screen_name)
        else:
        	print(status.user.name + " @" + status.user.screen_name)

        print(status.text.replace("https://t.co","\nhttps://t.co"))
        print(f"Favorites:{status.favorite_count} Retweet:{status.retweet_count}")
        if status.favorited == True:
          print("Favorited")
        elif status.favorited ==True and status.retweeted == True:
          print("Favorited Retweeted")
        elif status.favorited == False and status.retweeted == True:
          print("Retweeted")
        else:
          pass

        print(str(status.created_at)+ " " +status.source)
        print()
        print(f"Tweet id:{status.id}")
        print(f"User id:{status.user.id}")
        print(f"url:https://twitter.com/{status.user.screen_name}/status/{status.id}")
    if limits_output == True:
      limit_data = api.rate_limit_status()
      print("\nTimeline acquisition remaining:"+str(limit_data['resources']['statuses']['/statuses/home_timeline']['remaining']))

      print("\nUntil reset:"+(str(limit_data['resources']['statuses']['/statuses/home_timeline']['reset'])))  
    else:
      pass
    
  except:
    if limits_output == True:
      limit_data = api.rate_limit_status()
      print("The API call limit has been exceeded.\nPlease wait a while and try again.")
      print(limit_data['resources']['statuses']['/statuses/home_timeline']['remaining'])
    else:
      pass

def tweet(api,content,id="",fav=False,image_path=""):
	
  fav = False
  
  me = api.me()
  
  if len(content) == 0:
    print("The number of characters in a tweet must be 1 or more.")
    return

  if len(image_path) == 0:
    image_tweet = False
  else:
    image_tweet = True
      
  if fav == True and image_tweet == False:
    try:
      api.create_favorite(id)
      print("Tweet favorited.")
    except:
      pass
    try:
      api.update_status(status = content, in_reply_to_status_id = id,auto_populate_reply_metadata=True)
      print("Tweeted.")
      for status in api.user_timeline(id=me.screen_name,count = 1):
        print("Tweet id:"+str(status.id))
        print("https://twitter.com/" + me.screen_name + "/status/" + str(status.id))
    except:
      print("Failed to send the tweet.")
      return

  elif fav == True and image_tweet == True:
    try:
      api.create_favorite(id)
      print("Tweet favorited.")
    except:
      pass
    try:
      api.update_with_media(status = content,filename=image_path, in_reply_to_status_id = id,auto_populate_reply_metadata=True)
      print("Tweeted.")
      for status in api.user_timeline(id=me.screen_name,count = 1):
        print("Tweet id:"+str(status.id))
        print("https://twitter.com/" + me.screen_name + "/status/" + str(status.id))
    except:
      print("Failed to send the tweet.")
      return

  elif fav == False and image_tweet == False:
    try:
      api.update_status(status = content, in_reply_to_status_id = id,auto_populate_reply_metadata=True)
      print("Tweeted.")
      for status in api.user_timeline(id=me.screen_name,count = 1):
        print("Tweet id:"+str(status.id))
        print("https://twitter.com/" + me.screen_name + "/status/" + str(status.id))
    except:
      print("Failed to send the tweet.")
      return

  elif fav == False and image_tweet == True:
    try:
      api.update_with_media(status = content,filename=image_path, in_reply_to_status_id = id,auto_populate_reply_metadata=True)
      print("Tweeted.")
      for status in api.user_timeline(id=me.screen_name,count = 1):
        print("Tweet id:"+str(status.id))
        print("https://twitter.com/" + me.screen_name + "/status/" + str(status.id))
    except:
      print("Failed to send the tweet.")
      return
  
  else:
    try:
      api.update_status(status = content, in_reply_to_status_id = id,auto_populate_reply_metadata=True) #画像無し
      print("Tweeted.")
      for status in api.user_timeline(id=me.screen_name,count = 1):
        print("Tweet id:"+str(status.id))
        print("https://twitter.com/" + me.screen_name + "/status/" + str(status.id))
    except:
      print("Failed to send the tweet.")
      return
      
def tweetdestroy(api,id):
  try:
    api.destroy_status(id)
    print("Deleted the tweet.")
  except:
    print("Failed to delete tweet.")

def favorite(api,id):
  try:
    api.create_favorite(id)
    print("Tweet favorited.")
  except:
    api.destroy_favorite(id)
    print("Canceled the favorite.")

def retweet(api,id):

  id = input("Tweet_id:")

  try:
    if not len(id) == 0:
      api.retweet(id)
      print("Retweeted.")
    else:
      print("Canceled.")
  except:
    status = api.get_status(id, include_my_retweet=1)

    if status.retweeted == True:
      api.destroy_status(status.current_user_retweet['id'])
          
    print("Deleted retweet.")

def follow(api,user_id):
  try:
    api.create_friendship(screen_name=user_id)
    print("Followed.")
  except:
  	print("Failed to follow.")

def unfollow(api,follow_id):
  try:
    api.destroy_friendship(follow_id)
    print("Follow deleted.")
  except:
	  print("Failed to delete.")


def profile(api,user_id):
  try:
    user = api.get_user(user_id)
  except:
    print("Failed to get user information")
    return

  print(user.name + f"\n@{user.screen_name}")
  
  print(user.description)
  
  print("Location:" + user.location)
  
def user_timeline(api,user_id):
  try:
    for status in api.user_timeline(user_id):
      if (("RT" in status.text) == False):

        print("\n")	
        print("-"*42)

        if status.user.verified == True:
          print(status.user.name + " ✔︎" + " @" + status.user.screen_name)
        else:
        	print(status.user.name + " @" + status.user.screen_name)

        print(status.text.replace("https://t.co","\nhttps://t.co"))
        print(f"Favorites:{status.favorite_count} Retweet:{status.retweet_count}")
        if status.favorited == True:
          print("Favorited")
        elif status.favorited ==True and status.retweeted == True:
          print("Favorited Retweeted")
        elif status.favorited == False and status.retweeted == True:
          print("Retweeted")
        else:
          pass

        print(str(status.created_at)+ " " +status.source)
        print()
        print(f"Tweet id:{status.id}")
        print(f"User id:{status.user.id}")
        print(f"url:https://twitter.com/{status.user.screen_name}/status/{status.id}")
  except:
    print("Failed to get user information.")
    return


def search(api,search_text):
    try:
      word = [search_text]
      set_count = 10
      results = api.search(q=word, count=set_count)

      for status in results:
        if (("RT" in status.text) == False):

          print("\n")	
          print("-"*42)

          if status.user.verified == True:
            print(status.user.name + " ✔︎" + " @" + status.user.screen_name)
          else:
          	print(status.user.name + " @" + status.user.screen_name)

          print(status.text.replace("https://t.co","\nhttps://t.co"))
          print(f"Favorites:{status.favorite_count} Retweet:{status.retweet_count}")
          if status.favorited == True:
            print("Favorited")
          elif status.favorited ==True and status.retweeted == True:
            print("Favorited Retweeted")
          elif status.favorited == False and status.retweeted == True:
            print("Retweeted")
          else:
            pass

          print(str(status.created_at)+ " " +status.source)
          print()
          print(f"Tweet id:{status.id}")
          print(f"User id:{status.user.id}")
          print(f"url:https://twitter.com/{status.user.screen_name}/status/{status.id}")
    except:
      print("Failed to search.")
