#네이버 플레이스 링크 클릭 
# 셀레니움 사용

from selenium import webdriver
import time,re,os
import Setting
# import sentry_sdk
# from sentry_sdk import capture_exception
# sentry_sdk.init("https://d794285a418545868f837c97d45570c2@sentry.io/1885204")

os.chdir("C:\Program Files (x86)\OneClickTethering\OneClickThthering")
os.system("adb start-server")

keywordList = [
['티앤북스','남포동 카페',['s', 'k', 'a', 'v', 'h', 'e', 'h', 'd', 'spacebar', 'z', 'k', 'v', 'p']],
['토모','부산대 술집',['q', 'n', 't', 'k', 's', 'e', 'o', 'spacebar', 't', 'n', 'f', 'w', 'l', 'q']],
['모시모시','부산대 맛집',['q', 'n', 't', 'k', 's', 'e', 'o', 'spacebar', 'a', 'k', 't', 'w', 'l', 'q']],
['이안헤어3호점','서면 미용실',['t', 'j', 'a', 'u', 's', 'spacebar', 'a', 'l', 'd', 'y', 'd', 't', 'l', 'f']],
['다깡','부산 중앙동 맛집',['q', 'n', 't', 'k', 's', 'spacebar', 'w', 'n', 'd', 'd', 'k', 'd', 'e', 'h', 'd', 'spacebar', 'a', 'k', 't', 'w', 'l', 'q']],
]


for j in range(10000):
	i = j%len(keywordList) 
	try:
		os.system("adb shell svc data disable")
		time.sleep(2)
		os.system("adb shell svc data enable")
		time.sleep(3)
		browser, nid = Setting.setting()
		time.sleep(5)
		# browser = Setting.whatismyUA(browser)
		# 뉴스 등 탐색
		browser, nid = Setting.inputKW(keywordList[i][1],keywordList[i][2],browser,nid)
		# time.sleep(500)
		browser, nid = Setting.searchPlace(keywordList[i][0],browser, nid)
		# # 플레이스 안에서 스크롤하기
		# # browser.implicitly_wait(3)
		browser = Setting.randomLink(browser, nid)
		browser.quit()
	except Exception as e:
		print(e)
		# capture_exception(e)
		browser.quit()

	time.sleep(161)