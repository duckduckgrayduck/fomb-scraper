You can use fomb.py to scrape the FOMB site for Google Drive links.
It requires [Firefox](https://www.mozilla.org/en-US/firefox/new/), the [Firefox WebDriver](https://github.com/mozilla/geckodriver/releases), and [Selenium](https://selenium-python.readthedocs.io/installation.html). 
 
already_seen.txt keeps track of ALL of the links it has seen since we have scraped the site. 

new.txt keeps track of new links (links that haven't been seen before)
 
You will want to delete new.txt after you've downloaded the documents in there, so that a new
new.txt gets generated the next time the Scraper runs. 

After scraping the FOMB site for links, you will want to use this [Google Drive API Script](https://github.com/duckduckgrayduck/google-drive-api-script) to download the documents from new.txt.

Or, if there are only a handful of new links, you can download them manually. 
