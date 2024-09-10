import os
import datetime
import feedparser
import requests
from dateutil import parser
import json
import argparse

# Step 1: Create a directory structure based on Category/Sector/Country
def create_directory_structure(base_dir):
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    for subdir in ["RSSFeeds-Sources", "RSSFeeds-Logs", "RSSFeeds-Errors", "RSSFeeds-JSON"]:
        path = os.path.join(base_dir, subdir)
        if not os.path.exists(path):
            os.makedirs(path)

# Step 2: Place individual RSS Feed list files in each Category/Sector/Country
def read_rss_feed_list(file_path):
    with open(file_path, 'r') as file:
        feeds = file.readlines()
    return [feed.strip() for feed in feeds]

# Step 3: Take input arguments for Category, Sector, or Country
def parse_arguments():
    parser = argparse.ArgumentParser(description="RSS Feed Aggregator")
    parser.add_argument("--sector", type=str, help="Select sector-specific news", required=False)
    parser.add_argument("--category", type=str, help="Select category-specific news", required=False)
    parser.add_argument("--country", type=str, help="Select country-specific news", required=False)
    return parser.parse_args()

# Step 4: Check if each feed inside the list is accessible and returns XML data
def check_feed_accessibility(feed_url):
    try:
        response = requests.get(feed_url)
        if response.status_code == 200 and response.headers['Content-Type'] == 'application/rss+xml':
            return True
        else:
            return False
    except Exception as e:
        return False

# Step 5: Create log files of each feed in the respective directories
def process_rss_feeds(feed_list, log_dir, json_dir, error_dir):
    all_articles = []
    for idx, feed_url in enumerate(feed_list):
        log_file = os.path.join(log_dir, f"FEED{idx + 1}.txt")
        error_file = os.path.join(error_dir, f"Error_FEED{idx + 1}.txt")
        if check_feed_accessibility(feed_url):
            feed = feedparser.parse(feed_url)
            if 'entries' in feed:
                articles = []
                for entry in feed.entries:
                    article_data = {
                        "title": entry.get("title", "No Title"),
                        "link": entry.get("link", "No Link"),
                        "description": entry.get("description", "No Description"),
                        "published": entry.get("published", "No Date")
                    }
                    articles.append(article_data)

                # Writing to log file
                with open(log_file, 'w', encoding='utf-8') as log:
                    for article in articles:
                        log.write(f"Title: {article['title']}\n")
                        log.write(f"Link: {article['link']}\n")
                        log.write(f"Description: {article['description']}\n")
                        log.write(f"Published: {article['published']}\n\n")

                # Append articles to global list
                all_articles.extend(articles)
            else:
                with open(error_file, 'w', encoding='utf-8') as error_log:
                    error_log.write(f"Feed not accessible: {feed_url}\n")
        else:
            with open(error_file, 'w', encoding='utf-8') as error_log:
                error_log.write(f"Feed not accessible: {feed_url}\n")

    # Step 6: Create a consolidated JSON file for the entire category/sector/country
    consolidated_json_file = os.path.join(json_dir, "Consolidated_RSSFeed.json")
    with open(consolidated_json_file, 'w', encoding='utf-8') as json_file:
        json.dump(all_articles, json_file, indent=4)

    return all_articles

# Step 7: Error handling for feeds not accessible, missing tags, etc.
def handle_feed_errors(feed_url):
    try:
        response = requests.get(feed_url)
        if response.status_code == 200:
            feed = feedparser.parse(response.content)
            return feed
        else:
            print(f"Error accessing {feed_url}. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Exception occurred while accessing feed {feed_url}: {e}")

# Step 8: Print information on terminal and write logs
def print_feed_summary(feed_data):
    for article in feed_data:
        print(f"Title: {article['title']}")
        print(f"Link: {article['link']}")
        print(f"Published: {article['published']}")
        print(f"Description: {article['description']}\n")

def main():
    # Step 1: Setup directory structure
    args = parse_arguments()

    if args.sector:
        base_dir = f"./RSSFeeds-Sources/Sector/{args.sector}"
    elif args.category:
        base_dir = f"./RSSFeeds-Sources/Category/{args.category}"
    elif args.country:
        base_dir = f"./RSSFeeds-Sources/Country/{args.country}"
    else:
        print("Please provide either sector, category, or country.")
        return

    create_directory_structure(base_dir)
    
    rss_feed_list_file = os.path.join(base_dir, "RSSFeedsList.txt")
    log_dir = os.path.join(base_dir, "RSSFeeds-Logs")
    error_dir = os.path.join(base_dir, "RSSFeeds-Errors")
    json_dir = os.path.join(base_dir, "RSSFeeds-JSON")

    # Step 2: Read the feed list from file
    feed_list = read_rss_feed_list(rss_feed_list_file)

    # Step 5 & 6: Process feeds, create logs and consolidated JSON
    all_articles = process_rss_feeds(feed_list, log_dir, json_dir, error_dir)

    # Step 8: Print consolidated feed summary
    print_feed_summary(all_articles)

if __name__ == "__main__":
    main()
