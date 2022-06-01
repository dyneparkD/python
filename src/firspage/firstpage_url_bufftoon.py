from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import openpyxl

chrome_driver = "C:\\Users\\s6xya\\Desktop\\dyneparkD\\python\\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:8989")
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

count = 0
url_list = [
    'https://bufftoon.plaync.com/series/10099',
    'https://bufftoon.plaync.com/series/10085',
    'ht,tps://bufftoon.plaync.com/series/1000381',
    'https://bufftoon.plaync.com/series/745054',
    'https://bufftoon.plaync.com/series/10089',
    'https://bufftoon.plaync.com/series/10077',
    'https://bufftoon.plaync.com/series/759046',
    'https://bufftoon.plaync.com/series/745052',
    'https://bufftoon.plaync.com/series/697057',
    'https://bufftoon.plaync.com/series/10078',
    'https://bufftoon.plaync.com/series/10073',
    'https://bufftoon.plaync.com/series/1000608',
    'https://bufftoon.plaync.com/series/1000580',
    'https://bufftoon.plaync.com/series/758341',
    'https://bufftoon.plaync.com/series/672930',
    'https://bufftoon.plaync.com/series/1001740',
    'https://bufftoon.plaync.com/series/10079',
    'https://bufftoon.plaync.com/series/1001442',
    'https://bufftoon.plaync.com/series/758331',
    'https://bufftoon.plaync.com/series/10076',
    'https://bufftoon.plaync.com/series/10102',
    'https://bufftoon.plaync.com/series/1000384',
    'https://bufftoon.plaync.com/series/10105',
    'https://bufftoon.plaync.com/series/1001767',
    'https://bufftoon.plaync.com/series/10081',
    'https://bufftoon.plaync.com/series/10106',
    'https://bufftoon.plaync.com/series/10075',
    'https://bufftoon.plaync.com/series/672931',
    'https://bufftoon.plaync.com/series/10096',
    'https://bufftoon.plaync.com/series/10094',
    'https://bufftoon.plaync.com/series/698318',
    'https://bufftoon.plaync.com/series/665750',
    'https://bufftoon.plaync.com/series/748280',
    'https://bufftoon.plaync.com/series/1000578',
    'https://bufftoon.plaync.com/series/1002864',
    'https://bufftoon.plaync.com/series/10104',
    'https://bufftoon.plaync.com/series/1000972',
    'https://bufftoon.plaync.com/series/1001463',
    'https://bufftoon.plaync.com/series/708837',
    'https://bufftoon.plaync.com/series/758888',
    'https://bufftoon.plaync.com/series/100871',
    'https://bufftoon.plaync.com/series/1000833',
    'https://bufftoon.plaync.com/series/10101',
    'https://bufftoon.plaync.com/series/689367',
    'https://bufftoon.plaync.com/series/1001739',
    'https://bufftoon.plaync.com/series/1002914',
    'https://bufftoon.plaync.com/series/10092',
    'https://bufftoon.plaync.com/series/1001836',
    'https://bufftoon.plaync.com/series/1004032',
    'https://bufftoon.plaync.com/series/10090',
    'https://bufftoon.plaync.com/series/745055',
    'https://bufftoon.plaync.com/series/1001918',
    'https://bufftoon.plaync.com/series/1002215',
    'https://bufftoon.plaync.com/series/1000574',
    'https://bufftoon.plaync.com/series/1002880',
    'https://bufftoon.plaync.com/series/1000385',
    'https://bufftoon.plaync.com/series/1001917',
    'https://bufftoon.plaync.com/series/665748',
    'https://bufftoon.plaync.com/series/1000583',
    'https://bufftoon.plaync.com/series/663484',
    'https://bufftoon.plaync.com/series/1002917',
    'https://bufftoon.plaync.com/series/744995',
    'https://bufftoon.plaync.com/series/1000834',
    'https://bufftoon.plaync.com/series/1005698',
    'https://bufftoon.plaync.com/series/1003907',
    'https://bufftoon.plaync.com/series/1000581',
    'https://bufftoon.plaync.com/series/1001867',
    'https://bufftoon.plaync.com/series/1000391',
    'https://bufftoon.plaync.com/series/10100',
    'https://bufftoon.plaync.com/series/1001726',
    'https://bufftoon.plaync.com/series/1000577',
    'https://bufftoon.plaync.com/series/1002926',
    'https://bufftoon.plaync.com/series/1001744',
    'https://bufftoon.plaync.com/series/1001803',
    'https://bufftoon.plaync.com/series/1002853',
    'https://bufftoon.plaync.com/series/636747',
    'https://bufftoon.plaync.com/series/749633',
    'https://bufftoon.plaync.com/series/10069',
    'https://bufftoon.plaync.com/series/1001111',
    'https://bufftoon.plaync.com/series/745779',
    'https://bufftoon.plaync.com/series/753216',
    'https://bufftoon.plaync.com/series/1000575',
    'https://bufftoon.plaync.com/series/1001470',
    'https://bufftoon.plaync.com/series/10082',
    'https://bufftoon.plaync.com/series/1001745',
    'https://bufftoon.plaync.com/series/1000582',
    'https://bufftoon.plaync.com/series/1002920',
    'https://bufftoon.plaync.com/series/10114',
    'https://bufftoon.plaync.com/series/731847',
    'https://bufftoon.plaync.com/series/636748',
    'https://bufftoon.plaync.com/series/1000494',
    'https://bufftoon.plaync.com/series/1000382',
    'https://bufftoon.plaync.com/series/1001817',
    'https://bufftoon.plaync.com/series/1000576',
    'https://bufftoon.plaync.com/series/1001404',
    'https://bufftoon.plaync.com/series/1003990',
    'https://bufftoon.plaync.com/series/1004392',
    'https://bufftoon.plaync.com/series/1001742',
    'https://bufftoon.plaync.com/series/1000573',
    'https://bufftoon.plaync.com/series/1002918',
    'https://bufftoon.plaync.com/series/1001215',
    'https://bufftoon.plaync.com/series/1005442',
    'https://bufftoon.plaync.com/series/1002923',
    'https://bufftoon.plaync.com/series/1002924',
    'https://bufftoon.plaync.com/series/1001768',
    'https://bufftoon.plaync.com/series/1000579',
    'https://bufftoon.plaync.com/series/1002921',
    'https://bufftoon.plaync.com/series/650576',
    'https://bufftoon.plaync.com/series/1002681',
    'https://bufftoon.plaync.com/series/1001319',
    'https://bufftoon.plaync.com/series/1002916',
    'https://bufftoon.plaync.com/series/1002650',
    'https://bufftoon.plaync.com/series/10107',
    'https://bufftoon.plaync.com/series/10087',
    'https://bufftoon.plaync.com/series/1002674',
    'https://bufftoon.plaync.com/series/1001216',
    'https://bufftoon.plaync.com/series/1005370',
    'https://bufftoon.plaync.com/series/647360',
    'https://bufftoon.plaync.com/series/1002652',
    'https://bufftoon.plaync.com/series/1007346',
    'https://bufftoon.plaync.com/series/1002922',
    'https://bufftoon.plaync.com/series/1004009',
    'https://bufftoon.plaync.com/series/1002919',
    'https://bufftoon.plaync.com/series/689415',
    'https://bufftoon.plaync.com/series/650677']

WB = openpyxl.Workbook()  # 엑셀 파일 생성
WS = WB.active

print("start----------------")
for webtoon in url_list:
    try:
        driver.get(url_list[count])
        driver.implicitly_wait(5)
        first_episode_url = driver.find_element_by_xpath(
            "//*[@id='content']/div/div/div[2]/a").get_attribute("href")

        WS.cell(count+2, 1, first_episode_url)
        count = count+1
        print(first_episode_url)
        print(count)
        print(len(url_list))
    except:
        print("Error!")
        break

WB.save("bufftoon.xls")
print("File saved")
