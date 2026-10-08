# Tugas 2 — Bab 2 A, B, dan C

> **Catatan cakupan:** Soal hanya menyebut “Bab 2 A, B dan C” tanpa judul atau isi modul. Jawaban ini memakai tiga pokok bahasan dasar jaringan sebagai susunan sementara: media transmisi, topologi, serta perangkat dan arsitektur. Cocokkan dengan bahan ajar sebelum dikumpulkan.

## A. Media transmisi

Media transmisi adalah jalur yang membawa sinyal dari pengirim ke penerima.

**Media terpandu (kabel):**

- **Twisted pair (UTP/STP):** pasangan kabel tembaga yang dipilin untuk mengurangi gangguan. Umum digunakan pada Ethernet LAN; STP memiliki pelindung tambahan.
- **Koaksial:** konduktor inti dengan lapisan pelindung; digunakan pada beberapa sistem kabel dan komunikasi radio.
- **Serat optik:** mengirim data sebagai cahaya. Mendukung bandwidth tinggi dan jarak jauh serta tidak rentan terhadap interferensi elektromagnetik, tetapi instalasi dan penyambungannya memerlukan perangkat khusus.

**Media tak terpandu (nirkabel):** gelombang radio, gelombang mikro, dan inframerah membawa data tanpa kabel fisik. Wi-Fi dan Bluetooth menggunakan gelombang radio. Mobilitas menjadi kelebihan media nirkabel; interferensi, penghalang, jarak, dan keamanan perlu dipertimbangkan.

Pemilihan media dipengaruhi jarak, laju data, biaya, lingkungan, kemudahan pemasangan, dan tingkat gangguan.

## B. Topologi jaringan

Topologi fisik menunjukkan susunan kabel/perangkat, sedangkan topologi logis menjelaskan aliran komunikasi data.

| Topologi | Susunan | Kelebihan | Kekurangan |
| --- | --- | --- | --- |
| Star | Setiap node terhubung ke perangkat pusat | Mudah ditambah; gangguan satu kabel biasanya terbatas | Perangkat pusat menjadi titik kegagalan |
| Bus | Semua node berbagi satu jalur utama | Hemat kabel dan sederhana untuk jaringan kecil | Gangguan jalur utama dapat mengganggu seluruh jaringan |
| Ring | Node membentuk lingkaran | Aliran dapat teratur pada implementasi tertentu | Gangguan jalur/node dapat mengganggu ring tanpa redundansi |
| Mesh | Node memiliki beberapa jalur antarnode | Toleran terhadap kegagalan jalur | Mahal dan lebih rumit |
| Tree | Beberapa star tersusun bertingkat | Mudah dikembangkan secara hierarkis | Gangguan pada backbone berdampak luas |

LAN Ethernet modern umumnya memakai topologi fisik star dengan switch sebagai pusat. Wi-Fi infrastruktur biasanya berbentuk star secara logis, dengan access point sebagai titik penghubung klien.

## C. Perangkat jaringan dan arsitektur layanan

- **NIC:** antarmuka untuk mengirim dan menerima data; memiliki alamat MAC.
- **Hub:** meneruskan sinyal ke semua port tanpa memilih tujuan; kini umumnya digantikan switch.
- **Switch:** meneruskan frame dalam LAN berdasarkan alamat MAC.
- **Router:** meneruskan paket antarjaringan berdasarkan alamat IP dan tabel rute.
- **Access point:** menghubungkan klien nirkabel ke jaringan.
- **Modem/ONT:** mengakhiri atau menyesuaikan koneksi dari penyedia internet sesuai teknologi akses.
- **Server:** menyediakan layanan atau sumber daya bagi klien.

Dalam arsitektur **client-server**, server menyediakan layanan terpusat dan klien memintanya. Pengelolaan dan kontrol akses lebih mudah, tetapi layanan bergantung pada ketersediaan server. Dalam **peer-to-peer**, perangkat dapat menjadi klien sekaligus penyedia sumber daya; cara ini sederhana untuk kelompok kecil tetapi lebih sulit dikelola saat skala bertambah.

Contohnya, switch menghubungkan perangkat di dalam satu LAN, sedangkan router menghubungkan LAN ke jaringan lain seperti internet.