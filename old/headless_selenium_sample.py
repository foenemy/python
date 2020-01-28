#네이버 플레이스 링크 클릭 
# 셀레니움 사용


from selenium import webdriver


TEST_URL = 'https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")
# UserAgent값을 바꿔줍시다!
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = webdriver.Chrome('../chromedriver.exe', chrome_options=options)

driver.get(TEST_URL)
# driver.implicitly_wait(3)
user_agent = driver.find_element_by_css_selector('#user-agent').text

print('User-Agent: ', user_agent)

driver.quit()