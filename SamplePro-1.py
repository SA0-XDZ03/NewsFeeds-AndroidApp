import os
import requests
import feedparser
import json
import datetime
from dateutil import parser

# Step 1: Create Directory Structure based on Category/Sector/Countries
def create_directory_structure(base_path, categories, sectors, countries):
    os.makedirs(base_path, exist_ok=True)
    for category in categories:
        category_path = os.path.join(base_path, "Category", category)
        os.makedirs(category_path, exist_ok=True)
    for sector in sectors:
        sector_path = os.path.join(base_path, "Sector", sector)
        os.makedirs(sector_path, exist_ok=True)
    for country in countries:
        country_path = os.path.join(base_path, "Country", country)
        os.makedirs(country_path, exist_ok=True)

# Step 2: Place an individual RSS Feed List File in each Category/Sector/Country directory
def save_rss_feed_list(base_path, feed_type, name, rss_feeds):
    feed_list_path = os.path.join(base_path, feed_type, name, "RSSFeedsList.txt")
    with open(feed_list_path, 'w') as file:
        file.writelines("\n".join(rss_feeds))

# Step 3: Program takes input as arguments
def get_rss_feed_list(base_path, feed_type, name):
    feed_list_path = os.path.join(base_path, feed_type, name, "RSSFeedsList.txt")
    if os.path.exists(feed_list_path):
        with open(feed_list_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    else:
        print(f"No RSS Feed list found for {name} in {feed_type}")
        return []

# Step 4: Check if each feed is accessible (Status 200 & XML Format)
def check_feed_accessibility(rss_url):
    try:
        response = requests.get(rss_url)
        if response.status_code == 200 and 'xml' in response.headers.get('Content-Type', ''):
            return True
    except Exception as e:
        print(f"Error accessing {rss_url}: {e}")
    return False

# Step 5: Create log files for each feed in their respective directories
def process_rss_feeds(base_path, feed_type, name, feed_urls):
    logs_dir = os.path.join(base_path, feed_type, name, "RSSFeeds-Logs")
    os.makedirs(logs_dir, exist_ok=True)
    feed_data = []
    
    for index, rss_url in enumerate(feed_urls):
        if check_feed_accessibility(rss_url):
            feed = feedparser.parse(rss_url)
            log_file = os.path.join(logs_dir, f"FEED{index + 1}.txt")
            with open(log_file, 'w', encoding='utf-8') as log:
                for entry in feed.entries:
                    if hasattr(entry, 'published'):
                        log.write(f"Title: {entry.title}\nLink: {entry.link}\nDescription: {entry.description}\nPublished: {entry.published}\n\n")
                    feed_data.append({
                        "title": entry.title,
                        "link": entry.link,
                        "description": entry.description,
                        "published": entry.published
                    })
    return feed_data

# Step 6: Create a consolidated JSON file
def save_consolidated_json(base_path, feed_type, name, feed_data):
    json_file_path = os.path.join(base_path, feed_type, name, f"RSSFeed-{name}.json")
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(feed_data, json_file, indent=4)

# Step 7: Complete error handling and create error logs
def handle_errors_and_log(base_path, feed_type, name, feed_urls):
    error_log_path = os.path.join(base_path, feed_type, name, "RSSFeeds-ErrorLogs.txt")
    with open(error_log_path, 'w') as error_log:
        for rss_url in feed_urls:
            if not check_feed_accessibility(rss_url):
                error_log.write(f"Error accessing {rss_url}\n")

# Step 8: Print information on the terminal
def print_feed_info(feed_data):
    for article in feed_data:
        print(f"Title: {article['title']}\nLink: {article['link']}\nDescription: {article['description']}\nPublished: {article['published']}\n")

def main():
    # Defining the base directory, categories, sectors, and countries
    base_path = "./RSSFeeds-Sources"
    categories = ["Entertainment", "Technology", "Politics"]
    sectors = ["Energy", "Sports", "Defense"]
    countries = ["Global", "India", "USA"]

    # Create the directory structure
    create_directory_structure(base_path, categories, sectors, countries)

    # Sample RSS Feeds for different categories, sectors, and countries
    category_feeds = {
        "Entertainment": ["https://rss.cnn.com/rss/cnn_showbiz.rss"],
        "Technology": ["https://feeds.a.dj.com/rss/RSSWSJD.xml"]
    }
    sector_feeds = {
        "Energy": ["https://feeds.feedburner.com/oil-gas-news"],
        "Sports": ["https://rss.cnn.com/rss/cnn_sport.rss"]
    }
    country_feeds = {
        "Global": ["https://rss.nytimes.com/services/xml/rss/nyt/World.xml"],
        "India": ["https://www.thehindu.com/news/national/feeder/default.rss"]
    }

    # Save RSS feed lists for categories, sectors, and countries
    for category, feeds in category_feeds.items():
        save_rss_feed_list(base_path, "Category", category, feeds)

    for sector, feeds in sector_feeds.items():
        save_rss_feed_list(base_path, "Sector", sector, feeds)

    for country, feeds in country_feeds.items():
        save_rss_feed_list(base_path, "Country", country, feeds)

    # Select feed type and name
    feed_type = "Category"  # or Sector or Country
    name = "Technology"  # Choose from predefined names like Technology, Energy, India, etc.

    # Step 3: Fetch RSS Feed list
    rss_feed_urls = get_rss_feed_list(base_path, feed_type, name)

    # Step 5: Process RSS Feeds and save logs
    feed_data = process_rss_feeds(base_path, feed_type, name, rss_feed_urls)

    # Step 6: Save consolidated JSON
    save_consolidated_json(base_path, feed_type, name, feed_data)

    # Step 7: Handle errors and save error logs
    handle_errors_and_log(base_path, feed_type, name, rss_feed_urls)

    # Step 8: Print feed info on terminal
    print_feed_info(feed_data)

if __name__ == "__main__":
    main()
