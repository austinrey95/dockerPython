import os
import time
import re
from slackclient import SlackClient
from flask import Flask, request, Response
import json
import requests
from redis import Redis, RedisError
import os
import socket
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
app = Flask(__name__)

# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"
SLACK_DEV_TOKEN ='xoxp-231334506688-306981381971-336249794148-de735b35d625579380eb813a52e7284c'
SLACK_WEBHOOK_TOKEN = 'm5ZeHmzWVoo9i64kMKonBO85' #Put your webhook token here
slack_client = SlackClient(SLACK_DEV_TOKEN)

def send_message(channel_id, message):
    slack_client.api_call(
    "chat.postMessage",
    channel=channel_id,
    text=message,
    username='Slack-Alert',
    icon_emoji=':joystick:'
    )

@app.route('/slack-alert/<string>', methods=['GET'])
def inbound(string):
    channel_id='C9W508U91'
    message=string
    send_message(channel_id, message)
    if 200:
        varst = {
            "input" : message,
            "output" : "Success!"
            }
    else:
        varst = {
            "input" : message,
            "output" : "Failed to send!"
            }        
    return Response(json.dumps(varst)), 200

@app.route('/is-prime/<int:num>', methods=['GET'])
def prime(num):
    if app.route('/is-prime/<int:num>', methods=['GET']):
        a = num
        # make sure n is a positive integer
        n = abs(int(a))
        # Counter used to help determine if number is prime or not
        y = 0
        # 0 and 1 are not primes
        if n < 2:
            y += 1
          # 2 is the only even prime number
        elif n == 2:
            y = 0
            # all other even numbers are not primes
        elif not n & 1:
            y += 1
            # range starts with 3 and only needs to go up
            # the square root of n for all odd numbers
        for x in range(3, int(n**0.5) + 1, 2):
            if n % x == 0:
                y = y + 1
                break
        if y >= 1:
                res = "Not Prime!"
        else:
                res = "Prime!"
                
        varp = {
            "input" : num,
            "output" : res
            }
        return Response(json.dumps(varp)), 200
    else:
        nope = {
            "error" : "Invalid input!"
            }
        return Response(json.dumps(nope)), 200        
            
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
