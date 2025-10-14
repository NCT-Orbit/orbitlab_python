### Giriş

Programlama yalnızca işlemleri sırayla yürütmek değildir; aynı zamanda belirli koşullara göre karar verebilmeyi de içerir.
Python’da bu karar verme yapısı, if, elif ve else ifadeleriyle sağlanır.

Bu yapı sayesinde program, farklı durumlara göre farklı sonuçlar üretebilir — tıpkı gerçek dünyada “Eğer ... olursa, o zaman ...” şeklinde düşünen bir sistem gibi.

---

### if ve else Temelleri

if ifadesi bir koşulu test eder.
Koşul doğruysa (True) altındaki kod bloğu çalışır.
Aksi durumda (False), else bloğu devreye girer.

```python
sicaklik = 10

if sicaklik < 15:
    print("Hava soğuk — ısıtıcı devreye alınıyor.")
else:
    print("Hava ılık — sistem normal modda.")

```

Çıktı:

```python
Hava soğuk — ısıtıcı devreye alınıyor.
```

---

### elif ile Çoklu Koşullar

Birden fazla durumu kontrol etmek istiyorsak, elif (else if) yapısını kullanırız.
Python bu koşulları sırayla değerlendirir — ilk doğru koşul bulunduğunda diğerleri kontrol edilmez.

```python
enerji = 65

if enerji > 80:
    print("Enerji yüksek — sistem tam kapasitede çalışıyor.")
elif enerji > 50:
    print("Enerji orta seviyede — tasarruf modu aktif.")
else:
    print("Enerji düşük — acil şarj gerekiyor.")

```

---

### Mantıksal Operatörlerle Koşul Birleştirme

Birden fazla şartı aynı anda değerlendirmek için mantıksal operatörler (and, or, not) kullanılabilir.

```python
sicaklik = 25
nem = 60

if sicaklik > 20 and nem < 70:
    print("Koşullar uygun — üretim başlatılıyor.")
else:
    print("Uyarı: Ortam koşulları uygun değil.")

```

---

and : Her iki koşul da doğru olmalıdır.
or : En az biri doğruysa koşul sağlanır.
not : Sonucun tersini alır.


---

### Listelerde Koşul Kontrolü (in Operatörü)

in anahtar sözcüğü, bir öğenin bir koleksiyonun içinde olup olmadığını kontrol eder.

```python
izinli_personeller = ["Ali", "Zehra", "Can"]

if "Can" in izinli_personeller:
    print("Can bugün izinli. Görev devri yapılıyor.")
else:
    print("Can görevde. Sistem aktif.")

```

---

### Kullanıcıdan Veri Alarak Koşul Kurmak

Kullanıcı girdisi ile karar verme sistemleri geliştirilebilir.
Python’da input() fonksiyonu kullanıcıdan veri alır.
Girdi sayısal bir değer olacaksa int() ile dönüştürülmelidir.

```python
sicaklik = int(input("Ortam sıcaklığını gir (°C): "))
hava = input("Hava durumu (Güneşli/Bulutlu/Yağmurlu): ")

if sicaklik > 25 and hava.lower() == "güneşli":
    print("Soğutma sistemi devreye alındı.")
elif sicaklik < 10 or hava.lower() == "yağmurlu":
    print("Isıtma sistemi aktif.")
else:
    print("Sistem standart çalışma modunda.")

``` 

---

### Gerçekçi Senaryo: Akıllı Fabrika Kontrolü

Aşağıdaki örnek, bir üretim tesisinin çalışma koşullarını değerlendirir.
Tüm koşullar gerçek zamanlı sensör verilerini temel alır.

```python
enerji = 78
basinc = 1.5
ariza_var = False

if enerji < 40:
    print("⚠️ Enerji seviyesi düşük! Üretim durduruluyor.")
elif basinc > 2:
    print("⚠️ Basınç kritik seviyede! Güvenlik valfi açılıyor.")
elif not ariza_var:
    print("✅ Sistem kararlı. Üretim devam ediyor.")
else:
    print("🔧 Arıza tespit edildi. Bakım modu aktif.")

```

---

###  Çoklu Koşulların Bağımsız Kullanımı

Bazı durumlarda tüm if bloklarının birbirinden bağımsız çalışması gerekir.
Bu durumda her koşul ayrı if olarak yazılır (tek bir zincir değil).

```python
gun = "Cuma"
sicaklik = 32
mesai_var = True

if gun == "Cuma":
    print("Hafta sonu yaklaşıyor.")
if sicaklik > 30:
    print("Hava çok sıcak, klima açık kalmalı.")
if mesai_var:
    print("Ek vardiya planı aktif.")

```

!!! info "ÖRNEK UYGULAMALAR" 
    Örnek uygulamalar için <a href="/python-egitimi-konu-anlatim/assets/if_statements.pdf" target="_blank">tıklayınız</a>