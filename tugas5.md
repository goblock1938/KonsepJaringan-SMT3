# Tugas 5 — Cara Kerja Traceroute dan Mekanisme TTL

**Traceroute** (disebut `tracert` pada Windows) memperkirakan router yang dilewati paket dari komputer sumber menuju tujuan. Program mengirim rangkaian probe dengan nilai **TTL (Time To Live)** atau **Hop Limit** yang dinaikkan bertahap.

## Cara kerja TTL

Pada IPv4, TTL adalah nilai pada header paket yang dibatasi oleh pengirim. Setiap router yang meneruskan paket mengurangi TTL sedikitnya satu. TTL bukan hitung mundur waktu nyata; fungsinya terutama membatasi jumlah hop agar paket yang berputar akibat kesalahan routing tidak beredar selamanya. Jika nilainya mencapai nol, router membuang paket dan biasanya mengirim pesan ICMP **Time Exceeded**.

IPv6 menggunakan field **Hop Limit** dengan fungsi serupa, bukan field TTL.

## Proses traceroute

1. Program mengirim probe pertama dengan TTL 1.
2. Router pertama menguranginya menjadi 0, membuang probe, lalu mengirim ICMP Time Exceeded. Alamat sumber pesan menunjukkan router pertama.
3. Probe dengan TTL 2 melewati router pertama setelah TTL dikurangi menjadi 1; router kedua kemudian menghabiskannya dan mengirim Time Exceeded.
4. TTL dinaikkan lagi untuk mengungkap hop berikutnya.
5. Ketika probe mencapai tujuan, respons yang menandakan tujuan tercapai bergantung pada jenis probe dan implementasi traceroute.

Traceroute Unix/Linux tradisional lazim mengirim probe UDP ke port tujuan tinggi, sedangkan `tracert` Windows umumnya memakai ICMP Echo Request. Implementasi lain dapat memakai ICMP atau TCP. Firewall mungkin mengizinkan satu jenis probe tetapi memblokir jenis lain.

## Membaca hasil dan keterbatasan

Setiap baris biasanya memuat nomor hop, alamat/nama router, serta waktu pulang-pergi dari beberapa probe. Tanda `*` berarti probe tidak menerima jawaban sebelum batas waktu, bukan bukti pasti router atau seluruh koneksi mati. Router dapat memfilter atau membatasi balasan ICMP; jalur balik juga mungkin berbeda. Load balancing dapat membuat probe menampilkan router berbeda pada hop yang sama.

Traceroute membantu memperkirakan lokasi jalur mulai tidak merespons atau mengalami latensi, tetapi satu hasil tidak selalu membuktikan penyebab gangguan. Bandingkan beberapa pengujian, tujuan, dan waktu; jangan menyimpulkan bahwa jalur balik sama dengan jalur paket aplikasi.