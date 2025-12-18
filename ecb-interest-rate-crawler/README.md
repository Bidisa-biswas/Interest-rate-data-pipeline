## ECB Interest Rate Change Crawler

This project demonstrates browser-based web crawling and data extraction using Playwright.

## Why Playwright?
ECB press releases are rendered dynamically and contain semi-structured text. Playwright allows reliable JavaScript execution and page interaction.

## Pipeline Overview
1. Crawl ECB monetary policy decision pages
2. Extract interest rate information from announcements
3. Clean and normalize data
4. Store results in CSV format

## How to Run
pip install -r requirements.txt  
playwright install  
python main.py

## Scalability Considerations
For production-scale crawling, this pipeline could be extended with async Playwright, retry logic, proxy rotation, and structured NLP extraction.
