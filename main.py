import requests
finansal_tablo_url = 'https://malitablolar.com/finansal-tablo/{kagit}/bilanco?kur=TL'
# Kullanıcıdan bilgileri alma
kullanici_adi = input("Email: ")
sifre = input("Şifre: ")

# Giriş bilgileri
login_data = {
    'Email': kullanici_adi,
    'Sifre': sifre
}

# Giriş yapılacak sayfanın URL'si
url = 'https://malitablolar.com/Aut/Login'

# Oturum başlatma ve giriş yapma
with requests.Session() as session:
    response = session.get(url)

    # Giriş verilerini ekleyerek POST isteği gönderme
    response = session.post(url, data=login_data)

    # Giriş sonrası HTTP durum koduna göre kontrol
    if response.status_code == 200:
        # Giriş sonrası sayfanın içeriğini kontrol et
        if 'https://malitablolar.com/Analiz' in response.url:
            print('Parola Doğru.')
            kagit_adi = input("Finansal tablosu için kağıt adı girin: ")

            # Finansal tablo URL'sini oluşturarak yönlendirme
            finansal_tablo_url = finansal_tablo_url.format(kagit=kagit_adi)

            # Finansal tablo sayfasına yönlendirme
            response = session.get(finansal_tablo_url)

            # Finansal tablo sayfasının içeriğini kontrol et
            if response.status_code == 200:
                print(f"{kagit_adi} finansal tablo sayfasına yönlendirildi.")
            else:
                print("HATA!KAĞIT ADI YANLIŞ GİRİLDİ")
        elif 'https://malitablolar.com/Aut/Login' in response.url:
            print('Şifre yanlış, tekrar deneyin.')
        else:
            print('Bilinmeyen bir durum oluştu.')
    else:
        print('Bilinmeyen bir durum oluştu.')
