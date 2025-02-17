from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# Kullanıcı bilgileri
USERNAME = os.getenv("DEU_USERNAME")
PASSWORD = os.getenv("DEU_PASSWORD")

# Telegram Bot Bilgileri
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Kontrol edilecek derslerin isimleri
TARGET_COURSES = [
    "BİL 3110 Bilimsel Hesaplama",
    "BİL 3112 Makine Öğrenimi",
    "BİL 3129 Programlama Dilleri Konseptleri",
    "BİL 3130 Bulanık Karar Sistemleri",
    "FİZ 3118 Bilgisayar Bilimleri için Fizik II",
    "BİL 4108 Fizik",
    "BİL 4112 Yapay Zeka",
    "BİL 4114 Hesaplama Kuramına Giriş",
    "BİL 4120 Gömülü Sistem Programlama",
    "BİL 4122 Tamsayılı Programlama",
    "BİL 4125 Yazılımlarda Hata Ayıklama",
    "İST 4202 Aktüerya ve Risk Yönetimi"
]

# Daha önce bildirilen dersleri saklamak için
previous_available_courses = set()

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=data)

# WebDriver ayarları
chrome_options = Options()
chrome_options.add_argument("--headless")  # Tarayıcıyı görünmez yaparak çalıştır
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
service = Service("/usr/local/bin/chromedriver")

def login(driver):
    driver.get("https://kayit.deu.edu.tr/index.php")
    time.sleep(2)
    
    # Kullanıcı adı ve şifreyi gir
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "user"))).send_keys(USERNAME)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "pass"))).send_keys(PASSWORD)
    
    # "TAMAM" butonuna bas
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='TAMAM']"))).click()
    time.sleep(3)

def navigate_to_ders_kayit(driver):
    # Ders kayıt sayfasına git
    driver.find_element(By.LINK_TEXT, "DERS KAYIT").click()
    time.sleep(3)
    
    # Popup kapatma
    try:
        close_popup = driver.find_element(By.XPATH, "//td[@class='close']/div/span[text()='Kapat ']")
        close_popup.click()
        time.sleep(2)
    except:
        print("Popup bulunamadı, devam ediliyor...")

def check_available_courses(driver):
    # Ders listesini al
    rows = driver.find_elements(By.XPATH, "//table//tr")
    available_courses = set()
    
    for row in rows:
        try:
            course_name = row.find_element(By.XPATH, ".//td[1]").text  # İlk sütundaki ders adını al
            if course_name in TARGET_COURSES:
                checkbox = row.find_element(By.XPATH, ".//input[@type='checkbox']")
                status = row.text  # Satırın içeriğini al
                
                # Engelleyici metinler içeriyor mu kontrol et
                if not any(block in status for block in ["DPY", "ALZ", "ÖŞT", "KÜM", "KNT", "DDKA"]):
                    available_courses.add(course_name)
                    print(f"Seçilebilir Ders: {course_name}")
        except:
            pass
    
    return available_courses

def main():
    global previous_available_courses
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        login(driver)
        navigate_to_ders_kayit(driver)
        available_courses = check_available_courses(driver)
        
        new_courses = available_courses - previous_available_courses  # Yeni açılan dersleri bul
        
        if new_courses:
            message = "📢 Yeni dersler açıldı! Hemen kayıt ol!\n\n" + "\n".join(new_courses)
            send_telegram_message(message)
            print("Yeni dersler açıldı! Telegram bildirimi gönderildi.")
            previous_available_courses = available_courses  # Önceki dersleri güncelle
        else:
            print("Yeni ders eklenmedi, bildirim gönderilmiyor.")
    finally:
        driver.quit()
        
if __name__ == "__main__":
    while True:
        main()
        time.sleep(60)  # 1 dakikada bir kontrol et