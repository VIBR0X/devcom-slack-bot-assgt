import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime

# Set the bot token and channel name
client = WebClient(token=os.environ['xoxb-4861105113075-4884936352320-4sNd9hbTh07xe3JOxLw9ZXl7'])     # This is the corresponding to my devcom assgt workspace (ofc to be changed later)
channel = "#general"

# Get today's date
today = datetime.today().strftime('%m-%d')

# Loop through all the users in the workspace
try:
    response = client.users_list()
    users = response['members']
    for user in users:
        # Get the user's birthday if available
        if 'birthday' in user['profile']:
            birthday = user['profile']['birthday']
            if birthday == today:
                # Send a birthday message to the channel
                client.chat_postMessage(channel=channel, text=f"🎂 Happy birthday <@{user['id']}>! 🎉")
except SlackApiError as e:
    print(f"Error: {e}")


