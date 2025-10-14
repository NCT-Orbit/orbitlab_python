### Giriş

Python’da birden fazla veriyi tek bir yapı içinde saklamak istiyorsak list veri türünü kullanırız.
Listeler, köşeli parantezler [ ] içinde yazılır ve öğeler virgülle ayrılır.

```python
gorevler = ["Veri topla", "Sensörleri kontrol et", "Rapor oluştur"]
print(gorevler)

```

Listeler, metin, sayı, hatta başka listeler gibi farklı veri türlerini aynı anda tutabilir.
Bu esneklik, listeleri Python’daki en güçlü veri yapılarından biri haline getirir.

---


### Liste Ögelerine Erişim

Bir listedeki öğelere indeks (index) numarasıyla ulaşılır.
İndeksler 0’dan başlar — yani ilk eleman 0, ikinci eleman 1, üçüncü eleman 2 indeksindedir.

```python
gorevler = ["Veri topla", "Sensörleri kontrol et", "Rapor oluştur"]

print(gorevler[0])  # İlk öğe
print(gorevler[1])  # İkinci öğe
print("Toplam görev sayısı:", len(gorevler))

```

📘 Not: len() fonksiyonu bir listenin uzunluğunu, yani içindeki öğe sayısını döndürür.

---

### Negatif İndeksler

Python’da indeksler sadece baştan değil, sondan da okunabilir.
Negatif indeksler kullanarak listeyi ters yönden erişebilirsin.

```python
gorevler = ["Veri topla", "Sensörleri kontrol et", "Rapor oluştur", "Yazılımı güncelle"]

print(gorevler[-1])  # Son öğe
print(gorevler[-2])  # Sondan ikinci öğe
```

Bu yöntem, özellikle uzun listelerde son elemanlara ulaşmak için oldukça pratiktir.

---

### Liste Öğelerini Güncelleme

Listelerdeki öğeler değiştirilebilir (mutable) yapıdadır.
Yani bir listedeki herhangi bir elemanı doğrudan yeni bir değerle güncelleyebilirsin.

```python
gorevler = ["Veri topla", "Sensörleri kontrol et", "Rapor oluştur"]
print("Eski liste:", gorevler)

gorevler[1] = "Kamerayı kalibre et"  # 2. öğeyi değiştir
print("Yeni liste:", gorevler)

```

---


### Liste Öğelerini Güncelleme

Listelerdeki öğeler değiştirilebilir (mutable) yapıdadır.
Yani bir listedeki herhangi bir elemanı doğrudan yeni bir değerle güncelleyebilirsin.

```python
gorevler = ["Veri topla", "Sensörleri kontrol et", "Rapor oluştur"]
print("Eski liste:", gorevler)

gorevler[1] = "Kamerayı kalibre et"  # 2. öğeyi değiştir
print("Yeni liste:", gorevler)

```

---

### Listeye Yeni Öğeler Ekleme

Yeni bir öğe eklemek için append() metodunu kullanırız.
Bu metot, öğeyi her zaman listenin sonuna ekler.

```python
gorevler = ["Veri topla", "Rapor oluştur"]
gorevler.append("Verileri buluta yükle")
print(gorevler)
```

İstersen insert() metoduyla belirli bir indekse de öğe ekleyebilirsin:

```python
gorevler.insert(1, "Sensörleri başlat")
print(gorevler)

```

---

### Listeyi Çoğaltma

Bir öğeyi birden fazla kez tekrarlayarak liste oluşturmak için * operatörünü kullanabiliriz.
```python
puanlar = [0] * 5
print("Başlangıç puanları:", puanlar)
```

Bu yöntem, örneğin başlangıçta tüm skorların 0 olduğu bir tablo oluşturmak için oldukça kullanışlıdır.

---

### Liste Öğelerini Silme

Bir listedeki öğeleri silmek için birkaç yöntem vardır:

```python
gorevler = ["Veri topla", "Rapor oluştur", "Yazılımı güncelle"]

del gorevler[1]         # İkinci öğeyi siler
gorevler.remove("Veri topla")  # Belirli bir değeri siler
print(gorevler)

```

---

### Özet

|İşlem/ Fonksiyon            | Açıklama                  | Örnek       |
|:---------------------------|:--------------------------|:------------|
| []                         | Liste tanımlar            | liste = [1,2,3]|
| liste[i]                   | İndeksle öğeye erişim     | liste[0] → 1  |
| len(liste)                 | Liste Uzunluğu            | len([1,2,3]) → 3 |
| append()                   | Liste sonuna öğe ekler    | liste.append(4) |
| insert(i,x)                | Belirli konuma öğe ekler  | liste.insert(1,5) |
| *                          | Listeyi çoğaltır          | [0] * 5 |
| del, remove()              | Öğeleri siler             |  del liste[0]  |

---

!!! info "ÖRNEK UYGULAMALAR" 
    Örnek uygulamalar için <a href="/python-egitimi-konu-anlatim/assets/lists.pdf" target="_blank">tıklayınız</a>
