from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")


chrome_service = Service(ChromeDriverManager().install())


driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


url = 'https://www.alza.cz/mobily/18843445.htm'
driver.get(url)


driver.implicitly_wait(10)

html = driver.page_source


def get_cheapest_mobile(html):
    soup = BeautifulSoup(html, 'html.parser')

    mobiles = soup.select('a.name.browsinglink')

    cheapest_mobile = None
    cheapest_price = float('inf')

    for mobile in mobiles:
        try:
            price_text = mobile.find_next('span', class_='price-box__price').get_text(strip=True)
            price = float(price_text.replace(' ', '').replace(' ', '').replace(',-', '').replace(',', '.'))

            if price < cheapest_price:
                cheapest_price = price
                cheapest_mobile = {
                    'name': mobile.get_text(strip=True),
                    'price': price,
                    'link': 'https://www.alza.cz' + mobile['href']
                }
        except Exception as e:
            print(f"An error occurred: {e}")

    return cheapest_mobile

cheapest_mobile = get_cheapest_mobile(html)

if cheapest_mobile:
    print("Cheapest Mobile Phone:")
    print(f"Name: {cheapest_mobile['name']}")
    print(f"Price: {cheapest_mobile['price']} Kč")
    print(f"Link: {cheapest_mobile['link']}")
else:
    print("No mobile phones found.")

driver.quit()
