import selenium
import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import threading
import time
from msedge.selenium_tools import Edge, EdgeOptions
import shutil
shutil.rmtree('D:\\Edge Data\\')
os.makedirs("D:\\Edge Data\\")


credentials = [
    
    ("nyanko24","nyanko14022004"),
    ("h3h3h3275","Hoviets@ng2005"),
    ("LivingGrapefruit7906","fduonguwu"),
    ("Historical-Net6114","dat120106"),
    ("h4h4h4275","Hoviets@ng2005"),
    ("Sandhurts","123321123")
    ]





import urllib.request

def read_to_string(target_url):
    with urllib.request.urlopen(target_url) as response:
        return response.read().decode('utf-8').strip()
    
js = read_to_string("https://raw.githubusercontent.com/LiquidRekto/rplacevnhideout/master/us.js")

def login(driver: webdriver.Edge | webdriver.Chrome | webdriver.Firefox, username: str, password: str):
    # Đăng nhập vào reddit
    try:
        username_box = driver.find_element(By.ID, "loginUsername")
        password_box = driver.find_element(By.ID, "loginPassword")
        username_box.clear()
        username_box.send_keys(username)
        password_box.clear()
        password_box.send_keys(password)
        # Bấm nút đăng nhập
        password_box.send_keys(Keys.ENTER)

        # r/place canvas là một iframe, source là https://garlic-bread.reddit.com.
        # ID của iframe này thay đổi sau mỗi reload, phải fetch lại
        time.sleep(5)
        driver.get("https://www.reddit.com/settings/")
        #driver.execute_script(js)
    except Exception as e:
        driver.delete_all_cookies()

        print(e)



N = len(credentials)   # Number of browsers to spawn
thread_list = list()

# Start test
for i in range(N):
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_experimental_option("detach", True)
    edge_options.add_argument("-inprivate")

    # Set the path of the profile ending with User Data, not the profile folder
    edge_options.add_argument(f"--user-data-dir=D:\\Edge Data\\{i}")

    # Specify the actual profile folder
    edge_options.add_argument(f"profile-directory=My_Profile_{i}")
    edge_options.add_argument("--disable-dev-shm-usage")
    driver = Edge(executable_path='MicrosoftWebDriver.exe',options=edge_options)
    driver.get("https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2Fsettings%2F")
    
    t = threading.Thread(name='Test {}'.format(i), target=login, args=[driver,credentials[i][0],credentials[i][1]])
    t.start()
    time.sleep(1)
    print(t.name + ' started!')
    

# Wait for all threads to complete
#for thread in thread_list:
#    thread.join()

print('Test completed!')