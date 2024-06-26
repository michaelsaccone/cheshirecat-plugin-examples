from apiclient.discovery import build
from pytube import Search


API_KEY = "AIzaSyA3EdtSU48_qg02vKw-YPso9YXpw0Ccw8M" # prendere da settings
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                                        developerKey = API_KEY)

def search_youtube_video(video_title):
    search = Search(video_title)
    print("Video trovati: ")
    # for v in search.results:
    #     print(f"{v.title}: {v.watch_url}\n")
    return search.results[0]

def video_comments(video_id):
    # empty list for storing reply
    replies = []
 
    # retrieve youtube video results
    video_response=youtube.commentThreads().list(
    part='snippet,replies',
    videoId=video_id
    ).execute()
 
    # iterate video response
    while video_response:
       
        # extracting required info
        # from each result object 
        for item in video_response['items']:
           
            # Extracting comments
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
             
            # counting number of reply of comment
            replycount = item['snippet']['totalReplyCount']
 
            # if reply is there
            if replycount>0:
               
                # iterate through all reply
                for reply in item['replies']['comments']:
                   
                    # Extract reply
                    reply = reply['snippet']['textDisplay']
                     
                    # Store reply is list
                    replies.append(reply)
 
            # print comment with list of reply
            print(comment, replies, end = '\n\n')
 
            # empty reply list
            replies = []
 
        # Again repeat
        if 'nextPageToken' in video_response:
            video_response = youtube.commentThreads().list(
                    part = 'snippet,replies',
                    videoId = video_id,
                      pageToken = video_response['nextPageToken']
                ).execute()
        else:
            break

video = search_youtube_video("Cheshire cat AI")

print(video.video_id)

video_comments(video_id=video.video_id)