# Discord Weather Bot
> ## Access your concurrent weather, anytime, anywhere!
## Environment and Requirement
* Python 3.9.2
* [OpenWeatherMap](https://openweathermap.org/current) API
* [Discord API](https://discord.com/developers/applications)
* [Heroku](https://www.heroku.com)
### Local machine
```
pip3 install discord.py
pip3 install requests
```
Create a **Procfile** in your project's root directory and add following to it. It will contain a worker command that will start the bot.
```
worker: python main.py
```
Create a **requirements.txt** file and add required libraries to it.
```
# creates the output installed packages in requirements format.
pip freeze > requirements.txt
```
Create a **runtime.txt** file in your project's root directory and add following to it.
```
# python version
python-3.9.2
```
### Heroku deployment
#### Settings
Add OpenWeatherMap API and Discord Bot Token to Config Vars
![](https://i.imgur.com/3AOUTPE.png)
#### Deploy
Connects Heroku app to Github repository.

![](https://i.imgur.com/zidJWZc.png)

Choose Deploy Branch and enable Auto Deploy.

After then it will be look like thw following image.

![](https://i.imgur.com/rjwSpCY.png)


### Get the bot online
#### Resources
Enable the Dynos.

![](https://i.imgur.com/QnllpD1.png)

Test the bot!

![ezgif com-gif-maker](https://user-images.githubusercontent.com/61106644/124215941-a433d580-db27-11eb-9bdc-87e112f429bc.gif)


The bot will now be online and ready to serve 24/7. If we commit on the remote repository, the bot will be updated and deployed automatically.
