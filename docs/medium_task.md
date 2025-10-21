## Orbit Bloğunun Açıklaması

<div style="display: flex; align-items: center;">
  <img src="../assets/medium_task/orbit.png" alt="İleri Hareket" style="height: 210px; margin-right: 8px;">
  <span>Medium Task içinde bulunan "Orbit" sekmesindeki blokların detaylı açıklanması ve verilecek değerlerin ksıtları.
  </span>
</div>

### ROBOTUN YÖNÜ VE HAREKETİ
Mavi bloklar, robotun yön ve hareket davranışlarını belirler.


<div style="display: flex; align-items: center;">
  <img src="../assets/medium_task/ileri.png" alt="İleri Hareket" style="height: 60px; margin-right: 8px;">
  <span>Robot, bu blokta belirtilen değer kadar metere ileri hareket eder ve hareket tamamlandıktan sonra durur. <br>
    Mesafe (metre) : Robotun ilerleyeceği mesafe değeridir. <br>
    Geçerli aralık : 0.2 ≤ mesafe ≤ 1.0
  </span>
</div>
<br>
<div style="display: flex; align-items: center;">
  <img src="../assets/medium_task/geri.png" alt="Geri Hareket" style="height: 60px; margin-right: 8px;">
  <span>Robot, bu blokta belirtilen değer kadar metere geri hareket eder ve hareket tamamlandıktan sonra durur. <br>
    Mesafe (metre) : Robotun geri gideceği mesafe değeridir. <br>
    Geçerli aralık : 0.2 ≤ mesafe ≤ 1.0
  </span>
</div>
<br>

<div style="display: flex; align-items: center;">
  <img src="../assets/medium_task/sag.png" alt="Sağa dönüş" style="height: 60px; margin-right: 8px;">
  <span>Bu blok, robotun sağ yöne belirli bir açı kadar dönmesini sağlar. Blok çalıştırıldığında robot, girilen derece değerine göre saat yönünde döner ve dönüş tamamlandığında durur. <br>
    Açı (derece) : Robotun döneceği açı miktarını belirtir.
    Geçerli değer aralığı : 0° - 360°

  </span>
</div>
<br>
<div style="display: flex; align-items: center;">
  <img src="../assets/medium_task/sol.png" alt="Sola dönüş" style="height: 60px; margin-right: 8px;">
  <span>Bu blok, robotun sol yöne belirli bir açı kadar dönmesini sağlar. Blok çalıştırıldığında robot, girilen derece değerine göre saat yönünün tersine döner ve dönüş tamamlandığında durur. <br>
    Açı (derece) : Robotun döneceği açı miktarını belirtir.
    Geçerli değer aralığı : 0° - 360°

  </span>
</div>

<br>

<div style="display: flex; align-items: center;">
  <img src="../assets/medium_task/rpm.png" alt="Tekerlek ile hız Kontrolü" style="height: 105px; margin-right: 8px;">
  <span>Bu blok, robotun tekerleklerini ayrı ayrı kontrol ederek istenen yönde hareket etmesini sağlar.
    Her bir tekerleğe verilen değer, o tekerleğin dönme hızını (RPM – dakika başına devir) belirtir. <br>
    Bu aralığın dışındaki değerler hatalı çalışmaya neden olabilir. <br>
    Geçerli değer aralığı: -15 ≤ hız ≤ 15 <br>
    Not: Bu aralığın dışında girilen değerler motorun hatalı çalışmasına neden olabilir.
  </span>
</div>

<br>

| HAREKET  TÜRÜ   | SOL TEKER   | SAĞ TEKER   |
|:----------------|:-----------:|------------:|
|İleri            |  10         | -10         |
|Geri             | -10         |  10         |
|Sağa 90° Dönüş   |  10         |  10         |
|Sola 90° Dönüş   | -10         | -10         |

💡 NOT : 10 optimum değer olduğu için tablodaki örnekte 10 rpm kullanılmıştır.

<br>

<div style="display: flex; align-items: center;">
  <img src="../assets/medium_task/durdur.png" alt="Tekerlek ile hız Kontrolü" style="height: 60px; margin-right: 8px; margin-left : -2px">
  <span>Bu blok, robotun motorlarını durdurmak için her iki tekerleğe de 0 RPM değeri gönderir.
    Bu sayede tekerleklerin dönme hareketi sonlandırılır ve robot hareketsiz konuma geçer.
  </span>
</div>

### ROBOTUN SENSÖRLERİ

![](/orbitlab_python/docs/medium_task_folder/../assets/sensor_with_orbit_dark.png){ width=400px }



<div style="display: flex; align-items: center;">
  <img src="../assets/medium_task/mesafe.png" alt="Tekerlek ile hız Kontrolü" style="height: 50px; margin-right: 8px; margin-left : -10px">
  <span>Mesafe sensörü, çevresindeki nesnelerin uzaklığını ölçer ve sistem kontrol birimine iletir. <br>
  Mesafe (metre) : Ölçtüğü birim metredir.
  Ölçüm aralığı : 0.2 ≤ veri ≤ 1.0
  </span>
</div>

<br>

<div style="display: flex; align-items: center;">
  <img src="../assets/medium_task/ldr.png" alt="Tekerlek ile hız Kontrolü" style="height: 45px; margin-right: 8px; margin-left : -2px">
  <span style="margin-left : 20px">LDR sensörü, ortam ışık seviyesini ölçer ve analog değer olarak sistem kontrol birimine iletir.<br>
  Mesafe (metre) : Ölçtüğü birim metredir.
  Ölçüm aralığı : 0 ≤ veri ≤ 1023 <br>
    0 (karanlık ortam)
    1023 (aydınlık ortam)
  </span>
</div>

<br> 

<div style="display: flex; align-items: center;">
  <img src="../assets/medium_task/akim.png" alt="Tekerlek ile hız Kontrolü" style="height: 45px; margin-right: 8px; margin-left : -2px">
  <span style="margin-left : 10px">Akım sensörü, robotun elektrik devresinden geçen akım değerini ölçer ve sistem kontrol birimine iletir.<br>
    Ölçüm aralığı :  0.0 ≤ veri ≤ 1.6 (Tekerleklerin zorlanmadığı durumda) <br>
   
  </span>
</div>

<br>

<div style="display: flex; align-items: center;">
  <img src="../assets/medium_task/voltage.png" alt="Tekerlek ile hız Kontrolü" style="height: 45px; margin-right: 8px; margin-left : -4px">
  <span style="margin-left : 4px">Voltaj sensörü, robotun besleme hattındaki gerilim değerini ölçer ve sistem kontrol birimine iletir. Ölçümler Volt (V) cinsindendir. <br>
  Not: Eğer ölçülen gerilim 23 V’nin altına düşerse, kontrol sistemi robotu otomatik olarak kapatır (undervoltage shutdown).
   
  </span>
</div>

<br>

<div style="display: flex; align-items: center;">
  <img src="../assets/medium_task/sicaklik.png" alt="Tekerlek ile hız Kontrolü" style="height: 45px; margin-right: 8px; margin-left : -3px">
  <span>Sıcaklık sensörü, ortam sıcaklığını ölçer ve ölçüm sonucunu sistem kontrol birimine iletir. Ölçümler genellikle derece Celsius (°C) cinsindendir. <br>
    
   
  </span>
</div>

<br>

<div style="display: flex; align-items: center;">
  <img src="../assets/medium_task/hiz.png" alt="Tekerlek ile hız Kontrolü" style="height: 45px; margin-right: 8px; margin-left : 10px">
  <span style="margin-left : 40px">Tekerlek sensörlerinden elde edilen hız verisi, devir/dakika (RPM) cinsinden ölçülür ve ilgili sistem bileşenlerine iletilir.<br>
   
  </span>
</div>

### GÖRSEL EFEKT ve KAFA HAREKET YÖNETİMİ


<div style="display: flex; align-items: center;">
  <img src="../assets/medium_task/rgb.png" alt="Tekerlek ile hız Kontrolü" style="height: 150px; margin-right: 8px; margin-left : 10px">
  <span>Robot üstündeki şerit ledin rengini kontrol etmek için kullanılır.
    RGB, Kırmızı (Red), Yeşil (Green) ve Mavi (Blue) renklerinin
    karışımını temsil eder. Bu üç rengin değerini değiştirerek
    binlerce farklı renk oluşturabilir. Değerler 0 – 255 arasında
    değişir.<br>
   
  </span>
</div>

<br>

<div style="display: flex; align-items: center;">
  
  <span>Robot üstündeki şerit ledin rengini kontrol etmek için kullanılır.
    RGB, Kırmızı (Red), Yeşil (Green) ve Mavi (Blue) renklerinin
    karışımını temsil eder. Bu üç rengin değerini değiştirerek
    binlerce farklı renk oluşturabilir. Değerler 0 – 255 arasında
    değişir.<br>
   
  </span>
  <img src="../assets/medium_task/animation_rgb.png" alt="Tekerlek ile hız Kontrolü" style="height: 120px; margin-right: 8px; margin-left : 10px">
</div>

<br>

<div style="display: flex; align-items: center;">
  <img src="../assets/medium_task/kafa.png" alt="Tekerlek ile hız Kontrolü" style="height: 100px; margin-right: 8px; margin-left : 10px">
  <span>Bu blok, robotun kafasının yatay (X) ve dikey (Y) eksenlerde hareket etmesini sağlar. <br>
  Hareket, adım adım kontrol edilir; yani verilen değer
  kadar adet adım (step) robot kafasını ilgili eksende
  hareket ettirir.<br>
  Geçerli değer aralığı: <br>
  x ekseninde [-216, 216] adım; <br>
  y ekseninde [-300,300] adım.
   
  </span>
</div>

<br>

<div style="display: flex; align-items: center;">
  
  <span>Robotun yüz ifadesini kontrol eden bloktur. 12 farklı
mevcut yüz ifadesi vardır.<br>
   
  </span>
  <img src="../assets/medium_task/yuz_ifadesi.png" alt="Tekerlek ile hız Kontrolü" style="height: 70px; margin-right: 8px; margin-left : 10px">
</div>

### ETKİLEŞİM ve SESLİ İLETİŞİM BLOKLARI

<div style="display: flex; align-items: center;">
  <img src="../assets/medium_task/konus.png" alt="Tekerlek ile hız Kontrolü" style="height: 60px; margin-right: 8px; margin-left : 10px">
  <span>Bu blok, robota doğrudan metin (string) göndererek konuşmasını sağlar. Gönderilen metin, robotun Text-to-Speech (TTS) motoru aracılığıyla seslendirilir.
  </span>
</div>

<br>

<div style="display: flex; align-items: center;">
  <span>Bu blok, robotun internet üzerinden bir şarkıyı çalmasını sağlar. Kullanıcı sadece şarkının adını girer; blok şarkıyı internetten bulur ve oynatır.
</span>
 <img src="../assets/medium_task/sarki.png" alt="Tekerlek ile hız Kontrolü" style="height: 60px; margin-right: 8px; margin-left : 10px">
</div>

<br>
<div style="display: flex; align-items: center;">
  <img src="../assets/medium_task/danset.png" alt="Tekerlek ile hız Kontrolü" style="height: 60px; margin-right: 8px; margin-left : 10px">
  <span>Bu blok, robotun gelişmiş etkileşimli davranışlarını kontrol eder. <br>
        Kullanıcı bir metin girer; blok şunları eş zamanlı olarak yapar: <br>
• Metni internet üzerinden arar ve şarkıyı çalar. <br>
• Robotun ileri, geri, sağ, sol hareketlerini ve kafasının yukarı-aşağı
hareketlerini kullanarak dans figürleri gerçekleştirir.
<br>
   
  </span>
</div>
