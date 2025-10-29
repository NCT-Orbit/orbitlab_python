## Başlangıç
### 💻⚙️ Sistem Gereksinimleri 
Herhangi bir pakete veya indirme aracına gereksinim yoktur. Bir adet tarayıcı ve internet bağlantısı yeterlidir. 

---
### 👩🏻‍🏫 Öğretmen Kaydı
Öğretmen hesabı oluşturmak için yalnızca e-posta adresi ve şifre bilgisi gereklidir.
Kayıt tamamlandıktan sonra öğretmen, öğrencilere özel odalar oluşturabilir ve içerik yönetimini gerçekleştirebilir.

### 🎓 Öğrenci Kaydı
Öğrenciler, öğretmen tarafından paylaşılan oda numarası (ROOM CODE) ile sisteme giriş yapabilir.
Giriş sonrasında öğrenciden yalnızca bir kullanıcı adı (NICKNAME) belirlemesi istenir.
Bu sayede öğrenciler, kendi profilleri üzerinden derslere katılım sağlayabilir. 👩‍💻

## Öğretmen Paneli
### Sınıflar
Platform üzerindeki odalar iki farklı seviyeye ayrılmıştır:

+ Temel Seviye — Başlangıç düzeyindeki öğrenciler için hazırlanmıştır.

+ Orta Seviye — Daha ileri seviye uygulamaları içerir.

Bu yapı sayesinde öğretmenler, öğrencilerin gelişim düzeyine uygun içeriklerle dersleri yönetebilir. 

!!! warning "DİKKAT"
    Sınıf oluşturma süreci her iki kategori (Temel ve Orta) için de aynı adımları içerir.
    Bu kategoriler arasındaki fark, yalnızca tanımlanan görevlerin seviye bazlı ayrımıdır.
    Yani Temel seviye sınıflarda temel düzey görevler, orta seviye sınıflarda ise orta seviye görevler yer alır.
    Bu yapı, görevlerin sistem içerisinde öğrenme seviyelerine göre sınıflandırılmasını sağlar.



### Temel Seviye Görev Oluşturma
<iframe width="560" height="315"
    src="https://www.youtube.com/embed/QD5ic5xB__4" 
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen>
</iframe>
  
### Orta Seviye Görev Oluşturma
<iframe width="560" height="315"
    src="https://www.youtube.com/embed/-2Ut-s4M_SQ" 
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen>
</iframe>

### Temel Seviye Görevin Robot Üzerinde Çalıştırılması
<iframe width="560" height="315"
    src="https://www.youtube.com/embed/AxAg6ZONfr4" 
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen>
</iframe>

### Orta Seviye Görevin Robot Üzerinde Çalıştırılması


### Orta Seviye Görevin Bloklarının Ayrıntılı Anlatımı

Videoda anlatılan bloklar:

+ If bloğuna else if ve else ekleme

+ Function bloğuna parametre ekleme

+ List ve text bloklarına `item` ekleme

<iframe width="560" height="315"
    src="https://www.youtube.com/embed/7AVII3ycv4g" 
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen>
</iframe>


### Robots 

![](assets/robot_page.png)

Bu sayfa, admin tarafından sisteme eklenen öğretmenin bağlı olduğu robotun görüntülendiği alandır.

#### Chatbot Ayarları
<div class="video-container">

  <iframe 
      width="560" 
      height="315"
      src="https://www.youtube.com/embed/v4GWSSOluco" 
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen>
  </iframe>

</div>

#### Wifi Ayarları 

<div class="video-container">

  <iframe 
      width="560" 
      height="315"
      src="https://www.youtube.com/embed/GbmS4-eEjC0" 
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen>
  </iframe>

</div>


#### Help Menüsü

<div class="video-container">

  <iframe 
      width="560" 
      height="315"
      src="https://www.youtube.com/embed/tDcApuIG4ng" 
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen>
  </iframe>

</div>





## Öğrenci Paneli

### Temel Görevin Kodlanması



!!! info "İKONLAR"
    | İKON | İSİM | GÖREV |
    |:-----|:----:|------:|
    | ![Yeşil Bayrak](assets/icons/yesil_bayrak.png){ width=60px } | Yeşil Bayrak | Programı başlatmak için kullanılır. |
    | ![Kırmızı Bayrak](assets/icons/kirmizi_bayrak.png){ width=60px } | Kırmızı Bayrak | Programı durdurmak için kullanılır. |
    | ![İleri](assets/icons/ileri.png){ width=60px } | İleri | Robotu bir adım ileri götürür. |
    | ![Sağa Dönüş](assets/icons/saga_don.png){ width=60px } | Sağa Dönüş | Robotu sağa döndürür. |
    | ![Sola Dönüş](assets/icons/sola_don.png){ width=60px } | Sola Dönüş | Robotu sola döndürür. |
    | ![Döngü](assets/icons/dongu.png){ width=60px } | Döngü | İçine yazılan komutları tekrar tekrar çalıştırmayı sağlar. |
    | ![Sıcaklık Ölçümü](assets/icons/sicaklik.png){ width=60px } | Sıcaklık Ölçümü | Ortam sıcaklığını ölçer. |
    | ![Ses Kaydı](assets/icons/ses_kaydi.png){ width=60px } | Ses Kaydı | Öğrencinin mikrofon aracılığıyla ses kaydetmesini sağlar. |



<div class="video-container">

  <iframe 
      width="560" 
      height="315"
      src="https://www.youtube.com/embed/F0QlPf13xc4" 
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen>
  </iframe>

</div>





### Orta Seviye Görevin Kodlanması

<div class="video-container">

  <iframe 
      width="560" 
      height="315"
      src="https://www.youtube.com/embed/ZCj5bfg4zHA" 
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen>
  </iframe>

</div>


