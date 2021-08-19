from pprint import pprint
from pathlib import Path

from click import confirm
import fire
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import taglib
import re
from tqdm import tqdm


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(), language="ja")


def get_full_album_tracks(album):
    paginated_album_tracks = album["tracks"]
    album_tracks = paginated_album_tracks["items"]
    while paginated_album_tracks["next"]:
        paginated_album_tracks = sp.next(paginated_album_tracks)
        album_tracks.extend(paginated_album_tracks["items"])
    return album_tracks


def main(album_id, dir="."):
    album = sp.album(album_id)
    album_dir = Path(dir)
    songfiles = [p for p in sorted(album_dir.iterdir()) if p.is_file()]

    total_tracks_album = album["total_tracks"]
    total_files_dir = len(songfiles)
    if total_tracks_album != total_files_dir:
        print(
            f"'{album_dir}' has {total_files_dir} files, but '{album['name']}' has {total_tracks_album} tracks according to Spotify",
        )
        confirm("Do you want to continue?", abort=True)

    album_tracks = get_full_album_tracks(album)
    pbar = tqdm(total=total_tracks_album)
    for file, track in zip(songfiles, album_tracks):
        song = taglib.File(str(file))

        # always wrap values into a list even it is single value
        # and no tag can contain 'int'
        song.tags["DISCNUMBER"] = [str(track["disc_number"])]
        song.tags["TRACKNUMBER"] = [str(track["track_number"])]
        song.tags["TITLE"] = [track["name"]]
        song.tags["ARTIST"] = [a["name"] for a in track["artists"]]
        song.tags["ALBUM"] = [album["name"]]
        song.tags["ALBUMARTIST"] = [a["name"] for a in album["artists"]]
        song.save()
        # pprint(song.tags)
        song.close()

        # track name may contain some characters that won't be allowed to use in filename
        # so make sure to turn it into a valid filename
        track_name = re.sub(r'[\\/:*?"<>|]+', "_", track["name"])
        file_name = (
            str(track["disc_number"]) + "." + str(track["track_number"]).zfill(2) + ". " + track_name + file.suffix
        )
        file.rename(album_dir / file_name)
        
        pbar.update()

    album_dir.rename(album_dir.parent / album["name"])


if __name__ == "__main__":
    fire.Fire(main)