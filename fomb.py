from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

start_time = time.time() 

def grab_links(browser):
    links = []
    rows = browser.find_elements(By.CSS_SELECTOR, "#docuDataTable tbody tr")
    for row in rows:
        link_element = row.find_element(By.TAG_NAME, 'a')
        href_value = link_element.get_attribute('href')
        links.append(href_value)
    return links

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        return set()

def write_to_file(file_path, data):
    with open(file_path, 'a') as file:
        for item in data:
            file.write(item + '\n')

# Start the webdriver
browser = webdriver.Firefox()
browser.get('https://juntasupervision.pr.gov/documents/')

try:
    # Set display to 100 rows per page
    dropdown = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#docuDataTable_length > label:nth-child(1) > select:nth-child(1)"))
    )
    dropdown.click()

    option_100 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#docuDataTable_length > label:nth-child(1) > select:nth-child(1) > option:nth-child(4)"))
    )
    option_100.click()

    already_seen = read_file("already_seen.txt")
    new_links = set()

    # Get the last pagination link's text to determine the final page
    last_page_element = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.paginate_button:nth-child(7)"))
    )
    last_page = int(last_page_element.text) if last_page_element.text else 1

    # Loop through pages
    for _ in range(1, last_page + 1):
        links_on_page = grab_links(browser)
        print(links_on_page)
        new_links.update(set(links_on_page) - already_seen)

        try:
            next_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#docuDataTable_next"))
            )
            next_button.click()
            time.sleep(2)  # Adding a delay for the page to load
        except Exception as e:
            print(f"Error clicking next button: {str(e)}")
            break

    # Save new links to a file named "new.txt"
    write_to_file("new.txt", new_links)

    # Update already_seen.txt with new links
    write_to_file("already_seen.txt", new_links)

    print(f"Total new links collected: {len(new_links)}")
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total execution time: {total_time} seconds")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser
    browser.quit()
