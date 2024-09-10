### Roadmap For NewsApp Android
- [ ] Gather Resources: Data Sources Status
	- [ ] Category-based / Country-based / Sector-based RSS Feeds
		- [ ] Free News RSS Feeds
		- [ ] Paid News RSS Feeds
	- [ ] Consolidated List of RSS Feeds with Detailed Information
	- [ ] Category-based / Country-based / Sector-based APIs
		- [ ] Social Media APIs
		- [ ] Open APIs
		- [ ] 3rd Party APIs
	- [ ] Consolidated List of APIs with Detailed Information
	- [ ] Data Sources Gathering Status Report with Above Consolidated Lists
- [ ] Data Sources Modelling
	- [ ] Modelling RSS Feeds Data Sources & Types
	- [ ] Updated Data Modelling Information in the Consolidated RSS Feeds List
	- [ ] Modelling API Data Sources & Types
	- [ ] Updated Data Modelling Information in the Consolidated APIs List
- [ ] Plan Clear Business & Financial Models
	- [ ] Update the Application Documentation (for Future References & Monetization)
	- [ ] Planning Financial Models 
- [ ] Application UI & UX Wireframe
	- [ ] Building Application UI/UX Based on Business & Financial Models
	- [ ] Rough Wireframes of Application UI/UX
- [ ] Developing & Deploying Back-end Engine
	- [ ] Developing RSS Feed Back-end Engine
	- [ ] Deploying & Scheduling RSS Feed Back-end Engine
	- [ ] Developing API Services Back-end Engine
	- [ ] Deploying & Scheduling API Services Back-end Engine
	- [ ] Testing Information Output
- [ ] Develop Front-end
	- [ ] Identify Technology & Build Front-End
- [ ] Integrating Back-end with Front-end
- [ ] Unit Testing Application
- [ ] Automated Basic Security Testing
- [ ] Launch v0.1 on PlayStore
- [ ] Build App Website - Integrated to Beyond Beacon Corporation Website (Products & Services)
- [ ] Google AdSense
- [ ] Affiliations & Other Marketing-Financial Models Implementations

> Note: Get RSS Feeds From Previous Sources List & Feedspot

### Directory Structure

├── ConsolidatedRSS-RawFeedsList.txt
├── CoreFunction
│   ├── DoubleEnhancedRSS.py
│   ├── EnhancedRSSAggregator.py
│   ├── FeedDataStructure.py
│   ├── NLP-Module.py
│   └── RSSAggregator.py
├── DataSources
│   ├── Country-Specific
│   │   ├── RSSFEED_CHINA_GENERALSOURCE.txt
│   │   ├── RSSFEED_GENERALNEWS_SOURCE.txt
│   │   ├── RSSFEED_GLOBAL_GENERALSOURCE.txt
│   │   ├── RSSFEED_INDIA_GENERALSOURCE.txt
│   │   ├── RSSFEED_PAKISTAN_GENERALSOURCE.txt
│   │   └── RSSFEED_SRILANKA_GENERALSOURCE.txt
│   ├── Raw-Collections
│   │   ├── 2016-US-RSSFeeds.pdf
│   │   ├── RSS-FEED-ISSUES-LIST.txt
│   │   ├── RSSFEED-SOURCE.txt
│   │   └── RSSFEED_TEMPSOURCE.txt
│   ├── RSSFEED_LOGFILES
│   │   ├── Articles.json
│   │   ├── COUNTRY-India-0.txt
│   │   ├── COUNTRY-India-1.txt
│   │   ├── COUNTRY-India-2.txt
│   │   ├── COUNTRY-India-3.txt
│   │   ├── FEED0.txt
│   │   ├── FEED1.txt
│   │   ├── FEED2.txt
│   │   ├── General-AllNews.json
│   │   ├── Global-AllNews.json
│   │   ├── India-0.json
│   │   ├── India-1.json
│   │   ├── India-2.json
│   │   ├── India-3.json
│   │   ├── India-AllNews.json
│   │   ├── SECTOR-Technology-0.txt
│   │   ├── SECTOR-Technology-1.txt
│   │   ├── SECTOR-Technology-2.txt
│   │   ├── Technology-0.json
│   │   ├── Technology-1.json
│   │   ├── Technology-2.json
│   │   └── Technology-AllNews.json
│   └── Sector-Specific
│       ├── RSSFEED_ENTERTAINMENT_SPORTS_GENERALSOURCE.txt
│       ├── RSSFEED_GOVERNMENT_POLITICS_GENERALSOURCE.txt
│       ├── RSSFEED_MILITARY_GENERALSOURCE.txt
│       └── RSSFEED_TECHNOLOGY_GENERALSOURCE.txt
├── README.md
├── RSSFeeds-Sources
│   ├── Category
│   │   ├── Crime
│   │   │   └── RSSFeedsList.txt
│   │   ├── Entertainment
│   │   │   └── RSSFeedsList.txt
│   │   ├── Lifestyle
│   │   │   ├── RSSFeeds-Errors
│   │   │   │   └── Error_FEED1.txt
│   │   │   ├── RSSFeeds-JSON
│   │   │   │   └── Consolidated_RSSFeed.json
│   │   │   ├── RSSFeedsList.txt
│   │   │   └── RSSFeeds-Logs
│   │   │       └── FEED1.txt
│   │   ├── Military
│   │   ├── Politics
│   │   ├── Sports
│   │   └── Technology
│   │       ├── RSSFeeds-ErrorLogs.txt
│   │       ├── RSSFeedsList.txt
│   │       ├── RSSFeeds-Logs
│   │       │   └── FEED1.txt
│   │       └── RSSFeed-Technology.json
│   ├── Country
│   │   ├── Global
│   │   │   └── RSSFeedsList.txt
│   │   ├── India
│   │   │   ├── RSSFeeds-Errors
│   │   │   │   └── Error_FEED1.txt
│   │   │   ├── RSSFeeds-JSON
│   │   │   │   └── Consolidated_RSSFeed.json
│   │   │   ├── RSSFeedsList.txt
│   │   │   └── RSSFeeds-Logs
│   │   ├── Pakistan
│   │   │   └── RSSFeedsList.txt
│   │   ├── US
│   │   └── USA
│   └── Sector
│       ├── Defense
│       ├── Energy
│       │   └── RSSFeedsList.txt
│       ├── Financial
│       │   ├── RSSFeeds-Errors
│       │   │   └── Error_FEED1.txt
│       │   ├── RSSFeeds-JSON
│       │   │   └── Consolidated_RSSFeed.json
│       │   ├── RSSFeedsList.txt
│       │   └── RSSFeeds-Logs
│       ├── Manufacture
│       ├── Medical
│       ├── Political
│       ├── Retail
│       ├── Space
│       │   └── RSSFeedsList.txt
│       └── Sports
│           └── RSSFeedsList.txt
├── SamplePro-1.py
├── SamplePro-2.py
└── SamplePro-3.py
