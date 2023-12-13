You can use fomb.py to scrape the FOMB site for Google Drive links.
It requires Firefox, the Firefox WebDriver, and Selenium. 
 
already_seen.txt keeps track of ALL of the links it has seen since we have scraped the site. 

new.txt keeps track of new links (links that haven't been seen before)
 
You will want to delete new.txt after you've downloaded the documents in there, so that a new
new.txt gets generated the next time the Scraper runs. 

After scraping the FOMB site for links, you will want to use the Google Drive API Script:
https://github.com/duckduckgrayduck/google-drive-api-script

To download the documents from those links.
