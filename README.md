# tag-from-spotify
![PyPI](https://img.shields.io/pypi/v/tag-from-spotify)
![output](https://user-images.githubusercontent.com/36166146/130316281-506d9210-1744-455a-9e47-82f98e1ef3ed.gif)
`tag-from-spotify` is a Python CLI tool to fetch audio metadata from Spotify and tag them to your audio files.

## Installation
```
pip install tag-from-spotify
```

## Authorization
### 1. Create Credentials
To fetch data from Spotify, you have to register this app to [your dashboard](https://developer.spotify.com/dashboard/applications) and create your Client ID and Client Sectet. You will see the detail process on [the Spotify Developer page](https://developer.spotify.com/documentation/general/guides/app-settings/), but note that you won't have to prepare your website URL or a redirection URL.
### 2. Set Credentials to Enviroment Variables
Then add your Client ID and Client Secret to your enviroment variables like this:
```
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
```

## Usage
```
tfsp ALBUM_ID [DIR]
```
- ALBUM_ID: the album ID, URI or URL such as the following examples:
  - ID: 0WHIgko1oBSbayvwe9tdze
  - URI: spotify:album:0WHIgko1oBSbayvwe9tdze
  - URL: https://open.spotify.com/album/0WHIgko1oBSbayvwe9tdze
- DIR: path to the directory containing audio files to set tags (cwd by default)
