import os
import requests
import feedparser
import json

# Step 1: Create Directory Structure
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

# Step 2: Save RSS Feed List in each Category/Sector/Country
def save_rss_feed_list(base_path, feed_type, name, rss_feeds):
    feed_list_path = os.path.join(base_path, feed_type, name, "RSSFeedsList.txt")
    with open(feed_list_path, 'w') as file:
        file.writelines("\n".join(rss_feeds))

# Step 3: Load RSS Feed List from Directory
def get_rss_feed_list(base_path, feed_type, name):
    feed_list_path = os.path.join(base_path, feed_type, name, "RSSFeedsList.txt")
    if os.path.exists(feed_list_path):
        with open(feed_list_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    else:
        print(f"No RSS Feed list found for {name} in {feed_type}")
        return []

# Step 4: Check RSS Feed Accessibility (Status 200 & XML Format)
def check_feed_accessibility(rss_url):
    try:
        response = requests.get(rss_url)
        if response.status_code == 200 and 'xml' in response.headers.get('Content-Type', ''):
            return True
    except Exception as e:
        print(f"Error accessing {rss_url}: {e}")
    return False

# Step 5: Process RSS Feeds and Create Logs
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
                    published = entry.published if hasattr(entry, 'published') else "No Date"
                    log.write(f"Title: {entry.title}\nLink: {entry.link}\nDescription: {entry.description}\nPublished: {published}\n\n")
                    feed_data.append({
                        "title": entry.title,
                        "link": entry.link,
                        "description": entry.description,
                        "published": published
                    })
    return feed_data

# Step 6: Save Consolidated JSON
def save_consolidated_json(base_path, feed_type, name, feed_data):
    json_dir = os.path.join(base_path, feed_type, name, "RSSFeeds-JSON")
    os.makedirs(json_dir, exist_ok=True)
    json_file_path = os.path.join(json_dir, f"Consolidated_RSSFeed.json")
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(feed_data, json_file, indent=4)

# Step 7: Handle Errors and Save Error Logs
def handle_errors_and_log(base_path, feed_type, name, feed_urls):
    error_log_dir = os.path.join(base_path, feed_type, name, "RSSFeeds-Errors")
    os.makedirs(error_log_dir, exist_ok=True)
    error_log_path = os.path.join(error_log_dir, "Error_FEED1.txt")
    with open(error_log_path, 'w') as error_log:
        for rss_url in feed_urls:
            if not check_feed_accessibility(rss_url):
                error_log.write(f"Error accessing {rss_url}\n")

# Step 8: Print Information on the Terminal
def print_feed_info(feed_data):
    for article in feed_data:
        print(f"Title: {article['title']}\nLink: {article['link']}\nDescription: {article['description']}\nPublished: {article['published']}\n")

# Main Function to Handle Arguments and Run the Program
def main():
    # Defining the base directory, categories, sectors, and countries
    base_path = "./RSSFeeds-Sources"
    categories = ["Crime", "Entertainment", "Lifestyle", "Military", "Politics", "Sports"]
    sectors = ["Energy", "Financial", "Manufacture", "Medical", "Political", "Retail", "Space"]
    countries = ["Global", "India", "Pakistan", "US"]

    # Create the directory structure
    create_directory_structure(base_path, categories, sectors, countries)

    # Example Feeds
    category_feeds = {
        "Entertainment": ["https://rss.cnn.com/rss/cnn_showbiz.rss"],
        "Lifestyle": ["https://rss.nytimes.com/services/xml/rss/nyt/FashionandStyle.xml"]
    }
    sector_feeds = {
        "Energy": ["https://feeds.feedburner.com/oil-gas-news"],
        "Financial": ["https://feeds.reuters.com/reuters/businessNews"]
    }
    country_feeds = {
        "Global": ["https://rss.nytimes.com/services/xml/rss/nyt/World.xml"],
        "India": ["https://www.thehindu.com/news/national/feeder/default.rss"]
    }

    # Save RSS Feed Lists
    for category, feeds in category_feeds.items():
        save_rss_feed_list(base_path, "Category", category, feeds)

    for sector, feeds in sector_feeds.items():
        save_rss_feed_list(base_path, "Sector", sector, feeds)

    for country, feeds in country_feeds.items():
        save_rss_feed_list(base_path, "Country", country, feeds)

    # Specify feed type and name for testing
    feed_type = "Category"  # Or "Sector" or "Country"
    name = "Lifestyle"  # Change to any valid directory name

    # Step 3: Load RSS Feed list
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
