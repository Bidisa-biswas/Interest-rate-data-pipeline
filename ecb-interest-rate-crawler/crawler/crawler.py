def crawl_decision_links(page, base_url, max_pages=2):
    page.goto(base_url)
    decision_links = []

    for _ in range(max_pages):
        page.wait_for_load_state("networkidle")

        links = page.locator("a[href*='pressconf']")
        for i in range(links.count()):
            href = links.nth(i).get_attribute("href")
            if href and "pressconf" in href:
                full_url = "https://www.ecb.europa.eu" + href
                decision_links.append(full_url)

        next_button = page.locator("text=Older")
        if next_button.count() == 0:
            break

        next_button.click()

    return list(set(decision_links))
