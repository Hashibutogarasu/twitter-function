# twitter-function

twitter-for-CUIの関数版

import twitter_functionでインポート可能。
長いのでimport twitter_function as twなどにするとよき。

<h1>リファレンス:</h1>

timeline(api,count=20,limits_output=False)

api:必須

auth = tweepy.OAuthHandler(ck, cs)
auth.set_access_token(at, ats)
api = tweepy.API(auth)

count:タイムラインの取得件数

limits_output:制限の出力Trueの場合出力する。

tweet(api,content,id="",fav=False,image_path="")

api:以下略

content:ツイートする内容

id:リプライ先

fav:Trueの時、idにいいねをするFalseは何もしない。

image_path:画像を添付する時の画像のパス。相対パスでも絶対パスでもどちらでも良い。

tweetdestroy(api,id)

api:以下略

id:ツイートのid。自分のものでないとエラーが出る。

favorite(api,id)

id:ツイートのid。いいねするだけ。いいね済みである時、いいねを外す。

retweet(api,id)

id:ツイートのid。リツイート済みの場合はリツイートを外す。

follow(api,user_id)

user_id:ユーザーのidを入れることによってフォロー可能。

unfollow(api,user_id)

user_id:ユーザーidを入れることによってフォロー解除可能。

profile(api,user_id)

user_id:ユーザーidまたはスクリーンネームでユーザーの情報を出力できる。

user_timeline(api,user_id)

user_id:ユーザーidまたはスクリーンネームでユーザーのツイートを出力できる。

search(api,search_text)

search_text:検索する内容。
