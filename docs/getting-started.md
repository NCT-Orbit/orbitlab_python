Bu yazılım, Orbit robotunu yerel ağ üzerinden Python ile kontrol etmek için geliştirilmiştir. 
Temel amacı, öğrencilerin fiziksel bir robotla etkileşim kurarak robotik programlama konusunda 
uygulamalı deneyim kazanmalarını sağlamaktır. Kütüphane, Orbit platformunun temel işlevlerini 
sunar: motor kontrolü, sensör verilerine erişim, robot yüz ifadesinin değiştirilmesi, 
ses çalma, LDR (ışığa duyarlı direnç) ayarı ve daha fazlası. Bu sayede kapsamlı ve pratik 
bir öğrenme deneyimi sunar. Aynı zamanda da simulasyon özelliği sahiptir.

## Yazılım gereksinimleri

1. Orbit robot: Daha fazla bilgi için [Orbitrobots](https://orbitrobots.com/) ziyaret edin
2. Python >= 3.0: Python'u indirin [Python](https://www.python.org/downloads/)

## Kurulum

```
pip install orbitlab-python
```
## Kullanım örneği

Orbitlab-python'u kurduktan sonra, bilgisayarınızın robotla aynı ağa bağlı olduğundan emin olun. 
**Robotun IP adresini ekranından alın**.

```python
import time
from orbitlab import Orbit

orbit = Orbit("<orbit_ip_address>")

orbit.set_rpm([10, -10])
time.sleep(5)
orbit.stop()
```

Bu örnekte, robotu 5 saniye boyunca 10 RPM hızla hareket ettirdik.

!!! warning "Dikkat"
    Robottan güvenli bir şekilde bağlantıyı kesmek için programınızın sonunda `orbit.stop()` 
    fonksiyonunu her zaman çağırın.
