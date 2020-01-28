#네이버 플레이스 링크 클릭 
# 셀레니움 사용


from selenium import webdriver
import time,re
import Setting

keywordList = [
['티앤북스','남포동 카페',['e','o','r','n','spacebar','c','l','a','t','k','s','e','h','d','spacebar','a','k','t','w','l','q']],
['이안헤어3호점','서면 미용실',['t', 'j', 'a', 'u', 's', 'spacebar', 'a', 'l', 'd', 'y', 'd', 't', 'l', 'f']],
['다깡 중앙점','부산 중앙동 맛집',['q', 'n', 't', 'k', 's', 'spacebar', 'w', 'n', 'd', 'd', 'k', 'd', 'e', 'h', 'd', 'spacebar', 'a', 'k', 't', 'w', 'l', 'q']],
['반타르','남포동 카페',['s', 'k', 'a', 'v', 'h', 'e', 'h', 'd', 'spacebar', 'z', 'k', 'v', 'p']],
['토모','부산대 술집',['q', 'n', 't', 'k', 's', 'e', 'o', 'spacebar', 't', 'n', 'f', 'w', 'l', 'q']],
['모시모시','부산대 맛집',['q', 'n', 't', 'k', 's', 'e', 'o', 'spacebar', 'a', 'k', 't', 'w', 'l', 'q']],
]


for j in range(10000):
	i = j%len(keywordList)
	try:
		browser = Setting.setting()
		# 뉴스 등 탐색
		browser = Setting.inputKW(keywordList[i][1],keywordList[i][2],browser)
		browser = Setting.searchPlace(keywordList[i][0],browser)
		# 플레이스 안에서 스크롤하기
		# browser.implicitly_wait(3)
		browser.quit()
	except Exception as e:
		browser.quit()

	time.sleep(130)