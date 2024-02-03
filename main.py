import requests

# Giriş yapılacak sayfa
url = 'https://malitablolar.com/login'

# Giriş bilgileri
login_data = {
    'username': 'kullanici_adi',
    'password': 'sifre',
    'submit': 'Login'
}

# Oturum başlatma ve giriş yapma
with requests.Session() as session:
    response = session.get(url)

    # Giriş URL'sini almak için HTML içeriğini inceleme
    login_url = 'https://malitablolar.com/login'  # Örneğin, burada login sayfasının URL'sini belirtin

    # Giriş verilerini ekleyerek POST isteği gönderme
    response = session.post(login_url, data=login_data)

    # Giriş sonrası HTTP durum koduna göre kontrol
    if response.status_code == 200:
        print('Giriş başarılı!')
    else:
        print('Giriş başarısız!')
