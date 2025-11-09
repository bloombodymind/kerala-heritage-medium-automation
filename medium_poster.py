import json
import os
from datetime import datetime, timezone
import requests

def get_current_day():
    """Calculate current day number (1-35) based on days since epoch"""
    epoch = datetime(1970, 1, 1, tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)
    days_since_epoch = (now - epoch).days
    return (days_since_epoch % 35) + 1

def load_posts():
    """Load posts from posts.json"""
    with open('posts.json', 'r') as f:
        return json.load(f)

def post_to_medium(author_id, access_token, content, title):
    """Post story to Medium"""
    url = f"https://api.medium.com/v1/users/{author_id}/posts"
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    # Format content for Medium
    data = {
        'title': title,
        'contentFormat': 'markdown',
        'content': content,
        'publishStatus': 'public',
        'tags': ['Kerala', 'Travel', 'Homestay', 'Heritage', 'Tourism']
    }
    
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def main():
    # Get environment variables
    author_id = os.environ.get('MEDIUM_AUTHOR_ID')
    access_token = os.environ.get('MEDIUM_ACCESS_TOKEN')
    
    if not author_id or not access_token:
        print("Error: MEDIUM_AUTHOR_ID and MEDIUM_ACCESS_TOKEN must be set")
        return
    
    # Get current day and load posts
    current_day = get_current_day()
    posts = load_posts()
    
    # Find post for current day
    post = next((p for p in posts if p['id'] == current_day), None)
    
    if not post:
        print(f"Error: No post found for day {current_day}")
        return
    
    # Extract title from post text (first line)
    lines = post['post_text'].split('\n')
    title = lines[0] if lines else f"Kerala Heritage Homestay - Day {current_day}"
    content = post['post_text']
    
    # Post to Medium
    print(f"Posting day {current_day} to Medium...")
    result = post_to_medium(author_id, access_token, content, title)
    
    if 'id' in result:
        print(f"Successfully posted! Post URL: {result.get('url', 'N/A')}")
    else:
        print(f"Error posting to Medium: {result}")

if __name__ == '__main__':
    main()
