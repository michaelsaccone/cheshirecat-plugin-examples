from cat.mad_hatter.decorators import tool, hook
from pytube import Search
import os
import requests

def search_youtube_video(video_title):
    # cerca il video
    search_results = Search(video_title)
    video = search_results.results[0]

    audio_stream = video.streams.filter(only_audio=True).first()

    audio_url = audio_stream.url
    return audio_url

@tool(examples=['download this song', 'scarica la canzone'])
def download_song_from_youtube(song_title, cat):
    """
    Download a song or music or whatever audio from YouTube locally. 
    Input is ALWAYS the name of the song or video to search for
    """
    audio_url = search_youtube_video(song_title)
    # scarica il file audio localmente (il file audio si andrà sempre a sovrascrivere)
    audio_file = requests.get(audio_url)
    audio_file_path = 'audio.mp3'
    with open(audio_file_path, 'wb') as f:
        f.write(audio_file.content)

@tool(examples=['give me the link', 'find the link of'], return_direct=True)
def get_youtube_audio_link(song_title, cat):
    """
       Find the link to download a song or audio from YouTube.
       Input is ALWAYS the title of the song or audio to download
    """
    audio_url = search_youtube_video(song_title)
    # link per il download
    return audio_url