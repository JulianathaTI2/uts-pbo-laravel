import os
import subprocess
import base64

def get_base64_image(path):
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        data = f.read()
    ext = os.path.splitext(path)[1].lower().replace(".", "")
    if ext == "jpg": ext = "jpeg"
    return f"data:image/{ext};base64,{base64.b64encode(data).decode('utf-8')}"

img_dir = r"C:\laragon\www\pbo-laravel\screenshots"
logo_b64 = get_base64_image(os.path.join(img_dir, "ucic_logo.jpeg"))
r_list_b64 = get_base64_image(os.path.join(img_dir, "uts_route_list.png"))
c1_b64 = get_base64_image(os.path.join(img_dir, "uts_crud_1_index.png"))
c2_b64 = get_base64_image(os.path.join(img_dir, "uts_crud_2_create.png"))
c3_b64 = get_base64_image(os.path.join(img_dir, "uts_crud_3_store_success.png"))
c4_b64 = get_base64_image(os.path.join(img_dir, "uts_crud_4_show.png"))
c5_b64 = get_base64_image(os.path.join(img_dir, "uts_crud_5_edit.png"))
c6_b64 = get_base64_image(os.path.join(img_dir, "uts_crud_6_update_success.png"))
c7_b64 = get_base64_image(os.path.join(img_dir, "uts_crud_7_delete_success.png"))
c8_b64 = get_base64_image(os.path.join(img_dir, "uts_crud_8_not_found.png"))

html = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<style>
    @page {{
        size: A4;
        margin: 30mm 30mm 30mm 40mm; /* Top=3cm, Right=3cm, Bottom=3cm, Left=4cm */
    }}
    * {{
        box-sizing: border-box;
    }}
    body {{
        font-family: 'Times New Roman', Times, serif;
        font-size: 10.5pt;
        line-height: 1.35;
        color: #000000;
        margin: 0;
        padding: 0;
    }}
    .page {{
        page-break-after: always;
        height: 236mm; /* 297mm - 60mm margins */
        max-height: 236mm;
        overflow: hidden;
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }}
    .page:last-child {{
        page-break-after: avoid;
    }}

    /* Page Number */
    .page-number {{
        text-align: right;
        font-size: 11pt;
        font-family: 'Times New Roman', Times, serif;
        color: #000;
        padding-top: 5px;
    }}

    /* Typography */
    .bab-title {{
        text-align: center;
        font-size: 13pt;
        font-weight: bold;
        text-transform: uppercase;
        margin-bottom: 12px;
        line-height: 1.3;
    }}
    .sub-bab {{
        font-size: 11pt;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 4px;
        color: #000;
    }}
    .sub-sub-bab {{
        font-size: 11pt;
        font-weight: bold;
        margin-top: 8px;
        margin-bottom: 4px;
        color: #000;
    }}
    p {{
        text-align: justify;
        text-indent: 1.25cm;
        margin: 0 0 6px 0;
    }}
    .p-noindent {{
        text-align: justify;
        text-indent: 0;
        margin: 0 0 6px 0;
    }}

    /* Numbering Lists (NO BULLETS) */
    ol.num-list {{
        margin: 0 0 6px 0;
        padding-left: 1.25cm;
    }}
    ol.num-list li {{
        text-align: justify;
        margin-bottom: 3px;
        padding-left: 4px;
    }}
    ol.alpha-list {{
        margin: 0 0 6px 0;
        padding-left: 1.25cm;
        list-style-type: lower-alpha;
    }}
    ol.alpha-list li {{
        text-align: justify;
        margin-bottom: 3px;
        padding-left: 4px;
    }}

    /* Tables */
    .table-caption {{
        font-size: 10pt;
        font-weight: normal;
        margin-bottom: 3px;
        text-align: left;
    }}
    .table-caption strong {{
        font-weight: bold;
    }}
    table.custom-table {{
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 8px;
        font-size: 9pt;
    }}
    table.custom-table th, table.custom-table td {{
        border: 1px solid #000;
        padding: 4px 6px;
        line-height: 1.25;
    }}
    table.custom-table th {{
        background-color: #d1d5db; /* 25% grey */
        font-weight: bold;
        text-align: center;
    }}

    /* Images */
    .img-container {{
        text-align: center;
        margin: 6px 0;
    }}
    .report-img {{
        max-width: 100%;
        border: 1px solid #333;
        display: block;
        margin: 0 auto;
    }}
    .img-caption {{
        font-size: 9.5pt;
        text-align: center;
        margin-top: 3px;
        line-height: 1.2;
    }}
    .img-caption strong {{
        font-weight: bold;
    }}

    /* Code Box */
    .code-snippet {{
        font-family: 'Courier New', Courier, monospace;
        font-size: 8.5pt;
        background-color: #f8fafc;
        border: 1px solid #94a3b8;
        padding: 6px 10px;
        margin: 5px 0 8px 0;
        line-height: 1.25;
        white-space: pre-wrap;
    }}

    /* Cover Styling */
    .cover-container {{
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        text-align: center;
    }}
    .cover-top h1 {{
        font-size: 13.5pt;
        font-weight: bold;
        margin: 0 0 4px 0;
        line-height: 1.3;
    }}
    .cover-top h2 {{
        font-size: 13.5pt;
        font-weight: bold;
        margin: 0 0 10px 0;
    }}
    .cover-top h3 {{
        font-size: 11pt;
        font-weight: bold;
        margin: 0 0 14px 0;
        line-height: 1.35;
        padding: 0 10px;
    }}
    .cover-dosen {{
        font-size: 11pt;
        font-weight: bold;
        margin-bottom: 20px;
    }}
    .cover-logo {{
        margin: 15px auto;
    }}
    .cover-mid p {{
        text-align: center;
        text-indent: 0;
        font-size: 11pt;
        margin: 0;
    }}
    .cover-mid h4 {{
        font-size: 12pt;
        font-weight: bold;
        margin: 4px 0 0 0;
    }}
    .cover-bottom h3 {{
        font-size: 13pt;
        font-weight: bold;
        margin: 2px 0;
        line-height: 1.25;
    }}

    /* TOC Table */
    .toc-table {{
        width: 100%;
        border-collapse: collapse;
        font-size: 10pt;
        line-height: 1.4;
    }}
    .toc-table td {{
        padding: 2px 0;
        vertical-align: bottom;
    }}
    .toc-page {{
        text-align: right;
        width: 30px;
        white-space: nowrap;
    }}
    .toc-leader {{
        border-bottom: 1px dotted #000;
        margin: 0 4px;
        flex-grow: 1;
    }}
</style>
</head>
<body>

<!-- ========================================================
     HALAMAN COVER (Sesuai Contoh Format Lembar Jawaban UTS)
     ======================================================== -->
<div class="page">
    <div class="cover-container">
        <div class="cover-top">
            <h1>LEMBAR JAWABAN UJIAN TENGAH SEMESTER (UTS)</h1>
            <h2>GANJIL TAHUN AKADEMIK 2026/2027</h2>
            <h3>
                PEMROGRAMAN BERORIENTASI OBJEK (TI033015): SISTEM INFORMASI KEHILANGAN DAN TEMUAN BARANG DI LINGKUNGAN KAMPUS (STUDI KASUS CAPSTONE PROJECT BERBASIS LARAVEL 13 MVC &amp; SESSION FILE DRIVER)
            </h3>
            <div class="cover-dosen">
                Dosen Pengampu: Hilman Lesmana, S.T., M.S.F.
            </div>
        </div>

        <div class="cover-logo">
            <img src="{logo_b64}" style="height: 135px;" alt="Logo Universitas Catur Insan Cendekia">
        </div>

        <div class="cover-mid">
            <p>Disusun oleh:</p>
            <h4>Julian Atha Maulana (20251020052)</h4>
            <p style="margin-top: 2px; font-size: 10.5pt;">Kelas: TI 2</p>
        </div>

        <div class="cover-bottom">
            <h3>PROGRAM STUDI TEKNIK INFORMATIKA</h3>
            <h3>FAKULTAS TEKNOLOGI INFORMASI</h3>
            <h3>UNIVERSITAS CATUR INSAN CENDEKIA 2026</h3>
        </div>
    </div>
</div>

<!-- ========================================================
     HALAMAN DAFTAR ISI (Format Bertitik / Dots Leader)
     ======================================================== -->
<div class="page">
    <div class="content-area">
        <div class="bab-title" style="margin-bottom: 18px;">DAFTAR ISI</div>
        
        <table class="toc-table">
            <tr>
                <td style="font-weight: bold;">DAFTAR ISI</td>
                <td class="toc-page" style="font-weight: bold;">i</td>
            </tr>
            <tr>
                <td style="font-weight: bold;">BAB I PENDAHULUAN</td>
                <td class="toc-page" style="font-weight: bold;">1</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">1.1 Latar Belakang Masalah</td>
                <td class="toc-page">1</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">1.2 Ruang Lingkup Masalah</td>
                <td class="toc-page">1</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">1.3 Tujuan dan Manfaat</td>
                <td class="toc-page">2</td>
            </tr>
            <tr>
                <td style="font-weight: bold;">BAB II PERANCANGAN ROUTING DAN ARSITEKTUR (SOAL 1)</td>
                <td class="toc-page" style="font-weight: bold;">3</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">2.1 Alur Arsitektur Route &rarr; Controller &rarr; Blade</td>
                <td class="toc-page">3</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">2.2 Tabel Pemetaan 7 Route RESTful Wajib Data Barang</td>
                <td class="toc-page">3</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">2.3 Urutan Definisi Route Statis dan Dinamis</td>
                <td class="toc-page">4</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">2.4 Bukti Eksekusi Terminal Route List</td>
                <td class="toc-page">4</td>
            </tr>
            <tr>
                <td style="font-weight: bold;">BAB III PENGELOLAAN CONTROLLER DAN SESSION (SOAL 2)</td>
                <td class="toc-page" style="font-weight: bold;">5</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">3.1 Struktur BarangController</td>
                <td class="toc-page">5</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">3.2 Pengelolaan Session File Driver (SESSION_DRIVER=file)</td>
                <td class="toc-page">5</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">3.3 Penjelasan Rinci Setiap Method CRUD</td>
                <td class="toc-page">6</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">3.4 Validasi Form, Flash Messages, dan Penanganan Error 404</td>
                <td class="toc-page">6</td>
            </tr>
            <tr>
                <td style="font-weight: bold;">BAB IV IMPLEMENTASI BLADE TEMPLATE ENGINE (SOAL 3)</td>
                <td class="toc-page" style="font-weight: bold;">7</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">4.1 Master Layout Konsisten (layouts/app.blade.php)</td>
                <td class="toc-page">7</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">4.2 Halaman Tabel dengan 7 Kolom Wajib (barang/index.blade.php)</td>
                <td class="toc-page">7</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">4.3 Formulir Tambah dan Edit dengan Pre-filled Values</td>
                <td class="toc-page">8</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">4.4 Halaman Detail Barang (barang/show.blade.php)</td>
                <td class="toc-page">8</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">4.5 Penggunaan Direktif Blade dan Keamanan Form</td>
                <td class="toc-page">9</td>
            </tr>
            <tr>
                <td style="font-weight: bold;">BAB V HASIL PENGUJIAN SISTEM (SCREENSHOT CRUD)</td>
                <td class="toc-page" style="font-weight: bold;">10</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">5.1 Pengujian Halaman Daftar Barang (Read)</td>
                <td class="toc-page">10</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">5.2 Pengujian Formulir Tambah Barang (Create)</td>
                <td class="toc-page">10</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">5.3 Pengujian Notifikasi Sukses Tambah Data (Store)</td>
                <td class="toc-page">11</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">5.4 Pengujian Halaman Detail Barang (Show)</td>
                <td class="toc-page">11</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">5.5 Pengujian Formulir Ubah Barang (Edit)</td>
                <td class="toc-page">12</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">5.6 Pengujian Notifikasi Sukses Ubah Data (Update)</td>
                <td class="toc-page">12</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">5.7 Pengujian Penghapusan Data dan Konfirmasi (Destroy)</td>
                <td class="toc-page">13</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">5.8 Pengujian Penanganan Kode Barang Tidak Ditemukan</td>
                <td class="toc-page">13</td>
            </tr>
            <tr>
                <td style="font-weight: bold;">BAB VI KESIMPULAN DAN SARAN</td>
                <td class="toc-page" style="font-weight: bold;">14</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">6.1 Kesimpulan</td>
                <td class="toc-page">14</td>
            </tr>
            <tr>
                <td style="padding-left: 15px;">6.2 Saran</td>
                <td class="toc-page">14</td>
            </tr>
            <tr>
                <td style="font-weight: bold;">DAFTAR PUSTAKA</td>
                <td class="toc-page" style="font-weight: bold;">15</td>
            </tr>
            <tr>
                <td style="font-weight: bold;">LAMPIRAN</td>
                <td class="toc-page" style="font-weight: bold;">16</td>
            </tr>
        </table>
    </div>
    <div class="page-number">i</div>
</div>

<!-- ========================================================
     BAB I PENDAHULUAN (HALAMAN 1)
     ======================================================== -->
<div class="page">
    <div class="content-area">
        <div class="bab-title">BAB I<br>PENDAHULUAN</div>

        <div class="sub-bab">1.1 Latar Belakang Masalah</div>
        <p>
            Aktivitas akademik dan kemahasiswaan di lingkungan Universitas Catur Insan Cendekia (UCIC) melibatkan mobilitas fisik mahasiswa, dosen, serta staf yang sangat dinamis setiap harinya. Fasilitas perkuliahan bersama seperti ruang kelas teori, laboratorium komputer, perpustakaan kampus, mushola, lobi, dan area kantin kerap menjadi titik konsentrasi di mana barang-barang pribadi tertinggal atau hilang tanpa sengaja. Fenomena kehilangan barang berharga seperti dompet, kartu tanda mahasiswa (KTM), kunci kontak kendaraan, botol minum, hingga perangkat elektronik merupakan kendala nyata yang kerap dihadapi sivitas akademika kampus.
        </p>
        <p>
            Pengelolaan informasi laporan barang hilang dan temuan barang pada saat ini masih mengandalkan pencatatan konvensional atau penyebaran pesan singkat media sosial yang sifatnya tidak terpusat dan mudah tertimbun. Ketiadaan sistem informasi terstruktur menimbulkan kesulitan bagi petugas keamanan maupun mahasiswa saat hendak melakukan verifikasi kepemilikan maupun pelacakan status penemuan barang. Dampak yang ditimbulkan adalah rendahnya tingkat pengembalian barang temuan kepada pemilik sahnya serta tidak tersedianya rekam jejak pelaporan yang tertib.
        </p>
        <p>
            Solusi yang dihadirkan melalui proyek Ujian Tengah Semester (UTS) mata kuliah Pemrograman Berorientasi Objek (TI033015) ini adalah membangun modul aplikasi berbasis web bertajuk <strong>Sistem Informasi Kehilangan dan Temuan Barang di Lingkungan Kampus</strong>. Aplikasi dikembangkan memanfaatkan framework modern <em>Laravel 13</em> dengan bahasa pemrograman <em>PHP 8.3</em>. Sesuai ketentuan praktikum kelas, pengelolaan data dirancang secara in-memory menggunakan driver penyimpanan sesi file lokal (<em>SESSION_DRIVER=file</em>) tanpa ketergantungan database eksternal, dengan fokus utama pada pemisahan arsitektur yang bersih melalui pola <em>Route &rarr; Controller &rarr; Blade</em>.
        </p>

        <div class="sub-bab">1.2 Ruang Lingkup Masalah</div>
        <p>
            Pembatasan ruang lingkup masalah bertujuan agar analisis dan implementasi teknis tetap terarah pada capaian pembelajaran UTS. Ruang lingkup pengerjaan sistem ini mencakup:
        </p>
        <ol class="num-list">
            <li>Pengembangan difokuskan pada pengelolaan entitas utama berupa <strong>Data Barang</strong> (baik barang hilang maupun barang yang ditemukan di kampus).</li>
            <li>Penyimpanan data memanfaatkan media sesi berkas Laravel (<em>file session storage</em>) pada direktori <code>storage/framework/sessions/</code>.</li>
            <li>Implementasi siklus penuh <em>CRUD (Create, Read, Update, Delete)</em> menggunakan 7 route RESTful standar industri.</li>
            <li>Penyediaan antarmuka terintegrasi berbasis Blade Template Engine dengan validasi form, notifikasi umpan balik (<em>flash message</em>), serta proteksi keamanan <code>@csrf</code> dan <code>@method</code>.</li>
        </ol>
    </div>
    <div class="page-number">1</div>
</div>

<!-- ========================================================
     BAB I PENDAHULUAN (HALAMAN 2)
     ======================================================== -->
<div class="page">
    <div class="content-area">
        <div class="sub-bab">1.3 Tujuan dan Manfaat</div>
        <p>
            Penyusunan proyek perangkat lunak dan laporan ujian ini memiliki serangkaian tujuan akademis dan praktis yang terukur sebagai berikut:
        </p>
        
        <div class="sub-sub-bab">1.3.1 Tujuan</div>
        <p class="p-noindent">Tujuan yang ingin dicapai melalui pengerjaan proyek UTS ini adalah:</p>
        <ol class="num-list">
            <li>Menerapkan prinsip arsitektur web MVC (<em>Model-View-Controller</em>) secara murni dan terstruktur menggunakan framework Laravel 13.</li>
            <li>Merancang 7 route RESTful yang memetakan seluruh operasi HTTP (GET, POST, PUT/PATCH, DELETE) ke Controller yang bersesuaian dengan <em>named routes</em> konsisten.</li>
            <li>Mengimplementasikan <code>BarangController</code> yang memisahkan seluruh logika bisnis CRUD secara modular dan memanfaatkan driver session file untuk persistensi data sementara.</li>
            <li>Membangun antarmuka pengguna yang konsisten dan responsif menggunakan Blade Template Engine dengan layout induk tunggal serta direktif standar seperti <code>@extends</code>, <code>@section</code>, <code>@yield</code>, <code>@foreach</code>, <code>@if</code>, <code>@csrf</code>, dan <code>@method</code>.</li>
            <li>Mendokumentasikan seluruh pengujian operasional aplikasi dan mempublikasikan kode sumber proyek ke dalam repositori GitHub mandiri.</li>
        </ol>

        <div class="sub-sub-bab">1.3.2 Manfaat</div>
        <p class="p-noindent">Manfaat yang diperoleh dari penyelesaian sistem ini terbagi menjadi dua aspek:</p>
        <ol class="alpha-list">
            <li><strong>Manfaat Teoritis dan Akademik</strong>: Memperdalam pemahaman praktis mahasiswa mengenai alur penanganan HTTP request dalam framework modern, pemisahan tugas Controller, mekanisme session storage, serta pembuatan antarmuka dinamis berbasis komponen Blade.</li>
            <li><strong>Manfaat Praktis</strong>: Menyediakan fondasi sistem informasi pencatatan kehilangan dan penemuan barang yang siap dikembangkan lebih lanjut menjadi aplikasi terintegrasi dengan database MySQL pada tugas akhir Capstone Project.</li>
        </ol>
    </div>
    <div class="page-number">2</div>
</div>

<!-- ========================================================
     BAB II PERANCANGAN ROUTING DAN ARSITEKTUR (SOAL 1) (HALAMAN 3)
     ======================================================== -->
<div class="page">
    <div class="content-area">
        <div class="bab-title">BAB II<br>PERANCANGAN ROUTING DAN ARSITEKTUR (SOAL 1)</div>

        <div class="sub-bab">2.1 Alur Arsitektur Route &rarr; Controller &rarr; Blade</div>
        <p>
            Prinsip arsitektur yang diwajibkan pada soal ujian adalah pemisahan peran yang tegas antara rute URL, pengendali logika, dan tampilan antarmuka. Alur pemrosesan request berjalan secara linier:
        </p>
        <ol class="num-list">
            <li><strong>Route Layer (<code>routes/web.php</code>)</strong>: Menerima HTTP Request dari peramban web pengguna dan mencocokkan pola URI beserta method HTTP-nya ke method spesifik di Controller. Dilarang keras menaruh logika olah data di dalam closure route.</li>
            <li><strong>Controller Layer (<code>app/Http/Controllers/BarangController.php</code>)</strong>: Bertindak sebagai pengatur alur kerja. Controller membaca atau menulis data pada array session, melakukan validasi, dan menyiapkan variabel data. Controller dilarang mencetak tag HTML secara langsung.</li>
            <li><strong>View Layer (<code>resources/views/barang/</code>)</strong>: Menerima variabel data dari Controller untuk dirender ke dalam struktur HTML yang bersih menggunakan template engine Blade.</li>
        </ol>

        <div class="sub-bab">2.2 Tabel Pemetaan 7 Route RESTful Wajib Data Barang</div>
        <p class="p-noindent">
            Sesuai instruksi Soal No. 1, seluruh 7 route RESTful yang dibutuhkan untuk mengelola data barang telah didaftarkan pada <code>routes/web.php</code>:
        </p>

        <div class="table-caption"><strong>Tabel 2.1</strong> Pemetaan 7 Route RESTful Pengelolaan Data Barang</div>
        <table class="custom-table">
            <thead>
                <tr>
                    <th style="width: 6%;">No</th>
                    <th style="width: 14%;">HTTP Method</th>
                    <th style="width: 25%;">URI Pattern</th>
                    <th style="width: 22%;">Nama Route</th>
                    <th style="width: 15%;">Method</th>
                    <th style="width: 18%;">Tugas Operasional</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="text-align: center;">1</td>
                    <td style="text-align: center; font-weight: bold;">GET</td>
                    <td>/barang</td>
                    <td>barang.index</td>
                    <td>index()</td>
                    <td>Daftar seluruh barang (Read)</td>
                </tr>
                <tr>
                    <td style="text-align: center;">2</td>
                    <td style="text-align: center; font-weight: bold;">GET</td>
                    <td>/barang/create</td>
                    <td>barang.create</td>
                    <td>create()</td>
                    <td>Formulir tambah barang</td>
                </tr>
                <tr>
                    <td style="text-align: center;">3</td>
                    <td style="text-align: center; font-weight: bold;">POST</td>
                    <td>/barang</td>
                    <td>barang.store</td>
                    <td>store()</td>
                    <td>Simpan barang baru ke session</td>
                </tr>
                <tr>
                    <td style="text-align: center;">4</td>
                    <td style="text-align: center; font-weight: bold;">GET</td>
                    <td>/barang/{{kode}}</td>
                    <td>barang.show</td>
                    <td>show($k)</td>
                    <td>Detail satu barang lengkap</td>
                </tr>
                <tr>
                    <td style="text-align: center;">5</td>
                    <td style="text-align: center; font-weight: bold;">GET</td>
                    <td>/barang/{{kode}}/edit</td>
                    <td>barang.edit</td>
                    <td>edit($k)</td>
                    <td>Formulir ubah data barang</td>
                </tr>
                <tr>
                    <td style="text-align: center;">6</td>
                    <td style="text-align: center; font-weight: bold;">PUT/PATCH</td>
                    <td>/barang/{{kode}}</td>
                    <td>barang.update</td>
                    <td>update($k)</td>
                    <td>Perbarui data pada session</td>
                </tr>
                <tr>
                    <td style="text-align: center;">7</td>
                    <td style="text-align: center; font-weight: bold;">DELETE</td>
                    <td>/barang/{{kode}}</td>
                    <td>barang.destroy</td>
                    <td>destroy($k)</td>
                    <td>Hapus barang dari session</td>
                </tr>
            </tbody>
        </table>
    </div>
    <div class="page-number">3</div>
</div>

<!-- ========================================================
     BAB II PERANCANGAN ROUTING DAN ARSITEKTUR (SOAL 1) (HALAMAN 4)
     ======================================================== -->
<div class="page">
    <div class="content-area">
        <div class="sub-bab">2.3 Urutan Definisi Route Statis dan Dinamis</div>
        <p>
            Aturan utama dalam perancangan routing Laravel adalah mendefinisikan route statis sebelum route dinamis berparameter. Pada berkas <code>routes/web.php</code>, route statis <code>/barang/create</code> wajib diletakkan sebelum route dinamis <code>/barang/{{kode}}</code>:
        </p>
        <div class="code-snippet">// 1. Route statis diletakkan terlebih dahulu
Route::get('/barang/create', [BarangController::class, 'create'])->name('barang.create');

// 2. Route dinamis berparameter {{kode}} diletakkan setelah route statis
Route::get('/barang/{{kode}}', [BarangController::class, 'show'])->name('barang.show');</div>
        <p>
            Mekanisme ini sangat penting karena parser routing Laravel melakukan pencocokan URL secara sekuensial dari atas ke bawah. Apabila <code>/barang/{{kode}}</code> dideklarasikan lebih awal, peramban yang mengakses alamat <code>/barang/create</code> akan ditafsirkan sebagai pemanggilan route dinamis dengan nilai argumen <code>$kode = 'create'</code>, sehingga sistem akan mencari barang dengan kode 'create' dan menimbulkan galat <em>not found</em>.
        </p>

        <div class="sub-bab">2.4 Bukti Eksekusi Terminal Route List</div>
        <p class="p-noindent">
            Validasi seluruh route yang telah didaftarkan dibuktikan melalui eksekusi perintah terminal <code>php artisan route:list --path=barang</code> pada konsol pengembang:
        </p>
        <div class="img-container">
            <img src="{r_list_b64}" class="report-img" style="max-height: 125px;" alt="Terminal Route List">
            <div class="img-caption"><strong>Gambar 2.1</strong> Output Perintah Terminal <code>php artisan route:list --path=barang</code></div>
        </div>
        <p>
            Berdasarkan Gambar 2.1 di atas, tampak jelas bahwa ketujuh rute RESTful beserta method HTTP, URI pattern, nama route unik (<em>named route</em>), dan pemetaan ke <code>BarangController</code> telah terkonfigurasi secara tepat dan tanpa konflik.
        </p>
    </div>
    <div class="page-number">4</div>
</div>

<!-- ========================================================
     BAB III PENGELOLAAN CONTROLLER DAN SESSION (SOAL 2) (HALAMAN 5)
     ======================================================== -->
<div class="page">
    <div class="content-area">
        <div class="bab-title">BAB III<br>PENGELOLAAN CONTROLLER DAN SESSION (SOAL 2)</div>

        <div class="sub-bab">3.1 Struktur BarangController</div>
        <p>
            File <code>app/Http/Controllers/BarangController.php</code> bertindak sebagai otak aplikasi yang mengontrol seluruh operasi data barang. Controller ini menerapkan prinsip modularitas dengan memisahkan tiap method sesuai tugas CRUD masing-masing:
        </p>
        <ol class="num-list">
            <li><code>getBarangFromSession()</code>: Method privat pembantu untuk membaca array <code>data_barang</code> dari session dan melakukan inisialisasi 5 data tiruan awal jika sesi kosong.</li>
            <li><code>saveBarangToSession(array $data)</code>: Method privat untuk menyimpan kembali array barang yang telah dimanipulasi ke penyimpanan file session serta memanggil <code>session()->save()</code>.</li>
            <li>Tujuh method aksi publik: <code>index()</code>, <code>create()</code>, <code>store()</code>, <code>show()</code>, <code>edit()</code>, <code>update()</code>, dan <code>destroy()</code>.</li>
        </ol>

        <div class="sub-bab">3.2 Pengelolaan Session File Driver (SESSION_DRIVER=file)</div>
        <p>
            Sesuai petunjuk pengerjaan UTS, konfigurasi pada berkas <code>.env</code> diatur secara tegas menggunakan driver session berkas:
        </p>
        <div class="code-snippet">SESSION_DRIVER=file
SESSION_LIFETIME=120
SESSION_ENCRYPT=false</div>
        <p>
            Dengan pengaturan ini, Laravel mengabaikan driver database dan menyimpan seluruh data sesi aplikasi ke dalam berkas-berkas terenkripsi pada folder <code>storage/framework/sessions/</code>. Mekanisme ini memastikan bahwa data barang yang ditambahkan, diubah, maupun dihapus selama pengujian CRUD tetap tersimpan secara persisten selama siklus sesi peramban berlangsung tanpa memerlukan tabel database SQL.
        </p>
        <p>
            Struktur data barang yang disimpan dalam array asosiatif session memuat atribut lengkap: <code>kode</code> (string unik), <code>nama</code> (nama barang), <code>kategori</code> (kelompok barang), <code>lokasi</code> (posisi ditemukan/hilang), <code>jumlah</code> (kuantitas unit), <code>kondisi</code> (keadaan fisik), <code>status</code> (Hilang / Ditemukan / Diklaim), <code>tgl_lapor</code> (tanggal lapor), <code>pelapor</code> (identitas pelapor), dan <code>deskripsi</code> (ciri fisik khusus).
        </p>
    </div>
    <div class="page-number">5</div>
</div>

<!-- ========================================================
     BAB III PENGELOLAAN CONTROLLER DAN SESSION (SOAL 2) (HALAMAN 6)
     ======================================================== -->
<div class="page">
    <div class="content-area">
        <div class="sub-bab">3.3 Penjelasan Rinci Setiap Method CRUD</div>
        <p class="p-noindent">
            Logika yang dijalankan pada masing-masing method Controller dirangkum pada tabel berikut:
        </p>

        <div class="table-caption"><strong>Tabel 3.1</strong> Rincian Tugas Method pada BarangController</div>
        <table class="custom-table">
            <thead>
                <tr>
                    <th style="width: 20%;">Nama Method</th>
                    <th style="width: 48%;">Alur Proses dan Logika Session</th>
                    <th style="width: 32%;">Umpan Balik / Redirect</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><code>index(Request $r)</code></td>
                    <td>Mengambil data session, memfilter berdasarkan query pencarian <code>?q=...</code> jika tersedia, dan menghitung total statistik barang.</td>
                    <td>Merender view <code>barang.index</code> dengan variabel data barang dan ringkasan.</td>
                </tr>
                <tr>
                    <td><code>create()</code></td>
                    <td>Menghasilkan usulan kode otomatis (misal: <code>BRG-006</code>) serta opsi kategori dan kondisi fisik.</td>
                    <td>Merender view formulir <code>barang.create</code>.</td>
                </tr>
                <tr>
                    <td><code>store(Request $r)</code></td>
                    <td>Menerima data POST, mengecek keunikan kode barang pada session, membentuk array barang baru, dan menyimpan ke session.</td>
                    <td>Redirect ke <code>barang.index</code> disertai pesan flash <code>success</code>.</td>
                </tr>
                <tr>
                    <td><code>show($kode)</code></td>
                    <td>Mencari data barang di session berdasarkan parameter kode URL huruf kapital.</td>
                    <td>Jika ditemukan buka <code>barang.show</code>; jika nihil redirect dengan flash <code>error</code>.</td>
                </tr>
                <tr>
                    <td><code>edit($kode)</code></td>
                    <td>Mengambil data barang yang tersimpan untuk disiapkan sebagai nilai awal (*pre-filled*).</td>
                    <td>Merender view formulir ubah <code>barang.edit</code>.</td>
                </tr>
                <tr>
                    <td><code>update(Request $r, $k)</code></td>
                    <td>Memvalidasi masukan pembaharuan, memperbarui atribut barang pada session, dan menyimpan file sesi.</td>
                    <td>Redirect ke <code>barang.index</code> disertai notifikasi flash <code>success</code>.</td>
                </tr>
                <tr>
                    <td><code>destroy($kode)</code></td>
                    <td>Menghapus entri barang dari array session dengan fungsi <code>unset()</code> dan menyimpan sesi.</td>
                    <td>Redirect ke <code>barang.index</code> disertai notifikasi flash <code>success</code>.</td>
                </tr>
            </tbody>
        </table>

        <div class="sub-bab">3.4 Validasi Form, Flash Messages, dan Penanganan Error 404</div>
        <p>
            Seluruh data masukan dari form divalidasi secara ketat melalui method <code>$request->validate()</code> untuk mencegah masukan kosong atau inkonsisten. Setelah operasi manipulasi berhasil, Controller mengirimkan pesan umpan balik melalui flash session <code>with('success', ...)</code>. Apabila pengguna mengakses kode barang yang tidak terdaftar, Controller secara proaktif menangkap kondisi tersebut dan mengalihkan pengguna kembali ke halaman utama melalui <code>with('error', ...)</code> tanpa menimbulkan crash pada aplikasi.
        </p>
    </div>
    <div class="page-number">6</div>
</div>

<!-- ========================================================
     BAB IV IMPLEMENTASI BLADE TEMPLATE ENGINE (SOAL 3) (HALAMAN 7)
     ======================================================== -->
<div class="page">
    <div class="content-area">
        <div class="bab-title">BAB IV<br>IMPLEMENTASI BLADE TEMPLATE ENGINE (SOAL 3)</div>

        <div class="sub-bab">4.1 Master Layout Konsisten (layouts/app.blade.php)</div>
        <p>
            Seluruh antarmuka aplikasi dibangun menginduk pada satu master layout tunggal yaitu <code>resources/views/layouts/app.blade.php</code>. Layout ini dirancang menggunakan Tailwind CSS untuk menyajikan tampilan yang modern, rapi, dan responsif. Elemen-elemen yang terdapat pada master layout meliputi:
        </p>
        <ol class="num-list">
            <li><strong>Header dan Navigasi Atas</strong>: Memuat identitas brand sistem, tautan menu navigasi Data Barang (CRUD), Tambah Barang, serta indikator badge resmi UTS PBO 2026/2027.</li>
            <li><strong>Subheader Identitas Akademik</strong>: Menampilkan data mahasiswa: Nama (Julian Atha Maulana), NIM (20251020052), Kelas (TI 2), Dosen Pengampu (Hilman Lesmana, S.T., M.S.F.), dan indikator <code>SESSION_DRIVER=file</code>.</li>
            <li><strong>Container Notifikasi Flash</strong>: Menangkap pesan sesi secara dinamis melalui <code>@if(session('success'))</code>, <code>@if(session('error'))</code>, dan <code>@if(session('info'))</code> dengan palet warna kontekstual (hijau, merah, biru).</li>
            <li><strong>Main Content Container</strong>: Menggunakan direktif <code>@yield('content')</code> untuk menampung konten dinamis dari masing-masing halaman turunan.</li>
            <li><strong>Footer Halaman</strong>: Memuat informasi hak cipta akademik Universitas Catur Insan Cendekia.</li>
        </ol>

        <div class="sub-bab">4.2 Halaman Tabel dengan 7 Kolom Wajib (barang/index.blade.php)</div>
        <p>
            Sesuai kriteria Soal No. 3, halaman daftar barang menampilkan tabel data dari session dengan <strong>7 Kolom Wajib</strong>:
        </p>
        <ol class="alpha-list">
            <li><strong>Kode</strong>: Menampilkan kode unik barang dengan styling badge font proporsional (contoh: <code>BRG-001</code>).</li>
            <li><strong>Nama Barang</strong>: Menampilkan nama barang disertai badge indikator status pelaporan (Hilang, Ditemukan, Diklaim).</li>
            <li><strong>Kategori</strong>: Menampilkan klasifikasi barang (Aksesoris, Kunci, Pakaian, Elektronik).</li>
            <li><strong>Lokasi</strong>: Menampilkan posisi fisik terakhir atau tempat penemuan barang di kampus.</li>
            <li><strong>Jumlah</strong>: Menampilkan kuantitas barang dalam satuan unit.</li>
            <li><strong>Kondisi</strong>: Menampilkan kondisi fisik barang (Baik, Sangat Baik, Lecet Pemakaian).</li>
            <li><strong>Aksi</strong>: Menyediakan tiga tombol aksi operasional: tombol <strong>Detail</strong>, tombol <strong>Edit</strong>, dan form <strong>Hapus</strong> yang dilengkapi dialog konfirmasi JavaScript.</li>
        </ol>
    </div>
    <div class="page-number">7</div>
</div>

<!-- ========================================================
     BAB IV IMPLEMENTASI BLADE TEMPLATE ENGINE (SOAL 3) (HALAMAN 8)
     ======================================================== -->
<div class="page">
    <div class="content-area">
        <div class="sub-bab">4.3 Formulir Tambah dan Edit dengan Pre-filled Values</div>
        <p>
            Pembuatan data baru ditangani oleh file <code>resources/views/barang/create.blade.php</code>. Formulir ini dilengkapi dengan usulan kode barang otomatis dari Controller (misal: <code>BRG-006</code>), seleksi opsi dropdown kategori dan kondisi fisik, pemilih tanggal lapor, isian identitas pelapor, serta textarea deskripsi ciri khusus barang.
        </p>
        <p>
            Proses penyuntingan ditangani oleh berkas <code>resources/views/barang/edit.blade.php</code>. Sesuai ketentuan soal, formulir edit wajib menampilkan nilai lama barang sebagai nilai awal (<em>pre-filled values</em>). Hal ini diimplementasikan menggunakan helper Laravel <code>old('field', $barang['field'])</code>:
        </p>
        <div class="code-snippet">&lt;!-- Contoh Pre-filled input pada edit.blade.php --&gt;
&lt;input type="text" name="nama" id="nama" 
       value="{{{{ old('nama', $barang['nama']) }}}}" 
       class="w-full border rounded-lg p-2" required&gt;</div>
        <p>
            Khusus pada atribut kode barang, kolom isian diatur dengan atribut <code>readonly</code> karena kode barang berfungsi sebagai kunci unik (<em>primary identifier</em>) dalam array session yang tidak boleh diubah saat mode penyuntingan berlangsung.
        </p>

        <div class="sub-bab">4.4 Halaman Detail Barang (barang/show.blade.php)</div>
        <p>
            Halaman detail pada berkas <code>resources/views/barang/show.blade.php</code> menyajikan profil barang terpilih secara komprehensif dalam bentuk kartu informasi terstruktur. Atribut yang disajikan meliputi:
        </p>
        <ol class="num-list">
            <li>Identitas barang: Kode unik, nama barang, badge status pelaporan berwarna, dan tanggal laporan masuk.</li>
            <li>Informasi fisik dan logistik: Kategori barang, jumlah unit, kondisi fisik, dan lokasi kejadian/penemuan.</li>
            <li>Identitas pelapor: Nama dan nomor kontak mahasiswa atau petugas kampus yang melaporkan.</li>
            <li>Deskripsi lengkap: Ciri-ciri visual khusus (warna, merk, stiker, atau isi di dalam barang).</li>
            <li>Navigasi terpadu: Tombol kembali ke daftar barang, tombol edit data langsung, dan tombol hapus data.</li>
        </ol>
    </div>
    <div class="page-number">8</div>
</div>

<!-- ========================================================
     BAB IV IMPLEMENTASI BLADE TEMPLATE ENGINE (SOAL 3) (HALAMAN 9)
     ======================================================== -->
<div class="page">
    <div class="content-area">
        <div class="sub-bab">4.5 Penggunaan Direktif Blade dan Keamanan Form</div>
        <p>
            Aplikasi mengimplementasikan seluruh direktif utama Blade Template Engine secara konsisten dan sesuai standar rekayasa web modern:
        </p>
        <ol class="num-list">
            <li><strong><code>@extends('layouts.app')</code></strong>: Digunakan di awal setiap berkas view untuk mewarisi struktur kerangka master layout.</li>
            <li><strong><code>@section('content')</code> dan <code>@yield('content')</code></strong>: Mendefinisikan dan menyuntikkan blok konten dinamis dari masing-masing halaman anak ke master layout.</li>
            <li><strong><code>@foreach($dataBarang as $item)</code></strong>: Melakukan perulangan iterasi untuk merender setiap baris barang dari session ke dalam baris tabel HTML.</li>
            <li><strong><code>@if(count($dataBarang) > 0) ... @else ... @endif</code></strong>: Melakukan pengecekan kondisional ketersediaan data barang serta pewarnaan badge status secara dinamis.</li>
            <li><strong><code>@csrf</code> (Cross-Site Request Forgery Protection)</strong>: Disematkan pada seluruh form HTML (POST, PUT, DELETE) untuk menyertakan token otentikasi rahasia bawaan Laravel guna mengamankan aplikasi dari serangan eksploitasi pihak ketiga.</li>
            <li><strong><code>@method('PUT')</code> dan <code>@method('DELETE')</code></strong>: Mengingat formulir HTML standar peramban web hanya mendukung method <code>GET</code> dan <code>POST</code>, direktif method spoofing ini digunakan untuk menyimulasikan method RESTful <code>PUT</code> pada proses update dan <code>DELETE</code> pada proses penghapusan data.</li>
            <li><strong>Konfirmasi Penghapusan JavaScript</strong>: Setiap form hapus dilengkapi atribut dialog <code>onsubmit="return confirm('Apakah Anda yakin ingin menghapus data barang ...?');"</code> untuk memvalidasi intensi pengguna sebelum mengeksekusi penghapusan dari session.</li>
        </ol>
    </div>
    <div class="page-number">9</div>
</div>

<!-- ========================================================
     BAB V HASIL PENGUJIAN SISTEM (SCREENSHOT CRUD) (HALAMAN 10)
     ======================================================== -->
<div class="page">
    <div class="content-area">
        <div class="bab-title">BAB V<br>HASIL PENGUJIAN SISTEM (SCREENSHOT CRUD)</div>

        <div class="sub-bab">5.1 Pengujian Halaman Daftar Barang (Read) - GET /barang</div>
        <p>
            Pengujian operasi <em>Read</em> dilakukan dengan mengakses alamat URL <code>http://127.0.0.1:8000/barang</code>. Halaman merender tabel 7 kolom dengan data barang yang diambil langsung dari session storage:
        </p>
        <div class="img-container">
            <img src="{c1_b64}" class="report-img" style="max-height: 140px;" alt="Tampilan Halaman Daftar Barang">
            <div class="img-caption"><strong>Gambar 5.1</strong> Tampilan Halaman Utama Daftar Barang (Read) dari Session File Driver</div>
        </div>

        <div class="sub-bab">5.2 Pengujian Formulir Tambah Barang (Create) - GET /barang/create</div>
        <p>
            Pengujian formulir input dilakukan dengan mengakses URL <code>http://127.0.0.1:8000/barang/create</code>. Sistem menampilkan formulir lengkap dengan kode otomatis BRG-006 dan proteksi CSRF:
        </p>
        <div class="img-container">
            <img src="{c2_b64}" class="report-img" style="max-height: 140px;" alt="Formulir Tambah Barang">
            <div class="img-caption"><strong>Gambar 5.2</strong> Tampilan Formulir Tambah Data Barang Baru (Create)</div>
        </div>
    </div>
    <div class="page-number">10</div>
</div>

<!-- ========================================================
     BAB V HASIL PENGUJIAN SISTEM (SCREENSHOT CRUD) (HALAMAN 11)
     ======================================================== -->
<div class="page">
    <div class="content-area">
        <div class="sub-bab">5.3 Pengujian Notifikasi Sukses Tambah Data (Store) - POST /barang</div>
        <p>
            Setelah pengguna mengisi formulir tambah dan menekan tombol simpan, request dikirim melalui method <code>POST</code>. Data baru disimpan ke file session, lalu pengguna dialihkan kembali ke daftar barang dengan alert notifikasi sukses berwarna hijau:
        </p>
        <div class="img-container">
            <img src="{c3_b64}" class="report-img" style="max-height: 145px;" alt="Notifikasi Sukses Tambah Data">
            <div class="img-caption"><strong>Gambar 5.3</strong> Notifikasi Flash Message Berhasil Menyimpan Data Barang Baru (Store)</div>
        </div>

        <div class="sub-bab">5.4 Pengujian Halaman Detail Barang (Show) - GET /barang/{{kode}}</div>
        <p>
            Pengujian melihat rincian informasi dilakukan dengan menekan tombol Detail pada salah satu barang (contoh: <code>/barang/BRG-001</code>). Seluruh spesifikasi barang dan identitas pelapor tersaji secara jelas:
        </p>
        <div class="img-container">
            <img src="{c4_b64}" class="report-img" style="max-height: 145px;" alt="Halaman Detail Barang">
            <div class="img-caption"><strong>Gambar 5.4</strong> Tampilan Halaman Detail Lengkap Barang (Show)</div>
        </div>
    </div>
    <div class="page-number">11</div>
</div>

<!-- ========================================================
     BAB V HASIL PENGUJIAN SISTEM (SCREENSHOT CRUD) (HALAMAN 12)
     ======================================================== -->
<div class="page">
    <div class="content-area">
        <div class="sub-bab">5.5 Pengujian Formulir Ubah Barang (Edit) - GET /barang/{{kode}}/edit</div>
        <p>
            Pengujian form edit dilakukan dengan menekan tombol Edit (contoh: <code>/barang/BRG-001/edit</code>). Seluruh isian lama barang ditampilkan kembali secara utuh (<em>pre-filled values</em>) dengan simulasi method <code>PUT</code>:
        </p>
        <div class="img-container">
            <img src="{c5_b64}" class="report-img" style="max-height: 145px;" alt="Formulir Edit Barang">
            <div class="img-caption"><strong>Gambar 5.5</strong> Tampilan Formulir Ubah Data Barang (Edit) dengan Pre-filled Values</div>
        </div>

        <div class="sub-bab">5.6 Pengujian Notifikasi Sukses Ubah Data (Update) - PUT /barang/{{kode}}</div>
        <p>
            Setelah formulir perubahan dikirimkan, Controller memvalidasi data dan memperbarui file session. Pengguna dialihkan kembali ke halaman utama disertai umpan balik sukses pembaharuan data:
        </p>
        <div class="img-container">
            <img src="{c6_b64}" class="report-img" style="max-height: 145px;" alt="Notifikasi Sukses Update Data">
            <div class="img-caption"><strong>Gambar 5.6</strong> Notifikasi Flash Message Berhasil Memperbarui Data Barang pada Session (Update)</div>
        </div>
    </div>
    <div class="page-number">12</div>
</div>

<!-- ========================================================
     BAB V HASIL PENGUJIAN SISTEM (SCREENSHOT CRUD) (HALAMAN 13)
     ======================================================== -->
<div class="page">
    <div class="content-area">
        <div class="sub-bab">5.7 Pengujian Penghapusan Data dan Konfirmasi (Destroy) - DELETE /barang/{{kode}}</div>
        <p>
            Pengujian operasi <em>Delete</em> dilakukan dengan menekan tombol Hapus. Peramban menampilkan dialog konfirmasi JavaScript. Setelah dikonfirmasi, request <code>DELETE</code> dikirim, barang dihapus dari array session, dan muncul alert sukses:
        </p>
        <div class="img-container">
            <img src="{c7_b64}" class="report-img" style="max-height: 145px;" alt="Notifikasi Sukses Hapus Data">
            <div class="img-caption"><strong>Gambar 5.7</strong> Notifikasi Flash Message Berhasil Menghapus Data Barang dari Session (Destroy)</div>
        </div>

        <div class="sub-bab">5.8 Pengujian Penanganan Kode Barang Tidak Ditemukan</div>
        <p>
            Pengujian keandalan sistem terhadap galat (<em>error handling</em>) dilakukan dengan memasukkan kode barang yang tidak terdaftar (contoh: <code>/barang/BRG-999</code>). Controller secara aman mengalihkan pengguna kembali ke halaman utama dengan pesan error merah:
        </p>
        <div class="img-container">
            <img src="{c8_b64}" class="report-img" style="max-height: 145px;" alt="Penanganan Error Kode Tidak Ditemukan">
            <div class="img-caption"><strong>Gambar 5.8</strong> Penanganan Error Handling Saat Mengakses Kode Barang yang Tidak Terdaftar</div>
        </div>
    </div>
    <div class="page-number">13</div>
</div>

<!-- ========================================================
     BAB VI KESIMPULAN DAN SARAN (HALAMAN 14)
     ======================================================== -->
<div class="page">
    <div class="content-area">
        <div class="bab-title">BAB VI<br>KESIMPULAN DAN SARAN</div>

        <div class="sub-bab">6.1 Kesimpulan</div>
        <p>
            Berdasarkan seluruh tahapan perancangan, implementasi, serta serangkaian pengujian teknis yang telah dilaksanakan pada proyek Ujian Tengah Semester (UTS) mata kuliah Pemrograman Berorientasi Objek (TI033015), dapat ditarik beberapa kesimpulan utama sebagai berikut:
        </p>
        <ol class="num-list">
            <li>Pola arsitektur perangkat lunak <strong>Route &rarr; Controller &rarr; Blade</strong> telah berhasil diterapkan secara konsisten dan murni menggunakan framework Laravel 13 dan PHP 8.3 tanpa mencampurkan logika bisnis ke dalam routing closure maupun menampilkan HTML langsung dari Controller.</li>
            <li>Seluruh <strong>7 route RESTful</strong> telah terkonfigurasi dengan tepat menggunakan <em>named routes</em> yang seragam, dan penempatan route statis <code>/barang/create</code> sebelum route dinamis <code>/barang/{{kode}}</code> terbukti sukses mencegah konflik penangkapan parameter URL.</li>
            <li>Mekanisme penyimpanan data berbasis berkas sesi lokal (<strong>SESSION_DRIVER=file</strong>) yang tersimpan di direktori <code>storage/framework/sessions/</code> terbukti andal dalam melayani seluruh operasi CRUD tanpa memerlukan koneksi database SQL.</li>
            <li>Antarmuka aplikasi yang dibangun dengan template engine Blade dan Tailwind CSS menyajikan layout yang konsisten, aman melalui proteksi <code>@csrf</code> dan <code>@method</code>, serta informatif melalui kehadiran notifikasi flash message dan dialog konfirmasi penghapusan data.</li>
            <li>Seluruh berkas proyek aplikasi telah dipublikasikan secara bersih pada repositori GitHub khusus UTS yang terpisah dari repositori tugas mingguan lainnya.</li>
        </ol>

        <div class="sub-bab">6.2 Saran</div>
        <p>
            Untuk pengembangan lebih lanjut dari sistem ini, beberapa saran konstruktif yang dapat diimplementasikan adalah:
        </p>
        <ol class="alpha-list">
            <li>Mengintegrasikan sistem dengan database relasional (seperti MySQL) menggunakan fitur <em>Migration</em> dan <em>Eloquent ORM</em> setelah materi perkuliahan pasca-UTS disampaikan.</li>
            <li>Menambahkan fitur autentikasi multi-peran (Admin Satpam dan Mahasiswa) untuk membatasi hak akses verifikasi pengembalian barang temuan.</li>
            <li>Menambahkan fitur unggah berkas foto fisik barang yang hilang atau ditemukan menggunakan media penyimpanan lokal <code>storage/app/public/</code>.</li>
        </ol>
    </div>
    <div class="page-number">14</div>
</div>

<!-- ========================================================
     DAFTAR PUSTAKA (HALAMAN 15)
     ======================================================== -->
<div class="page">
    <div class="content-area">
        <div class="bab-title">DAFTAR PUSTAKA</div>

        <div style="font-size: 11pt; line-height: 1.5; padding-left: 1.25cm; text-indent: -1.25cm; text-align: justify; margin-bottom: 12px;">
            Hilman, L. (2026). <em>Modul Pembelajaran Pemrograman Berorientasi Objek (TI033015): Arsitektur MVC dan Framework Laravel</em>. Cirebon: Fakultas Teknologi Informasi, Universitas Catur Insan Cendekia.
        </div>

        <div style="font-size: 11pt; line-height: 1.5; padding-left: 1.25cm; text-indent: -1.25cm; text-align: justify; margin-bottom: 12px;">
            Otwell, T. (2026). <em>Laravel Documentation: Routing, Controllers, Session, and Blade Templates (Release 13.x)</em>. Diakses dari https://laravel.com/docs.
        </div>

        <div style="font-size: 11pt; line-height: 1.5; padding-left: 1.25cm; text-indent: -1.25cm; text-align: justify; margin-bottom: 12px;">
            Pressman, R. S., &amp; Maxim, B. R. (2020). <em>Software Engineering: A Practitioner's Approach</em> (9th ed.). New York: McGraw-Hill Education.
        </div>

        <div style="font-size: 11pt; line-height: 1.5; padding-left: 1.25cm; text-indent: -1.25cm; text-align: justify; margin-bottom: 12px;">
            Sommerville, I. (2019). <em>Software Engineering</em> (10th ed.). London: Pearson Education.
        </div>

        <div style="font-size: 11pt; line-height: 1.5; padding-left: 1.25cm; text-indent: -1.25cm; text-align: justify; margin-bottom: 12px;">
            Universitas Catur Insan Cendekia. (2026). <em>Panduan Tata Tulis Penulisan Laporan Akademik dan Praktik Kerja Lapangan</em>. Cirebon: Pusat Pengembangan Akademik UCIC.
        </div>
    </div>
    <div class="page-number">15</div>
</div>

<!-- ========================================================
     LAMPIRAN (HALAMAN 16)
     ======================================================== -->
<div class="page">
    <div class="content-area">
        <div class="bab-title">LAMPIRAN</div>

        <div class="sub-bab">Lampiran 1: Tautan Repositori GitHub Khusus UTS</div>
        <p class="p-noindent">
            Sesuai ketentuan pengerjaan UTS bahwa repositori UTS dipisahkan dari tugas pertemuan lainnya, seluruh kode program, konfigurasi, tampilan Blade, dan pengujian telah dipublikasikan pada repositori GitHub resmi berikut:
        </p>
        <div class="code-snippet" style="font-size: 9.5pt; font-weight: bold; color: #1e3a8a;">
Repository URL : https://github.com/JulianathaTI2/uts-pbo-laravel.git
Cabang Aktif   : main
Nama Mahasiswa : Julian Atha Maulana
NIM            : 20251020052
Program Studi  : S1 Teknik Informatika - UCIC</div>

        <div class="sub-bab">Lampiran 2: Struktur Berkas Utama Proyek Laravel 13</div>
        <p class="p-noindent">
            Susunan direktori berkas utama yang diimplementasikan pada proyek UTS ini:
        </p>
        <div class="code-snippet">pbo-laravel/
├── app/
│   └── Http/
│       └── Controllers/
│           └── BarangController.php          &lt;-- Controller Utama CRUD Session (UTS)
├── resources/
│   └── views/
│       ├── layouts/
│       │   └── app.blade.php                 &lt;-- Master Layout Konsisten
│       └── barang/
│           ├── index.blade.php               &lt;-- Tabel Daftar 7 Kolom Wajib
│           ├── create.blade.php              &lt;-- Formulir Tambah Barang
│           ├── edit.blade.php                &lt;-- Formulir Ubah Pre-filled
│           └── show.blade.php                &lt;-- Kartu Detail Lengkap
├── routes/
│   └── web.php                               &lt;-- 7 Route RESTful Wajib
├── storage/
│   └── framework/
│       └── sessions/                         &lt;-- Lokasi Penyimpanan File Session
└── .env                                      &lt;-- SESSION_DRIVER=file</div>
    </div>
    <div class="page-number">16</div>
</div>

</body>
</html>
"""

html_file = r"C:\laragon\www\pbo-laravel\screenshots\laporan_uts_v2.html"
with open(html_file, "w", encoding="utf-8") as f:
    f.write(html)
print(f"HTML v2 saved to {html_file} ({len(html)} chars)")

pdf_out = r"C:\laragon\www\pbo-laravel\UTS_PBO_20251020052_JulianAthaMaulana.pdf"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

cmd = [
    chrome_path,
    "--headless",
    f"--print-to-pdf={pdf_out}",
    "--no-pdf-header-footer",
    html_file
]

res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(pdf_out):
    size = os.path.getsize(pdf_out)
    print(f"[SUCCESS] PDF Generated: {pdf_out} ({size} bytes)")
else:
    print(f"[FAIL] Could not generate PDF: {res.stderr}")
