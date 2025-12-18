##ECB INTEREST RATE CHANGE CRAWLER
This is a small project demonstrating browser-based web crawling and data extraction using Playwright and beautifulsoup.

##DATA SOURCE NOTE
ECB interest rates are officially available via structured datasets.
This project intentionally uses press releases to demonstrate
browser-based crawling and scraping of real-world announcements.

##PIPELINE OVERVIEW
1. Crawl ECB monetary policy decision pages
2. Extract interest rate information from announcements
3. Clean and normalize data
4. Store results in CSV format --(df.to_csv)

##TESTING PURPOSE, USE UNITTEST OR PYTEST LIBRARIES

##RUN REQUIREMENTS
pip install -r requirements.txt  
playwright install  
python main.py



