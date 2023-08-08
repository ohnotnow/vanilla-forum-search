#!/usr/bin/env python3

import requests
from datetime import datetime, timedelta
import sys
import time
import os
import json
import re

base_url = os.getenv('VANILLA_URL', '')

def get_discussions():
    # Calculate the start date as two weeks ago
    start_date = (datetime.now() - timedelta(weeks=2)).strftime("%Y-%m-%d")
    end_date = datetime.now().strftime("%Y-%m-%d")

    # URL for the Vanilla forums API
    url = f"{base_url}/discussions?start=%3E{start_date}&end={end_date}"

    # Headers (add authentication if needed)
    headers = {
        "Content-Type": "application/json",
        # "Authorization": "your_auth_token",
    }

    response = requests.get(url, headers=headers)

    # Check for a successful response
    if response.status_code != 200:
        print("Error fetching discussions!")
        return []

    return response.json()

def search_comments(discussion_id, keywords):
    # URL for the Vanilla forums API to get comments for a specific discussion
    url = f"{base_url}/comments?discussionID={discussion_id}"

    # Headers (add authentication if needed)
    headers = {
        "Content-Type": "application/json",
        # "Authorization": "your_auth_token",
    }

    response = requests.get(url, headers=headers)

    # Check for a successful response
    if response.status_code != 200:
        print(f"Error fetching comments for discussion {discussion_id}!")
        return []

    # Process the comments
    comments = response.json()
    results = []
    for comment in comments:
        body = comment.get('body', '').lower() # Convert body to lowercase
        comment_url = comment.get('url') # Modify as needed to get the correct URL
        embedded_urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', body)
        embedded_urls = [re.sub(r'</[^>]+>', '', url) for url in embedded_urls]
        embedded_urls = list(set(embedded_urls))

        matching_keywords = [word for word in keywords if word.lower() in body] # Convert each keyword to lowercase
        if matching_keywords:
            result = {
                "keywords": matching_keywords,
                "comment_url": comment_url,
                "embedded_urls": embedded_urls
            }
            results.append(result)

    return results

if __name__ == "__main__":
    if not base_url:
        print("Please set VANILLA_URL environment variable")
        exit(1)
    if not base_url.endswith('/api/v2'):
        base_url = f"{base_url}/api/v2"

    keywords = sys.argv[1:]
    if not keywords:
        print("Please provide keywords to search for")
        exit(1)

    discussions = get_discussions()

    results = []

    for discussion in discussions:
        discussion_title = discussion.get('name')
        discussion_id = discussion.get('discussionID')
        comment_results = search_comments(discussion_id, keywords)
        thread_results = {
            "Thread": discussion_title,
            "Matches": comment_results
        }
        results.append(thread_results)
        # Pause for 1 seconds...
        time.sleep(1)

    print(json.dumps(results, indent=2))
