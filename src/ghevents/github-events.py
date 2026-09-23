#!/usr/bin/env python3
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'
def retrieve_events(url):
    """
    Downloads GitHub event data from the URL, 
    parses the text, and returns a list of event dictionaries.
    """
    json_text = requests.get(url).text
    events_data = json.loads(json_text)
    return events_data

def print_events(events, n=5):
    """
    Loops through the GitHub events list and prints type 
    and repository name for the first n items.
    """
    for event in events[:n]:
        event = event['type'] + ' :: ' + event['repo']['name']
        print(event)
def main():
    """
    Main function that coordinates fetching and printing 
    GitHub events for the specified user.
    """
    print(GHUSER)
    print(url)
    events_list = retrieve_events(url)
    print_events(events_list)

if __name__ == "__main__":
    main()
