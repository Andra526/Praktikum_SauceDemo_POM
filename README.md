# Otomasi Pengujian SauceDemo (Selenium + Pytest + POM)

Praktikum Pengujian Perangkat Lunak - Pertemuan 7.
Target aplikasi: https://www.saucedemo.com/

## Anggota Kelompok
| No | Nama | NIM |
|----|------|-----|
| 1  | (Andra setya ramadhani) | (24090003) |
| 2  | (Naiya Resda Novalia) | (24090073) |
| 3  | (Lazuardi Augian Pratama) | (24090029) |

## Struktur Folder
```
saucedemo-pom/
├── pages/              # Page Object Model (locator Relative XPath + aksi halaman)
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/              # Skenario uji
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_checkout.py
├── conftest.py         # Fixture driver & page object
├── pytest.ini
├── requirements.txt
└── README.md
```

## Cara Menjalankan
```bash
python -m venv venv
venv\Scripts\activate        # Windows  (Linux/Mac: source venv/bin/activate)
pip install -r requirements.txt
pytest                       # jalankan semua tes
HEADLESS=1 pytest            # tanpa membuka jendela browser
```
Prasyarat: Google Chrome terpasang (Selenium Manager mengunduh driver otomatis).
Laporan HTML tersimpan di `reports/report.html`.
