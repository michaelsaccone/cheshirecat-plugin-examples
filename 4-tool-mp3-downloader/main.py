from cat.mad_hatter.decorators import tool, hook
from pytube import Search
import os
import requests

def search_youtube_video(video_title):
    # cerca il video
    print ("Searching " + video_title)
    search_results = Search(video_title)

    for v in search_results.results:
        print(f"{v.title}\n{v.watch_url}\n")

    video = search_results.results[0]

    audio_stream = video.streams.filter(only_audio=True).first()

    return audio_stream

@tool(examples=['send me this song', 'scarica la canzone', 'mandami la canzone'], return_direct=True)
def download_song_from_youtube(song_title, cat):
    """
    Download a song or music or whatever audio from YouTube locally.
    Sends a song to the Human.
    Input is ALWAYS the name of the song or video to search for
    """
    audio = search_youtube_video(song_title)
    # scarica il file audio localmente (il file audio si andrà sempre a sovrascrivere)
    out_file = audio.download(output_path='/app/cat/static') 

    print("FILE: " + out_file)

    new_file = '/app/cat/static/audio.mp3'
    os.rename(out_file, new_file)

    return '<audio controls><source src="http://localhost:1865/static/audio.mp3" type="audio/mpeg"></audio>'