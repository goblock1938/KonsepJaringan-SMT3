# Tugas 5 — Analisis Traceroute dan Mekanisme TTL

**Traceroute** (`tracert` pada Windows) adalah alat diagnostik untuk menemukan router atau *hop* yang dilewati paket menuju alamat tujuan. Traceroute juga mengukur waktu pulang-pergi (RTT) ke tiap hop, sehingga membantu mengidentifikasi bagian jalur yang lambat atau tidak merespons.

## TTL (Time To Live)

TTL adalah field pada header IPv4 yang membatasi jumlah hop yang boleh dilalui paket. Setiap router yang meneruskan paket mengurangi TTL sedikitnya satu. TTL bukan pengukur waktu nyata: fungsinya mencegah paket beredar tanpa batas akibat kesalahan routing. Jika TTL menjadi nol, router membuang paket.

IPv6 menggunakan field **Hop Limit** dengan fungsi yang sama. Nilai awal TTL/Hop Limit ditetapkan oleh sistem pengirim.

## Cara traceroute menggunakan TTL dan ICMP

Traceroute mengirim serangkaian probe dengan nilai TTL yang dimulai dari 1 dan dinaikkan satu per satu:

1. Probe dengan TTL 1 tiba di router pertama. Router mengurangi TTL menjadi 0, membuang probe, lalu biasanya mengirim pesan **ICMP Time Exceeded** (Type 11, Code 0). Traceroute mencatat alamat router tersebut sebagai hop pertama.
2. Probe berikutnya dikirim dengan TTL 2. Router pertama menguranginya menjadi 1 dan meneruskannya. Router kedua menghabiskan TTL menjadi 0 dan mengirim ICMP Time Exceeded. Alamatnya dicatat sebagai hop kedua.
3. Proses diulang dengan TTL 3, 4, dan seterusnya sampai probe mencapai tujuan atau batas hop tercapai.
4. Saat tujuan menerima probe, ia mengirim respons sesuai jenis probe. Traceroute mengenali respons itu sebagai tanda tujuan tercapai.

**ICMP (Internet Control Message Protocol)** membawa pesan kendali dan kesalahan jaringan. Pesan Time Exceeded mengungkap router yang menghabiskan TTL; pesan Destination Unreachable dapat menunjukkan tujuan atau layanan tidak dapat dicapai. Traceroute Unix/Linux tradisional sering menggunakan probe UDP, sedangkan `tracert` Windows lazim menggunakan ICMP Echo Request. Implementasi lain dapat menggunakan TCP.

## Contoh alur

Misalkan host `192.0.2.10` menelusuri rute menuju `198.51.100.20`. Probe TTL 1 dibalas oleh R1 dengan ICMP Time Exceeded. Probe TTL 2 melewati R1, lalu dibalas R2. Probe TTL 3 dibalas R3, dan seterusnya. Ketika salah satu probe mendapat respons dari `198.51.100.20`, tujuan tercapai dan traceroute berhenti.

Setiap hop biasanya menampilkan alamat/nama router dan waktu respons dari beberapa probe. Tanda `*` berarti tidak ada balasan sebelum batas waktu, bukan bukti pasti bahwa router atau seluruh jalur mati. Router dapat menyaring atau membatasi ICMP, jalur balik bisa berbeda, dan load balancing dapat menyebabkan probe menampilkan router berbeda.
