# Orbitlab Python library

Bu yazılım, Orbit robotunu yerel ağ üzerinden Python ile kontrol etmek için geliştirilmiştir. Temel amacı, öğrencilerin fiziksel bir robotla etkileşim kurarak robotik programlama konusunda uygulamalı deneyim kazanmalarını sağlamaktır. Kütüphane, Orbit platformunun temel işlevlerini sunar: motor kontrolü, sensör verilerine erişim, robot yüz ifadesinin değiştirilmesi, ses çalma, LDR (ışığa duyarlı direnç) ayarı ve daha fazlası. Bu sayede kapsamlı ve pratik bir öğrenme deneyimi sunar. Aynı zamanda da simulasyon özelliği sahiptir.

## Yazılım gereksinimleri

1. Orbit robot: Daha fazla bilgi için [Orbitrobots](https://orbitrobots.com/) ziyaret edin
2. Python >= 3.0: Python'u indirin [Python](https://www.python.org/downloads/)

## Kurulum

```
pip install orbitlab
```
## Kullanım örneği

```python
import time
from orbitlab import OrbitDriver

orbit = OrbitDriver("<orbit_ip_address>")

orbit.set_rpm([10, -10])
time.sleep(5)
orbit.stop()
```

1. `import time`

   * Programın belirli bir süre duraklamasını sağlamak için Python’un yerleşik time modülünü içe aktarır.

2. `from orbitlab import OrbitDriver`

   * Orbit robotunu kontrol etmek için kullanılan özel OrbitDriver sınıfını içe aktarır.

3. `orbit = OrbitDriver("<orbit_ip_address>")`

   * Orbit robotuna yerel ağ üzerinden bağlantı kurar.

   * `"<orbit_ip_address>"` kısmı robotun gerçek IP adresiyle (örneğin "192.168.1.42") değiştirilmelidir.

4. `orbit.set_rpm([10, -10])`

   * Motorlara RPM komutu gönderir:

     * Sol tekerlek: 10 RPM (ileri)

     * Sağ tekerlek: -10 RPM

   * Bu durumda, sağ motor fiziksel olarak ters bağlandığı için -10 RPM komutu da onu ileri yönde hareket ettirir.

   * Sonuç olarak, her iki tekerlek de ileri aynı hızda hareket eder ve robot düz bir şekilde ileri gider (dönme yapmaz).

5. `time.sleep(5)`

   * Robotun 5 saniye boyunca hareket etmeye devam etmesini sağlar.

6. `orbit.stop()`

   * Her iki motoru da durdurarak robotu durdurur.

## RPM ve Enkoderleri Anlamak.

**RPM**, dakikadaki devir sayısı anlamına gelen **"Revolutions Per Minute"** ifadesinin kısaltmasıdır.

Bu, dönen bir nesnenin **bir dakikada kaç tam tur attığını** gösteren **dönme hızı birimidir**. Genellikle aşağıdaki gibi dönen cihazların hızını tanımlamak için kullanılır:

* **Motorlar** (örneğin: bir DC motorun 3000 RPM’de dönmesi)
* **Tekerlekler**
* **Fanlar**
* **Sabit diskler**
* **Robot aktüatörleri**

**Örnek:**

* Bir motor **60 RPM** hızında dönüyorsa, bu motorun **her saniyede 1 tam dönüş yaptığı** anlamına gelir.
* Bir robotun sol ve sağ tekerlek hızları `[10, -10] RPM` olarak ayarlandığında:

  * Sol tekerlek 10 RPM ile ileri döner
  * Sağ tekerlek -10 RPM ile geri döner → bu da robotun **yerinde dönmesini** sağlar


**Motor enkoderleri**, motorlara bağlı olan ve **milin dönüşünü ölçen sensörlerdir**. Bu sayede motorun **konumu**, **hızı** ve **dönüş yönü** hakkında bilgi edinilebilir.

---

**Motor Enkoderleri Ne İşe Yarar?**

Motorun dönme hareketini **elektrik sinyallerine** çevirir ve bu sinyaller bir mikrodenetleyici, motor sürücü ya da kontrol sistemi tarafından okunabilir.

---

**Enkoderler Neden Önemlidir?**

Geri bildirim (feedback) sağlayarak:

* Motorun **ne kadar döndüğünü** anlayabiliriz (konum kontrolü)
* **Ne kadar hızlı döndüğünü** ölçebiliriz (hız kontrolü)
* Robot, tekerlek, kol gibi sistemlerin **kesin hareketlerini** kontrol edebiliriz
* **Kapalı çevrim kontrol** (örneğin PID) sistemleri kurabiliriz

---

**Kullanım Örneği:**

Eğer bir robot tekerleğine bağlı enkoder **1 turda 1000 pulse** üretiyorsa ve siz **500 pulse** saydıysanız, tekerlek **yarım tur dönmüş** demektir.

---


## Diferansiyel sürüş

**Diferansiyel sürüş**, özellikle **karasal mobil robotlarda** yaygın olarak kullanılan bir sürüş sistemidir. Bu sistemde robotun **iki bağımsız tahrikli tekerleği** bulunur (genellikle sol ve sağ), ve robot bu tekerleklerin hızıyla yönlendirilir.

---

**Temel Kavram:**

Robot, **sol ve sağ tekerleklerin hız ve yön farkına göre hareket eder ve yön değiştirir**.

---

**Nasıl Çalışır:**

| Sol Tekerlek | Sağ Tekerlek | Robotun Hareketi                     |
| ------------ | ------------ | ------------------------------------ |
| İleri        | İleri        | Düz ileri gider                      |
| Geri         | Geri         | Düz geri gider                       |
| İleri        | Durur        | Sağa döner (ekseni etrafında)        |
| Durur        | İleri        | Sola döner (ekseni etrafında)        |
| İleri        | Geri         | Yerinde döner (saat yönü veya tersi) |

---

**Donanım Yapısı:**

* **2 tahrikli tekerlek** (sol ve sağ)
* **1 veya 2 yardımcı tekerlek** (denge için, döner ama tahriksiz)
* Genellikle şu sistemlerde kullanılır: **iç mekân robotları**, **robot süpürgeler**, **eğitim robotları**, **otomatik yönlendirmeli araçlar (AGV)** vb.

---

**Avantajları:**

* Basit mekanik yapı ve kontrol
* Düz yüzeylerde iyi performans
* Tekerlek enkoderleri ile hassas konum kontrolü yapılabilir

**Dezavantajları:**

* Engebeli zeminlerde iyi çalışmaz
* Dönüşler kayarak yapılır (araba gibi direksiyonlu dönemez)

---

**Örnek:**

1. Sol tekerlek 10 RPM hızla, sağ tekerlek -10 RPM hızla dönerse, robot **yerinde döner**.

```python
import time
from orbitlab import OrbitDriver

orbit = OrbitDriver()
orbit.set_rpm([10, 10])  #sağ tekel fizksel ters -10 RPM yerine (-1 * -10) = 10 RPM
time.sleep(5)
orbit.stop()
```

2. **Çember şeklinde hareket etme**: Bir diferansiyel sürüşlü robotun çember şeklinde hareket etmesini sağlamak için, sol ve sağ tekerlekler aynı yönde fakat farklı hızlarda döndürülmelidir.

    * Hız farkı, robotun döneceği çemberin yarıçapını belirler.

    * Robot, daha yavaş dönen tekerlek yönüne doğru döner.

    `orbit.set_rpm([20, -10])`

3.  **Bir kare çizmek**
```python
import time
from orbitlab import OrbitDriver

orbit = OrbitDriver()
orbit.set_rpm([10, -10]) #ileri git
time.sleep(2)
orbit.set_rpm([10, 10])  #sag don
time.sleep(1)
orbit.set_rpm([10, -10]) #ileri git
time.sleep(2)
orbit.set_rmp([10, 10]) #sag don
time.sleep(1)
orbit.set_rpm([10, -10]) #ileri git
time.sleep(2)
orbit.set_rpm([10, 10])  #sag don
time.sleep(1)
orbit.set_rpm([10, -10]) #ileri git
time.sleep(2)
orbit.set_rmp([10, 10]) #sag don
time.sleep(1)

orbit.stop()
```
    
**for loop ile:**
```python
import time
from orbitlab import OrbitDriver
for i in range(4):
    orbit.set_rpm([10, -10]) #ileri git
    time.sleep(2)
    orbit.set_rpm([10, 10])  #sag don
    time.sleep(1)

orbit.stop()
```

## Robot hızını okumak

Önceki uygulamalarda, robotun ne kadar mesafe kat etmesi gerektiğini kontrol etmek için `time.sleep()` fonksiyonunu kullandık. Ancak bu yöntem güvenilir değildir; engeller, düzensiz yüzeyler veya motorlardaki tutarsızlıklar gibi nedenlerle hızda meydana gelen değişiklikler, robotun gerçekte kat ettiği mesafede önemli sapmalara yol açabilir.

Orbit robotu, her motorun gerçek hızını anlık olarak geri bildiren enkoderlerle donatılmıştır. Bu sayede hareket kontrolü çok daha hassas ve tutarlı bir şekilde gerçekleştirilebilir.

`orbitlab` kütüphanesini kullanarak robotun mevcut hızını okumak için `speed` modülünden faydalanabilirsiniz. Bu modül, sol ve sağ motorların dakikadaki devir sayısını (RPM - rotations per minute) temsil eden iki tam sayıdan oluşan bir liste döndürür:

```python
sol_motor_rpm, sag_motor_rpm = orbit.speed()
```

Enkoder geri bildirimi kullanarak robot programlarınızda daha hassas mesafe ve hız kontrolü sağlayabilirsiniz.

**Örnek:**

```python
import time
from orbitlab import OrbitDriver

zaman = 0.0
orbit = OrbitDriver()

orbit.set_rpm([10, 10])

while zaman <= 5.0:
    sol_motor_rpm, sag_motor_rpm = orbit.speed()
    print(f"Sol motor RPM: {sol_motor_rpm}, Sağ motor RPM: {sag_motor_rpm}")
    time.sleep(0.5)
    zaman += 0.5

orbit.stop()
```

## Diferansiyel Sürücülü Robotta Doğrusal ve Açısal Hızın Motor RPM Değerine Dönüştürülmesi

Bir diferansiyel tahrikli robotta hareket, sol ve sağ tekerleklerin dönme hızları ayarlanarak sağlanır. Belirli bir **doğrusal hız** (ileri/geri hareket) ve **açısal hız** (dönme) elde etmek için, her motorun ne kadar hızlı dönmesi gerektiğini — yani **RPM (dakikadaki devir sayısı)** cinsinden — hesaplamamız gerekir.

Bu dönüşüm, motor enkoderleriyle donatılmış Orbit gibi robotlar için oldukça önemlidir. Sabit gecikmeler kullanmak yerine, gerçek kinematik denklemlere dayanarak tekerlek hızlarını hassas bir şekilde komutlandırabiliriz.

---

**Gerekli Parametreler:**

* **v**: Robotun doğrusal hızı (m/s cinsinden)
* **ω**: Robotun açısal hızı (rad/s cinsinden)
* **r**: Tekerlek yarıçapı (metre cinsinden)
* **L**: İki tekerlek arasındaki mesafe, yani dingil açıklığı (metre cinsinden)

---

**Adım Adım Dönüştürme Süreci:**

1. **Tekerleklerin Doğrusal Hızını Hesaplayın:**

   Robotun hareketi iki tekerleğe bölünür:

   $$
   v_L = v - \frac{L}{2} \cdot \omega
   $$

   $$
   v_R = v + \frac{L}{2} \cdot \omega
   $$

   * $v_L$ ve $v_R$: Sol ve sağ tekerleklerin doğrusal hızlarıdır.

2. **Doğrusal Hızı Açısal Hıza Dönüştürün:**

   Motorlar döner hareket yaptığı için tekerlek hızını radyan/saniye (rad/s) cinsine çeviriyoruz:

   $$
   \omega_L = \frac{v_L}{r}, \quad \omega_R = \frac{v_R}{r}
   $$

3. **Açısal Hızı RPM’ye Dönüştürün:**

   RPM (dakikadaki devir sayısı) elde etmek için:

   $$
   RPM = \omega \cdot \frac{60}{2\pi}
   $$

   Yani:

   $$
   RPM_L = \omega_L \cdot \frac{60}{2\pi}, \quad RPM_R = \omega_R \cdot \frac{60}{2\pi}
   $$

---

**Örnek Python Fonksiyonu:**

Tekerlekler arasındaki yarıçap ve mesafe `orbitlab` sabit değerlerinde bulunur.

```python
import math
from orbitlab import OrbitDriver
orbit = OrbitDriver()

r = orbit.RADIUS
L = orbit.WHEEL_L

def speed_to_rpm(v, omega, r, L):
    v_l = v - (L / 2.0) * omega
    v_r = v + (L / 2.0) * omega

    omega_l = v_l / r
    omega_r = v_r / r

    rpm_l = omega_l * 60 / (2 * math.pi)
    rpm_r = omega_r * 60 / (2 * math.pi)

    return [rpm_l, rpm_r]
```

---

**Kullanım Örneği:**

```python
rpm_degerleri = speed_to_rpm(v=0.3, omega=0.4, r=r, L=L)
print("Sol RPM:", rpm_degerleri[0])
print("Sağ RPM:", rpm_degerleri[1])
```
---

## Sol ve Sağ Motor RPM Değerlerinden Doğrusal ve Açısal Hız Hesaplama

Bir diferansiyel tahrikli robotta, **sol ve sağ motorların RPM değerlerini** kullanarak robotun gerçek **doğrusal (ileri/geri)** ve **açısal (dönme)** hızlarını hesaplamak mümkündür. Bu işlem, ileri kinematiğin tersidir.

---

**Verilen Parametreler:**

* $\text{RPM}_L$: Sol motorun RPM değeri
* $\text{RPM}_R$: Sağ motorun RPM değeri
* $r$: Tekerlek yarıçapı (metre cinsinden)
* $L$: İki tekerlek arasındaki mesafe (dingil açıklığı) (metre cinsinden)

---

**Adım Adım Dönüştürme Süreci:**

1. **RPM’yi açısal hıza çevirin (rad/s):**

    $$
    \omega_L = \text{RPM}_L \cdot \frac{2\pi}{60}
    $$

    $$
    \omega_R = \text{RPM}_R \cdot \frac{2\pi}{60}
    $$

2. **Açısal hızı doğrusal hıza çevirin:**

    $$
    v_L = \omega_L \cdot r
    $$

    $$
    v_R = \omega_R \cdot r
    $$

3. **Robotun doğrusal ve açısal hızını hesaplayın:**

    $$
    v = \frac{v_L + v_R}{2}
    $$

    $$
    \omega = \frac{v_R - v_L}{L}
    $$


**Python Kod Örneği:**

```python
import math
from orbitlab import OrbitDriver
orbit = OrbitDriver()

r = orbit.RADIUS
L = orbit.WHEEL_L

def rpm_to_speed(rpm_l, rpm_r, r, L):
    # 1. RPM → rad/s
    omega_l = rpm_l * 2 * math.pi / 60
    omega_r = rpm_r * 2 * math.pi / 60

    # 2. rad/s → m/s
    v_l = omega_l * r
    v_r = omega_r * r

    # 3. Robotun hızları
    v = (v_l + v_r) / 2
    omega = (v_r - v_l) / L

    return v, omega
```

---

**Kullanım Örneği:**

```python
v, omega = rpm_to_speed(rpm_l=100, rpm_r=120, r=r, L=L)
print(f"Doğrusal hız: {v:.2f} m/s")
print(f"Açısal hız: {omega:.2f} rad/s")
```

Bu işlem sayesinde, robotunuzun enkoderlerinden gelen RPM verilerini kullanarak robotun gerçek hareketini (ileri gitme hızı ve dönüş hızı) doğru bir şekilde ölçebilirsiniz.

Artık robotun motorlarından alınan gerçek zamanlı RPM verilerini kullanarak, zamanla kat edilen mesafeyi hassas bir şekilde hesaplayabiliriz. Bu yöntem, zaman tabanlı tahminlere kıyasla daha doğru ve güvenilir bir hareket takibi sağlamak için enkoder geri bildiriminden yararlanır.

**Örnek:**
```python
from orbitlab import OrbitDriver
import time
mesafe = 0.0

orbit = OrbitDriver()

r = orbit.RADIUS
L = orbit.WHEEL_L

orbit.set_rpm([10, -10])

while mesafe <= 1.0:
    sol_motor_rpm, sag_motor_rpm = orbit.speed()
    v, omega = rpm_to_speed(sol_motor_rpm, sag_motor_rpm, r, L)
    mesafe += v * 0.1
    time.sleep(0.1)

orbit.set_rpm([0, 0])
orbit.stop()
```
---
Robotun yönelme açısı, açısal hızının geçen zamanla çarpılmasıyla hesaplanabilir. Bu yöntem, zaman içinde robotun yönelimini tahmin etmek için basit fakat etkili bir yaklaşımdır.

**Örnek:**
```python
from orbitlab import OrbitDriver
import math
import time

aci = 0.0

orbit = OrbitDriver()

r = orbit.RADIUS
L = orbit.WHEEL_L

orbit.set_rpm([10, 10])

while mesafe <= math.pi/2:
    sol_motor_rpm, sag_motor_rpm = orbit.speed()
    v, omega = rpm_to_speed(sol_motor_rpm, sag_motor_rpm, r, L)
    phi += omega * 0.1
    phi = math.atan2(math.sin(phi), math.cos(phi))
    time.sleep(0.1)

orbit.set_rpm([0, 0])
orbit.stop()
```