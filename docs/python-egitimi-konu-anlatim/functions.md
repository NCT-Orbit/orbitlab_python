### Giriş

Python’da fonksiyonlar, bir işi tanımlayıp ihtiyaç duyduğunda tekrar kullanmanı sağlayan kod bloklarıdır.
Böylece kodlar hem daha düzenli, hem de tekrar kullanılabilir hale gelir.

Bir fonksiyon, def anahtar kelimesiyle tanımlanır ve adıyla çağrılır:

```python
def selamla():
    print("Merhaba, Python öğrenmeye hazırım!")

selamla()  # Fonksiyon çağrılır

```

Fonksiyon bir kez tanımlandıktan sonra istediğin kadar çağrılabilir.


---
### Parametreli Fonksiyonlar

Fonksiyonlar dışarıdan bilgi (parametre) alarak farklı durumlarda kullanılabilir.
Örneğin, verilen sayının çift mi tek mi olduğunu kontrol eden bir fonksiyon:

```python
def cift_mi(sayi):
    if sayi % 2 == 0:
        print(f"{sayi} çift sayıdır ✅")
    else:
        print(f"{sayi} tek sayıdır ❗")

cift_mi(12)
cift_mi(7)

```

Çıktı:
```python
12 çift sayıdır ✅
7 tek sayıdır ❗
```

💡 % işareti modül (kalan) operatörüdür:
sayi % 2 == 0 ifadesi, sayının çift olup olmadığını kontrol eder.
Detaylı anlatım için [Numbers – Modül (Kalan) İşlemi](/python-egitimi-konu-anlatim/numbers/#modula-kalan-islemi)
konusuna göz atın.

---

### Değer Döndüren Fonksiyonlar 

Bazı fonksiyonlar sonucu ekrana yazdırmak yerine geri döndürür.
Bu, sonucu başka bir işlemde kullanmamızı sağlar.

```python
def topla(a, b):
    return a + b

sonuc = topla(8, 5)
print("Toplam:", sonuc)
```

`return`, fonksiyonun dışına veri göndermek için kullanılır.

---

### Birden Fazla İşlem Fonksiyonu 

Birden fazla işlemi fonksiyonlarla ayrı ayrı tanımlayabilir ve tekrar kullanılabilir hale getirebilirsin.

```python
def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    if b != 0:
        return a / b
    else:
        return "❗Sıfıra bölünemez!"

print("➕ 10 + 5 =", topla(10, 5))
print("➖ 10 - 5 =", cikar(10, 5))
print("✖ 10 × 5 =", carp(10, 5))
print("➗ 10 ÷ 5 =", bol(10, 5))
```

Bu yapı, “mini hesap makinesi” gibi gerçek uygulamalarda temel bir yaklaşımdır.

---
### Kullanıcı Girdisiyle Fonksiyon Kullanımı

Fonksiyonlar, kullanıcıdan alınan bilgileri işlemek için de kullanılabilir.
Örneğin, girilen kelimenin uzunluğunu ölçen bir program:

```python
def kelime_uzunlugu(kelime):
    return len(kelime)

girdi = input("Bir kelime yaz: ")
uzunluk = kelime_uzunlugu(girdi)

print(f"'{girdi}' kelimesi {uzunluk} harf içeriyor.")
```

Burada:

+ input() → kullanıcıdan bilgi alır

+ len() → karakter sayısını ölçer

+ return → sonucu dışarıya gönder

---

### Fonksiyonlarla Basit Hesap Makinesi

Gerçek bir örnek olarak, kullanıcıdan iki sayı alıp seçilen işleme göre uygun fonksiyonu çağırabiliriz:

```python
def topla(a, b): return a + b
def cikar(a, b): return a - b
def carp(a, b): return a * b
def bol(a, b): return a / b if b != 0 else "❗Sıfıra bölünemez!"

print("Yapmak istediğin işlem: topla / çıkar / çarp / böl")
islem = input("👉 İşlem türü: ")

sayi1 = float(input("Birinci sayı: "))
sayi2 = float(input("İkinci sayı: "))

if islem == "topla":
    print("Sonuç:", topla(sayi1, sayi2))
elif islem == "çıkar":
    print("Sonuç:", cikar(sayi1, sayi2))
elif islem == "çarp":
    print("Sonuç:", carp(sayi1, sayi2))
elif islem == "böl":
    print("Sonuç:", bol(sayi1, sayi2))
else:
    print("❗Geçersiz işlem seçimi!")
```

---
### Özet

| Kullanım                   | Açıklama                                  | Örnek                   |          
|:---------------------------|:------------------------------------------|:------------------------|       
| def                        | Yeni fonksiyon tanımlar                   | def selamla():          |
| ()                         | Parametre alır.                           | def topla(a,b):         |
| return                     | Değer döndürür                            | return a + b            |
| input()                    | Kullanıcıdan bilgi alır                   | ad = input("İsim gir: ")|
| len()                      | Uzunluk döndürür                          | len("Python")→ 6        |
| %                          | Modül (kalan) operatörü                   | sayi%2==0               |


!!! info "ÖRNEK UYGULAMALAR" 
    Örnek uygulamalar için <a href="/orbitlab_python/python-egitimi-konu-anlatim/assets/functions.pdf" target="_blank">tıklayınız</a>

    