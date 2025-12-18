# Example improved function (illustrative)
import re
from bs4 import BeautifulSoup

# Accept "123", "123.45", ".45", "123,45" and allow optional space before %
RATE_PATTERN = re.compile(r"((?:\d+|\.\d+)(?:[.,]\d+)?)\s*%")

def scrape_decision_improved(html):
    soup = BeautifulSoup(html, "html.parser")
    # remove script and style to avoid false positives
    for t in soup(["script", "style", "noscript"]):
        t.decompose()
    text = soup.get_text(separator="\n", strip=True)
    matches = []
    for m in RATE_PATTERN.finditer(text):
        raw_num = m.group(1)
        # normalize comma decimal to dot
        norm = raw_num.replace(",", ".")
        try:
            value = float(norm)
        except ValueError:
            continue
        # context snippet
        start, end = max(0, m.start()-30), min(len(text), m.end()+30)
        context = text[start:end]
        matches.append({"raw": raw_num, "value": value, "context": context})
    return {"rates_found": matches, "raw_text_sample": text[:500]}