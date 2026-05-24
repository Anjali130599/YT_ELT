import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY=os.getenv("API_KEY")
Channel_handle="MrBeast"

def get_playlist():
 
 try:
   url=f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={Channel_handle}&key={API_KEY}"

   response=requests.get(url)
   response.raise_for_status()

   data=response.json()
   #print(json.dumps(data, indent=4))

   channel_items=data["items"][0]
   channel_playlist=channel_items["contentDetails"]["relatedPlaylists"]["uploads"]
   print(channel_playlist)
   return channel_playlist
 
 except requests.exceptions.RequestException as e:
   raise e



def get_video_ids(playlist_id):
  videos_ids=[]
  pageToken= None
  base_url=f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&playlistId=UUX6OQ3DkcsbYNE6H8uQQuVA&key={API_KEY}"   
  try:
    while True:
      url=base_url
      if pageToken:
        url+=f"&pageToken={pageToken}"
      response=requests.get(url)
      response.raise_for_status()
      data=response.json()  
      for item in data.get("items",[]):
        video_id=item["contentDetails"]["videoId"]
        videos_ids.append(video_id)
      pageToken=data.get("nextPageToken")

      if pageToken is None:
        break

    return videos_ids    

  except requests.exceptions.RequestException as e:
    raise e  
  
  
if __name__=="__main__":
  playlist_id=get_playlist() 
  get_video_ids(playlist_id)
 
