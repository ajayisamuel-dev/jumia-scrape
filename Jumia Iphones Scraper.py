import undetected_chromedriver as UC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains as AC
import time

driver_path = r"C:\Program Files (x86)\chromedriver.exe"
service = Service(executable_path=driver_path)
driver = UC.Chrome(service=service)

#for future waits
wait=WebDriverWait(driver, 5)
#for ActionChains
action=AC(driver)


def avail_phones():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "name")))
    #Get the names of phones available on the active page
    available_phones = driver.find_elements(By.CLASS_NAME, "name")
    iphones = [phone.text for phone in available_phones]

    #Get the prices
    prices_elements = driver.find_elements(By.CLASS_NAME, "prc")
    prices = [price.text for price in prices_elements]

    #Pair them together using zip()
    #This ensures Phone A matches Price A
    for ph, p in zip(iphones, prices):
        print(f"{ph} is being sold at {p}")

def next():
    for n in range(2,10):
        next_page_btn=driver.find_element(By.CSS_SELECTOR, f"a[aria-label='Next Page']")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_page_btn)
        action.click(next_page_btn).perform()
        print("Next Page ... ")

def scrape():
    #try loading Jumia.com.ng, prints "An error occurred" if not successful
    try:
        driver.get("https://jumia.com.ng")

        def close_popup(driver):
            try:
            # Waiting for popup
                popup_wait = WebDriverWait(driver, 3)
            # tried svg tag_name, "use", twas uninteractable so changed to parent class_name, "cls"
                close_btn = popup_wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cls")))
                close_btn.click()
                print("Newsletter PopUp Closed...")
            except TimeoutException:
                print("No popup found, proceeding...")
        
        close_popup(driver)

        #Accept Cookies
        #cookies_btn=driver.find_element(By.CSS_SELECTOR, ".btn._prim.-df.-mla").click()
        driver.execute_script("""
            var el = document.querySelector('article.banner-pop');
            if (el) el.remove();
            document.body.style.overflow = 'auto';
        """)
        print("Cookies handled.")

        #to hover on phones and tablets text
        popup=wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Phones & Tablets")))
        action.move_to_element(popup).perform()
        print("Iphones Tab Opened...")

        #wait 1s then click iphones
        time.sleep(1)
        iphones_btn=driver.find_element(By.LINK_TEXT, "iPhones").click()
        print("Iphones Store Opened...")

        for page_num in range(1, 4): # Scraping first 3 pages as an example
            time.sleep(2) # Wait for page transition
            avail_phones()

            try:
                # Find the 'Next' button
                next_btn = driver.find_element(By.CSS_SELECTOR, "a[aria-label='Next Page']")
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_btn)
                time.sleep(1)
                driver.execute_script("arguments[0].click();", next_btn)
                print(f"Moving to page {page_num + 1}...")
            except NoSuchElementException:
                print("No more pages available.")
                break

        print("Scraping Task Complete.")

        time.sleep(30)
        driver.quit()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    scrape()