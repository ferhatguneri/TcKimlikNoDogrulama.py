# Python SOAP ile Nüfus Müdürlüğünden TC Kimlik Doğrulama - Ferhat Güneri


Bu Python scripti TC Kimlik No, Ad, Soyad, Doğum Yılı bilgilerini TC Nüfus Müdürlüğünün Soap API si ile kontrol ederek bilgilerin doğru olup olmadığını gönderir.


Örnek:
TCDogrula("11111111111","JOHN","DOE","1111")

Sonuç:
<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><TCKimlikNoDogrulaResponse xmlns="http://tckimlik.nvi.gov.tr/WS"><TCKimlikNoDogrulaResult>false</TCKimlikNoDogrulaResult></TCKimlikNoDogrulaResponse></soap:Body></soap:Envelope>

Görüldüğü gibi <TCKimlikNoDogrulaResult>false</TCKimlikNoDogrulaResult> bilgiler yanlış olduğundan False değeri döndü.
