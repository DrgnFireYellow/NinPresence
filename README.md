# NinPresence

A simple way to share what switch game you're playing on discord.

## Getting Started
Start by downloading Python 3 and, if the Python installer didn't install it for you, tkinter. Next, download this repository to your computer. Now, run this command while in the directory you downloaded:

If on Mac/Linux:
`pip3 install -r requirements.txt`

If on Windows:
`python -m pip install -r requirements.txt`

Next, go to the [Discord Developer Portal](https://discord.com/developers) and create a new app named "NinPresence". Optionally, go to the rich presence section and upload images with the associated game name **in lowercase without spaces** (For example splatoon3 or animalcrossingnewhorizons). Now, go to the general information section and copy the application id. Next, run the application using the following command:

If on Mac/Linux:
`python3 ninpresence.py`

If on Windows:
`python ninpresence.py`

Lastly, paste in the application id in the first field and select a game.
