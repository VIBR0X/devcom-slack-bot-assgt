# Devcom slack bot assignment

### Overview - How to create the slack Bot

1) Went to api.slack.com and created a new app for my (devcom assgt => (to be changed in future)) workspace.
2) After creating the bot app, I installed it to my workspace. To do this, I just followed the instructions written on the api.slack.com
3) Once the bot was installed in the workspace, I took the token. The token is used to authenticate the bot and send messages to thewo workspace. We can find the bot token on the "Install App" page.
4) Then, I wrote the python script using the slack_sdk library for generating automated messages to slack.
5) Saved the script as a file and run it on a server or cloud service Heroku. The script will check for users' birthdays every day and send birthday messages to the specified channel on a user's birthday.



### How can be upload on Heroku:-   ( for future refrence)

1) First Login to heroku and download the CLI version heroku.
2) Create a new Heroku app using the Heroku CLI command: **heroku create <app-name>**
3) Push the code to the Heroku app's git repository using the command: `git push heroku main`
4) For some time, the heroku will automatically install the required dependencies from the requirements.txt

  

