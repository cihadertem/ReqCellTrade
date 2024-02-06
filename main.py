from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

def indirilen_dosyayi_guncelle():
    # Kullanıcıdan bilgileri alma
    kullanici_adi = input("Email: ")
    sifre = input("Şifre: ")
    kagit_adi = input("Finansal tablosu için kağıt adı girin: ")

    # Giriş bilgileri
    login_data = {
        'Email': kullanici_adi,
        'Sifre': sifre
    }

    # Giriş yapılacak sayfanın URL'si
    url = 'https://malitablolar.com/Aut/Login'
    finansal_tablo_url = f'https://malitablolar.com/finansal-tablo/{kagit_adi}/bilanco?kur=TL'

    # Tarayıcı sürücüsünü başlatma
    driver = webdriver.Chrome()

    # Oturum başlatma ve giriş yapma
    driver.get(url)

    # Email alanını bulma ve giriş yapma
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'Email'))
    )
    email_input.send_keys(kullanici_adi)

    # Şifre alanını bulma ve giriş yapma
    sifre_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'Sifre'))
    )
    sifre_input.send_keys(sifre)

    # Giriş butonuna tıklama
    sifre_input.submit()

    # Giriş sonrası HTTP durum koduna göre kontrol
    if 'https://malitablolar.com/Analiz' in driver.current_url:
        print('Parola Doğru.')

        # Finansal tablo sayfasına yönlendirme
        driver.get(finansal_tablo_url)

        # Sayfanın yüklenmesini bekleyelim
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "buttons-excel"))
        )

        # Excel butonunu bulma ve tıklama
        try:
            excel_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "buttons-excel"))
            )
            excel_button.click()
            print("Excel butonuna tıklandı.")

            # İndirme işlemi tamamlanmasını beklemek için kısa bir süre bekleyelim
            time.sleep(5)  # Bu süreyi ihtiyaca göre ayarlayabilirsiniz

            # İndirilenler klasörü
            indirilenler_klasoru = os.path.expanduser('~') + '\\Downloads\\'

            # İndirilenler klasöründeki dosyayı bul
            hedef_dosya = "MALİTABLOLAR  Analiz.xlsx"
            dosya_yolu = os.path.join(indirilenler_klasoru, hedef_dosya)

            # Dosya varsa, finansal tablo adıyla yeni bir dosya adı oluştur
            if os.path.isfile(dosya_yolu):
                yeni_dosya_adı = f"{kagit_adi}_bilanco.xlsx"

                # Dosyayı yeniden adlandır
                yeni_dosya_yolu = os.path.join(indirilenler_klasoru, yeni_dosya_adı)
                os.rename(dosya_yolu, yeni_dosya_yolu)

                print(f"{hedef_dosya} dosyasının yeni adı: {yeni_dosya_adı}")

            else:
                print(f"Hata: {hedef_dosya} dosyası bulunamadı.")

        except Exception as e:
            print(f"Hata: Excel butonu bulunamadı veya tıklanamadı. {e}")

    else:
        print('Şifre yanlış, tekrar deneyin.')

    # Tarayıcıyı kapatma
    driver.quit()

if __name__ == "__main__":
    indirilen_dosyayi_guncelle()