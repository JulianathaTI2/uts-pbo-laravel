# UJIAN TENGAH SEMESTER (UTS) - PEMROGRAMAN BERORIENTASI OBJEK (TI033015)
### Sistem Kehilangan & Temuan Barang di Lingkungan Kampus (Laravel 13 Session CRUD)

Proyek ini dibuat untuk memenuhi tugas **Ujian Tengah Semester (UTS) Ganjil Tahun Akademik 2026/2027** pada mata kuliah **Pemrograman Berorientasi Objek (TI033015)** di **Universitas Catur Insan Cendekia (UCIC)**.

---

## Identitas Mahasiswa & Ujian
- **Nama Mahasiswa** : Julian Atha Maulana
- **NIM**            : 20251020052
- **Kelas**          : TI 2
- **Program Studi**  : S1 Teknik Informatika
- **Fakultas**       : Fakultas Teknologi Informasi
- **Perguruan Tinggi**: Universitas Catur Insan Cendekia (UCIC)
- **Mata Kuliah**    : Pemrograman Berorientasi Objek (TI033015)
- **Dosen Pengampu** : Hilman Lesmana, S.T., M.S.F.
- **Hari, Tanggal**  : Selasa, 24 November 2026

---

## Ringkasan Proyek & Ketentuan Pengerjaan
Sesuai instruksi soal UTS:
1. **Framework & Lingkungan**: Menggunakan **Laravel 13** dan **PHP 8.3** (lingkungan Laragon praktikum kelas).
2. **Penyimpanan Session**: Mengatur `SESSION_DRIVER=file` pada file `.env`. Seluruh data barang dikelola pada file session di `storage/framework/sessions/` tanpa koneksi database.
3. **Pola Arsitektur**: Mengimplementasikan pola ketat **Route &rarr; Controller &rarr; Blade**. Seluruh proses dipisahkan berdasarkan method Controller (tidak menumpuk di route closure atau Controller inline).
4. **Keamanan & Standar Form**: Menggunakan **Named Routes** secara konsisten, proteksi CSRF form dengan `@csrf`, serta HTTP method spoofing `@method('PUT')` dan `@method('DELETE')`.
5. **UI & UX**: Menggunakan Blade Template Engine dengan layout utama `app.blade.php`, alert feedback notifikasi, pencarian barang, ringkasan statistik, serta konfirmasi sebelum menghapus data.

---

## Soal No. 1 - Pemetaan 7 Route RESTful (`routes/web.php`)

Seluruh route didefinisikan secara rapi di `routes/web.php`. Route statis `/barang/create` didefinisikan **sebelum** route dinamis `/barang/{kode}` untuk mencegah konflik penangkapan parameter URL.

| No | HTTP Method | URI | Nama Route (Named Route) | Method Controller | Keterangan |
|---|---|---|---|---|---|
| 1 | `GET` | `/barang` | `barang.index` | `index()` | Menampilkan seluruh daftar barang dari session |
| 2 | `GET` | `/barang/create` | `barang.create` | `create()` | Menampilkan form penambahan barang baru |
| 3 | `POST` | `/barang` | `barang.store` | `store()` | Menerima data form & menyimpan ke session |
| 4 | `GET` | `/barang/{kode}` | `barang.show` | `show($kode)` | Menampilkan detail lengkap satu barang |
| 5 | `GET` | `/barang/{kode}/edit` | `barang.edit` | `edit($kode)` | Menampilkan form edit data barang |
| 6 | `PUT/PATCH` | `/barang/{kode}` | `barang.update` | `update($kode)` | Memperbarui data barang pada session |
| 7 | `DELETE` | `/barang/{kode}` | `barang.destroy` | `destroy($kode)` | Menghapus barang dari session |

### Bukti Eksekusi Route List (`php artisan route:list`)
```
GET|HEAD   barang ............ barang.index › BarangController@index
POST       barang ............ barang.store › BarangController@store
GET|HEAD   barang/create ..... barang.create › BarangController@create
GET|HEAD   barang/{kode} ..... barang.show › BarangController@show
PUT|PATCH  barang/{kode} ..... barang.update › BarangController@update
DELETE     barang/{kode} ..... barang.destroy › BarangController@destroy
GET|HEAD   barang/{kode}/edit  barang.edit › BarangController@edit
```

---

## Soal No. 2 - Logika Controller (`app/Http/Controllers/BarangController.php`)

Controller menangani seluruh alur aplikasi secara terpisah dan modular:
1. `index()`: Mengambil array barang dari `session('data_barang')`. Jika session masih kosong, sistem otomatis menginisialisasi 5 data awal mock (*default sample*). Mendukung fitur pencarian keyword `?q=...` dan menghitung statistik.
2. `create()`: Menyiapkan usulan kode barang otomatis (`suggestedKode`) dan daftar opsi kategori serta kondisi fisik untuk dikirim ke Blade form.
3. `store(Request $request)`: Melakukan validasi input form (wajib, tipe data, unik kode). Jika lolos validasi, membentuk array barang dan menyimpannya ke session, kemudian melakukan redirect ke `barang.index` disertai pesan flash `success`.
4. `show($kode)`: Mencari data barang pada session berdasarkan `$kode`. Jika kode tidak ditemukan, melakukan redirect ke `barang.index` dengan pesan flash `error`. Jika ditemukan, menampilkan halaman detail barang.
5. `edit($kode)`: Mencari barang dan mengembalikan form edit yang telah terisi data lama (*pre-filled value*).
6. `update(Request $request, $kode)`: Memvalidasi data masukan pembaruan, memperbarui data barang di session, dan redirect kembali ke daftar barang dengan flash message `success`.
7. `destroy($kode)`: Menghapus elemen barang dari array session dengan `unset($dataBarang[$kode])`, menyimpan perubahan ke file storage session, lalu redirect dengan konfirmasi status sukses.

---

## Soal No. 3 - Desain & Implementasi Blade Template

Semua tampilan halaman mewarisi satu layout induk yang konsisten:
1. **Layout Utama (`resources/views/layouts/app.blade.php`)**:
   - Area header navigasi dengan menu interaktif dan indikator badge UTS.
   - Subheader identitas mahasiswa (Julian Atha Maulana - 20251020052).
   - Area notifikasi global untuk menangkap session flash: `@if(session('success'))`, `@if(session('error'))`, dan `@if(session('info'))`.
   - Area konten dinamis dengan `@yield('content')`.
   - Footer resmi akademik Universitas Catur Insan Cendekia.
2. **Daftar Barang (`resources/views/barang/index.blade.php`)**:
   - Menampilkan minimal 7 kolom wajib: **Kode, Nama Barang, Kategori, Lokasi, Jumlah, Kondisi, dan Aksi**.
   - Dilengkapi kartu statistik (Total Barang, Hilang, Ditemukan, Diklaim).
   - Tombol Aksi: **Detail**, **Edit**, dan form **Hapus** dengan dialog konfirmasi JavaScript `onsubmit="return confirm(...)"`.
   - Menggunakan direktif `@extends`, `@section`, `@foreach`, `@if`, `@csrf`, dan `@method('DELETE')`.
3. **Form Tambah (`resources/views/barang/create.blade.php`)**:
   - Formulir input lengkap dengan proteksi CSRF (`@csrf`), pesan validasi error `@error`, dan tombol kembali.
4. **Form Edit (`resources/views/barang/edit.blade.php`)**:
   - Formulir ubah data dengan simulasi method PUT (`@method('PUT')`), nilai lama pre-filled melalui `old('...', $barang['...'])`, dan kode barang yang dikunci sebagai identitas unik.
5. **Detail Barang (`resources/views/barang/show.blade.php`)**:
   - Kartu profil barang menampilkan seluruh atribut lengkap, badge status, identitas pelapor, serta navigasi cepat ke Edit dan Hapus.

---

## Langkah Menjalankan Aplikasi di Komputer Lokal

1. **Clone Repositori**:
   ```bash
   git clone https://github.com/JulianathaTI2/uts-pbo-laravel.git
   cd uts-pbo-laravel
   ```

2. **Salin File Environment**:
   ```bash
   cp .env.example .env
   ```
   Pastikan pengaturan session pada file `.env`:
   ```env
   SESSION_DRIVER=file
   ```

3. **Install Dependensi Composer** (jika belum ada folder vendor):
   ```bash
   composer install
   ```

4. **Generate Application Key**:
   ```bash
   php artisan key:generate
   ```

5. **Jalankan Development Server**:
   ```bash
   php artisan serve
   ```
   Buka browser dan akses URL: **`http://127.0.0.1:8000/barang`** atau **`http://127.0.0.1:8000`**.

---

## Struktur Direktori Utama
```
pbo-laravel/
├── app/
│   ├── Http/
│   │   └── Controllers/
│   │       ├── BarangController.php   # Controller Utama CRUD Session (UTS)
│   │       └── LaporanController.php  # Controller OOP Laporan (Pertemuan 7)
│   └── Models/                        # Domain OOP Model Capstone Project
├── resources/
│   └── views/
│       ├── layouts/
│       │   └── app.blade.php          # Master Layout Blade Konsisten
│       └── barang/
│           ├── index.blade.php        # Halaman Tabel Daftar Barang (Read)
│           ├── create.blade.php       # Halaman Form Tambah Barang (Create)
│           ├── edit.blade.php         # Halaman Form Edit Barang (Update)
│           └── show.blade.php         # Halaman Detail Barang (Show)
├── routes/
│   └── web.php                        # Definisi 7 Route RESTful Wajib
└── screenshots/                       # Bukti Pengujian & Screenshot Aplikasi
```

---

&copy; 2026 **Julian Atha Maulana** (20251020052) &bull; Teknik Informatika S1 &bull; **Universitas Catur Insan Cendekia**
