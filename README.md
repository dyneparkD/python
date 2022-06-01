# python

### How to connect Selenium to an existing browser:

```
cd "C:\Program Files\Google\Chrome\Application"
chrome.exe --remote-debugging-port=8989 --user-data-dir="C:\Users\s6xya\Desktop\chromefile"
<Chrome driver opens>
```

### file setting

chrome_driver = "C:\\Users\\s6xya\\Desktop\\dyneparkD\\python\\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:8989")
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

### FYI

1. chromedriver.exe and .py must be in same directory
2. KakaoWebtoon crawling limit: around 50. (403 Error)
