# -*- coding: utf-8 -*-
import requests

def TCDogrula(TCKimlikNo,Ad,Soyad,DogumYili):
    veri=("""<?xml version="1.0" encoding="utf-8"?>
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
    headers = {'Content-Type': 'application/soap+xml', 'Accept':'application/json'}
    response = requests.post(url,data=veri,headers=headers)
    print response.content
    
#TCDogrula("11111111111","John","Doe","1111")
