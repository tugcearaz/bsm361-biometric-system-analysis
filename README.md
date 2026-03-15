# bsm361-biometric-system-analysis


Bu projede bir biyometrik tanıma sisteminin performansı analiz edilmiştir. 
Çalışmada parmak izi özellik vektörlerini içeren **Features.npz** veri seti kullanılmıştır.

## Veri Seti
Veri seti farklı zamanlarda elde edilmiş parmak izi özellik vektörlerinden oluşmaktadır. 
Analiz kapsamında veri setindeki ilk **100 kişi** kullanılmıştır.

## Yöntem

Öncelikle tüm özellik vektörleri **[0,1] aralığında normalize edilmiştir**.  
İki özellik vektörü arasındaki benzerlik skoru **Euclidean mesafesi** kullanılarak hesaplanmıştır.

Kullanılan skor fonksiyonu:

Score = 1 / (1 + d)

Burada **d**, iki özellik vektörü arasındaki Euclidean mesafesini ifade etmektedir.

## Hesaplanan Değerler

Projede aşağıdaki biyometrik sistem performans ölçütleri hesaplanmıştır:

- Genuine Score dağılımı
- Imposter Score dağılımı
- FAR (False Acceptance Rate)
- FRR (False Rejection Rate)
- EER (Equal Error Rate)

## Grafikler

Analiz sonucunda aşağıdaki grafikler elde edilmiştir:

- Genuine ve Imposter skor dağılımı
- FAR ve FRR – Threshold grafiği
- FAR – FRR grafiği

## Amaç

Bu çalışmanın amacı biyometrik bir doğrulama sisteminin performansını 
genuine ve imposter skorları üzerinden analiz etmek ve sistemin hata oranlarını incelemektir.
