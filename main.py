import getpass
import requests

# Kullanıcıdan bilgileri alma
kullanici_adi = input("Email: ")
sifre = getpass.getpass("Şifre: ")  # getpass kullanarak şifreyi gizle

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
        print('Giriş başarılı!')
    else:
        print('Giriş başarısız!')
