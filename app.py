# import requests
# import streamlit as st

# API_KEY = "AIzaSyBl0nIx3r_dzRmiIA8LG2OltLhWNNjcFIY"
# REGION_CODE = "PK"




# # Streamlit UI
# st.title("YouTube Trending Videos")
# st.write("Select a country to see trending videos")

# # Dropdown for region selection
# region_code = st.selectbox(
#     "Choose Region", 
#     ["US", "IN", "PK", "GB", "CA", "AU", "FR", "DE", "JP", "KR", "BR"], 
#     index=2
# )

# # YouTube API URL
# YOUTUBE_API_URL = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode={region_code}&maxResults=10&key={API_KEY}"

# # Fetching Data from YouTube API
# def get_trending_videos():
#     response = requests.get(YOUTUBE_API_URL)
#     if response.status_code == 200:
#         return response.json().get("items", [])
#     else:
#         return None

# # Button to fetch trending videos
# if st.button("Get Trending Videos"):
#     videos = get_trending_videos()
#     if videos:
#         for idx, video in enumerate(videos, start=1):
#             title = video["snippet"]["title"]
#             thumbnail = video["snippet"]["thumbnails"]["medium"]["url"]
#             video_url = f"https://www.youtube.com/watch?v={video['id']}"
            
#             # Display Video Title and Thumbnail
#             st.write(f"**{idx}. [{title}]({video_url})**")
#             st.image(thumbnail, width=300)
#     else:
#         st.error("Failed to fetch data. Check your API key or quota.")
import requests
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")


# Streamlit UI
st.title("YouTube Trending Videos")
st.write("Select a country and category to see trending videos")

# Dropdown for region selection
region_code = st.selectbox(
    "Choose Region", 
    ["US", "IN", "PK", "GB", "CA", "AU", "FR", "DE", "JP", "KR", "BR"], 
    index=2
)

# Function to get available categories for the selected region
def get_categories():
    url = f"https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&regionCode={region_code}&key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        categories = response.json().get("items", [])
        return {cat["snippet"]["title"]: cat["id"] for cat in categories}
    else:
        return {}

# Fetch categories
categories_dict = get_categories()

# Dropdown for category selection
if categories_dict:
    category_name = st.selectbox("Choose Category", list(categories_dict.keys()))
    category_id = categories_dict[category_name]
else:
    st.error("Failed to fetch categories. Check API key or quota.")
    category_id = None

# Function to fetch trending videos based on region and category
def get_trending_videos(category_id):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode={region_code}&videoCategoryId={category_id}&maxResults=10&key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        return None

# Button to fetch trending videos
if st.button("Get Trending Videos") and category_id:
    videos = get_trending_videos(category_id)
    
    if videos:
        for idx, video in enumerate(videos, start=1):
            title = video["snippet"]["title"]
            thumbnail = video["snippet"]["thumbnails"]["medium"]["url"]
            video_url = f"https://www.youtube.com/watch?v={video['id']}"
            
            # Display Video Title and Thumbnail
            st.write(f"**{idx}. [{title}]({video_url})**")
            st.image(thumbnail, width=300)
    else:
        st.error("Failed to fetch data. Check your API key or quota.")
