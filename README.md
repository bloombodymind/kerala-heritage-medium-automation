# Kerala Heritage Medium Automation

Automated daily Medium posts for Kerala Village Heritage Homestay using the Medium API and GitHub Actions.

## Overview

This repository automatically posts content to Medium once per day, cycling through 35 pre-written posts about Kerala Heritage Homestay.

## Setup Instructions

### 1. Get Medium API Credentials

1. Go to Medium Settings: https://medium.com/me/settings
2. Scroll down to "Integration tokens"
3. Generate a new access token
4. Get your author ID by visiting: https://api.medium.com/v1/me with your token

### 2. Add Repository Secrets

1. Go to your repository Settings > Secrets and variables > Actions
2. Click "New repository secret"
3. Add these two secrets:
   - `MEDIUM_AUTHOR_ID`: Your Medium author/user ID
   - `MEDIUM_ACCESS_TOKEN`: Your Medium integration token

### 3. Update posts.json

The current `posts.json` file contains only 2 sample posts. You need to add all 35 posts:

1. Click on `posts.json` in the repository
2. Click the edit (pencil) icon
3. Replace the content with the complete JSON array of all 35 posts
4. Commit the changes

### 4. Enable GitHub Actions

1. Go to the "Actions" tab in your repository
2. Enable workflows if prompted
3. The workflow will run automatically every day at 2 AM UTC
4. You can also manually trigger it from the Actions tab

## How It Works

- The script calculates the current day number (1-35) based on days since epoch
- It cycles through the 35 posts automatically
- Posts are published as public stories on Medium
- Each post includes appropriate tags for Kerala tourism

## Files

- `medium_poster.py`: Python script that posts to Medium API
- `posts.json`: JSON file containing all post content
- `requirements.txt`: Python dependencies
- `.github/workflows/daily_post.yml`: GitHub Actions workflow

## Manual Testing

To test the script locally:

```bash
export MEDIUM_AUTHOR_ID="your_author_id"
export MEDIUM_ACCESS_TOKEN="your_access_token"
python medium_poster.py
```

## Troubleshooting

- Check the Actions tab for workflow run logs
- Ensure your Medium token hasn't expired
- Verify posts.json contains all 35 posts with correct format
- Make sure repository secrets are properly set

## Medium API Documentation

https://github.com/Medium/medium-api-docs
