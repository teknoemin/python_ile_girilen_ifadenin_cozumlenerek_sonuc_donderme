komut = "send-181-3-0-1\nreceive-170-3-0\n"
komut_parcala = komut.split("\n")
ayrac_sayac = 0
def degerleri_tut(kod_tipi, sinyal_verisi):
    if ((int(sinyal_verisi[0]) >= 0 and int(sinyal_verisi[0]) <= 255) and (int(sinyal_verisi[1]) >= 1 and int(sinyal_verisi[1]) <= 4) and (int(sinyal_verisi[2]) >= 0 and int(sinyal_verisi[2]) <= 1) and ((len(sinyal_verisi) == 4 and int(sinyal_verisi[3]) >= 0 and int(sinyal_verisi[3]) <= 1) or len(sinyal_verisi) == 3)):
        if kod_tipi == "receive":
            print("Kod Tipi: " + kod_tipi + " - Gelen")
            if (int(sinyal_verisi[0]) >= 0 and int(sinyal_verisi[0]) <= 50):
                print("Sinyal Gucu: " + sinyal_verisi[0] + " - Çok Zayıf Sinyal")
            elif (int(sinyal_verisi[0]) >= 51 and int(sinyal_verisi[0]) <= 100):
                print("Sinyal Gucu: " + sinyal_verisi[0] + " - Zayıf Sinyal")
            elif (int(sinyal_verisi[0]) >= 101 and int(sinyal_verisi[0]) <= 150):
                print("Sinyal Gucu: " + sinyal_verisi[0] + " - Orta Sinyal")
            elif (int(sinyal_verisi[0]) >= 151 and int(sinyal_verisi[0]) <= 200):
                print("Sinyal Gucu: " + sinyal_verisi[0] + " - Güçlü Sinyal")
            elif (int(sinyal_verisi[0]) >= 201 and int(sinyal_verisi[0]) <= 255):
                print("Sinyal Gucu: " + sinyal_verisi[0] + " - Çok Güçlü Sinyal")
            else:
                print("Sinyal Gucu: Gecersiz")
            if (int(sinyal_verisi[1]) == 1):
                print("Cihaz: " + sinyal_verisi[1] + " - Televizyon")
            elif (int(sinyal_verisi[1]) == 2):
                print("Cihaz: " + sinyal_verisi[1] + " - Camasir Makinesi")
            elif (int(sinyal_verisi[1]) == 3):
                print("Cihaz: " + sinyal_verisi[1] + " - Buzdolabi")
            elif (int(sinyal_verisi[1]) == 4):
                print("Cihaz: " + sinyal_verisi[1] + " - Firin")
            else:
                print("Cihaz: Gecersiz")
            if (int(sinyal_verisi[2]) == 0):
                print("Durumu: " + sinyal_verisi[2] + " - Off")
            elif (int(sinyal_verisi[2]) == 1):
                print("Durumu: " + sinyal_verisi[2] + " - On")
            else:
                print("Durumu: Gecersiz")
            if (len(sinyal_verisi) == 4):
                if (int(sinyal_verisi[3]) == 0):
                    print("Cevap: " + sinyal_verisi[3] + " - Cevap istenmiyor")
                elif (int(sinyal_verisi[3]) == 1):
                    print("Cevap: " + sinyal_verisi[3] + " - Cevap isteniyor")
                else:
                    print("Cevap: Gecersiz")
        else:
            print("Kod Tipi: " + kod_tipi + " - Giden")
            if (int(sinyal_verisi[0]) >= 0 and int(sinyal_verisi[0]) <= 50):
                print("Sinyal Gucu: " + sinyal_verisi[0] + " - Cok Zayif")
            elif (int(sinyal_verisi[0]) >= 51 and int(sinyal_verisi[0]) <= 100):
                print("Sinyal Gucu: " + sinyal_verisi[0] + " - Zayif")
            elif (int(sinyal_verisi[0]) >= 101 and int(sinyal_verisi[0]) <= 150):
                print("Sinyal Gucu: " + sinyal_verisi[0] + " - Orta")
            elif (int(sinyal_verisi[0]) >= 151 and int(sinyal_verisi[0]) <= 200):
                print("Sinyal Gucu: " + sinyal_verisi[0] + " - Guclu Sinyal")
            elif (int(sinyal_verisi[0]) >= 201 and int(sinyal_verisi[0]) <= 255):
                print("Sinyal Gucu: " + sinyal_verisi[0] + " - Cok Guclu")
            else:
                print("Sinyal Gucu: Gecersiz")
            if (int(sinyal_verisi[1]) == 1):
                print("Cihaz: " + sinyal_verisi[1] + " - Televizyon")
            elif (int(sinyal_verisi[1]) == 2):
                print("Cihaz: " + sinyal_verisi[1] + " - Camasir Makinesi")
            elif (int(sinyal_verisi[1]) == 3):
                print("Cihaz: " + sinyal_verisi[1] + " - Buzdolabi")
            elif (int(sinyal_verisi[1]) == 4):
                print("Cihaz: " + sinyal_verisi[1] + " - Firin")
            else:
                print("Cihaz: Gecersiz")
            if (int(sinyal_verisi[2]) == 0):
                print("Durumu: " + sinyal_verisi[2] + " - Off")
            elif (int(sinyal_verisi[2]) == 1):
                print("Durumu: " + sinyal_verisi[2] + " - On")
            else:
                print("Durumu: Gecersiz")
            if (len(sinyal_verisi) == 4):
                if (int(sinyal_verisi[3]) == 0):
                    print("Cevap: " + sinyal_verisi[3] + " - Istenmiyor")
                elif (int(sinyal_verisi[3]) == 1):
                    print("Cevap: " + sinyal_verisi[3] + " - Isteniyor")
                else:
                    print("Cevap: Gecersiz")
    else:
        print("Geçersiz ifade")
for donder in komut_parcala:
    if (len(donder) > 0):
        kac_parca_tip = donder.split("-")
        kod_tipi = kac_parca_tip.pop(0)
        ayrac_sayac += 1
        if (ayrac_sayac > 1):
            print("------")
        if (kod_tipi == "send"):
            if (len(kac_parca_tip) != 4):
                print("Geçersiz ifade")
            else:
                degerleri_tut(kod_tipi, kac_parca_tip)
        elif (kod_tipi == "receive"):
            if (len(kac_parca_tip) != 3):
                print("Geçersiz ifade")
            else:
                degerleri_tut(kod_tipi, kac_parca_tip)
        else:
            print("Geçersiz ifade")