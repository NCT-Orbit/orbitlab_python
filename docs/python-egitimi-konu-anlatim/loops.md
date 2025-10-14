### Giriş
Programlama dillerinde döngüler (loops), belirli işlemleri birden fazla kez tekrarlamak için kullanılır.
+ Python’da en sık kullanılan iki döngü türü şunlardır:

+ for döngüsü → belirli bir veri kümesini sırayla işler.

+ while döngüsü → bir koşul doğru olduğu sürece devam eder.

+ Döngüler, veri listelerini okumaktan sensör verilerini analiz etmeye kadar birçok alanda kullanılır.

---
### for Döngüsü Temelleri

for döngüsü, bir koleksiyonun (liste, dizi, metin vb. ) elemanlarını sırayla işler. 
Her yinelemede (iteration), listedeki bir öğeye erişilir ve tanımlanan işlemler yapılır.

Örnek
```python
gorevler = ["Veri alımı", "Filtreleme", "Kayıt analizi"]

for gorev in gorevler:
    print("Görev tamamlandı:", gorev)

```

Çıktı:
```python
Görev tamamlandı: Veri alımı
Görev tamamlandı: Filtreleme
Görev tamamlandı: Kayıt analizi

```

💡 Döngü, listedeki her elemanı sırayla işler.
Listenin sonuna gelindiğinde döngü otomatik olarak durur.

---

### Sayısal Aralıklarla Döngü Kurmak

`range()` fonksiyonu belirli bir aralıkta sayılar üretir.
Bu sayılar üzerinde döngü kurarak tekrar sayısını kontrol edebilirsin.

```python
for i in range(1, 6):
    print(f"{i}. ölçüm tamamlandı."
```

Çıktı:
```python
1. ölçüm tamamlandı.
2. ölçüm tamamlandı.
3. ölçüm tamamlandı.
4. ölçüm tamamlandı.
5. ölçüm tamamlandı.

```

---
### Metin Üzerinde Döngü Kurmak

Bir string (metin), karakterlerden oluşan bir listedir.
Bu nedenle her harfe sırayla erişilebilir.

```python
kelime = "Python"

for harf in kelime:
    print("Karakter:", harf)

```

Bu yöntem, karakter sayımı, analiz veya metin işleme için kullanışlıdır.

---
### Koşullu Döngü (For + If)

Döngüler, koşul ifadeleriyle birleştirilerek belirli durumlarda işlem yapabilir.
Örneğin, negatif değerleri veya belirli aralık dışındaki değerleri tespit etmek mümkündür.

```python
degerler = [15, -3, 8, -1, 0, 9]

for d in degerler:
    if d < 0:
        print("Negatif değer bulundu:", d)

```

Çıktı:

```python
Negatif değer bulundu: -3
Negatif değer bulundu: -1

```

---
### Kümülatif Toplam (Birikimli Hesaplama)

Döngüler, verileri birleştirerek veya toplayarak ilerleyen bir sonucu hesaplamak için kullanılabilir.

```python
enerji_degerleri = [10, 15, 20, 5]
birikimli = 0
birikim_listesi = []

for e in enerji_degerleri:
    birikimli += e
    birikim_listesi.append(birikimli)

print("Birikimli enerji listesi:", birikim_listesi)

```
Çıktı:
```python
Birikimli enerji listesi: [10, 25, 45, 50]

```

---
### while Döngüsü Temelleri

while döngüsü, belirtilen koşul True olduğu sürece çalışır.
Koşul False olduğunda döngü sona erer.

```python
sayac = 0

while sayac < 5:
    print("Sayaç değeri:", sayac)
    sayac += 1

```

Çıktı:
```python
Sayaç değeri: 0
Sayaç değeri: 1
Sayaç değeri: 2
Sayaç değeri: 3
Sayaç değeri: 4

```

---
### Döngü Kontrol Komutları

Python’da iki önemli döngü kontrol ifadesi bulunur:

break → Döngüyü anında sonlandırır.
continue → Mevcut adımı atlayarak bir sonraki yinelemeye geçer.

```python
for sayi in range(10):
    if sayi == 5:
        break
    print(sayi)

```

→ 0’dan 4’e kadar yazdırır, 5’e geldiğinde döngü biter.

```python
for sayi in range(6):
    if sayi == 3:
        continue
    print(sayi)

```
→ 0, 1, 2, 4, 5 değerlerini yazdırır (3 atlanır).


---
### İç İçe Döngüler

Bir döngü içinde başka bir döngü tanımlayabiliriz.
Bu yapı genellikle matris veya tablo işlemlerinde kullanılır.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"Hücre [{i},{j}] işlendi.")

```

💡 İpucu:
Liste veya dizilerle çalışırken, aynı anda hem indeksi hem de değeri almak için enumerate() fonksiyonunu kullanabilirsin.

```python
sensor_degerleri = [3.2, 3.5, 3.8]

for i, deger in enumerate(sensor_degerleri, start=1):
    print(f"{i}. sensör değeri: {deger}")

```

!!! info "ÖRNEK UYGULAMALAR" 
    Örnek uygulamalar için <a href="/python-egitimi-konu-anlatim/assets/loops.pdf" target="_blank">tıklayınız</a>