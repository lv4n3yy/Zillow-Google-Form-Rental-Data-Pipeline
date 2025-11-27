# Zillow Rental Scraper & Google Form Filler

A Python automation script that scrapes rental listings from Zillow for San Francisco and automatically submits each listing’s address, price, and URL into a Google Form, creating a structured dataset (for example in Google Sheets) without manual copy‑paste.

## Features

- Sends an HTTP request to a Zillow search results page and parses the HTML with BeautifulSoup.
- Extracts listing titles/addresses, prices, and detail page URLs.
- Normalizes relative URLs to full `https://www.zillow.com/...` links.
- Uses Selenium WebDriver (Chrome) to open a Google Form and submit one response per listing.

## Requirements

- Python 3.10+
- Google Chrome browser
- ChromeDriver (installed automatically via `webdriver_manager`)
- A Google Form with three input fields: address/title, price, and URL.
- A `.env` file with:
  - `USER_AGENT` – browser User‑Agent string
  - `ACCEPT_LANGUAGE` (optional) – e.g. `ru,en-US;q=0.9,en;q=0.8,de;q=0.7`
  - `GOOGLE_URL` – the public “respond” URL of your Google Form

## Installation


Create `.env` in the project root:


Ensure `.env` is listed in `.gitignore` so it is not committed.

## Usage


The script will:

1. Request the Zillow search URL with the configured headers.
2. Parse the response with BeautifulSoup and collect:
   - `titles` – listing titles/addresses
   - `prices` – monthly rent values
   - `ads` – listing URLs
3. Open your Google Form in a Chrome window.
4. For each listing, fill in the three fields (address, price, URL) and submit the form.

You can adjust XPaths in the script if the Google Form structure changes.

## Notes

- Respect Zillow’s Terms of Service and robots.txt when scraping.
- Heavy scraping against production sites can trigger anti‑bot protections; this script is intended for small, educational experiments.
