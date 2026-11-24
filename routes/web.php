<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\BarangController;
use App\Http\Controllers\LaporanController;

/*
|--------------------------------------------------------------------------
| Web Routes - Ujian Tengah Semester (UTS) Pemrograman Berorientasi Objek
| Program Studi: S1 Teknik Informatika - Universitas Catur Insan Cendekia
| Mahasiswa   : Julian Atha Maulana (NIM: 20251020052)
| Dosen       : Hilman Lesmana, S.T., M.S.F.
| Topik       : Sistem Kehilangan & Temuan Barang (CRUD Session File Driver)
|--------------------------------------------------------------------------
*/

// Redirect root URL ke daftar barang
Route::get('/', function () {
    return redirect()->route('barang.index');
});

/*
|--------------------------------------------------------------------------
| SOAL 1: ROUTING RESTFUL DATA BARANG (7 ROUTE WAJIB)
| Pola: Route -> Controller -> Blade
| Perhatian: Route statis /barang/create diletakkan SEBELUM /barang/{kode}
|--------------------------------------------------------------------------
*/

// 1. GET /barang - Menampilkan seluruh daftar barang
Route::get('/barang', [BarangController::class, 'index'])
    ->name('barang.index');

// 2. GET /barang/create - Menampilkan form tambah barang baru (didefinisikan sebelum dinamis {kode})
Route::get('/barang/create', [BarangController::class, 'create'])
    ->name('barang.create');

// 3. POST /barang - Menyimpan data barang baru ke session
Route::post('/barang', [BarangController::class, 'store'])
    ->name('barang.store');

// 4. GET /barang/{kode} - Menampilkan detail satu barang berdasarkan kode
Route::get('/barang/{kode}', [BarangController::class, 'show'])
    ->name('barang.show');

// 5. GET /barang/{kode}/edit - Menampilkan form ubah data barang
Route::get('/barang/{kode}/edit', [BarangController::class, 'edit'])
    ->name('barang.edit');

// 6. PUT/PATCH /barang/{kode} - Memperbarui data barang di session
Route::match(['put', 'patch'], '/barang/{kode}', [BarangController::class, 'update'])
    ->name('barang.update');

// 7. DELETE /barang/{kode} - Menghapus data barang dari session
Route::delete('/barang/{kode}', [BarangController::class, 'destroy'])
    ->name('barang.destroy');

// Route Opsional: Reset session data barang ke nilai default awal
Route::post('/barang-reset', [BarangController::class, 'reset'])
    ->name('barang.reset');

/*
|--------------------------------------------------------------------------
| Route Tambahan: Modul Pertemuan 7 (OOP Polymorphism & Simulasi Klaim)
|--------------------------------------------------------------------------
*/
Route::get('/laporan', [LaporanController::class, 'index'])->name('laporan.index');
Route::get('/laporan/{id}', [LaporanController::class, 'show'])->name('laporan.show');
Route::get('/klaim/{status?}', [LaporanController::class, 'klaim'])->name('laporan.klaim');
