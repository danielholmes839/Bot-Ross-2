# discord-bot-ross
Bot Ross is a discord bot that does image manipulation and a true artist. 

## How to use
Bot Ross is currently hosted on heroku. If you would like to try this bot use this link to add it to your server: <br/>
https://discordapp.com/api/oauth2/authorize?client_id=507694799898542081&permissions=10240&scope=bot <br/>
source code for this bot is in the 'hosted-branch'. <br/>

Or if you would like to host the bot yourself download the 'self-hosted-branch'. Create a discord bot at: <br/>
https://discordapp.com/developers/applications/ <br/>
and change the token in bot_ross.py and add the bot to your server. Make sure you have the following packages installed when running the bot: <br/>
- discord.py 0.16.12
- Pillow 5.2.0
- sklearn 0.0

## Commands 
Once you've added the bot to your server here the commands you can use: <br/>
- !help 
  - List all commands
- !sobel [link]
  - Outlines the edges in the image 
- !compression [integer 2-16] [link] 
  - Reduces the number of colours in the image to the integer specified

http://danielholmes.ca/
