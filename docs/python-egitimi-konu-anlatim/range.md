### Giriş

Programlama dillerinde tekrarlayan işlemler genellikle sayı dizileri üzerinden yürütülür.
Python’da bu amaçla kullanılan en önemli araç range() fonksiyonudur.

range() belirli bir aralıktaki tamsayıları üretir ve genellikle for döngüsü ile birlikte kullanılır.
Bu sayede döngülerin kaç kez çalışacağını, hangi değerden başlayacağını ve hangi adımlarla ilerleyeceğini kolayca kontrol ederiz.

---

### Temel Kullanım: range(stop)

En basit kullanımda range() yalnızca bir bitiş değeri (stop) alır.
Üretilen sayılar 0’dan başlar ve bitiş değerine kadar (hariç) artar.

```python
for i in range(5):
    print("Adım:", i)
```

Çıktı:

```python
Adım: 0
Adım: 1
Adım: 2
Adım: 3
Adım: 4

```

💡 range(5) → [0, 1, 2, 3, 4] değerlerini üretir.
Bu yapı, tekrarlama sayısı belli olan döngüler için oldukça kullanışlıdır.

---

### Başlangıç ve Bitiş Belirleme: range(start, stop)

İstersen sayı dizisinin başlangıç değerini de belirtebilirsin.
Bu durumda, başlangıç değeri dahil, bitiş değeri hariç olacak şekilde sayılar üretilir.

```python
for sayi in range(3, 8):
    print("Değer:", sayi)
```

Çıktı:
```python
Değer: 3
Değer: 4
Değer: 5
Değer: 6
Değer: 7

```

💡 range(3, 8) → 3’ten 7’ye kadar olan sayıları üretir.

---

### Artış (Adım) Belirleme: range(start, stop, step)

Üçüncü parametre olan adım (step) değeri, artış miktarını belirtir.
Bu sayede belirli aralıklarla sayılar üretilebilir.

```python
for sayi in range(0, 10, 2):
    print("Çift sayı:", sayi)

```
Çıktı:

```python
Çift sayı: 0
Çift sayı: 2
Çift sayı: 4
Çift sayı: 6
Çift sayı: 8
```

💡 `range(0, 10, 2)` → 0, 2, 4, 6, 8 değerlerini üretir.
Adım değeri pozitifse dizi artan, negatifse azalan şekilde ilerler.

---
### Geri Sayım: Negatif Adım Kullanımı

Adım değeri negatif verilirse, range() geriye doğru sayar.
Bu özellik geri sayımlar veya azalan diziler oluşturmak için kullanılır.

```python
for saniye in range(10, 0, -1):
    print("Geri sayım:", saniye)

print("Kalkış tamamlandı 🚀")
```

Çıktı:

```python
Geri sayım: 10
Geri sayım: 9
...
Geri sayım: 1
Kalkış tamamlandı 🚀

```

💡 range(10, 0, -1) → 10’dan 1’e kadar olan sayıları üretir.
Son değer (0) dahil edilmez.

---

### range() ile Koşullu İşlemler

range() genellikle koşul ifadeleriyle birlikte kullanılarak belirli türdeki sayıları seçmek için kullanılır.
Örneğin, tek ve çift sayıları ayırt etmek mümkündür:

```python
for sayi in range(1, 11):
    if sayi % 2 == 0:
        print(f"{sayi} → Çift sayı")
    else:
        print(f"{sayi} → Tek sayı")
```

Çıktı:

```python
1 → Tek sayı
2 → Çift sayı
3 → Tek sayı
...
10 → Çift sayı

```

💡 `%` işareti modül (kalan) operatörüdür: `sayi % 2 == 0` ifadesi sayının çift olup olmadığını kontrol eder.  
Detaylı anlatım için [Numbers – Modül (Kalan) İşlemi](/python-egitimi-konu-anlatim/numbers/#modula-kalan-islemi) konusuna göz atın.

---

### range()’in Listeye Dönüştürülmesi

range() nesnesi doğrudan bir liste değildir, ancak list() fonksiyonu ile kolayca dönüştürülebilir.

```python
sayilar = list(range(5, 15))
print(sayilar)
```
Çıktı:
```python
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
```

💡 Bu yöntem, oluşturulan sayı aralığını saklamak veya üzerinde işlem yapmak için kullanışlıdır.
---
### İleri Düzey Kullanım: Döngü Kontrolüyle Birleştirme
range() genellikle break ve continue ifadeleriyle birleştirilerek daha esnek döngü yapıları oluşturulur.

```python
for sayi in range(1, 11):
    if sayi == 5:
        continue  # 5’i atla
    if sayi == 9:
        break     # 9’da döngüyü bitir
    print("İşlenen sayı:", sayi)
```
Çıktı:
```python
İşlenen sayı: 1
İşlenen sayı: 2
İşlenen sayı: 3
İşlenen sayı: 4
İşlenen sayı: 6
İşlenen sayı: 7
İşlenen sayı: 8
```

---
### Özet

Bu bölümde, Python’daki range() fonksiyonunun temellerini öğrendik:

| Kullanım                   | Açıklama                                  | Örnek                 |          
|:---------------------------|:------------------------------------------|:----------------------|       
| range(stop)                | 0’dan stop değerine kadar sayılar üretir  | range(5) → 0–4        |
| range(start, stop)         | Başlangıç ve bitiş belirtilir             | range(3, 8) → 3–7     |
| range(start, stop, step)   | Belirli adımlarla artar veya azalır       | range(0, 10, 2)       |
| Negatif adım               | Geriye doğru sayım yapar                  | range(10, 0, -1)      |

💡 İpucu: Eğer döngüde sadece belirli adımların çalışması gerekiyorsa, range() parametrelerini dikkatli seçerek gereksiz hesaplamaları önleyebilirsin. 
Örneğin, yalnızca çift sayılar için range(0, n, 2) ifadesi performans açısından en verimli çözümdür.
---
!!! info "ÖRNEK UYGULAMALAR" 
    Örnek uygulamalar için <a href="/python-egitimi-konu-anlatim/assets/range.pdf" target="_blank">tıklayınız</a>

