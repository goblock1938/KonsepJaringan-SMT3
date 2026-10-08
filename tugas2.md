# Tugas 2 — Model dan Protokol Jaringan

## Level A — Ingatan dan Pemahaman

### 1. Mengapa komunikasi jaringan disusun berlapis?

Pembagian berlapis memecah komunikasi yang kompleks menjadi fungsi-fungsi dengan tanggung jawab dan batas yang jelas. Setiap lapisan menggunakan layanan lapisan di bawahnya dan menyediakan layanan bagi lapisan di atasnya. Cara ini memudahkan perancangan, pengujian, interoperabilitas antarvendor, serta penggantian teknologi pada satu lapisan tanpa harus mengubah seluruh sistem.

### 2. Bedakan layanan, antarmuka, dan protokol

- **Layanan** menjelaskan _apa_ yang disediakan suatu lapisan kepada lapisan di atasnya, misalnya pengiriman data yang andal.
- **Antarmuka** menjelaskan cara lapisan di atas meminta layanan itu, termasuk operasi dan parameter yang tersedia.
- **Protokol** adalah aturan komunikasi antara entitas sejajar pada dua sistem, seperti format pesan, urutan pertukaran, dan tindakan ketika terjadi kesalahan.

Layanan bersifat vertikal di antara lapisan dalam satu sistem; protokol mengatur komunikasi horizontal antara sistem.

### 3. Tujuh lapisan OSI dari bawah ke atas dan fungsi utamanya

1. **Physical (Fisik):** mengirim bit melalui media fisik; mencakup sinyal, konektor, dan karakteristik transmisi.
2. **Data Link (Tautan Data):** mengirim frame pada satu tautan, menggunakan alamat tautan, serta menangani akses media dan deteksi kesalahan tautan.
3. **Network (Jaringan):** pengalamatan logis dan penerusan paket antarjaringan.
4. **Transport:** komunikasi proses-ke-proses, segmentasi, multiplexing, dan—bergantung protokol—keandalan serta kontrol aliran.
5. **Session (Sesi):** pengelolaan dialog dan konteks sesi antara aplikasi.
6. **Presentation (Presentasi):** representasi, format, kompresi, dan transformasi data agar dapat dipahami aplikasi.
7. **Application (Aplikasi):** layanan jaringan yang digunakan aplikasi, seperti web, surat elektronik, dan resolusi nama.

### 4. Empat lapisan model TCP/IP

Model TCP/IP empat lapisan terdiri atas **Link/Network Access**, **Internet**, **Transport**, dan **Application**. Nama lapisan terbawah dan rincian cakupannya dapat berbeda antarreferensi; model ini menggabungkan fungsi OSI Data Link dan Physical dalam Link, serta menggabungkan Session, Presentation, dan Application dalam Application.

### 5. Mengapa model TCP/IP kadang disajikan sebagai lima lapisan?

Model lima lapisan memisahkan Link menjadi **Data Link** dan **Physical**, sehingga lebih mudah mengajarkan media, sinyal, dan framing sebagai konsep yang berbeda. Empat lapisan lebih dekat pada pengelompokan arsitektur TCP/IP; lima lapisan merupakan kerangka pedagogis yang mempertahankan pemisahan fungsi tersebut.

### 6. Perbedaan frame, IP packet, TCP segment, dan UDP datagram

Semua istilah itu menyebut unit data pada lapisan berbeda:

- **Frame** adalah unit Data Link untuk pengiriman melalui satu tautan. Frame membawa alamat tautan dan payload yang biasanya memuat paket lapisan jaringan.
- **IP packet (datagram IP)** adalah unit lapisan Internet/Jaringan yang membawa alamat IP sumber dan tujuan untuk diteruskan antarjaringan.
- **TCP segment** adalah unit TCP yang membawa port, nomor urut, dan informasi kontrol TCP.
- **UDP datagram** adalah unit UDP dengan port sumber/tujuan, panjang, dan checksum, tanpa mekanisme koneksi dan pengiriman andal seperti TCP.

Istilah _datagram_ kadang digunakan lebih luas, tetapi dalam konteks ini “IP packet” dan “UDP datagram” membedakan unit pada lapisan masing-masing.

### 7. Header, trailer, dan payload

- **Header** memuat informasi kendali sebelum data, seperti alamat, port, panjang, atau nomor urut.
- **Trailer** memuat informasi kendali setelah data, misalnya FCS pada Ethernet untuk mendeteksi kerusakan frame.
- **Payload** adalah isi yang dibawa oleh suatu unit protokol; payload pada satu lapisan dapat berupa seluruh unit lapisan di atasnya.

Tidak semua protokol menggunakan trailer.

### 8. Enkapsulasi dan dekapsulasi

Saat mengirim, setiap lapisan membungkus data dari lapisan di atasnya dengan informasi kendalinya; proses ini disebut **enkapsulasi**. Contohnya, data aplikasi dibungkus header TCP, lalu header IP, lalu header dan trailer Ethernet. Penerima melakukan **dekapsulasi** dengan memeriksa dan melepas informasi setiap lapisan sebelum menyerahkan payload ke lapisan berikutnya.

### 9. Fungsi multiplexing dan demultiplexing

**Multiplexing** memungkinkan satu lapisan atau protokol melayani beberapa aliran/entitas di atasnya dan membawa datanya melalui sumber daya bersama. **Demultiplexing** memilih penerima atau protokol yang tepat berdasarkan pengenal di header. Contohnya, IP menggunakan field _Protocol_ atau _Next Header_ untuk memilih TCP/UDP, sedangkan TCP/UDP menggunakan nomor port untuk mengarahkan data ke soket atau proses yang sesuai.

### 10. Mengapa OSI bukan spesifikasi implementasi?

OSI adalah **model referensi konseptual** yang mengelompokkan fungsi dan hubungan layanan. Model itu tidak dengan sendirinya menetapkan format paket, algoritma, API, atau implementasi lengkap. Standar protokol tertentu dapat mengisi fungsi terkait, tetapi implementasi Internet nyata mengikuti protokol dan standar yang spesifik, bukan kewajiban menerapkan tujuh modul OSI secara persis.

## Level B — Penerapan dan Analisis

### 11. Pemetaan protokol ke model TCP/IP

| Protokol            | Lapisan TCP/IP                                                           | Catatan                                                                                                                                                     |
| ------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HTTP                | Application                                                              | Protokol aplikasi web.                                                                                                                                      |
| TLS                 | Di antara aplikasi dan transport; lazim dikelompokkan dengan Application | TLS memberi keamanan pada aliran aplikasi di atas TCP; bukan satu lapisan OSI yang selalu tetap.                                                            |
| TCP                 | Transport                                                                | Aliran byte andal dan berurutan antarsoket.                                                                                                                 |
| UDP                 | Transport                                                                | Pengiriman datagram tanpa koneksi.                                                                                                                          |
| QUIC                | Transport                                                                | Transport terenkripsi dan termultipleks yang berjalan di atas UDP; pemetaan sebagai transport berdasarkan fungsinya, walau implementasinya menggunakan UDP. |
| IPv6                | Internet                                                                 | Pengalamatan dan penerusan paket.                                                                                                                           |
| ICMP                | Internet                                                                 | Pesan kendali dan diagnostik yang terkait erat dengan IP; ICMPv6 juga menyediakan fungsi penting untuk operasi IPv6, termasuk Neighbor Discovery.           |
| Ethernet            | Link/Network Access                                                      | Framing dan pengiriman pada LAN Ethernet.                                                                                                                   |
| Wi-Fi (IEEE 802.11) | Link/Network Access                                                      | Mencakup fungsi tautan dan mekanisme radio fisik; karena itu rincian standar 802.11 dapat menyentuh dua lapisan terbawah.                                   |
| DNS                 | Application                                                              | Protokol aplikasi yang biasanya memakai UDP atau TCP; DNS terenkripsi dapat memakai TLS atau HTTPS.                                                         |

Pemetaan adalah alat bantu, bukan aturan bahwa setiap protokol hanya dapat berinteraksi dengan satu lapisan.

### 12. Enkapsulasi permintaan DNS melalui UDP, IPv4, dan Ethernet

```text
Bit pada media
└─ Ethernet frame [MAC tujuan, MAC sumber, EtherType=IPv4]
   └─ IPv4 packet [IP sumber, IP tujuan, Protocol=UDP]
      └─ UDP datagram [port sumber sementara, port tujuan 53]
         └─ Pesan DNS [ID transaksi, flags, pertanyaan nama/tipe]
```

Pada batas aplikasi, ID transaksi DNS membantu mencocokkan respons dengan kueri. UDP memakai port untuk demultiplexing ke layanan DNS dan soket peminta. IPv4 memakai alamat IP untuk pengiriman antarjaringan serta field Protocol untuk memilih UDP. Ethernet memakai alamat MAC untuk pengiriman pada tautan lokal dan EtherType untuk menunjukkan IPv4. Port tujuan biasanya 53; port sumber klien biasanya sementara. Respons biasanya dikirim dari port 53 ke port sumber tersebut. DNS juga dapat menggunakan TCP, dan detail keamanan seperti DNS over TLS mengubah enkapsulasinya.

### 13. Enkapsulasi HTTP/3 melalui QUIC

```text
Bit pada media
└─ Frame tautan (mis. Ethernet) [MAC sumber/tujuan, EtherType]
   └─ Paket IP [IP sumber/tujuan, penanda UDP]
      └─ UDP datagram [port UDP; umumnya 443]
         └─ Paket QUIC [Connection ID, nomor paket, frame QUIC, data terenkripsi]
            └─ Aliran HTTP/3 [frame HTTP/3; header terkompresi QPACK]
```

QUIC dapat dianggap protokol transport karena menyediakan aliran termultipleks, reliabilitas per aliran, kontrol kemacetan, pengelolaan koneksi, dan keamanan TLS 1.3 yang terintegrasi. UDP berperan sebagai pembawa datagram yang memudahkan QUIC berjalan melalui jaringan IP dan perangkat perantara yang sudah mendukung UDP. Jadi, QUIC berfungsi pada transport, tetapi tidak menggantikan fakta bahwa paketnya dibawa oleh UDP. Nomor port memilih layanan UDP, sedangkan Connection ID membantu QUIC mengenali koneksi, termasuk ketika alamat jaringan berubah. HTTP/3 memakai aliran QUIC; detail HTTP di dalamnya terenkripsi.

### 14. Header yang berubah dan tetap ketika paket melewati router (tanpa NAT)

Router menerima frame tautan masuk, memproses paket IP, lalu membungkusnya dalam frame tautan baru untuk tautan keluar. Karena itu, **header Data Link berubah**: alamat MAC sumber dan tujuan serta nilai terkait tautan disesuaikan dengan hop berikutnya. Trailer/FCS juga dihitung ulang.

Alamat IP sumber dan tujuan umumnya tetap, demikian pula port TCP/UDP dan isi transport/aplikasi. Pada IPv4, TTL berkurang satu dan checksum header IPv4 diperbarui. Pada IPv6, Hop Limit berkurang; IPv6 tidak memiliki checksum header. Router biasa tidak mengubah checksum TCP/UDP karena alamat IP dan port tidak berubah. Pengecualian dapat terjadi akibat fragmentasi IPv4, kebijakan jaringan, atau layanan perantara tertentu. Jika ada tag VLAN, penanganannya bergantung konfigurasi tautan.

### 15. Perubahan jika router melakukan NAT/PAT

NAT mengubah satu atau lebih alamat IP di header dan harus memperbarui checksum yang dipengaruhi perubahan tersebut. **PAT/NAPT** juga mengubah port TCP/UDP agar beberapa aliran dapat berbagi alamat publik; checksum TCP/UDP terkait juga diperbarui. Perangkat menyimpan pemetaan agar balasan dapat diterjemahkan kembali. Karena terjemahan mengubah tuple alamat/port, NAT dapat memengaruhi koneksi masuk, protokol yang membawa alamat di payload, pelacakan koneksi, dan diagnostik. Header tautan tetap dibuat ulang per hop seperti pada router biasa.

### 16. Checksum TCP salah pada paket keluar tanpa gangguan komunikasi

Hipotesis yang masuk akal adalah **TCP checksum offload**. Sistem operasi atau capture point menangkap paket sebelum NIC menghitung checksum akhir, sehingga terlihat checksum belum valid meskipun NIC mengisinya sebelum transmisi. TSO/GSO dapat membuat capture lokal juga menampilkan segmen besar yang kemudian dipecah oleh NIC. Periksa capture di sisi penerima atau gunakan capture eksternal; bila checksum di sana valid dan komunikasi berjalan, offload kemungkinan menjelaskan gejala. Jika tetap salah pada capture eksternal, periksa konfigurasi offload, driver, atau kerusakan paket.

### 17. Portal dapat dibuka dengan IP, tetapi tidak dengan nama

Karena akses langsung dengan IP berhasil, konektivitas dasar ke alamat tersebut mungkin tersedia, tetapi itu belum membuktikan semua layanan berfungsi. Telusuri berurutan:

1. **Application/naming:** pastikan nama yang dimasukkan benar dan uji resolusi DNS; periksa hasil A/AAAA, search suffix, cache, dan konfigurasi resolver.
2. **Transport:** pastikan kueri DNS dapat mencapai resolver (umumnya UDP/TCP port 53, atau DNS terenkripsi melalui port lain); periksa firewall dan timeout.
3. **Internet/Network:** periksa rute ke resolver serta kemungkinan perbedaan jangkauan IPv4 dan IPv6.
4. **Application/web:** jika nama berhasil di-resolve tetapi situs gagal, periksa virtual hosting dan TLS. Mengakses alamat IP dapat mengirim Host header atau SNI yang berbeda dari permintaan memakai nama.

Gunakan `nslookup`/`dig` atau alat setara, lalu bandingkan DNS, koneksi ke IP, sertifikat, dan respons HTTP. Jangan langsung menyimpulkan DNS adalah satu-satunya kemungkinan.

### 18. Ping berhasil, tetapi HTTPS gagal: hipotesis Transport hingga Application

Ping umumnya memakai ICMP, bukan TCP/TLS/HTTPS, sehingga keberhasilannya hanya membuktikan sebagian jalur IP. Hipotesis yang dapat diuji antara lain:

1. TCP port 443 diblokir atau tidak ada rute/policy untuk port tersebut.
2. Server tidak mendengarkan pada port 443 atau layanan sedang gagal.
3. Handshake TCP gagal karena kehilangan paket, MTU/PMTUD, atau middlebox.
4. Negosiasi TLS gagal akibat sertifikat tidak valid/kedaluwarsa, nama sertifikat tidak cocok, waktu sistem salah, atau trust store bermasalah.
5. Versi TLS atau cipher yang didukung klien dan server tidak cocok.
6. SNI salah/tidak dikirim atau virtual host memilih situs yang keliru.
7. Proxy, firewall aplikasi, inspeksi TLS, atau kebijakan autentikasi menghalangi permintaan.
8. HTTPS terbentuk, tetapi aplikasi mengembalikan error HTTP, redirect bermasalah, atau backend tidak sehat.

### 19. Sesi aplikasi dibandingkan koneksi TCP

Koneksi TCP adalah hubungan transport antara endpoint yang dikenali oleh tuple alamat dan port, dengan status handshake, nomor urut, dan kontrol pengiriman. **Sesi aplikasi** adalah konteks yang ditetapkan aplikasi, seperti pengguna yang login, keranjang belanja, atau suatu panggilan konferensi. Sesi dapat mencakup beberapa koneksi dan berlangsung lebih lama daripada satu koneksi TCP.

Contoh: aplikasi web menyimpan sesi login dalam cookie atau token. Setelah koneksi TCP putus, pengguna terhubung kembali melalui koneksi TCP baru dan aplikasi mengenali sesi yang sama dari token tersebut. Implementasi tertentu juga dapat mempertahankan koneksi QUIC ketika jalur jaringan berubah.

### 20. Mengapa enkripsi tidak selalu berada pada Presentation layer?

Enkripsi adalah fungsi keamanan yang dapat diterapkan pada batas berbeda, bukan fungsi yang secara eksklusif dimiliki satu lapisan OSI. TLS lazim digambarkan di antara aplikasi dan transport (atau secara pedagogis pada Application/Presentation), IPsec melindungi trafik pada lapisan IP, MACsec melindungi tautan Ethernet, dan aplikasi dapat melakukan enkripsi end-to-end sendiri. Lokasi, cakupan data, metadata yang terlihat, dan titik terminasi berbeda sesuai mekanismenya.

## Level C — Evaluasi dan Sintesis

### 21. “OSI tidak lagi relevan karena Internet menggunakan TCP/IP”

Pernyataan tersebut mencampuradukkan **model** dengan **protokol**. TCP/IP adalah keluarga protokol dan arsitektur yang digunakan Internet; OSI adalah model referensi untuk menjelaskan dan mengelompokkan fungsi komunikasi. Internet tidak perlu mengimplementasikan tujuh lapisan OSI secara persis agar model itu berguna.

OSI tetap berguna untuk mengajarkan pemisahan fungsi, membandingkan teknologi, dan menyusun hipotesis saat mendiagnosis masalah. Namun, pemetaan protokol nyata ke lapisan OSI sering tidak satu-banding-satu, sehingga model tidak boleh diperlakukan sebagai deskripsi implementasi literal. Secara akademik, lebih tepat menyatakan TCP/IP dominan sebagai arsitektur operasional Internet, sementara OSI tetap bernilai sebagai abstraksi dan alat pedagogis dengan keterbatasan.

### 22. Keuntungan dan kerugian _strict layering_

**Keuntungan:** batas tanggung jawab jelas, komponen dapat diuji atau diganti secara independen, interoperabilitas lebih mudah, dan perubahan lokal cenderung tidak merambat ke seluruh sistem.

**Kerugian:** lapisan dapat menggandakan fungsi (misalnya retry atau kontrol kesalahan), menambah overhead dan latensi, serta menyembunyikan informasi yang diperlukan untuk optimasi.

Cross-layer information membantu bila digunakan secara terbatas dan terukur. Contohnya, aplikasi real-time dapat menyesuaikan bitrate berdasarkan estimasi kemacetan atau kualitas tautan. Namun, ketergantungan langsung pada rincian implementasi lapisan bawah membuat sistem rapuh terhadap perubahan, mengurangi portabilitas, dan dapat menghasilkan optimasi yang salah untuk kondisi lain. Pertukaran informasi sebaiknya memakai antarmuka yang jelas, tanpa menghapus tanggung jawab utama tiap lapisan.

### 23. Prosedur diagnosis video konferensi tersendat pada Wi-Fi kampus saat jam sibuk

1. **Tetapkan pembanding dan waktu:** ulangi panggilan di lokasi, perangkat, dan jam berbeda; bandingkan Wi-Fi dengan Ethernet atau jaringan lain jika diizinkan. Catat waktu, lokasi, access point, dan apakah semua pengguna terdampak.
2. **Physical/Data Link:** ukur kekuatan sinyal, SNR, retransmission, channel utilization, jumlah klien, roaming, dan kehilangan frame. Bandingkan access point/channel yang padat dengan titik yang tidak padat.
3. **Network:** ukur kehilangan, latensi, jitter, rute, dan MTU menuju server konferensi; bandingkan gateway dan jalur saat sibuk dengan luar jam sibuk. ICMP saja bukan pengganti pengukuran trafik aplikasi.
4. **Transport:** periksa statistik UDP/TCP aplikasi, kehilangan datagram, perubahan jalur, dan apakah trafik real-time atau koneksi kontrol dibatasi QoS/firewall.
5. **Application:** periksa metrik aplikasi seperti packet loss, jitter buffer, RTT, bitrate adaptif, frame rate, serta server/region yang dipilih.
6. **Simpulkan dari korelasi:** jika airtime dan retry Wi-Fi memburuk pada jam sibuk dan keluhan hanya di Wi-Fi, bukti mengarah ke kepadatan radio; jika Wi-Fi bersih tetapi kehilangan muncul setelah gateway, telusuri jalur kampus atau layanan. Ubah satu variabel setiap kali dan ulangi pengukuran untuk menghindari menyamakan korelasi dengan penyebab.

### 24. Skenario laboratorium perekaman paket tanpa data sensitif

Gunakan jaringan lokal terisolasi atau server laboratorium yang diizinkan, klien uji, dan nama/domain dummy. Buat satu permintaan HTTPS ke halaman yang hanya berisi teks sintetis, tanpa akun, cookie nyata, atau data pribadi. Ambil capture hanya pada antarmuka klien atau segmen lab, batasi durasi dan filter pada alamat/port uji, lalu identifikasi:

- Ethernet dan alamat MAC pada tautan lokal;
- IP sumber/tujuan dan TTL/Hop Limit;
- TCP handshake serta nomor port, atau datagram UDP bila protokol yang diuji menggunakannya;
- handshake TLS, versi, sertifikat, dan metadata yang memang terlihat;
- protokol aplikasi melalui metadata yang tidak terenkripsi atau log server laboratorium. Untuk HTTPS, isi HTTP biasanya terenkripsi; jangan mengklaim payload aplikasi dapat dibaca dari capture biasa.

Hapus alamat yang tidak perlu sebelum membagikan capture, batasi akses dan retensi berkas, serta jangan menangkap trafik pengguna lain. Jika perlu mengamati isi aplikasi, gunakan data dummy dan log pada endpoint laboratorium, bukan dekripsi trafik pihak lain.

### 25. VXLAN di atas UDP dan IPsec tunnel: urutan header dan risiko MTU

Salah satu susunan ketika IPsec tunnel melindungi paket VXLAN yang melintasi underlay:

```text
Ethernet underlay
└─ IP luar (alamat endpoint IPsec)
   └─ ESP/IPsec
      └─ IP dalam (alamat endpoint VTEP)
         └─ UDP (port tujuan VXLAN, biasanya 4789)
            └─ VXLAN (VNI)
               └─ Ethernet dalam
                  └─ IP asli dan payload
```

IPsec tunnel menambah header luar dan overhead ESP; VXLAN menambah UDP, header IP underlay, dan header VXLAN/Ethernet dalam. Jika IPsec diterapkan sebagai transport mode atau pada segmen/urutan tunnel yang berbeda, detail header berubah. Overhead ini mengurangi MTU efektif untuk payload. Paket yang terlalu besar dapat terfragmentasi (tergantung lapisan dan konfigurasi), dibuang, atau mengalami black hole bila Path MTU Discovery/ICMP terkait terhalang. Mitigasinya mencakup perhitungan MTU/MSS yang sesuai, mengizinkan pesan PMTUD yang diperlukan, dan menguji ukuran paket end-to-end.

### 26. MACsec, IPsec, TLS, dan enkripsi end-to-end aplikasi

| Mekanisme                    | Cakupan umum                                                             | Titik terminasi dan batas kepercayaan                                                                                                                          |
| ---------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MACsec                       | Satu tautan Ethernet antara perangkat/port yang memiliki hubungan MACsec | Berakhir pada peer MACsec berikutnya; perangkat perantara di luar tautan itu tidak otomatis terlindungi.                                                       |
| IPsec                        | Trafik IP antara host atau gateway/tunnel                                | Berakhir pada endpoint IPsec; gateway tunnel dapat melihat trafik setelah dekripsi kecuali perlindungan lain diteruskan.                                       |
| TLS                          | Satu koneksi TLS antara klien dan terminator TLS                         | Berakhir pada server atau proxy/load balancer TLS; terminator dapat membaca plaintext. Koneksi TLS baru mungkin dibuat ke backend.                             |
| Enkripsi end-to-end aplikasi | Data aplikasi antara endpoint yang dipercaya aplikasi                    | Idealnya hanya endpoint akhir memiliki kunci plaintext; server perantara dapat meneruskan ciphertext. Desain kunci dan metadata menentukan perlindungan nyata. |

Keempat mekanisme dapat dipakai bersamaan. Enkripsi melindungi isi dalam cakupannya, tetapi tidak serta-merta menyembunyikan semua metadata atau melindungi endpoint yang telah dikuasai.

### 27. Bagaimana firewall, proxy, dan load balancer menantang pemisahan lapisan?

Perangkat jaringan tidak selalu terbatas membaca satu jenis header. Firewall _stateful_ mengaitkan IP dan port dengan status koneksi; firewall aplikasi dapat memeriksa protokol aplikasi. Proxy dapat mengakhiri TCP/TLS, membaca permintaan HTTP, lalu membuat koneksi baru ke server. Load balancer dapat merutekan berdasarkan alamat/port, nama host, URL, atau informasi TLS yang tersedia, dan dapat menjadi terminator TLS.

Perangkat tersebut menggabungkan fungsi dari beberapa lapisan karena kebutuhan kebijakan, keamanan, dan distribusi trafik. Ini tidak membatalkan model lapisan, tetapi menunjukkan bahwa model adalah abstraksi fungsi, bukan aturan bahwa satu perangkat hanya boleh memproses satu lapisan. Terminasi koneksi juga menciptakan batas kepercayaan dan dapat mengubah perilaku end-to-end.

### 28. Pemeriksaan integritas berkas menurut prinsip end-to-end

Pemeriksaan di router dapat mendeteksi kerusakan pada bagian atau hop tertentu, tetapi router umumnya tidak memiliki konteks berkas lengkap dan pemeriksaan per-hop tidak membuktikan bahwa berkas yang diterima aplikasi sama dengan berkas yang dikirim. Checksum transport mendeteksi kerusakan data pada cakupan segmen/aliran, tetapi bukan bukti identitas penerbit atau integritas semantik seluruh berkas.

Menurut prinsip end-to-end, aplikasi penerima sebaiknya memverifikasi berkas lengkap—misalnya dengan hash yang diharapkan dari kanal tepercaya atau tanda tangan digital—karena hanya endpoint yang memahami objek lengkap dan kebutuhannya. Pemeriksaan pada jaringan tetap dapat membantu diagnosis atau menolak kerusakan lebih awal, tetapi tidak menggantikan verifikasi endpoint. Hash tanpa sumber pembanding tepercaya hanya mendeteksi perubahan bila nilai hash tepercaya tersedia.

### 29. Retry storm lintas lapisan

Jika aplikasi, service mesh, dan client masing-masing mengulang permintaan, satu kegagalan dapat dikalikan menjadi banyak percobaan. Retry bertingkat memperbesar beban layanan yang sudah lambat, menghabiskan koneksi dan antrean, memperpanjang latensi, lalu memicu timeout dan retry tambahan. Karena setiap lapisan hanya melihat sebagian konteks, kebijakan lokal yang tampak wajar dapat saling memperkuat.

Mitigasi: tentukan satu pemilik utama retry untuk operasi, batasi jumlah dan durasi total, gunakan exponential backoff dengan jitter, tetapkan deadline end-to-end, dan retry hanya operasi yang aman/idempoten atau memiliki kunci idempotensi. Pantau percobaan ulang per lapisan; circuit breaker dan load shedding dapat mencegah layanan kewalahan. Jangan mengulang tanpa batas atau sekaligus pada semua lapisan.

### 30. Model yang tepat untuk mengajarkan jaringan pemula

Untuk tujuan memahami aliran data nyata dan dasar troubleshooting, pilihan yang efektif adalah **model lima lapisan**: Physical, Data Link, Network, Transport, dan Application. Model ini memisahkan media dan framing, lalu memetakan Ethernet/Wi-Fi, IP, TCP/UDP, dan protokol aplikasi tanpa memaksakan Session dan Presentation sebagai protokol Internet tersendiri.

Manfaatnya adalah cukup konkret untuk menelusuri enkapsulasi dan perubahan header, tetapi tetap ringkas. Keterbatasannya: bukan model TCP/IP formal yang universal, dan beberapa protokol—seperti TLS, QUIC, Wi-Fi, serta ICMP—tidak selalu pas di satu kotak. Karena itu, OSI tujuh lapisan tetap berguna untuk terminologi dan fungsi konseptual, sedangkan TCP/IP empat lapisan berguna untuk menghubungkan materi dengan arsitektur Internet. Pengajaran sebaiknya menyebutkan bahwa pemetaan adalah alat analisis, bukan batas implementasi mutlak.

## Rujukan

- Forouzan, B. A. _TCP/IP Protocol Suite_. Edisi ke-4. McGraw-Hill, 2010.
- Kurose, J. F., dan Ross, K. W. _Computer Networking: A Top-Down Approach_. Gunakan edisi yang ditetapkan dalam RPS atau edisi terbaru yang tersedia secara sah.
- Tanenbaum, A. S., Feamster, N., dan Wetherall, D. J. _Computer Networks_. Edisi ke-6. Pearson, 2021.
- ISO/IEC 7498-1:1994, _Open Systems Interconnection Basic Reference Model_: <https://www.iso.org/standard/20269.html>
- RFC 1122, _Requirements for Internet Hosts: Communication Layers_: <https://www.rfc-editor.org/info/rfc1122>
- RFC 1123, _Requirements for Internet Hosts: Application and Support_: <https://www.rfc-editor.org/info/rfc1123>
- RFC 8200, _Internet Protocol, Version 6 (IPv6) Specification_: <https://www.rfc-editor.org/info/rfc8200>
- RFC 9293, _Transmission Control Protocol (TCP)_: <https://www.rfc-editor.org/info/rfc9293>
- RFC 768, _User Datagram Protocol_: <https://www.rfc-editor.org/info/rfc768>
- RFC 9000, _QUIC: A UDP-Based Multiplexed and Secure Transport_: <https://www.rfc-editor.org/info/rfc9000>
- RFC 9114, _HTTP/3_: <https://www.rfc-editor.org/info/rfc9114>
- Saltzer, J. H., Reed, D. P., dan Clark, D. D. “End-to-End Arguments in System Design.” _ACM Transactions on Computer Systems_, 1984. Verifikasi metadata bibliografis sesuai gaya sitasi yang digunakan sebelum penerbitan.

## Kegiatan Pembelajaran yang Disarankan

1. **Kartu lapisan:** kelompokkan protokol, PDU, alamat, dan perangkat; jelaskan kasus yang pemetaannya ambigu.
2. **Enkapsulasi manual:** gunakan kertas sebagai data dan header, lalu simulasikan pengirim, router, dan penerima untuk memperlihatkan perubahan Layer 2.
3. **Capture terkontrol:** rekam kueri DNS atau akses ke server laboratorium yang diizinkan; identifikasi pengenal demultiplexing dan waktu tiap tahap tanpa menangkap data sensitif.
4. **Diagnosis berbasis bukti:** telusuri gangguan seperti VLAN salah, DNS gagal, port tertutup, atau sertifikat tidak valid; bedakan gejala dari penyebab.
5. **Debat model:** bandingkan OSI, TCP/IP empat lapisan, dan model lima lapisan sebagai kerangka pengajaran, lalu susun sintesis.
