#!/usr/bin/env python3
from gmusicapi import Mobileclient
from spotipy import Spotify, util, client
import sys
import logging
import os.path
from os import path

# GPM keys
GPM_KEY_FILE="gpm_credentials.key"
# Spotify keys
# TODO: Set client keys and ids
SPOTIFY_CLIENT_ID=''
SPOTIFY_SECRET=''
SPOTIFY_USERNAME=''
SPOTIFY_REDIRECT_URI='http://localhost/'

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(lineno)d -- %(message)s")

def get_gpm_client():
    gpm_client = Mobileclient()
    if path.exists(GPM_KEY_FILE) == False:
        logging.info("Logging you in via oauth")
        gpm_client.perform_oauth(storage_filepath=GPM_KEY_FILE,open_browser=True)
    else:
        logging.info("Using previous key to authenticate")
        gpm_client.oauth_login(device_id=Mobileclient.FROM_MAC_ADDRESS,oauth_credentials=GPM_KEY_FILE)
    return gpm_client

def get_spotify_client(username,scope,client_id,client_secret,redirect_uri):
    token = util.prompt_for_user_token(username,scope,client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri)
    sp_client = Spotify(auth=token)
    return sp_client



def get_gpm_lib_generator(gpm_client):
    library_generator = gpm_client.get_all_songs(incremental=True)
    return library_generator

def upload_lib_to_spotify(gpm_lib,spotify_client):
    for track in gpm_lib:
        artist = track['artist']
        title = track['title']


def main():
    logging.info("Authenticating to gpm")
    gpm_client = get_gpm_client()
    logging.info("Authenticating to spotify")
    # scope for modifying the user's library
    scope='user-library-modify'
    spotify_client = get_spotify_client(SPOTIFY_USERNAME,scope,SPOTIFY_CLIENT_ID,SPOTIFY_SECRET,SPOTIFY_REDIRECT_URI)
    logging.info("Getting gpm lib")
    gpm_library_iter = get_gpm_lib_generator(gpm_client)
    logging.info("Uploading library to spotify")
    for lib in gpm_library_iter:
        logging.info("uploading next {} songs".format(len(lib)))
        upload_lib_to_spotify(lib,spotify_client)




if __name__ == '__main__':
    main()