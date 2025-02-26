# import os

# from googleapiclient.discovery import build
# from dotenv import load_dotenv

# # Load API keys from environment variables
# load_dotenv()
# YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

# def get_top_trending_titles(category):
#     """Fetch top 5 trending YouTube videos related to the given category."""
#     request = youtube.search().list(
#         part="snippet",   
#         maxResults=5,  # Fetch top 5 trending videos
#         q=category,
#         type="video",
#         order="viewCount"
#     )
#     response = request.execute()
    
#     # Extract and return top 5 video titles
#     return [item["snippet"]["title"] for item in response.get("items", [])]

# # User input
# category = input("Enter a category (e.g., tech, gaming, finance): ").strip()
# trending_titles = get_top_trending_titles(category)

# # Display results
# print("\nTop 5 Trending YouTube Video Titles:")
# for idx, title in enumerate(trending_titles, start=1):
#     print(f"{idx}. {title}")  
import os
import streamlit as st
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load API keys from environment variables
load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

def get_top_trending_titles(category):
    """Fetch top 5 trending YouTube videos related to the given category."""
    request = youtube.search().list(
        part="snippet",   
        maxResults=5,  # Fetch top 5 trending videos
        q=category,
        type="video",
        order="viewCount"
    )
    response = request.execute()
    
    # Extract and return top 5 video titles
    return [item["snippet"]["title"] for item in response.get("items", [])]

# Streamlit UI
st.title("YouTube Trending Videos Finder")
st.write("Enter a category to find the top 5 trending videos.")

category = st.text_input("Enter a category (e.g., tech, gaming, finance):").strip()

if st.button("Search"):
    if category:
        trending_titles = get_top_trending_titles(category)
        
        if trending_titles:
            st.subheader("Top 5 Trending YouTube Video Titles:")
            for idx, title in enumerate(trending_titles, start=1):
                st.write(f"{idx}. {title}")
        else:
            st.warning("No trending videos found for this category.")
    else:
        st.error("Please enter a valid category.")
