### Robot İlk Kullanım


<div style="display: flex; align-items: center;">
  <img src="../assets/kullanma_kilavuzu/siyah_button_gercekci.png" alt="Tekerlek ile hız Kontrolü" style="width: 250px; margin-right: 8px; margin-left : 10px">
  <span>Robotun buton panelindeki siyah buton sola çevrildiğinde, robot etkin hale gelir. <br>
  Siyah butonun sağ konuma çevrilmesiyle birlikte şarj sistemi etkinleştirilir ve pil şarj süreci başlatılır.
  </span>
  
</div>

<br>

<div style="display: flex; align-items: center;">
  
  <span>Voltaj Göstergesi  22.0 ile 29.0 arasında şarj değerini robot açıkken gösterir.</span>
  <img src="../assets/kullanma_kilavuzu/voltaj_gercekci.png" alt="Tekerlek ile hız Kontrolü" style="width: 250px; margin-right: 8px; margin-left : 10px">
</div>

<br>

<div style="display: flex; align-items: center;">
  <img src="../assets/kullanma_kilavuzu/acil_stop_gercekci.png" alt="Tekerlek ile hız Kontrolü" style="width: 250px; margin-right: 8px; margin-left : 10px">
  <span>Robot üzerinde iki adet acil durdurma butonu bulunmaktadır. Bu butonlar, robotun ana gücüne bağlıdır ve basıldığında güvenlik nedeniyle robotun gücünü keser. Buton serbest bırakıldığında sistem yeniden başlatılır.  
Acil durdurma butonunun, gösterildiği şekilde açılması gerekmektedir. Ters yönde döndüğünde butonun ömrü kısalmaktadır.
Robotu başlatırken acil durdurma butonları basılıysa, robot açılmaz. Siyah butonu ortaya alarak acil durdurma butonları kapatılmalı ve ardından robot tekrar açılmalıdır.</span>
  
</div>

<br>

#### Başlatma Süreci
<div style="display: flex; align-items: center;">
Robotun başlatma süreci, donanım bileşenlerinin ve sensörlerin düzgün şekilde çalıştığının doğrulanması amacıyla otomatik olarak gerçekleştirilir. <br><br>
İşlem Adımları:<br><br>

1. Güç Verilmesi: <br><br>  Robot enerji aldığında sistem başlatma dizisi otomatik olarak başlar. <br><br>

2. LED Göstergesi – Durum 1: <br><br>Başlangıç aşamasında şerit led kırmızı renkte yanar. Bu durum, sistem kontrolünün devam ettiğini belirtir. <br><br>

3. Sistem Kontrolü: <br><br>

· Ana kart, sensörler ve iletişim arabirimleri kontrol edilir.<br>

· Servo motorlar ve hareket bileşenleri bekleme konumuna alınır. <br><br>

4. Kafa Mekanizması Kalibrasyonu: <br><br>

· Kafa eksenleri sıfır (referans) konumuna getirilir.<br>

· Limit switch veya enkoder verileri doğrulanır. <br><br>

5. LED Göstergesi – Durum 2:<br><br> Sistem kontrolü ve kalibrasyon işlemleri başarıyla tamamlandığında şerit led yeşil renge döner. <br><br>

6. Sesli Uyarı: İnternet bağlantısı varsa ve başarılı başlatma işlemini doğrulandıysa sistem kısa bir sesli uyarı sinyali üretir.(Haydi Başlayalım der) <br><br>

7. Başlatma Tamamlandı: Robot, normal çalışma moduna geçer ve kullanıcı komutlarını kabul etmeye hazır hâle gelir. <br><br>
Notlar: <br>

· Eğer başlatma süreci sırasında bir hata algılanırsa, LED’ler kırmızı yanmaya devam eder ve sistem çalışmayı durdurur. <br>
· Hata kodları ve sinyal desenleri, sistem hata tablosunda tanımlanmıştır. 
  
</div>

#### Şarj Etme ve Batarya Kullanma İşlemi

<div style="display: flex; align-items: center;">
  <img src="../assets/kullanma_kilavuzu/şarj_doldurma_yeni.png"  style="width: 250px; margin-right: 8px; margin-left : 10px">
  <span>Siyah butonun sağ tarafa çevrildiğinden emin olduktan sonra şekildeki şarj soketine bataryanın konnektörü takılır.</span>
  
</div>

<div style="display: flex; align-items: center;">
  <span>Robotun güç kaynağı, yüksek verimli bir lityum batarya ile sağlanmaktadır. Şarj işlemi, sisteme entegre edilmiş lityum batarya şarj cihazı (Lithium Battery Charger) aracılığıyla gerçekleştirilir. Cihaz, güvenli şarj yönetimi için akım ve gerilim değerlerini otomatik olarak denetler.<br><br>
    Şarj cihazı üzerindeki gösterge LED’leri, şarj durumunu kullanıcıya bildirir: <br>

  · Kırmızı ışık yandığında batarya şarj olmaktadır.<br>

  · Yeşil ışık yandığında ise şarj işlemi tamamlanmıştır ve batarya kullanıma hazırdır.</span>
  <img src="../assets/kullanma_kilavuzu/batarya_charger.png"  style="width: 250px; margin-right: 8px; margin-left : 10px">

  
</div>


#### Kullanım Modları

<h5>Manuel Kullanım</h5>

Manuel kullanıma iki yerden erişelebilir:

1. Robot sayfasındaki kontrol panelden robot kontrol ile joystick kullanımı;

<div style="display: flex; justify-content: flex-center; align-items: center;">
  <img src="../assets/kullanma_kilavuzu/manuel_control.png" style="width: 500px; margin: 8px;">
  <span style="font-size: 30px; margin: 0 12px;">➡️ </span>
  <img src="../assets/kullanma_kilavuzu/manuel_control_ai.png" style="width: 420px; margin: 8px;">
</div>

2. Öğretmen Panelindeki sınıflara girilip robot bağlantısı sağlandıktan sonra manuel butonu ile gelen joystick kullanımı;

<div style="display: flex; justify-content: flex-center; align-items: center;">
  <img src="../assets/kullanma_kilavuzu/kullanim_modu_sinif.png" style="width: 1300px; margin: 8px;">
</div>
<div style="display: flex; justify-content: flex-center; align-items: center;">
  <img src="../assets/kullanma_kilavuzu/kullanim_modu_sinif_1.png" style="width: 1300px; margin: 8px;">
</div>

<div style="display: flex; justify-content: flex-center; align-items: center;">
  <img src="../assets/kullanma_kilavuzu/kullanim_modu_joystick.png" style="width: 1300px; margin: 8px;">
</div>


<h5>Otonom Kullanım</h5>

Otonom kullanım için navigasyon moduna geçilmesi gereklidir. Navigasyon modu detatylı olarak ------------------ kısmında anlatılmaktadır.

<h5>Kalibrasyon</h5>

Robot kafa ve çizgi izleyen olmak üzere iki kısımda kalibrasyon alır.
Robot açıldığı anda kafa kalibrasyonunu şekilde gösterilen videodaki gibi alır.


<div class="video-container">

  <iframe 
      width="560" 
      height="315"
      src="https://www.youtube.com/embed/BlsB2-nDhgk" 
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen>
  </iframe>

</div>




