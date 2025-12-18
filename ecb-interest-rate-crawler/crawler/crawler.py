def crawl_decision_links(page, base_url, max_pages=2):
    """Crawl the ECB press conference index for links to decision pages.

    Args:
        page: Playwright page object (sync API).
        base_url (str): URL of the listing page to start from.
        max_pages (int): maximum number of index pages to paginate through.

    Returns:
        list[str]: deduplicated list of full URLs to press conference pages.
    """
    page.goto(base_url)
    decision_links = []

    for _ in range(max_pages):
        page.wait_for_load_state("networkidle")

        links = page.locator("a[href*='pressconf']")
        # Use count() then iterate indices; count() on locator is synchronous in sync API
        for i in range(links.count()):
            href = links.nth(i).get_attribute("href")
            if href and "pressconf" in href:
                if href.startswith("http"):
                    full_url = href
                else:
                    full_url = "https://www.ecb.europa.eu" + href
                decision_links.append(full_url)

        next_button = page.locator("text=Older")
        if next_button.count() == 0:
            break

        # Click and continue to next page of results
        next_button.first.click()

    # return deterministic order by sorting the set
    return sorted(set(decision_links))
