# Spotify Playlist Creator

This script allows you to create a Spotify playlist based on the Billboard Hot 100 songs for a specific year.

## Prerequisites

- Python 3.x
- `spotipy` library: Install it using `pip install spotipy`
- `requests` library: Install it using `pip install requests`
- `beautifulsoup4` library: Install it using `pip install beautifulsoup4`

## Setup

1. Create an application on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
2. Obtain your `client_id` and `client_secret` from the application dashboard.
3. Set up your application's redirect URI. For this script, you can use `https://example.com`.
4. Make sure you have a Spotify account.

## Usage

1. Run the script.
2. Enter the year for which you want to create the playlist.
3. The script will fetch the Billboard Hot 100 songs for the specified year.
4. It will create a private playlist on your Spotify account named `<year>-hitlist` and add the songs to it.

## Note

- The script uses the `spotipy` library for interacting with the Spotify API.
- Ensure that your entered year is valid and within the available range.
- The playlist will be created as private by default.
- Make sure to keep your `client_id` and `client_secret` confidential.

## Disclaimer

This script is provided for educational purposes only. Use it responsibly and respect Spotify's terms of service.

