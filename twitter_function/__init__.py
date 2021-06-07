# -*- coding: utf-8 -*-

import tw_function

__copyright__    = 'Copyright (C) 2021 Columba_Karasu'
__version__      = '1.0.6'
__license__      = 'BSD-3-Clause'
__author__       = 'Columba_Karasu'
__author_email__ = ''
__url__          = 'https://github.com/Hashibutogarasu/twitter-function'

__all__ = ['']


###########################
# -*- coding: utf-8 -*-
#2021/06/06
#made by Columba_Karasu
#Dependent libraries:tweepy
###########################

def timeline(api,count=20,limits_output=False):
  tw_function.timeline(api=api,count=20,limits_output=limits_output)

def tweet(api,content,id="",fav=False,image_path=""):
  tw_function.tweet(api,content,id=id,fav=fav,image_path=image_path)

def tweetdestroy(api,id):
  tw_function.tweetdestroy(api=api,id=id)

def favorite(api,id):
  tw_function.favorite(api=api,id=id)

def retweet(api,id):
  tw_function.retweet(api=api,id=id)

def follow(api,user_id):
  tw_function.follow(api=api,user_id=user_id)

def unfollow(api,follow_id):
  tw_function.unfollow(api=api,follow_id=follow_id)

def profile(api,user_id):
  tw_function.profile(api=api,user_id=user_id)

def user_timeline(api,user_id):
  tw_function.user_timeline(api=api,user_id=user_id)

def search(api,search_text):
  tw_function.search(api=api,search_text=search_text)
