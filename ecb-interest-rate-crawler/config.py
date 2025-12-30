"""
Configuration for ECB Interest Rate Crawler
"""

# Target URL for ECB press conferences
BASE_URL = "https://www.ecb.europa.eu/press/pressconf/html/index.en.html"

# Output file for results
OUTPUT_FILE = "ecb_interest_rates.csv"

# Maximum number of pages to crawl in the press conference index
MAX_PAGES = 5
# Limit on number of decision pages to scrape (for demo/testing purposes)
SCRAPE_LIMIT = 10
# Timeout for page loads in seconds
PAGE_LOAD_TIMEOUT = 30
