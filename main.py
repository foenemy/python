# 네이버 플레이스 클릭하기.
# url 방식?

import requests


response = requests.get('http://www.naver.com')



# print(response.status_code)


#print(response.text)



[{'name': 'page_uid', 'path': '/', 'value': 'UBvXelprvA4ssiZPVDwsssssssZ-330346', 'httpOnly': False, 'secure': False, 'domain': '.naver.com'}, {'name': 'NID_AUT', 'path': '/', 'value': 'jK2O9nT2GIWbL8bJj1hcoXmY+OxmiN53uH5xDw3ph1Ji0c+WoPM8iojA2Oye5J0G', 'httpOnly': False, 'secure': True, 'expiry': 1620502717, 'domain': '.naver.com'}, {'name': 'BMR', 'path': '/', 'value': 'r=https%3A%2F%2Fm.blog.naver.com%2FCommentList.nhn%3FblogId%3Dmelina526%26logNo%3D110084850684&s=1580260567571&proxyReferer=https%3A%2F%2Fwww.google.com%2F&r2=https%3A%2F%2Fm.blog.naver.com%2FPostView.nhn%3FblogId%3Dmelina526%26logNo%3D110084850684', 'httpOnly': False, 'secure': True, 'expiry': 1592867810, 'domain': '.naver.com'}, {'name': 'NNB', 'path': '/', 'value': 'JMOI4MBW5YYF4', 'httpOnly': False, 'secure': False, 'expiry': 2524640398.504473, 'domain': '.naver.com'}, {'name': 'NID_SES', 'path': '/', 'value': 'AAABoj/+5oOP9jwkNQmx2ZJSt06SXPrwm8RCTZZFUIzlDm0/j2Zovuj4wy/SwmFicHjROlF7LSXliOfeNQvktEGuA8ioOJQ3kZEprcwJ5wrMZKZkmx6LK42eVwRszRrAcMbfcSzuoldmlCcUoVBBdwPQuQsuEv6JEzpEzZNx0Gg3eCBUZC11/+Im1bAZnKiV1a7WPvuzkRm2g2Q6Kut2RYRVInxf1FFJCJb7was1c+0QOyio0TDwNgcpf7Br5KhCg76noaLUTse2b7HO4CalkBo+s87JqkPp3xBQ0ki8CvaB1gFYxuuLUYp3Mocpf/2abx0xl5axTLmEKdaFH4Vvw2DxKpyS3t9Z6kK64Di9UTOmEOL+iyI94zMPFN+wvLsyunh4xXrnPKUOHlzCaIUdWRH76hGGG5NgpV8q+U1Fy3kw7NDhnsl/4eCvtbB50pmr+S9ad/jv9hmlLWvTpkU69dDNYK3iJSLrmWYplPEp4urthC4RW85rDNte/UiBC6PVjcWpOpU9BKPUgPaQyGQidyD0uhCgCURf1qqztIbPcSbWHWdRPsGlwSHHT5/sWqJNl1i+8w==', 'httpOnly': False, 'secure': True, 'expiry': 2524608000, 'domain': '.naver.com'}, {'name': 'NFS', 'path': '/', 'value': '2', 'httpOnly': False, 'secure': False, 'expiry': 1895625012, 'domain': '.naver.com'}, {'name': '_naver_usersession_', 'path': '/', 'value': 'j9vKxynkPoV9MSPK98uoAhPz', 'httpOnly': False, 'secure': False, 'expiry': 1580265328.929177, 'domain': '.naver.com'}, {'name': 'NRTK', 'path': '/', 'value': 'ag#all_ma#-2_gr#1_si#0_en#0_sp#0', 'httpOnly': False, 'secure': False, 'expiry': 1611801012, 'domain': '.naver.com'}, {'name': 'MM_NEW', 'path': '/', 'value': '1', 'httpOnly': False, 'secure': False, 'expiry': 1611801012, 'domain': '.naver.com'}]
