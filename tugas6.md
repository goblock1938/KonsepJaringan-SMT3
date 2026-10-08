# Tugas 6 — VLSM `10.252.108.0/24`

VLSM (Variable Length Subnet Mask) membagi jaringan menjadi subnet dengan prefix berbeda sesuai kebutuhan host. Alokasikan kebutuhan host terbesar lebih dahulu agar ruang alamat tidak terfragmentasi.

## Perhitungan kebutuhan prefix

- **LabA, 90 host:** `/25` menyediakan \(2^7=128\) alamat, 126 host yang dapat digunakan.
- **LabB, 60 host:** `/26` menyediakan 64 alamat, 62 host yang dapat digunakan.
- **Administrasi, 14 host:** `/28` menyediakan 16 alamat, 14 host yang dapat digunakan.
- **End-point, 2 host:** `/30` menyediakan 4 alamat, 2 host yang dapat digunakan pada subnet IPv4 tradisional point-to-point.

## Hasil pembagian alamat

| Segmen | Kebutuhan host | Network/prefix | Subnet mask | Rentang host yang dapat digunakan | Broadcast |
| --- | ---: | --- | --- | --- | --- |
| LabA | 90 | `10.252.108.0/25` | `255.255.255.128` | `10.252.108.1`–`10.252.108.126` | `10.252.108.127` |
| LabB | 60 | `10.252.108.128/26` | `255.255.255.192` | `10.252.108.129`–`10.252.108.190` | `10.252.108.191` |
| Administrasi | 14 | `10.252.108.192/28` | `255.255.255.240` | `10.252.108.193`–`10.252.108.206` | `10.252.108.207` |
| End-point | 2 | `10.252.108.208/30` | `255.255.255.252` | `10.252.108.209`–`10.252.108.210` | `10.252.108.211` |

## Pemeriksaan alokasi

Blok `/25` memakai alamat `.0`–`.127`, blok `/26` berikutnya `.128`–`.191`, blok `/28` `.192`–`.207`, dan blok `/30` `.208`–`.211`. Tidak ada subnet yang tumpang tindih; semuanya berada di dalam `10.252.108.0/24`. Rentang `.212`–`.255` masih belum dialokasikan.

Gateway dapat dipilih dari alamat host yang dapat digunakan pada subnet masing-masing (misalnya alamat host pertama), selama pilihan dicatat dan tidak diberikan lagi ke perangkat lain.