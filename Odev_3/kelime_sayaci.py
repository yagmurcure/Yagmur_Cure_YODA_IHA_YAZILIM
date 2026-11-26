# Ayni kelimenin farkli yazimlarini ayri kelimeler gibi saymamak icin tum metni kucuk harfe cevirmeye karar verdim. yani bu program case-sensitive degil

metin = input("Bir cumle veya paragraf girin: ") #Kullanicidan metni string olarak aliyoruz
karakter_sayisi = len(metin) #Bosluklar dahil toplam karakter sayisini len() ile hesapliyoruz

kucuk_metin = metin.lower() #Harf farki olmasin diye tum karakterleri kucuk harfe ceviriyoruz

noktalamalar = [".", ",", "!", "?", ";", ":"] #Kelimelere yapisabilecek temel noktalama isaretlerini listeledik
for isaret in noktalamalar: #Listedeki her bir noktalama isaretini sirayla geziyoruz
    kucuk_metin = kucuk_metin.replace(isaret, " ") #Metindeki noktalama isaretlerini siliyoruz
kelimeler = kucuk_metin.split() #Metni bosluklardan parcalayip kelimelerden olusan bir liste yapiyoruz
kelime_sayisi = len(kelimeler) #Listedeki eleman sayisi toplam kelime sayisini verir

en_uzun = 0 #En uzun kelimenin uzunlugunu tutmak icin baslangic degerini 0 yapiyoruz
kelime_tekrarlari = {} #Her kelimenin kac kez gectigini tutmak icin bos bir sozluk olusturuyoruz

for kelime in kelimeler: #Kelimeler listesindeki her kelimeyi tek tek geziyoruz
    if len(kelime) > en_uzun: #Siradaki kelimenin uzunlugu mevcut en uzun degerden buyuk mu kontrol ediyoruz
        en_uzun = len(kelime) #buyukse yeni en uzun uzunluk olarak bunu kaydediyoruz

    if kelime in kelime_tekrarlari: #Kelime sozlukte daha onceden eklenmis mi kontrol ediyoruz
        kelime_tekrarlari[kelime] += 1 #Zaten varsa tekrar sayisini 1 artiriyoruz
    else: #Kelime sozlukte yoksa bu blok calisir
        kelime_tekrarlari[kelime] = 1 #Kelimeyi sozluge ilk kez 1 degeriyle ekliyoruz

print(f"Toplam kelime sayisi: {kelime_sayisi}") #Toplam kelime sayisini ekrana yazdiriyoruz
print(f"Toplam karakter sayisi: {karakter_sayisi}") #Bosluklar dahil karakter sayisini yazdiriyoruz
print(f"En uzun kelimenin uzunlugu: {en_uzun}") #En uzun kelimenin karakter sayisini yazdiriyoruz

print("Kelime Tekrarlari:") #Kelime frekanslari icin alt baslik yazdiriyoruz
for kelime in kelime_tekrarlari: #Sozlukteki her kelimeyi sirayla geziyoruz
    print(f"{kelime}: {kelime_tekrarlari[kelime]} kez") #Kelimeyi ve o kelimenin sozlukteki degerini (adedini) yazdiriyoruz