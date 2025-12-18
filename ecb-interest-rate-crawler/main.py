from crawler.browser import get_page
from crawler.crawler import crawl_decision_links
from crawler.scraper import scrape_decision_improved
from crawler.pipeline import process_and_save

BASE_URL = "https://www.ecb.europa.eu/press/pressconf/html/index.en.html"

def main(limit=5):
    playwright, browser, page = get_page()

    try:
        print("Crawling decision links...")
        links = crawl_decision_links(page, BASE_URL)

        print(f"Found {len(links)} decision pages")

        records = []

        for url in links[:limit]:  # limit for demo purposes
            try:
                page.goto(url)
                page.wait_for_load_state("networkidle")
                html = page.content()

                data = scrape_decision_improved(html)
                data["url"] = url
                records.append(data)
            except Exception as e:
                print(f"Error scraping {url}: {e}")
                continue

        process_and_save(records)
    finally:
        try:
            browser.close()
        except Exception:
            pass
        try:
            playwright.stop()
        except Exception:
            pass


if __name__ == "__main__":
    main()
