# İzometrik Küp Çizim Çalışması

Bu proje, Python ve Pygame kütüphanesi kullanarak 3 boyutlu nesnelerin (küplerin) izometrik izdüşüm tekniği ile 2 boyutlu bir ekranda görselleştirilmesini sağlar.

## 📌 Proje Özeti
Bilgisayar grafiklerinde derinlik algısı yaratmak için kullanılan en yaygın yöntemlerden biri olan izometrik dönüşüm, bu uygulamada matematiksel formüllerle (`numpy` kullanılmadan, temel matematik ile) uygulanmıştır. Uygulama, kullanıcıya 3D uzaydaki nesnelerin 2D düzlemdeki karşılıklarını görme imkanı tanır.

## 🚀 Özellikler
* **Dinamik Küp Oluşturma:** Boyut ve merkez koordinatları belirlenebilen küp yapıları.
* **İzometrik Dönüşüm:** 3D koordinatların ($x, y, z$) 2D ekran koordinatlarına dönüştürülmesi.
* **Koordinat Sistemi:** Görselleştirmeyi kolaylaştırmak için ekranda çizilen X, Y ve Z eksenleri.
* **Renklendirme:** Farklı küplerin ayırt edilebilmesi için özel renk paleti.

## 🛠 Kullanılan Teknolojiler
* **Dil:** Python 3.x
* **Kütüphane:** [Pygame](https://www.pygame.org/) (Grafiksel arayüz ve çizimler için)

## 📊 Kullanılan Dönüşüm Formülü
Kod içerisinde kullanılan temel izometrik dönüşüm mantığı şu şekildedir:
- `ekran_x = (x - z) * cos(30°)`
- `ekran_y = (x + z) * sin(30°) - y`

## 📂 Dosya Yapısı
* `odev.py`: Küp oluşturma, matematiksel dönüşüm ve Pygame döngüsünü içeren ana kaynak kod.

## ⚙️ Kurulum ve Çalıştırma
1. Sisteminize Pygame yüklü olduğundan emin olun:
   ```bash
   pip install pygame
