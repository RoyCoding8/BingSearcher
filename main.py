import os, random, time, traceback

try:
    import requests
except ImportError:
    print('Requirements not found, installing requirements...')
    os.system('pip install -r requirements.txt')
    import requests

from selenium                           import webdriver
from selenium.webdriver.common.by       import By
from selenium.webdriver.support.ui      import WebDriverWait
from selenium.webdriver.support         import expected_conditions as EC
from selenium.webdriver.chrome.service  import Service
from selenium.webdriver.common.keys     import Keys
from random_words                       import RandomWords
from dotenv import load_dotenv

load_dotenv()
# --------------------- Variables -------------------------
LOGIN = os.getenv('LOGIN')
ACCOUNTS = LOGIN.replace(" ", "").split(",")
TERMS = ["define ", "explain ", "example of ", "how to pronounce ", "what is ", "what is the ", "what is the definition of ","what is the example of ", "what is the pronunciation of ", "what is the synonym of ","what is the antonym of ", "what is the hypernym of ", "what is the meronym of ", "photos of ", "images of ", "pictures of ", "pictures of ", "pictures of ", "pictures of ", "pictures of ", "pictures of ", "information about ", "information on ", "information about the ", "information on the ", "information about the ", "synonym of ", "antonym of ", "hypernym of ", "meronym of ", "synonym for ", "antonym for ", "hypernym for ", "meronym for ", "pronunciation of ", "pronounce ", "how to pronounce ", "how to say ", "how to say the ", "interesting facts about ", "interesting facts on ", "interesting facts about the ", "interesting facts on the "]
BROWSER = os.getenv('BROWSER').lower()
BROWSER_PATH = os.getenv('BROWSER_PATH')
DRIVER_PATH = os.getenv('DRIVER_PATH')
CUR = os.getenv('CUR').lower()

if CUR == 'inr':
    CURRENCY = 15.68
    CUR_SYMBOL = "₹"
elif CUR == 'gbp':
    CURRENCY = 1520
    CUR_SYMBOL = "£"
else:
    CURRENCY = 1310
    CUR_SYMBOL = "$"

POINTS_PER_SEARCH = os.getenv('POINTS_PER_SEARCH')
START = time.time()
# ----------------------------------------------------------
xpaths = [
        '//*[@id="balanceToolTipDiv"]/p/mee-rewards-counter-animation/span',
        '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/mee-rewards-user-status-banner/div/div/div/div/div[2]/div[1]/mee-rewards-user-status-banner-item/mee-rewards-user-status-banner-balance/div/div/div/div/div/div/p/mee-rewards-counter-animation/span',
        '//*[@id="rewardsBanner"]/div/div/div[2]/div[1]/mee-rewards-user-status-banner-item/mee-rewards-user-status-banner-balance/div/div/div/div/div/p/mee-rewards-counter-animation/span',
        '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/mee-rewards-user-status-banner/div/div/div/div/div[2]/div[1]/mee-rewards-user-status-banner-item/mee-rewards-user-status-banner-balance/div/div/div/div/div/p/mee-rewards-counter-animation/span',
        '//*[@id="rewardsBanner"]/div/div/div[3]/div[1]/mee-rewards-user-status-item/mee-rewards-user-status-balance/div/div/div/div/div/p[1]/mee-rewards-counter-animation/span',
        '//*[@id="rewardsBanner"]/div/div/div[2]/div[2]/span',
    ]
# ------------------------------------------------------------

if len(ACCOUNTS) > 6:
    print('Using more than 6 accounts per IP is not allowed. I won\'t stop your dangerous adventure though, unless you do it yourself :)')

def get_current_ip(type, proxies=None):
    try:
        return ((requests.get(f"https://ip{type}.icanhazip.com", proxies=proxies)).text).strip("\n")
    except requests.ConnectionError:
        print(f"Network problem dummy!")
    except Exception as e:
        print(f"An exception occurred while trying to get your current IP address: {e}")
        time.sleep(60)
        raise Exception

def check_ip_address():
    current_ipv4 = get_current_ip("v4")
    print(f"Current IPv4 Address: {current_ipv4}")
    current_ipv6 = get_current_ip("v6")
    if current_ipv6:
        print(f"Current IPv6 Address: {current_ipv6}")
    print()

def get_driver(isMobile=False):
    if BROWSER in ['chrome', 'brave']:
        options = webdriver.ChromeOptions()
        options.binary_location = BROWSER_PATH
        service = Service(DRIVER_PATH)
    elif BROWSER == 'edge':
        options = webdriver.EdgeOptions()
        options.binary_location = BROWSER_PATH
        service = Service(DRIVER_PATH)
    else:
        options = webdriver.ChromeOptions()
        service = None
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-blink-features=AutomationControlled")
    if isMobile:
        mobile_emulation = {"deviceName": "Nexus 5"}
        options.add_experimental_option("mobileEmulation", mobile_emulation)
    if BROWSER in ['chrome', 'brave', '']:
        driver = webdriver.Chrome(options=options,service=service)
    elif BROWSER == 'edge':
        driver = webdriver.Edge(options=options,service=service)
    driver.maximize_window()
    return driver

def login(EMAIL, PASSWORD, driver):
    try:
        driver.find_element(By.XPATH, value='//*[@id="i0116"]').send_keys(EMAIL)
        driver.find_element(By.XPATH, value='//*[@id="i0116"]').send_keys(Keys.ENTER)
    except:
        try:
            username_field = driver.find_element(By.XPATH, value='//*[@id="i0116"]')
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(username_field)
            )
            username_field.send_keys(EMAIL)
            username_field.send_keys(Keys.ENTER)
        except:
            return False

    time.sleep(random.uniform(2, 4))

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Other ways to sign in")]')))
        other_ways_button = driver.find_element(By.XPATH, '//*[contains(text(), "Other ways to sign in")]')
        other_ways_button.click()
        time.sleep(random.uniform(2,5))
        
        password_option = driver.find_element(By.XPATH, '//*[contains(text(), "Use my password")]')
        password_option.click()

    except:
        print("No verification code prompt found,moving on...")
    time.sleep(random.uniform(3, 4))

    try:
        driver.find_element(By.XPATH, value='//*[@id="i0118"]').send_keys(PASSWORD)
        driver.find_element(By.XPATH, value='//*[@id="i0118"]').send_keys(Keys.ENTER)
    except:
        try:
            password_field = driver.find_element(By.XPATH, value='//*[@id="i0118"]')
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(password_field)
            )
            password_field.send_keys(PASSWORD)
            password_field.send_keys(Keys.ENTER)
        except:
            print(f'Unable to find password field for account {EMAIL}. Skipping...')
            return False

    time.sleep(random.uniform(3, 4))
    driver.get('https://rewards.bing.com/')
    return True


def get_points(EMAIL, PASSWORD, driver,isMobile=False):
    points = -1
    driver.implicitly_wait(5)
    time.sleep(random.uniform(3,5))
    if not isMobile:
        try:
            driver.get('https://rewards.bing.com/Signin?idru=%2F')
            if not login(EMAIL, PASSWORD, driver):
                return -404
        except Exception as e:
            driver.get('https://rewards.bing.com/')
            print(e)
        finally:
            time.sleep(random.uniform(3,8))
    else:
        try:
            driver.get('https://rewards.bing.com/pointsbreakdown')
        except Exception as e:
            driver.get('https://rewards.bing.com/')
            print(e)
        finally:
            time.sleep(random.uniform(3,8))
    for xpath in xpaths:
        try:
            element = driver.find_element(By.XPATH, xpath)
            points = element.text.strip().replace(',', '')
            return int(points)
        except:
            pass
    return -1

def pc_search(driver, EMAIL, PC_SEARCHES):
    rw = RandomWords()
    start =time.time()
    driver.get('https://www.bing.com/fd/auth/signin?action=interactive&provider=windows_live_id&return_url=https%3a%2f%2fwww.bing.com%2f%3fwlexpsignin%3d1&src=EXPLICIT&sig=35B73A5D1FC06A7726F02EB01E026B15')
    time.sleep(random.uniform(1, 6))
    for x in range(1,PC_SEARCHES+1):
        time.sleep(random.uniform(5.87,8.34))
        random_word = rw.random_word()
        search_url = f'https://www.bing.com/search?form=QBRE&q={random.choice(TERMS)+random_word}'
        driver.get(search_url)
        time.sleep(random.uniform(5, 10))
        progress = int((x / PC_SEARCHES) * 100)
        bar_length = 50
        num_equals = progress * bar_length // 100
        num_spaces = bar_length - num_equals
        print(f"\r\t[{'=' * num_equals}{' ' * num_spaces}] {progress}%", end='')

    print(f'\n\t{EMAIL} PC Searches completed. Time taken: {time.time()-start:2f}s\n')

def mobile_search(driver, EMAIL, MOBILE_SEARCHES):
    rw = RandomWords()
    start =time.time()
    driver.get('https://www.bing.com/fd/auth/signin?action=interactive&provider=windows_live_id&return_url=https%3a%2f%2fwww.bing.com%2f%3fwlexpsignin%3d1&src=EXPLICIT&sig=35B73A5D1FC06A7726F02EB01E026B15')
    for x in range(1,MOBILE_SEARCHES+1):
        time.sleep(random.uniform(5.87,8.34))
        random_word = rw.random_word()
        search_url = f'https://www.bing.com/search?form=QBRE&q={random.choice(TERMS)+random_word}'
        driver.get(search_url)
        time.sleep(random.uniform(5, 10))
        progress = int((x / MOBILE_SEARCHES) * 100)
        bar_length = 50
        num_equals = progress * bar_length // 100
        num_spaces = bar_length - num_equals
        print(f"\r\t[{'=' * num_equals}{' ' * num_spaces}] {progress}%", end='')
    
    print(f'\n\t{EMAIL} Mobile Searches completed: Time taken: {time.time()-start:2f}s\n')

def update_searches(driver):
    driver.get('https://rewards.bing.com/pointsbreakdown')
    PC_SEARCHES = 30
    try:
        time.sleep(10)
        PC = driver.find_element(By.XPATH, value='//*[@id="userPointsBreakdown"]/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]').text.replace(" ", "").split("/")
        if (int(PC[0]) < int(PC[1])):
            PC_SEARCHES = int((int(PC[1]) - int(PC[0])) / POINTS_PER_SEARCH)
            print(f'\tPC Searches Left:\t{PC_SEARCHES}')
        else:
            PC_SEARCHES = 0
            print(f'\tPC Searches Completed:\t{PC[0]}/{PC[1]}')
        if (int(PC[1]) > 50):
            MOBILE = driver.find_element(By.XPATH, value='//*[@id="userPointsBreakdown"]/div/div[2]/div/div[2]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]').text.replace(" ", "").split("/")
            if (int(MOBILE[0]) < int(MOBILE[1])):
                MOBILE_SEARCHES = int((int(MOBILE[1]) - int(MOBILE[0])) / POINTS_PER_SEARCH)
                print(f'\tMobile Searches Left:\t{MOBILE_SEARCHES}')
            else:
                MOBILE_SEARCHES = 0
                print(f'\tMobile Searches Completed:\t{MOBILE[0]}/{MOBILE[1]}')
        else:
            MOBILE_SEARCHES = 0
        try:
            driver.find_element(By.XPATH, '//*[@id="modal-host"]/div[2]/button').click()
        except:
            driver.get('https://rewards.bing.com/')
    except:
        driver.get('https://rewards.bing.com/')
        print("Error fetching points breakdown.")
        pass
    finally:
        print()
        return PC_SEARCHES, MOBILE_SEARCHES
    
def start_rewards():
    ranRewards = False
    print(f'\nStarting Automation:\n')
    for x in ACCOUNTS:
        driver = get_driver()
        colonIndex = x.index(":")
        EMAIL = x[0:colonIndex]
        PASSWORD = x[colonIndex+1:len(x)]
        PC_SEARCHES = 30
        MOBILE_SEARCHES = 20
        points,points_new=-1,-1
        try:
            points = get_points(EMAIL, PASSWORD, driver)
        except:
            driver.quit()
            continue
        if (points == -404):
            driver.quit()
            continue
        print(f'Email:\t{EMAIL}\n\tPoints:\t{points}\n\tCash Value:\t{CUR_SYMBOL}{round(points/CURRENCY,3)}\n')
        try:
            PC_SEARCHES,MOBILE_SEARCHES = update_searches(driver)
        except:
            print(traceback.format_exc())
            driver.quit()
            driver = get_driver()
        if (PC_SEARCHES > 0 or MOBILE_SEARCHES > 0):
            try:
                ranRewards = True
                pc_search(driver, EMAIL, PC_SEARCHES)

            except Exception as e:
                print(e,traceback.format_exc())
            finally:
                driver.quit()
            if MOBILE_SEARCHES:
                try:
                    driver = get_driver(True)
                    time.sleep(3)
                    driver.get('https://rewards.bing.com/Signin?idru=%2F')
                    time.sleep(random.uniform(3,5))
                    login(EMAIL,PASSWORD,driver)
                    mobile_search(driver,EMAIL,MOBILE_SEARCHES)
                    points_new = get_points(EMAIL,PASSWORD,driver,True)
                except Exception as e:
                    print(e,traceback.format_exc())
                finally:
                    driver.quit()
        print(f'\tFinished... \n')
        if MOBILE_SEARCHES:
            print(f'Points earned for {EMAIL}: {max(points_new-points,0)}\n')
    if ranRewards:
        report = f'\nAll accounts have been automated.'
        print(report)
        END = int(time.time())
        print(f'Program ran for: {(END-START)//60} minutes and {(END-START)%60} seconds.')
    return

def main():
    while True:
        try:
            start_rewards()
            print(f'Bing Rewards Automation Complete!\n')
            t = random.randint(3000,4000)
            print('\nSleeping for a few hours before restarting...\nThank you for using my bot:)\n\n')
            
        except Exception as e:
            print(f'Exception: {e}\n\n{traceback.format_exc()}\n\n\n Attempting to restart Bing Rewards Automation in 10 minutes...')
            time.sleep(600)
            continue

if __name__ == "__main__":
    check_ip_address()
    main()