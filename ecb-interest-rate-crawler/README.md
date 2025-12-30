##ECB Interest Rate Crawler
A Python web scraping tool that extracts historical interest rate decisions from European Central Bank press releases using Playwright and BeautifulSoup.

Overview
This is a small project demonstrating practical web crawling and data extraction skills by automating the collection of interest rate information from ECB monetary policy announcements. While the ECB provides structured datasets, this implementation focuses on parsing press releases to simulate real-world data extraction scenarios commonly encountered in financial analysis.

Prerequisites
Python 3.8 or higher

pip package manager

Installation
Clone the repository:

bash
git clone https://github.com/yourusername/ecb-interest-rate-crawler.git
cd ecb-interest-rate-crawler

Install Python dependencies:

bash
pip install -r requirements.txt
Install Playwright browser:

bash
playwright install chromium
Usage
Run the crawler:

bash
python main.py

The script will:

Navigate to ECB press conference pages

Extract interest rate information

Clean and structure the data

Save results to ecb_interest_rates.csv

📁 Project Structure
text
ecb-interest-rate-crawler/
├── README.md                 # This documentation
├── requirements.txt          # Python dependencies
├── config.py                # Configuration settings
├── main.py                  # Main orchestration script
└── crawler/                 # Modular components
    ├── __init__.py
    ├── browser.py           # Browser initialization
    ├── crawler.py           # Page navigation and link discovery
    ├── scraper.py           # Data extraction logic
    └── pipeline.py          # Data processing and CSV export
🔧 Technical Details
Technologies Used
Python 3 - Core programming language

Playwright - Modern browser automation for reliable web crawling

BeautifulSoup4 - HTML parsing and data extraction

Pandas - Data manipulation and CSV export

Key Features
Modular Design: Separated concerns for maintainability (browser, crawler, scraper, pipeline)

Error Handling: Graceful failure handling with comprehensive logging

Configurable: Easy adjustment of settings via config.py

Respectful Crawling: Built-in delays and proper browser cleanup

📊 Output Format
The crawler generates a CSV file with structured interest rate data:

Column	Description	Example
date	Announcement date	2024-12-12
main_refinancing_rate	ECB main refinancing rate	4.50
deposit_facility_rate	Deposit facility rate	4.00
url	Source press release URL	https://www.ecb.europa.eu/...
extracted_at	Timestamp of data extraction	2024-12-30T14:30:00
🎯 Project Purpose
This implementation serves as a practical demonstration of:

Web scraping and browser automation

Data extraction from real-world financial sources

Building maintainable data pipelines

Working with financial data formats

Note: The European Central Bank provides official structured data through its Statistical Data Warehouse. This project uses press releases for educational purposes to demonstrate web crawling techniques.

🔄 Extending the Project
Potential enhancements include:

Adding support for other central banks (Federal Reserve, Bank of England)

Implementing a simple web dashboard for visualization

Adding database storage for historical tracking

Creating automated email reports of rate changes

📝 License
This project is provided for educational and portfolio purposes.

