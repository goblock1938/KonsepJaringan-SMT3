# Tugas 6 — Subnetting VLSM `10.252.108.0/24`

VLSM (Variable Length Subnet Mask) menggunakan prefix dengan panjang berbeda sesuai kebutuhan setiap segmen. Alamat dialokasikan dari kebutuhan host terbesar ke terkecil agar ruang jaringan dapat digunakan secara efisien.

## Penentuan prefix

- **Laboratorium A — 90 host:** `/25` menyediakan \(2^7-2=126\) alamat host yang dapat digunakan.
- **Laboratorium B — 60 host:** `/26` menyediakan \(2^6-2=62\) host.
- **Administrasi — 14 host:** `/28` menyediakan \(2^4-2=14\) host.
- **Tautan Point-to-Point — 4 endpoint:** `/29` menyediakan \(2^3-2=6\) host. `/30` hanya menyediakan dua alamat host dan tidak cukup untuk empat endpoint.

## Hasil alokasi

| Segmen | Kebutuhan | IP Network/prefix | Subnet mask | Host pertama | Host terakhir | Broadcast | Host tersedia |
| --- | ---: | --- | --- | --- | --- | --- | ---: |
| Laboratorium A | 90 | `10.252.108.0/25` | `255.255.255.128` | `10.252.108.1` | `10.252.108.126` | `10.252.108.127` | 126 |
| Laboratorium B | 60 | `10.252.108.128/26` | `255.255.255.192` | `10.252.108.129` | `10.252.108.190` | `10.252.108.191` | 62 |
| Administrasi | 14 | `10.252.108.192/28` | `255.255.255.240` | `10.252.108.193` | `10.252.108.206` | `10.252.108.207` | 14 |
| Tautan Point-to-Point | 4 endpoint | `10.252.108.208/29` | `255.255.255.248` | `10.252.108.209` | `10.252.108.214` | `10.252.108.215` | 6 |

## Sisa alamat

Semua subnet berada di dalam `10.252.108.0/24` dan tidak saling tumpang tindih. Pada subnet Point-to-Point, 2 alamat host masih tersedia setelah empat endpoint digunakan (`10.252.108.213` dan `10.252.108.214`). Di luar seluruh subnet yang dialokasikan, rentang `10.252.108.216`–`10.252.108.255` masih belum dipakai, sebanyak 40 alamat IP.
