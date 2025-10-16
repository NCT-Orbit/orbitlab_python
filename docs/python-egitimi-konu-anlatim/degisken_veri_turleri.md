### Değişken Nedir?

Bir program çalışırken bilgileri geçici olarak bellekte tutar.
Python’da bu bilgileri saklamak için değişkenler (variables) kullanılır.
Her değişken bir isim ve değer ikilisinden oluşur.

```python
sensor_name = "LDR"
sensor_value = 720
max_value = 1023
min_value = 0
```

---

### Temel Veri Türleri

Python’da her değerin bir türü vardır.
En sık kullanılan dört temel veri türü:

|Veri Türü       | Açıklama                           | Örnek         |
|:---------------|:-----------------------------------| :------------|
|str             | Metinleri (string) ifade eder.     |"Merhaba", 'LDR' |
|int             | Tam sayıları (integer) ifade eder. |0, 42, -7 |
|float           | Ondalıklı sayıları (floating point) ifade eder.|3.14, 87.5 |
|bool            | Mantıksal değerleri (boolean) ifade eder. |True, False|

---

### type() Fonksiyonu

Bir değişkenin hangi veri türüne ait olduğunu anlamak için type() fonksiyonu kullanılır.

```python
temperature = 24.6
print("Sıcaklık:", temperature)
print("Veri tipi:", type(temperature))
```

Çıktı:

```python
Sıcaklık: 24.6
Veri tipi: <class 'float'>
```

Bu fonksiyon, özellikle sensör verilerini işlerken doğru türde işlem yapıldığını kontrol etmek için kullanışlıdır.

---

### Mantıksal (Boolean) Değerler

Mantıksal değerler yalnızca True (doğru) veya False (yanlış) olabilir.
Sıklıkla bir koşulun gerçekleşip gerçekleşmediğini belirtmek için kullanılır.

```python
kapak_kapali_mi = True
pil_zayif_mi = False

print("Kapak kapalı mı?", kapak_kapali_mi)
print("Pil zayıf mı?", pil_zayif_mi)
```

Bu tür değişkenler karar yapılarında sıkça kullanılır.

```python
if pil_zayif_mi:
    print("⚠️ Pil değiştirilmeli!")
else:
    print("🔋 Pil seviyesi yeterli.")
```

### Formatlı Yazdırma (f-string)

Python’da f-string (formatted string literal) yapısı, değişkenleri metinlerin içine doğrudan yerleştirmeyi sağlar.
Bu sayede çıktılar daha okunabilir ve düzenli olur.

```python
device_name = "Servo Motor"
rotation_angle = 90
current_value = 1.35

print(f"""
📄 Cihaz Raporu
--------------------
Adı: {device_name}
Açı: {rotation_angle}°
Akım: {current_value} A
Durum: {'Aktif' if rotation_angle > 0 else 'Kapalı'}
""")

```

---

!!! info "ÖRNEK UYGULAMALAR" 
    Örnek uygulamalar için <a href="/orbitlab_python/python-egitimi-konu-anlatim/assets/degiskenler_veri_turleri.pdf" target="_blank">tıklayınız</a>
