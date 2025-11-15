### Robot İlk Kullanım


<div style="display: flex; align-items: center;">
  <img src="../assets/kullanma_kilavuzu/siyah_button_gercekci.png" alt="Tekerlek ile hız Kontrolü" style="width: 250px; margin-right: 8px; margin-left : 10px">
  <span>Robot üzerindeki siyah konum anahtarı üç pozisyona sahiptir: <br>

  Sol konum: Robot aktif (çalışma modu) <br>

  Orta konum (0): Robot kapalı <br>

  Sağ konum: Şarj modu aktif

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


5. LED Göstergesi – Durum 2:<br><br> Sistem kontrolü ve kalibrasyon işlemleri başarıyla tamamlandığında şerit led yeşil renge döner. <br><br>

6. Sesli Uyarı: İnternet bağlantısı varsa ve başarılı başlatma işlemini doğrulandıysa sistem kısa bir sesli uyarı sinyali üretir.(Haydi Başlayalım der) <br><br>

7. Başlatma Tamamlandı: Robot, normal çalışma moduna geçer ve kullanıcı komutlarını kabul etmeye hazır hâle gelir. <br><br>
Notlar: <br>

· Eğer başlatma süreci sırasında bir hata algılanırsa, LED’ler kırmızı yanmaya devam eder ve sistem çalışmayı durdurur. <br>
· Hata kodları ve sinyal desenleri, sistem hata tablosunda tanımlanmıştır. 
  
</div>

#### Şarj Etme ve Batarya Kullanma İşlemi

<div style="display: flex; align-items: center;">
  <img src="../assets/kullanma_kilavuzu/şarj_doldurma_yeni.png"  style="width: 300px; height:350px; margin-right: 8px; margin-left : 10px">
  <span>Konum anahtarının orta (0) konumunda, yani robot kapalı durumda olduğundan emin olun. <br> <br>
  Şarj adaptörünün soketini robot üzerindeki şarj girişine güvenli şekilde bağlayın. <br> <br>
  Şarj işlemini başlatmak için konum anahtarını sağa çevirin. <br> <br>
  Şarj işlemi tamamlandığında anahtarı tekrar 0 (orta) konumuna alın. <br> <br>
  Şarj soketini yalnızca anahtar 0 konumundayken çıkarın.

</span>
  
</div>
<br>
<div style="display: flex; align-items: center;">
  <span>Robotun güç kaynağı, yüksek verimli bir lityum batarya ile sağlanmaktadır. Şarj işlemi, sisteme entegre edilmiş lityum batarya şarj cihazı (Lithium Battery Charger) aracılığıyla gerçekleştirilir. Cihaz, güvenli şarj yönetimi için akım ve gerilim değerlerini otomatik olarak denetler.<br><br>
    Şarj cihazı üzerindeki gösterge LED’leri, şarj durumunu kullanıcıya bildirir: <br>

  · Kırmızı ışık yandığında batarya şarj olmaktadır.<br>

  · Yeşil ışık yandığında ise şarj işlemi tamamlanmıştır ve batarya kullanıma hazırdır.</span>
  <img src="../assets/kullanma_kilavuzu/batarya_charger.png"  style="width: 250px; margin-right: 8px; margin-left : 10px">

  
</div>

#### Uyarılar ve Güvenlik Önlemleri
<div style="display: flex; align-items: center;">
  <img src="../assets/kullanma_kilavuzu/orbit_elektrik.png"  style="width: 250px; margin-right: 8px; margin-left : 10px"> <br>
  <span>· Konum anahtarı sağ konumdayken, robot üzerindeki şarj soketi elektrik altındadır; soket uçlarına elle dokunmayın. <br><br>

· Buton sağ konumdayken soket ve bağlantı noktalarını iletken malzemelerle temas ettirmeyin (metal aletler, anahtar, kablo uçları vb.). <br><br>

· Şarj aleti prize takılıyken, şarj adaptörünün kendi soket uçlarında da elektrik bulunur; adaptörün uçlarına kesinlikle dokunmayın. <br><br>

· Şarj soketinin takma ve çıkarma işlemlerini mutlaka 0 (orta) konumunda gerçekleştirin. <br><br> </span>

</div>
<div style="display: flex; align-items: center;">

  <span>· Teslim sırasında verilen eğitimde belirtilen tüm güvenlik kurallarına uyun. <br><br>

· Yalnızca üretici tarafından önerilen ve uyumlu şarj adaptörlerini kullanın. <br><br>

· Kablo veya sokette hasar tespit edilmesi durumunda şarj işlemine devam etmeyin; teknik servise başvurun. <br><br>

· Şarj sırasında robotu aşırı sıcaklık, sıvı teması veya yanıcı yüzeylerden uzak tutun.</span>

</div>

  


<br> <br>
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


### LED Komut Tablosu


<h3>🟩 Mat Üzeri LED Durumları</h3>
<table>
  <tr><th>Komut Adı</th><th>Mod</th><th>Renk</th><th>Açıklama</th></tr>
  <tr><td>ileri</td><td>2</td><td style="background-color:cyan;color:black;">Camgöbeği</td><td>İleri hareket — yanıp sönme efekti</td></tr>
  <tr><td>right</td><td>2</td><td style="background-color:yellow;color:black;">Sarı</td><td>Sağa dönüş — yanıp sönme efekti</td></tr>
  <tr><td>left</td><td>2</td><td style="background-color:yellow;color:black;">Sarı</td><td>Sola dönüş — yanıp sönme efekti</td></tr>
  <tr><td>error</td><td>2</td><td style="background-color:red;color:white;">Kırmızı</td><td>Genel hata — kırmızı yanıp sönme</td></tr>
</table>

<h3>🌐 İnternet Durumları</h3>
<table>
  <tr><th>Komut Adı</th><th>Mod</th><th>Renk</th><th>Açıklama</th></tr>
  <tr><td>online</td><td>3</td><td style="background-color:lime;color:black;">Yeşil</td><td>Cihaz çevrimiçi — parlaklık azalma</td></tr>
  <tr><td>hotspot</td><td>3</td><td style="background-color:orange;color:black;">Turuncu</td><td>Hotspot aktif — turuncu parlaklık azalma</td></tr>
  <tr><td>change_mode</td><td>3</td><td style="background-color:yellow;color:black;">Sarı</td><td>Mod değişimi sırasında uyarı</td></tr>
</table>

<h3>🤖 Navigasyon Durumları (nav2)</h3>
<table>
  <tr><th>Komut Adı</th><th>Mod</th><th>Renk</th><th>Açıklama</th></tr>
  <tr><td>reached</td><td>5</td><td style="background-color:lime;color:black;">Yeşil</td><td>Hedefe ulaşıldı</td></tr>
  <tr><td>active</td><td>6</td><td style="background-color:cyan;color:black;">Camgöbeği</td><td>Aktif navigasyon</td></tr>
  <tr><td>status</td><td>5</td><td style="background-color:deepskyblue;color:white;">Açık Mavi</td><td>İstasyon ekleme/silme işlemi</td></tr>
  <tr><td>complate</td><td>2</td><td style="background-color:lime;color:black;">Yeşil</td><td>Görev tamamlandı</td></tr>
</table>

<h3>🚨 Hata Kodları</h3>
<table>
  <tr><th>Kod</th><th>Mod</th><th>Yanıp Sönme Sayısı</th><th>Renk</th><th>Açıklama</th></tr>
  <tr><td>error 1</td><td>4</td><td>1</td><td style="background-color:red;color:white;">Kırmızı</td><td>[1] Navigasyon hatası (nav2 failed)</td></tr>
  <tr><td>error 2</td><td>4</td><td>2</td><td style="background-color:red;color:white;">Kırmızı</td><td>[2] Batarya hatası</td></tr>
  <tr><td>error 3</td><td>4</td><td>3</td><td style="background-color:red;color:white;">Kırmızı</td><td>[3] IMU'dan yanlış veri gelmesi</td></tr>
  <tr><td>error 4</td><td>4</td><td>4</td><td style="background-color:red;color:white;">Kırmızı</td><td>[4] İnternet bağlantısı yok</td></tr>
  <tr><td>error 5</td><td>4</td><td>5</td><td style="background-color:red;color:white;">Kırmızı</td><td>[5] Genel Sensör Hatası</td></tr>
  <tr><td>error 6</td><td>4</td><td>6</td><td style="background-color:red;color:white;">Kırmızı</td><td>[6] Navigasyon Hatası</td></tr>
  <!-- <tr><td>errors_7</td><td>4</td><td>7</td><td style="background-color:red;color:white;">Kırmızı</td><td>[7] Tanımlanmamış hata 7</td></tr>
  <tr><td>errors_8</td><td>4</td><td>8</td><td style="background-color:red;color:white;">Kırmızı</td><td>[8] Tanımlanmamış hata 8</td></tr>
  <tr><td>errors_9</td><td>4</td><td>9</td><td style="background-color:red;color:white;">Kırmızı</td><td>[9] Tanımlanmamış hata 9</td></tr> -->
</table>


