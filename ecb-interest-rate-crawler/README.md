## ECB Interest Rate Change Crawler
This is a small project demonstrating browser-based web crawling and data extraction using Playwright and beautifulsoup.

## Data Source Note
ECB interest rates are officially available via structured datasets.
This project intentionally uses press releases to demonstrate
browser-based crawling and scraping of real-world announcements.

## Pipeline Overview
1. Crawl ECB monetary policy decision pages
2. Extract interest rate information from announcements
3. Clean and normalize data
4. Store results in CSV format

## Testing 
For a production-grade system, this project could be extended with
unit tests using `pytest` or `unittest` to validate scraping and data
processing logic. Testing was kept minimal to maintain focus on the
crawling and pipeline design.

## How to Run
pip install -r requirements.txt  
playwright install 
python main.py

