# Spotify House Party 

This is an app where users can host 'music rooms'. A host, using their Spotify account, can invite
Guests to their room where they can vote to skip the host's currently playing song, or play/pause it. 

## Deployment
The live deployment of this project can be found here: https://house-party-djrt.herokuapp.com

## Project Breakdown

**Back-end: Django**
* Defines the Room model to be used
* Manages the creation of room, and determines whether a given user session is the host of a room or not
* Run queries on the database

**Spotify API**
* Used to access host user's Spotify Account
* Data is collected on the currently playing song such as artist, length, and cover art
* Permissions are requested to allow app to play/pause the current song and to skip to the next Sogn on their queue

**Front-end: React **
* Communicates with the back-end to display user room information
* Calls the Spotify API to perform app features
