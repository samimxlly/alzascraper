<b>Alza Mobile Phones Scraper</b>
Tento Python skript stahuje údaje o mobilních telefonech z webu Alza. Získává informace o nejlevnějším dostupném mobilním telefonu.

<b>Nutnosti</b>
Python 3.x
Pro WebDriver je potřeba prohlížeč Chrome
ChromeDriver (automaticky spravován pomocí webdriver_manager)
Instalace
Naklonujte si tento repozitář na své lokální zařízení:
git clone https://github.com/your-username/alza-mobile-scraper.git

<b>Nainstalujte potřebné Python balíčky:</b>
pip install selenium beautifulsoup4 webdriver_manager

Použití
Spusťte skript:
python alza_scraper.py

Skript otevře headless prohlížeč Chrome, přejde na stránku s mobilními telefony na webu Alza a extrahuje údaje o nejlevnějším mobilním telefonu.
Výsledek bude vypsán do konzole, včetně názvu mobilního telefonu, ceny a odkazu.
<b>Poznámky</b>
Skript používá headless prohlížeč, aby se během provádění nezobrazovalo uživatelské rozhraní prohlížeče.