import twitter
import json
import io

def oauth_login():
    CONSUMER_KEY = 'Dm1Q0DPbBWJh3NGvIGwWtINFm'
    CONSUMER_SECRET ='v29T668iPJYQXqjuQDskjNW8UF0bfjJ6uXOz3tm1baBMBWuLO3'
    OAUTH_TOKEN = '3148519900-uJjC7HEFck2Vvm8Knpd8YfHyC9zt4gTqM4XEfyZ'
    OAUTH_TOKEN_SECRET = 'xLlxPwwwIZUUHcTfdhxjqK1mnBP9eCS4GTuoqlqJhe5kZ'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api


