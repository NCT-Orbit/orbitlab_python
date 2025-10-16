### Giriş

Bir programın karar verebilmesi için koşulları değerlendirmesi gerekir.
Python’da bu karar yapıları, karşılaştırma ve mantıksal (logical) operatörler aracılığıyla kurulur.
Bu tür ifadelerin sonucu daima iki değerden biridir: True (Doğru) veya False (Yanlış).

Mantıksal değerler, programların akışını yönlendiren if, while gibi yapılarda sıkça kullanılır.

---

### Karşılaştırma Operatörleri

Karşılaştırma operatörleri iki değeri karşılaştırır ve sonucu True veya False olarak döndürür.


|Operatör            | Anlamı              | Örnek                | Sonuç        |
|:----------------   |:--------------------|:---------------------|:-------------|
| ==                 | eşittir             | 10 == 10             | True         |
| !=                 | eşit değildir       | 5 != 3               | True         |
| >                  | büyüktür            | 8 > 6                | True         |
| <                  | küçüktür            | 4 < 2                | False        |
| >=                 | büyük veya eşit     | 3 >= 5               | True         |
| <=                 | küçük veya eşit     | 7 <= 3               | False        |


Örnek :
```python
batarya_seviyesi = 50
sicaklik = 28
sistem_hatasi = False

print("Batarya yeterli mi?", batarya_seviyesi > 72)
print("Sıcaklık güvenli mi?", sicaklik < 35)
print("Sistem hatasız mı?", sistem_hatasi == False)

```
Çıktı :
```python
Batarya yeterli mi? False
Sıcaklık güvenli mi? True
Sistem hatasız mı? True
```

---

### Mantıksal Operatörler

Birden fazla koşulu aynı anda kontrol etmek için mantıksal operatörler kullanılır.

|Operatör            | Anlamı                           | Örnek                | Sonuç        |
|:----------------   |:---------------------------------|:---------------------|:-------------|
| and                | ve (tüm koşullar doğruysa True)  | (x > 0) and (y > 0)  | True         |
| or                 | veya (en az biri doğruysa True)  | (x > 0) or (y > 0)   | True         |
| not                | değil (True’yi False yapar)      | not True             | False        |

Örnek :

```python
batarya = 80
sicaklik = 29
sistem_stabil = True

hazir = (batarya > 60) and (sicaklik < 35) and sistem_stabil
print("Sistem çalışmaya hazır mı?", hazir)
```

---

### Metinlerin (String) Karşılaştırılması

Python’da yalnızca sayılar değil, metinler de karşılaştırılabilir.
Metin karşılaştırmaları alfabetik (lexicographical) düzene göre yapılır.

```python
gorev1 = "Analiz"
gorev2 = "Test"

print(gorev1 == gorev2)   # False
print(gorev1 != gorev2)   # True
print(gorev1 < gorev2)    # True ('A' harfi 'T'den önce gelir)

```

---


### Boolean Değerlerle Karar Verme

Boolean değişkenler, bir sistemin durumunu temsil etmek için sıkça kullanılır.

```python
guncelleme_var = True
internet_var = False

if guncelleme_var and internet_var:
    print("Sistem güncelleniyor...")
else:
    print("Güncelleme ertelendi.")

```

Çıktı:

```python
Güncelleme ertelendi.
```

---

### Uygulamalı Örnek

Aşağıdaki örnek, bir endüstriyel sistemin güvenli çalışma koşullarını değerlendirir.

```python
sicaklik = 42
basinc = 1.9
acil_durdurma = False

# Güvenli çalışma koşullarını kontrol et
guvenli_mi = (sicaklik < 50) and (basinc < 2.5) and (not acil_durdurma)

if guvenli_mi:
    print("✅ Sistem güvenli şekilde çalışıyor.")
else:
    print("⚠️ Uyarı: Sistem değerleri güvenli sınırların dışında!")

```

---


### Mantıksal (Boolean) Doğruluk Tabloları

| A                    | B       | A and B   | A or B        |
|:---------------------|:--------|:----------|:--------------|
| True                 | True    | True      | True          |
| True                 | False   | False     | True          |
| False                | True    | False     | True          |
| False                | False   | False     | False         |


not Operatörü

| İfade                | Sonuç   |
|:---------------------|:--------|
| not True             | False   |
| not False            | True    |


💡 İpucu:

Koşullar karmaşık hale geldiğinde, her adımı ayrı bir değişkene atayarak kodun okunabilirliğini artırabilirsin:

```python 
pil_yeterli = batarya > 60
sicaklik_uygun = sicaklik < 35
hazir = pil_yeterli and sicaklik_uygun
```


!!! info "ÖRNEK UYGULAMALAR" 
    Örnek uygulamalar için <a href="/orbitlab_python/python-egitimi-konu-anlatim/assets/logical_booleans.pdf" target="_blank">tıklayınız</a>

