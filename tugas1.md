# Tugas 1 — Analisis Alamat IP

Soal memberikan alamat IP tanpa subnet mask. Agar network, broadcast, dan rentang host bisa dihitung, jawaban ini **menggunakan subnet mask classful bawaan** sebagai asumsi akademik: Class A `/8`, Class B `/16`, dan Class C `/24`. Dalam jaringan modern yang menggunakan CIDR, alamat IP saja tidak cukup untuk menentukan subnet.

Gateway tidak ditentukan oleh alamat IP semata. Untuk melengkapi tabel, gateway diasumsikan memakai **alamat host pertama** pada subnet.

| No. | IP yang diberikan | Kelas / prefix asumsi | IP Gateway | Host pertama | Host terakhir | Broadcast | IP Network |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | `21.26.8.5` | A `/8` | `21.0.0.1` | `21.0.0.1` | `21.255.255.254` | `21.255.255.255` | `21.0.0.0` |
| 2 | `212.6.8.3` | C `/24` | `212.6.8.1` | `212.6.8.1` | `212.6.8.254` | `212.6.8.255` | `212.6.8.0` |
| 3 | `103.24.56.32` | A `/8` | `103.0.0.1` | `103.0.0.1` | `103.255.255.254` | `103.255.255.255` | `103.0.0.0` |
| 4 | `1.1.1.1` | A `/8` | `1.0.0.1` | `1.0.0.1` | `1.255.255.254` | `1.255.255.255` | `1.0.0.0` |
| 5 | `172.31.16.8` | B `/16` | `172.31.0.1` | `172.31.0.1` | `172.31.255.254` | `172.31.255.255` | `172.31.0.0` |

**Cara hitung:** alamat network didapat dengan operasi AND antara IP dan subnet mask. Alamat broadcast memiliki seluruh bit host bernilai 1. Host pertama adalah network + 1 dan host terakhir adalah broadcast − 1.

**Catatan:** alamat `172.31.16.8` termasuk rentang privat `172.16.0.0/12`. Penentuan alamat gateway pada praktiknya mengikuti konfigurasi jaringan, bukan kelas alamat.
