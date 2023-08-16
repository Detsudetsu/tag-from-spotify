# tag-from-spotify
[![PyPI](https://img.shields.io/pypi/v/tag-from-spotify)](https://pypi.org/project/tag-from-spotify/)
![out4](https://github.com/Detsudetsu/tag-from-spotify/assets/36166146/3a4d3afb-63ac-408d-b909-d6cd9fdc17d7)

`tag-from-spotify` is a Python CLI tool to fetch audio metadata from Spotify and tag them to your audio files.

## Installation
Since this package is meant to be an end-user app (not a library), it is highly recommended to install with `pipx`.
```
pipx install tag-from-spotify
```
Of course, you can use `pip` as well.

## Authorization
### 1. Create Credentials
To fetch data from Spotify, you have to register this app to [your dashboard](https://developer.spotify.com/dashboard/applications) and create your Client ID and Client Sectet. You will see the detail process on [the Spotify Developer page](https://developer.spotify.com/documentation/general/guides/app-settings/), but note that you won't have to prepare your website URL or a redirection URL.
### 2. Set Credentials to Environment Variables
Then add your Client ID and Client Secret to your environment variables like this:
```
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
```

## Usage
```
tfsp DIR ALBUM_ID
```
- DIR: path to the directory containing audio files to set tags
- ALBUM_ID: the album ID, URI or URL such as the following examples:
  - ID: 0WHIgko1oBSbayvwe9tdze
  - URI: spotify:album:0WHIgko1oBSbayvwe9tdze
  - URL: https://open.spotify.com/album/0WHIgko1oBSbayvwe9tdze

## Development
Create an `.env` that contains Spotify Client ID and Client Secret for the repository root (so you don't have to set them to the environment variables)

```.env
SPOTIPY_CLIENT_ID=piyopiyopiyopiyo
SPOTIPY_CLIENT_SECRET=megamegamegamega
```
