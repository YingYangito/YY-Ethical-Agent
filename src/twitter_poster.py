import time
import os
import pickle
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

COOKIES_FILE = "twitter_cookies.pkl"
TWITTER_URL = "https://twitter.com"

def start_browser(headless=False):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    return driver

def save_cookies(driver):
    with open(COOKIES_FILE, "wb") as f:
        pickle.dump(driver.get_cookies(), f)

def load_cookies(driver):
    if not os.path.exists(COOKIES_FILE):
        return False
    with open(COOKIES_FILE, "rb") as f:
        cookies = pickle.load(f)
    driver.get(TWITTER_URL)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    return True

def post_to_twitter(text):
    driver = start_browser()

    if not load_cookies(driver):
        print("🔐 Please log in to Twitter manually.")
        driver.get("https://twitter.com/login")
        input("✅ Press ENTER after you’ve logged in successfully...")
        save_cookies(driver)
        print("✅ Cookies saved. You won't need to log in next time.")

    try:
        driver.get("https://twitter.com/compose/tweet")
        time.sleep(5)

        tweet_box = driver.find_element(By.XPATH, "//div[@data-testid='tweetTextarea_0']")
        tweet_box.click()

        # ✅ Strip outer quotes and paste emoji-safe content
        cleaned = text.strip().strip('"')
        pyperclip.copy(cleaned)

        ActionChains(driver)\
            .key_down(Keys.CONTROL)\
            .send_keys("v")\
            .key_up(Keys.CONTROL)\
            .perform()

        time.sleep(1)

        # ✅ Post using keyboard shortcut
        ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.RETURN).key_up(Keys.CONTROL).perform()
        print("✅ Tweet posted successfully via paste.")

    except Exception as e:
        print("❌ Failed to post tweet:", e)

    finally:
        time.sleep(5)
        try:
            driver.quit()
        except Exception:
            pass
