# Tugas 4 — Perhitungan Subnetting

Subnetting membagi satu jaringan IP menjadi jaringan yang lebih kecil. Pada IPv4, panjang prefix menunjukkan jumlah bit network; bit sisanya digunakan untuk alamat host. Dalam subnet biasa, alamat dengan seluruh bit host bernilai 0 adalah alamat network dan seluruh bit host bernilai 1 adalah broadcast.

Jumlah alamat per subnet dengan prefix `/p` adalah \(2^{32-p}\). Pada subnet IPv4 tradisional, host yang dapat dipakai berjumlah alamat total dikurangi dua (network dan broadcast).

## Contoh: membagi `192.168.10.0/24` menjadi empat subnet sama besar

1. Prefix `/24` menyediakan 8 bit host.
2. Empat subnet memerlukan 2 bit tambahan untuk nomor subnet karena \(2^2=4\).
3. Prefix baru `/26` memiliki \(2^{32-26}=64\) alamat, atau 62 alamat host yang dapat dipakai.

| Subnet | Network/prefix | Rentang host | Broadcast |
| --- | --- | --- | --- |
| 1 | `192.168.10.0/26` | `192.168.10.1`–`192.168.10.62` | `192.168.10.63` |
| 2 | `192.168.10.64/26` | `192.168.10.65`–`192.168.10.126` | `192.168.10.127` |
| 3 | `192.168.10.128/26` | `192.168.10.129`–`192.168.10.190` | `192.168.10.191` |
| 4 | `192.168.10.192/26` | `192.168.10.193`–`192.168.10.254` | `192.168.10.255` |

Subnet mask `/26` adalah `255.255.255.192`. Ukuran blok pada oktet terakhir ialah \(256-192=64\), sehingga network dimulai pada `.0`, `.64`, `.128`, dan `.192`.

## Langkah umum

1. Tentukan jumlah subnet atau kebutuhan host tiap jaringan.
2. Untuk kebutuhan host \(H\), pilih bit host terkecil \(h\) yang memenuhi \(2^h-2\ge H\), lalu prefix-nya `/ (32-h)`.
3. Tentukan ukuran blok, lalu rentang network, host, dan broadcast.
4. Pastikan subnet tidak tumpang tindih dan tetap berada di jaringan asal.

Perhitungan VLSM untuk jaringan `10.252.108.0/24` terdapat di [tugas6.md](tugas6.md).