
# -*- coding: utf-8 -*-
import requests
import xml.etree.ElementTree as ET
def TCDogrula(TCKimlikNo,Ad,Soyad,DogumYili):
    Veri2=("""<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <TCKimlikNoDogrula xmlns="http://tckimlik.nvi.gov.tr/WS">
      <TCKimlikNo>{}</TCKimlikNo>
      <Ad>{}</Ad>
      <Soyad>{}</Soyad>
      <DogumYili>{}</DogumYili>
    </TCKimlikNoDogrula>
  </soap12:Body>
</soap12:Envelope>""".format(long(TCKimlikNo),str(Ad),str(Soyad),int(DogumYili)))
    url="https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx?WSDL"
    headers = {'Content-Type': 'application/soap+xml'}
    response = requests.post(url,data=Veri2,headers=headers,stream=True)
    namespaces = {
        'soap': 'http://www.w3.org/2003/05/soap-envelope',
        'a': 'http://tckimlik.nvi.gov.tr/WS',
    }
    tree = ET.fromstring(response.content)
    names = tree.findall(
    './soap:Body'
    '/a:TCKimlikNoDogrulaResponse'
    '/a:TCKimlikNoDogrulaResult',
    namespaces,
)
    for name in names:
        sonuc =name.text
    print sonuc
TCDogrula("1111111111","FERHAT","GÜNERİ","1111")
