# Google Play Music to Spotify
I've been a heavy user of Google Play Music (GPM) since early 2013, and built quite a large library since then. Unfortunately, in 2019 Google announced that GPM would eventually be sunset in favor of Youtube Music, a service which despite being over 4 years old as of this writing, still lacks basic functionality, such as library management, in order to become my every day music service of choice.

Google also let users know that their music library would eventually be migrated to Youtube Music hassle free. That was over 2 years ago, and I cannot understand what's holding them up. Tired of being stuck in limbo, I decided to jump ship onto Spotify. Unfortunately, that still left the problem of my library. Short of using shady third party sites that ask for your login credentials to both Spotify and Google, there is no simple way of migrating a music library from GPM to Spotify. So I decided to build my own.

This python script does 1 thing at the moment: take all the songs from you Music Library in GPM, and add them as saved songs in Spotify. Word of caution though- if you have a very large library as I did, you'll find that Spotify actually has a limit of 10,000 saved songs (Super lame!). Eventually, I will add support for migrating playlists from GPM to Spotify

## Step 1: Get Spotify Client ID and Secret
We need to get Spotify keys so that the script can save music to your library.
Go to the [Spotify developer page](https://developer.spotify.com/dashboard/), login, and create a client ID. You'll be asked for an app name and description. Give it enough info so that you can identify it. You'll also be asked for a redirect URL. Give it as `http://localhost/` 

Once that is done, you'll see your app's dashboard along with a client ID and client secret. Copy these into `SPOTIFY_CLIENT_ID` and 
`SPOTIFY_SECRET` in `main.py`
```
# Spotify keys
# TODO: Set client keys and ids
SPOTIFY_CLIENT_ID=''
SPOTIFY_SECRET=''
```

you'll also need your Spotify user id. You will find that under your [Account overview](https://www.spotify.com/us/account/overview/).
Copy it into `SPOTIFY_USERNAME` also in `main.py`
```
SPOTIFY_USERNAME=''
```
## Step 2: Login to your Google account

Login to your Google account on your browser of choice. 

## Step 3: Install requirements

with python 3 and pip3 installed, execute 
```
pip3 install -r requirements.txt
```
from the base directory to install the required python3 modules
## Step 4: Execute