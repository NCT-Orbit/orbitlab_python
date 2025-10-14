### Giriş

Python, matematiksel işlemleri kolayca yapabilmemiz için sayısal veri türlerini destekler.
Bu türler temel olarak ikiye ayrılır:

+ int (integer) → tam sayılar
+ float → ondalıklı sayılar

```python
a = 10        # int
b = 4.5       # float
print(a, b)

```
Python, toplama, çıkarma, çarpma ve bölme gibi temel aritmetik işlemleri doğrudan destekler.

---

### Temel Matematiksel İşlemler

```python
x = 12
y = 3

print("Toplam:", x + y)
print("Fark:", x - y)
print("Çarpım:", x * y)
print("Bölüm:", x / y)

```
Python’da bölme işlemi (/) daima ondalıklı sonuç döndürür.
Eğer tam sayı sonucu istiyorsan // (tam bölme) operatörünü kullanabilirsin:

```python
print("Tam bölme sonucu:", x // y)

```

---

### Modula (Kalan) İşlemi

% operatörü, bir sayının başka bir sayıya bölümünden kalan değeri verir.
Bu özellikle periyodik işlemlerde (örneğin hafta günleri, döngüler, sayaçlar) kullanılır.

```python
print(10 % 7)  # 10’un 7’ye bölümünden kalan 3’tür.
print(25 % 7)  # 25’in 7’ye bölümünden kalan 4’tür.
```

Bu şekilde, her 7 adımda aynı kalanla tekrar eden bir döngü elde edilir.

---


### Sayı ve Metin Farkı

Python’da "20" (tırnak içinde) bir string,
20 (tırnaksız) ise bir sayıdır.
Bu fark, işlem türlerini değiştirir:

```python
print("20")       # Metin olarak ekrana 20 yazar.
print(20 + 20)    # Toplama işlemi → 40
print("20" + "20")  # Metin birleştirme → "2020"

```

Çıktı: 

```python
20
40
2020
```
Bu örnekte + operatörü sayılarla toplama, string’lerle birleştirme yapar.

---

### Yuvarlama İşlemleri

Ondalıklı sayıları en yakın tam sayıya yuvarlamak için round() fonksiyonu kullanılır.
İstersen belirli bir ondalık basamak sayısını da belirtebilirsin.

```python
sayi = 7.68
print(round(sayi))      # 8
print(round(sayi, 1))   # 7.7

```

Çıktı:

```python
8
7.7
```

---


### Karekök Hesaplama

Matematiksel işlemler için math modülünden yararlanabiliriz.
Bir sayının karekökünü almak için math.sqrt() fonksiyonu kullanılır.

```python
import math

deger = 25
kok = math.sqrt(deger)
print("Sayı:", deger)
print("Karekök:", kok)

```
📘  **Not**: Tam kare olmayan bir sayının karekökü ondalıklı bir sonuç döndürür.
Örneğin math.sqrt(20) → 4.4721...


---

### Sayısal Dönüştürmeler

Kullanıcıdan alınan her değer string olarak gelir.
Bu verileri işlem yapmak için int() veya float() ile dönüştürmek gerekir.

```python
sayi = int(input("Bir tam sayı gir: "))
print("Girilen sayının iki katı:", sayi * 2)

```

Çıktı:
```python
Bir tam sayı gir: 25
Girilen sayının iki katı: 50

```

Tersi durumda, bir sayıyı metinle birleştirmek istersen str() fonksiyonunu kullanmalısın:

```python
print("Sonuç: " + str(sayi))
```

---

### Özet

|İşlem/ Fonksiyon            | Açıklama                  | Örnek       |
|:---------------------------|:--------------------------|:------------|
| + - * /                    | Temel aritmetik işlemler  | a * b |
| //                         | Tam Bölme                 | 10 // 3 → 3 |
| %                          | Kalan bulur.              | 10 % 7 → 3 |
| round()                    | Sayıyı yuvarlar.          | round(4.6) → 5|
| math.sqrt()                | Karekök alır.             | math.sqrt(16) → 4.0 |
| int(), float(), str()      | Tür Dönüşüm İşlemleri     | int("5") → 5   |


---

!!! info "ÖRNEK UYGULAMALAR" 
    Örnek uygulamalar için <a href="/python-egitimi-konu-anlatim/assets/numbers.pdf" target="_blank">tıklayınız</a>
