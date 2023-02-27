# Devcom slack bot assignment

### Overview - How to create the slack Bot

1) Went to api.slack.com and created a new app for your workspace.
2) After creating the bot app, we need to install it to our workspace. To do this, click the "Install App" button on the bot app's management page, and follow the instructions
3) Once the bot is installed in our workspace, we need to get its token. The token is used to authenticate the bot and send messages to your workspace. We can find the bot token on the "Install App" page.
4) Then, I wrote the python script using the slack_sdk library for generating automated messages to slack.
5) Saved the script as a file and run it on a server or cloud service Heroku. The script will check for users' birthdays every day and send birthday messages to the specified channel on a user's birthday.

