# Tugas 1 — Bab 1 dan Standar Protokol pada Teknologi Wi-Fi

## 1. Konsep dasar jaringan komputer

Jaringan komputer adalah kumpulan dua atau lebih perangkat yang saling terhubung untuk bertukar data dan menggunakan sumber daya bersama. Contohnya adalah koneksi internet, berkas, penyimpanan, dan printer.

Komponen jaringan terdiri dari **end device** (komputer, ponsel, server, printer), **media transmisi** (kabel tembaga, serat optik, atau gelombang radio), **perangkat perantara** (switch, router, access point), dan **protokol** yang mengatur format serta pertukaran data.

Menurut cakupan, **PAN** menghubungkan perangkat pribadi dalam jarak dekat; **LAN** mencakup area terbatas seperti rumah atau gedung; **MAN** mencakup area metropolitan; dan **WAN** menghubungkan area geografis luas. Internet adalah jaringan global yang terdiri dari banyak jaringan saling terhubung.

Topologi menggambarkan susunan koneksi perangkat. **Star** menghubungkan perangkat ke satu titik pusat, mudah dikelola tetapi bergantung pada perangkat pusat. **Bus** menggunakan satu jalur bersama, sederhana tetapi rentan pada gangguan jalur utama. **Ring** membentuk jalur melingkar. **Mesh** menyediakan beberapa jalur antarnode sehingga redundan, tetapi memerlukan lebih banyak koneksi.

## 2. Model komunikasi

Model OSI memiliki tujuh lapisan:

| Lapisan | Fungsi ringkas |
| --- | --- |
| 7. Application | Layanan jaringan yang digunakan aplikasi, misalnya HTTP dan DNS |
| 6. Presentation | Representasi data, enkripsi, dan kompresi |
| 5. Session | Mengatur sesi komunikasi |
| 4. Transport | Komunikasi antaraplikasi, port, segmentasi; contohnya TCP dan UDP |
| 3. Network | Pengalamatan logis dan pemilihan rute; contohnya IP |
| 2. Data Link | Pengiriman frame pada satu link dan alamat MAC |
| 1. Physical | Pengiriman bit melalui media fisik atau radio |

Model TCP/IP mengelompokkan fungsi tersebut menjadi **Application**, **Transport**, **Internet**, dan **Network Access**. Saat mengirim data, tiap lapisan menambahkan informasi kendali (enkapsulasi); penerima membukanya kembali secara berlapis (dekapsulasi).

## 3. Standar dan protokol Wi-Fi

Wi-Fi adalah teknologi jaringan lokal nirkabel yang terutama mengikuti keluarga standar **IEEE 802.11**. IEEE menetapkan spesifikasi teknis; Wi-Fi Alliance mengelola sertifikasi interoperabilitas dan nama generasi Wi-Fi. Nama Wi-Fi dan angka generasinya bukan pengganti nomor amendemen IEEE.

| Generasi Wi-Fi | Standar IEEE terkait | Pita frekuensi umum | Keterangan |
| --- | --- | --- | --- |
| Wi-Fi 4 | 802.11n | 2,4 dan 5 GHz | Mendukung MIMO |
| Wi-Fi 5 | 802.11ac | 5 GHz | Meningkatkan kapasitas dan laju data |
| Wi-Fi 6 / 6E | 802.11ax | 2,4 dan 5 GHz; Wi-Fi 6E juga 6 GHz jika diizinkan | Efisien pada jaringan padat; menggunakan OFDMA |
| Wi-Fi 7 | 802.11be | 2,4, 5, dan 6 GHz sesuai dukungan serta regulasi | Mendukung kanal lebih lebar dan operasi multi-link |

Standar lama antara lain 802.11b/g (2,4 GHz) dan 802.11a (5 GHz). Kemampuan nyata bergantung pada access point dan klien, lebar kanal, jarak, interferensi, jumlah klien, serta regulasi. Kecepatan maksimum standar adalah nilai teoretis, bukan jaminan throughput aplikasi.

Protokol terkait Wi-Fi meliputi **802.11 MAC/PHY** untuk akses kanal dan transmisi radio; **WPA2/WPA3** untuk keamanan dan autentikasi; **DHCP** untuk konfigurasi IP; serta **IP, TCP/UDP, DNS, dan HTTP(S)** yang berjalan di atas koneksi. Gunakan WPA2-AES atau WPA3 bila tersedia; hindari WEP dan WPA/TKIP yang sudah usang.

### Kesimpulan

Jaringan memungkinkan perangkat bertukar data melalui media dan protokol yang disepakati. Wi-Fi merupakan LAN nirkabel berbasis keluarga IEEE 802.11; keamanan, kualitas sinyal, kompatibilitas, dan regulasi sama pentingnya dengan generasi standar.