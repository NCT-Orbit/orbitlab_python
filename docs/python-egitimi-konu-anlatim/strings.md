### Giriş

Python’da metinlerle çalışmak için kullanılan temel veri türü string’dir.
Bir string, karakterlerin (harf, sayı, boşluk, sembol vb.) ardışık dizisidir ve "..." veya '...' tırnakları içinde yazılır.

```python
mesaj = "Python öğrenmek harika!"
print(mesaj)
```

Bu örnekte "Python öğrenmek harika!" bir string ifadedir. print() fonksiyonu ile ekrana yazdırılır.

---

### String Birleştirme (Concatenation)

Birden fazla string’i birleştirmek için + operatörü kullanılır.
Bu yöntem, metinleri dinamik biçimde oluşturmayı sağlar.

```python
isim = "Elif"
selam = "Merhaba, " + isim + "! Python dünyasına hoş geldin."
print(selam)

```
📘 **Not**: String dışındaki veriler (int, float gibi) doğrudan metinle birleştirilemez. Bu tür durumlarda str() fonksiyonuyla dönüştürme yapılır.

---

### String Tekrarlama

Bir metni belirli bir sayıda tekrarlamak için * operatörü kullanılır.
```python
banner = "✨ Hoş geldin! ✨\n"
print(banner * 2)

```
Bu kod, “Hoş geldin!” mesajını iki kez ekrana bastırır.

---

### Satır Atlama ve Biçimlendirme

Bir metinde yeni satıra geçmek için \n karakteri kullanılır.
Bu, uzun veya çok satırlı mesajları düzenli göstermeye yarar.

```python
bilgi = "Kurs Adı: Python 101\nSeviye: Başlangıç"
print(bilgi)
```
Sonuç:
 
```python
Kurs Adı: Python 101
Seviye: Başlangıç

```

---

### Metin Uzunluğu

Bir metnin toplam karakter sayısını (boşluklar dahil) öğrenmek için `len()` fonksiyonu kullanılır.

```python
cumle = "Kodlama keyiflidir."
print("Bu cümlede", len(cumle), "karakter var.")

```

Çıktı:

```python
Bu cümlede 19 karakter var.

```

---

### Kullanıcıdan Metin Almak

`input()` fonksiyonu, kullanıcıdan bilgi almak için kullanılır.
Alınan veri daima string türündedir.

```python
renk = input("Favori rengin nedir? 🎨 ")
print("Güzel seçim! " + renk + " harika bir renk.")

```

Çıktı:

```python
Favori rengin nedir? 🎨 Pembe
Güzel seçim! Pembe harika bir renk.
```

### Sayısal Girdilerle Çalışmak

Kullanıcıdan alınan sayısal değerleri işlem yapmak için `int()` veya `float()` ile dönüştürmek gerekir.
Eğer bu sayı daha sonra metinle birleştirilecekse, tekrar `str()` ile string'e çevrilir.

```python
yas = int(input("Kaç yaşındasın? "))
print("Demek " + str(yas) + " yaşındasın! Harika 🚀")

``` 
Çıktı:

```python
Kaç yaşındasın? 24
Demek 24 yaşındasın! Harika 🚀
```

--- 

### Özet

|İşlem            | Açıklama                 | Örnek       |
|:----------------|:-------------------------|:------------|
| +               | String’leri birleştirir  | "a" + "b" → "ab" |
| *               | Metni tekrarlar.         | "ha" * 3 → "hahaha" |
| \n              | Satır atlar.             | "Merhaba\nDünya" |
| len()           | Karakter sayısını verir. | len("Python")  → 6 |
| input()         | Kullanıcadan veri alır.  | input("Adın : ")   |
| str()           | Sayıyı metne çevirir.    | str(42)  →  "42" |


!!! info "ÖRNEK UYGULAMALAR" 
    Örnek uygulamalar için <a href="/orbitlab_python/python-egitimi-konu-anlatim/assets/strings.pdf" target="_blank">tıklayınız</a>



 