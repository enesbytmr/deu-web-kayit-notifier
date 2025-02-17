# DEU Web Kayit Notifier 📢

Bu Python botu, **Dokuz Eylül Üniversitesi (DEU) ders kayıt sistemini** takip ederek açılan dersleri otomatik olarak tespit eder ve Telegram ile bildirim gönderir.

## 🚀 Özellikler
- Üniversitenin ders kayıt sayfasına otomatik giriş yapar.
- Sadece belirlenen dersleri takip eder.
- Ders kontenjanı açıldığında Telegram üzerinden bildirim yollar.
- Sürekli çalışarak her 1 dakikada bir kontrol eder.

---

## 📦 Kurulum
Bu botu çalıştırmak için aşağıdaki adımları izleyin.

### **1️⃣ Gerekli Bağımlılıkları Yükleyin**
Python bağımlılıklarını yüklemek için:
```bash
pip3 install -r requirements.txt
```

Eğer `requirements.txt` dosyan yoksa, aşağıdaki komutla bağımlılıkları yükleyebilirsin:
```bash
pip3 install selenium requests python-dotenv
```

### **2️⃣ Chrome ve ChromeDriver Yükleyin**
Bu bot, **Selenium** kullanarak web sayfalarını otomatik olarak kontrol eder. Bunun için **Google Chrome** ve **ChromeDriver** yüklemelisin.

#### **🔹 Chrome Yükleme**
Eğer sisteminde Chrome yüklü değilse aşağıdaki bağlantıdan indir:
- [Google Chrome İndir](https://www.google.com/chrome/)

#### **🔹 ChromeDriver Yükleme**
1. Google Chrome sürümünü kontrol et:
   ```bash
   google-chrome --version   # Linux
   google-chrome-stable --version  # Linux bazı dağıtımlar
   chromedriver --version  # Mac ve Windows
   ```
2. Chrome'un sürümüne uygun **ChromeDriver'ı** şu bağlantıdan indir:
   - [ChromeDriver İndir](https://sites.google.com/chromium.org/driver/)
3. İndirilen `chromedriver` dosyasını `/usr/local/bin/` veya **Projenin Kök Dizini** içine taşı veya taşıma dosyanın olduğu yolu yaz:
   ```bash
   sudo mv chromedriver /usr/local/bin/
   sudo chmod +x /usr/local/bin/chromedriver
   ```

---

### **3️⃣ Telegram Botu Kurulumu**
Bu bot, Telegram üzerinden bildirim gönderecektir. Bunun için aşağıdaki adımları takip et:

#### **🔹 Telegram Bot Oluşturma**
1. Telegram'da [@BotFather](https://t.me/BotFather) ile konuş.
2. `/newbot` yaz ve bir bot oluştur.
3. Bot ismini ve kullanıcı adını belirle.
4. **BotFather**, sana bir **API Token** verecek. Bunu `.env` dosyasına ekleyeceğiz.

#### **🔹 Telegram Chat ID'yi Bulma**
1. Telegram'da [@userinfobot](https://t.me/userinfobot) ile konuş.
2. `/start` yaz ve **Chat ID'ni** al.

---

### **4️⃣ .env Dosyasını Hazırlayın**
**Gizli bilgileri saklamak için** `.env` dosyası oluşturun ve aşağıdaki bilgileri ekleyin:
```ini
DEU_USERNAME=ogrenci_kullanici_adi
DEU_PASSWORD=ogrenci_sifresi
TELEGRAM_BOT_TOKEN=telegram_bot_token
TELEGRAM_CHAT_ID=telegram_chat_id
```
`.env` dosyasını **GitHub'a yüklemeyin!** `.gitignore` içine şu satırı ekleyin:
```
.env
```

---

## 🏃‍♂️ Çalıştırma
Aşağıdaki komutu çalıştırarak botu başlatabilirsin:
```bash
python3 deu-web-kayit-notifier.py
```
Bot her 1 dakikada bir çalışarak **ders kontenjanlarını kontrol eder** ve **yeni açılan dersleri Telegram üzerinden bildirir**.

---

## 📜 Katkıda Bulunma
Bu projeye katkıda bulunmak istersen:
1. Reponun bir kopyasını al (Fork yap).
2. Yeni bir özellik ekleyerek veya hata düzelterek PR (Pull Request) aç.
3. Soruların varsa **GitHub Issues** kısmında belirtebilirsin.

---

## 📜 Lisans
Bu proje **MIT Lisansı** altında yayınlanmıştır. Özgürce kullanabilir, değiştirebilir ve geliştirebilirsiniz!

---

🔹 **Proje Sahibi:** Fevzi Enes Baytemir
🔹 **Repo:** [GitHub](https://github.com/enesbytmr/deu-web-kayit-notifier)