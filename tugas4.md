# Tugas 4 — Perhitungan Subnetting

Subnet baru dipilih dengan meminjam bit host secukupnya sehingga jumlah subnet yang terbentuk setidaknya sama dengan jumlah yang diminta. Jumlah host yang dapat digunakan per subnet biasa dihitung dengan \(2^{(32-\text{prefix baru})}-2\), setelah mengurangi alamat network dan broadcast.

## 1. `192.168.1.0/24` dibagi menjadi 4 subnet

Pinjam 2 bit: prefix baru `/26`, subnet mask `255.255.255.192`. Ada tepat 4 subnet, masing-masing 64 alamat dan 62 host yang dapat digunakan.

| No. | IP Network | Prefix | Host pertama | Host terakhir | Broadcast | Host tersedia |
| ---: | --- | --- | --- | --- | --- | ---: |
| 1 | `192.168.1.0` | `/26` | `192.168.1.1` | `192.168.1.62` | `192.168.1.63` | 62 |
| 2 | `192.168.1.64` | `/26` | `192.168.1.65` | `192.168.1.126` | `192.168.1.127` | 62 |
| 3 | `192.168.1.128` | `/26` | `192.168.1.129` | `192.168.1.190` | `192.168.1.191` | 62 |
| 4 | `192.168.1.192` | `/26` | `192.168.1.193` | `192.168.1.254` | `192.168.1.255` | 62 |

## 2. `132.10.0.0/16` dibagi menjadi 10 subnet

Pinjam 4 bit: prefix baru `/20`, subnet mask `255.255.240.0`. Tersedia 16 subnet sama besar; berikut 10 subnet yang diminta. Setiap subnet memiliki 4096 alamat dan 4094 host yang dapat digunakan.

| No. | IP Network | Prefix | Host pertama | Host terakhir | Broadcast | Host tersedia |
| ---: | --- | --- | --- | --- | --- | ---: |
| 1 | `132.10.0.0` | `/20` | `132.10.0.1` | `132.10.15.254` | `132.10.15.255` | 4094 |
| 2 | `132.10.16.0` | `/20` | `132.10.16.1` | `132.10.31.254` | `132.10.31.255` | 4094 |
| 3 | `132.10.32.0` | `/20` | `132.10.32.1` | `132.10.47.254` | `132.10.47.255` | 4094 |
| 4 | `132.10.48.0` | `/20` | `132.10.48.1` | `132.10.63.254` | `132.10.63.255` | 4094 |
| 5 | `132.10.64.0` | `/20` | `132.10.64.1` | `132.10.79.254` | `132.10.79.255` | 4094 |
| 6 | `132.10.80.0` | `/20` | `132.10.80.1` | `132.10.95.254` | `132.10.95.255` | 4094 |
| 7 | `132.10.96.0` | `/20` | `132.10.96.1` | `132.10.111.254` | `132.10.111.255` | 4094 |
| 8 | `132.10.112.0` | `/20` | `132.10.112.1` | `132.10.127.254` | `132.10.127.255` | 4094 |
| 9 | `132.10.128.0` | `/20` | `132.10.128.1` | `132.10.143.254` | `132.10.143.255` | 4094 |
| 10 | `132.10.144.0` | `/20` | `132.10.144.1` | `132.10.159.254` | `132.10.159.255` | 4094 |

Enam subnet `/20` sisanya tersedia dari `132.10.160.0/20` sampai `132.10.240.0/20`.

## 3. `17.8.0.0/16` dibagi menjadi 4 subnet

Pinjam 2 bit: prefix baru `/18`, subnet mask `255.255.192.0`. Ada tepat 4 subnet, masing-masing 16384 alamat dan 16382 host yang dapat digunakan.

| No. | IP Network | Prefix | Host pertama | Host terakhir | Broadcast | Host tersedia |
| ---: | --- | --- | --- | --- | --- | ---: |
| 1 | `17.8.0.0` | `/18` | `17.8.0.1` | `17.8.63.254` | `17.8.63.255` | 16382 |
| 2 | `17.8.64.0` | `/18` | `17.8.64.1` | `17.8.127.254` | `17.8.127.255` | 16382 |
| 3 | `17.8.128.0` | `/18` | `17.8.128.1` | `17.8.191.254` | `17.8.191.255` | 16382 |
| 4 | `17.8.192.0` | `/18` | `17.8.192.1` | `17.8.255.254` | `17.8.255.255` | 16382 |

## 4. `8.32.0.0/12` dibagi menjadi 6 subnet

Pinjam 3 bit: prefix baru `/15`, subnet mask `255.254.0.0`. Pembagian biner menghasilkan 8 subnet; tabel mencantumkan 6 yang diminta. Setiap subnet memiliki 131072 alamat dan 131070 host yang dapat digunakan.

| No. | IP Network | Prefix | Host pertama | Host terakhir | Broadcast | Host tersedia |
| ---: | --- | --- | --- | --- | --- | ---: |
| 1 | `8.32.0.0` | `/15` | `8.32.0.1` | `8.33.255.254` | `8.33.255.255` | 131070 |
| 2 | `8.34.0.0` | `/15` | `8.34.0.1` | `8.35.255.254` | `8.35.255.255` | 131070 |
| 3 | `8.36.0.0` | `/15` | `8.36.0.1` | `8.37.255.254` | `8.37.255.255` | 131070 |
| 4 | `8.38.0.0` | `/15` | `8.38.0.1` | `8.39.255.254` | `8.39.255.255` | 131070 |
| 5 | `8.40.0.0` | `/15` | `8.40.0.1` | `8.41.255.254` | `8.41.255.255` | 131070 |
| 6 | `8.42.0.0` | `/15` | `8.42.0.1` | `8.43.255.254` | `8.43.255.255` | 131070 |

Dua subnet lainnya adalah `8.44.0.0/15` dan `8.46.0.0/15`.
