class Hesap: #Banka hesabini temsil eden sinifi tanimliyoruz
    def __init__(self, ad_soyad, hesap_no, bakiye=0): #Nesne olusturulurken calisacak constructor method
        self.ad_soyad = ad_soyad #Hesap sahibinin ad ve soyad bilgisini atiyoruz
        self.hesap_no = hesap_no #Hesap numarasini atiyoruz
        self.bakiye = bakiye     #Baslangic bakiyesini atiyoruz

    def para_yatir(self, miktar): #Hesaba para yatirma
        if miktar > 0: #Yatirilacak tutarin pozitif olup olmadigini kontrol ediyoruz
            self.bakiye += miktar #Girilen miktari mevcut bakiyeye ekliyoruz
            print(f"{miktar} TL yatirildi. Yeni bakiyeniz: {self.bakiye} TL") #Guncel bakiyeyi yazdiriyoruz
        else: #0 veya negatif bir sayi girildiyse uyari veriyoruz
            print("Gecersiz miktar! Pozitif bir deger girmelisiniz.")

    def para_cek(self, miktar): #Hesaptan para cekme
        if miktar <= 0: #0 veya negatif tutar cekilmesini engelliyoruz
            print("Gecersiz miktar! Pozitif bir deger girmelisiniz")
        elif miktar > self.bakiye: #Cekilmek istenen tutar bakiyeden buyukse islem yapmiyoruz
            print(f"Yetersiz bakiye! Mevcut bakiyeniz: {self.bakiye} TL")
        else: #Kosullar uygunsa parayi bakiyeden dusuyoruz
            self.bakiye -= miktar 
            print(f"{miktar} TL cekildi. Kalan bakiyeniz: {self.bakiye} TL")

    def bakiye_goruntule(self): #Hesap bilgilerini ve guncel bakiyeyi gosteren metot
        print("\nHesap Bilgileri")
        print(f"Hesap Sahibi: {self.ad_soyad}")
        print(f"Hesap Numarasi: {self.hesap_no}")
        print(f"Guncel Bakiye: {self.bakiye} TL")


#Kullanicidan baslangic bilgilerini alarak hesabi olusturuyoruz
ad_soyad = input("Adiniz soyadiniz: ") 
hesap_no = input("Hesap numaraniz: ")     
baslangic_bakiye = float(input("Baslangic bakiyeniz (TL): ")) #Kusuratli olabilecegi icin float yapiyoruz
hesap1 = Hesap(ad_soyad, hesap_no, baslangic_bakiye) #Hesap sinifindan bir nesne uretiyoruz

secim = "" #Dongunun baslayabilmesi icin secim degiskenine baslangic degeri veriyoruz
while secim != "4": #Kullanici 4e basmadigi surece menu tekrar ekrana gelir
    print("\nIslem Menusu")
    print("1 - Para Yatir")
    print("2 - Para Cek")
    print("3 - Bakiye Goruntule")
    print("4 - Cikis")

    secim = input("Yapmak istediginiz islemi secin: ") 

    if secim == "1": #1 secildiyse para yatirma islemini yapiyoruz
        tutar = float(input("Yatirmak istediginiz tutar: "))
        hesap1.para_yatir(tutar) #Nesnenin para_yatir metodunu cagiriyoruz
    elif secim == "2": #2 secildiyse para cekme islemini yapiyoruz
        tutar = float(input("Cekmek istediginiz tutar: "))
        hesap1.para_cek(tutar) #Nesnenin para_cek metodunu cagiriyoruz
    elif secim == "3": # 3secildiyse bakiye ve hesap bilgilerini gosteriyoruz
        hesap1.bakiye_goruntule()
    elif secim == "4": # 4 ecildiyse cikis mesaji verip donguyu bitiriyoruz
        print("Cikis yapiliyor!")
    else: #1-4 disinda bir sey girilirse uyari veriyoruz
        print("Hatali secim yaptiniz, lutfen 1 ile 4 arasinda bir deger girin.")