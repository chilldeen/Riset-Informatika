# Penerapan Metode Segmentasi Citra Digital Untuk Pendeteksian Kutu Beras

## Persoalan Praktis
Beras adalah salah satu hal pokok dalam kehidupan masyarakat Indonesia. Namun, tidak semua beras yang beredar di pasaran bebas dari keberadaan suatu hama yang disebut kutu beras. Kutu beras dapat menyebabkan penurunan produksi dan kualitas beras. Penggunaan citra digital dan teknologi IoT telah menjadi fokus utama untuk penelitian ini. Penggunaan device seperti arduino dengan tambahan modul kamera untuk menangkap gambar yang lalu akan diproses menggunakan citra digital dengan metode segmentasi berupa thresholding dan edge detection untuk menampilkan keberadaan kutu beras.

## Metode 
Metode yang digunakan dalam pendeteksian kutu beras melalui segmentasi citra digital melibatkan serangkaian langkah-langkah algoritmik untuk memisahkan dan mengidentifikasi kutu beras dari latar belakang butiran beras. Pendekatan ini memanfaatkan gabungan beberapa teknik, termasuk Thresholding, Edge Detection, dan Clustering, yang dijelaskan sebagai berikut:
1. Thresholding
Digunakan untuk memisahkan piksel berdasarkan nilai intensitasnya. Dalam konteks ini, nilai ambang (threshold) ditentukan untuk memisahkan kutu beras dari latar belakang butiran beras.
2. Edge Detection
Digunakan untuk menyoroti tepi objek dalam citra, yang dapat membantu dalam pemisahan kutu beras dari latar belakangnya.
3. Clustering
Digunakan untuk mengelompokkan piksel berdasarkan kesamaan atribut, seperti warna atau tekstur, yang dapat membantu dalam memisahkan area yang mungkin mengandung kutu beras.

## Kode Program
Kode program dapat dilihat pada [file ini](program.py).

## Hasil Penelitian
Hasil output program dapat dilihat pada [file ini](output.png).

## Referensi
Referensi yang digunakan untuk penelitian ini adalah sebagai berikut:
1. Diaz, J. C., & Alegre, E. (2016). Image Processing Algorithms in the Identification of Pests and Diseases in Agriculture: A Review. Computer and Electronics in Agriculture, 125, 10-23.
2. Dong, Y., et al. (2018). Detection of Rice Plant Diseases using Deep Convolutional Neural Networks. Symmetry, 10(11), 640.
3. Patil, A. A., & Mankar, V. H. (2019). Rice Disease Detection using Image Processing Techniques: A Review. Procedia Computer Science, 165, 349-356.