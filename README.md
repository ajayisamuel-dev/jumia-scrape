Jumia iPhone Price Tracker (Project README)
Overview
An automated web scraping solution built with Python and Selenium to track iPhone pricing and availability on Jumia.com.ng. This tool handles dynamic content, bypasses promotional overlays, and exports structured data for market analysis.

Key Features.
Anti-Bot Bypass: Utilizes undetected-chromedriver to navigate seamlessly without triggering security blocks.
Dynamic UI Handling: Custom logic to detect and close newsletter popups and cookie banners using JavaScript injection.
Smart Pagination: Automatically crawls through multiple search result pages.
Data Integrity: Implements parallel iteration (zip) to ensure product names perfectly match their corresponding prices.
Export Ready: Automatically generates a timestamped .csv file for easy import into Excel or Google Sheets.

Technical Stack
Language: Python 3.13

Automation: Selenium / Undetected-Chromedriver

Data Handling: CSV / List Comprehension

Advanced Techniques: ActionChains (for hovering), Explicit Waits, and JavaScript Execution.

Installation & Usage
Clone the repository:

Bash
git clone https://github.com/yourusername/jumia-scraper.git
Install dependencies:

Bash
pip install -r requirements.txt
Run the scraper:

Bash
python main.py

Implementation Details (The "Pro" Stuff)
Handling Intercepted Clicks: Developed a "Nuke" strategy to remove DOM elements (like cookie banners) that physically block the automation path.
Robust Selectors: Used a mix of XPath and CSS Selectors to target elements that lack unique IDs.
Error Handling: Built-in try-except-finally blocks to ensure the browser closes properly, preventing memory leaks and orphaned driver handles.
