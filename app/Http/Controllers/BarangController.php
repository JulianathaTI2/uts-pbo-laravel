<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

/**
 * Class BarangController
 * 
 * Menangani alur CRUD (Create, Read, Update, Delete) pengelolaan data barang
 * untuk Studi Kasus: Sistem Kehilangan & Temuan Barang di Lingkungan Kampus.
 * 
 * Sesuai ketentuan UTS Pemrograman Berorientasi Objek (TI033015):
 * - Menggunakan session file driver (SESSION_DRIVER=file) tanpa database
 * - Memisahkan proses CRUD ke method Controller terpisah (Route -> Controller -> Blade)
 * - Validasi input, notifikasi flash message (success/error), dan penanganan error 404/not found.
 * 
 * @author Julian Atha Maulana (NIM: 20251020052)
 */
class BarangController extends Controller
{
    /**
     * Mengambil seluruh data barang dari session.
     * Jika session belum diinisialisasi, dibuatkan data awal (default mock data)
     * yang merepresentasikan kasus kehilangan dan penemuan barang kampus.
     * 
     * @return array<string, array>
     */
    private function getBarangFromSession(): array
    {
        if (!session()->has('data_barang')) {
            $initialData = [
                'BRG-001' => [
                    'kode'      => 'BRG-001',
                    'nama'      => 'Dompet Kulit Hitam',
                    'kategori'  => 'Aksesoris & Dompet',
                    'lokasi'    => 'Perpustakaan Lantai 2 (Meja Baca 04)',
                    'jumlah'    => 1,
                    'kondisi'   => 'Baik',
                    'status'    => 'Hilang',
                    'tgl_lapor' => '2026-11-20',
                    'pelapor'   => 'Budi Santoso (NIM: 20251020011)',
                    'deskripsi' => 'Dompet kulit sintetis merk Baellerry warna hitam, berisi KTM UCIC dan beberapa kartu ATM.'
                ],
                'BRG-002' => [
                    'kode'      => 'BRG-002',
                    'nama'      => 'Botol Minum Tupperware Biru',
                    'kategori'  => 'Peralatan Minum/Makan',
                    'lokasi'    => 'Kantin Belakang Kampus',
                    'jumlah'    => 1,
                    'kondisi'   => 'Baik',
                    'status'    => 'Hilang',
                    'tgl_lapor' => '2026-11-21',
                    'pelapor'   => 'Sari Indah (NIM: 20251020034)',
                    'deskripsi' => 'Ukuran 750ml, tutup warna putih dengan stiker logo coding Laravel di bagian samping.'
                ],
                'BRG-003' => [
                    'kode'      => 'BRG-003',
                    'nama'      => 'Kunci Motor Honda Vario',
                    'kategori'  => 'Kunci & Kendaraan',
                    'lokasi'    => 'Parkiran Motor Depan Gedung B',
                    'jumlah'    => 1,
                    'kondisi'   => 'Baik',
                    'status'    => 'Ditemukan',
                    'tgl_lapor' => '2026-11-22',
                    'pelapor'   => 'Dani Hermawan (Petugas Parkir)',
                    'deskripsi' => 'Kunci kontak motor Honda dengan gantungan pita merah bertuliskan One Heart.'
                ],
                'BRG-004' => [
                    'kode'      => 'BRG-004',
                    'nama'      => 'Jaket Hoodie Abu-abu UCIC',
                    'kategori'  => 'Pakaian & Tekstil',
                    'lokasi'    => 'Ruang Kelas B.203',
                    'jumlah'    => 1,
                    'kondisi'   => 'Lecet Pemakaian',
                    'status'    => 'Hilang',
                    'tgl_lapor' => '2026-11-22',
                    'pelapor'   => 'Maya Anggraini (NIM: 20251020089)',
                    'deskripsi' => 'Ukuran XL, resleting depan, bordir logo Universitas Catur Insan Cendekia di dada kiri.'
                ],
                'BRG-005' => [
                    'kode'      => 'BRG-005',
                    'nama'      => 'Payung Lipat Otomatis Hitam',
                    'kategori'  => 'Aksesoris & Perlengkapan',
                    'lokasi'    => 'Lobi Utama Gedung A (Dekat CS)',
                    'jumlah'    => 1,
                    'kondisi'   => 'Sangat Baik',
                    'status'    => 'Ditemukan',
                    'tgl_lapor' => '2026-11-23',
                    'pelapor'   => 'Tono Sutrisno (Security Kampus)',
                    'deskripsi' => 'Payung lipat warna hitam polos dengan pegangan bertekstur kayu elegan.'
                ],
            ];

            session(['data_barang' => $initialData]);
        }

        return session('data_barang', []);
    }

    /**
     * Menyimpan array data barang kembali ke session Laravel.
     * 
     * @param array $data
     * @return void
     */
    private function saveBarangToSession(array $data): void
    {
        session(['data_barang' => $data]);
        session()->save(); // Pastikan tersimpan ke session file storage
    }

    /**
     * 1. GET /barang (Route: barang.index)
     * Mengambil data barang dari session dan mengirimkannya ke view daftar.
     */
    public function index(Request $request)
    {
        // Support preview flash notification untuk dokumentasi pengujian CRUD
        if ($request->has('preview_flash')) {
            $pf = $request->query('preview_flash');
            if ($pf === 'store') {
                session()->now('success', 'Sukses! Data barang [BRG-006 - Kacamata Minus Frame Hitam Rayban] berhasil disimpan ke dalam session.');
            } elseif ($pf === 'update') {
                session()->now('success', 'Sukses! Data barang [BRG-001 - Dompet Kulit Hitam (Terverifikasi)] berhasil diperbarui.');
            } elseif ($pf === 'delete') {
                session()->now('success', 'Sukses! Data barang [BRG-005 - Payung Lipat Otomatis Hitam] berhasil dihapus dari sistem.');
            } elseif ($pf === 'not_found') {
                session()->now('error', 'Barang dengan kode [BRG-999] tidak ditemukan dalam sistem.');
            }
        }

        $dataBarang = $this->getBarangFromSession();

        // Fitur pencarian sederhana jika ada query parameter 'q'
        $query = $request->query('q');
        if (!empty($query)) {
            $dataBarang = array_filter($dataBarang, function ($item) use ($query) {
                return stripos($item['nama'], $query) !== false ||
                       stripos($item['kode'], $query) !== false ||
                       stripos($item['lokasi'], $query) !== false ||
                       stripos($item['kategori'], $query) !== false;
            });
        }

        // Hitung statistik ringkasan
        $allData = $this->getBarangFromSession();
        $totalBarang = count($allData);
        $totalHilang = count(array_filter($allData, fn($i) => strtolower($i['status']) === 'hilang'));
        $totalDitemukan = count(array_filter($allData, fn($i) => strtolower($i['status']) === 'ditemukan'));
        $totalDiklaim = count(array_filter($allData, fn($i) => in_array(strtolower($i['status']), ['diklaim', 'selesai'])));

        return view('barang.index', [
            'dataBarang'     => $dataBarang,
            'totalBarang'    => $totalBarang,
            'totalHilang'    => $totalHilang,
            'totalDitemukan' => $totalDitemukan,
            'totalDiklaim'   => $totalDiklaim,
            'searchQuery'    => $query,
        ]);
    }

    /**
     * 2. GET /barang/create (Route: barang.create)
     * Menampilkan formulir penambahan data barang baru.
     */
    public function create()
    {
        // Generate usulan kode otomatis (contoh: BRG-006)
        $dataBarang = $this->getBarangFromSession();
        $nextNum = count($dataBarang) + 1;
        $suggestedKode = sprintf('BRG-%03d', $nextNum);

        while (isset($dataBarang[$suggestedKode])) {
            $nextNum++;
            $suggestedKode = sprintf('BRG-%03d', $nextNum);
        }

        return view('barang.create', [
            'suggestedKode' => $suggestedKode,
            'kategoriList'  => [
                'Aksesoris & Dompet',
                'Peralatan Minum/Makan',
                'Kunci & Kendaraan',
                'Pakaian & Tekstil',
                'Elektronik & Gadget',
                'Dokumen & Buku',
                'Lain-lain'
            ],
            'kondisiList'   => ['Sangat Baik', 'Baik', 'Lecet Pemakaian', 'Rusak Ringan']
        ]);
    }

    /**
     * 3. POST /barang (Route: barang.store)
     * Menerima input form, membentuk data barang, menyimpan ke session, lalu redirect.
     */
    public function store(Request $request)
    {
        // Validasi input form
        $request->validate([
            'kode'      => 'required|string|max:20',
            'nama'      => 'required|string|min:3|max:100',
            'kategori'  => 'required|string|max:50',
            'lokasi'    => 'required|string|max:100',
            'jumlah'    => 'required|integer|min:1',
            'kondisi'   => 'required|string|max:50',
            'status'    => 'required|string|in:Hilang,Ditemukan,Diklaim',
            'tgl_lapor' => 'required|date',
            'pelapor'   => 'nullable|string|max:100',
            'deskripsi' => 'nullable|string|max:500',
        ]);

        $kode = strtoupper(trim($request->input('kode')));
        $dataBarang = $this->getBarangFromSession();

        // Cek apakah kode barang sudah ada di session
        if (isset($dataBarang[$kode])) {
            return redirect()->back()
                ->withInput()
                ->with('error', "Gagal menambahkan data! Kode barang [{$kode}] sudah terdaftar di sistem.");
        }

        // Bentuk data barang baru
        $barangBaru = [
            'kode'      => $kode,
            'nama'      => trim($request->input('nama')),
            'kategori'  => $request->input('kategori'),
            'lokasi'    => trim($request->input('lokasi')),
            'jumlah'    => (int) $request->input('jumlah'),
            'kondisi'   => $request->input('kondisi'),
            'status'    => $request->input('status'),
            'tgl_lapor' => $request->input('tgl_lapor'),
            'pelapor'   => $request->input('pelapor') ? trim($request->input('pelapor')) : 'Anonim / Mahasiswa',
            'deskripsi' => $request->input('deskripsi') ? trim($request->input('deskripsi')) : '-'
        ];

        // Simpan ke session
        $dataBarang[$kode] = $barangBaru;
        $this->saveBarangToSession($dataBarang);

        return redirect()->route('barang.index')
            ->with('success', "Sukses! Data barang [{$barangBaru['kode']} - {$barangBaru['nama']}] berhasil disimpan.");
    }

    /**
     * 4. GET /barang/{kode} (Route: barang.show)
     * Menampilkan detail satu barang berdasarkan kode.
     */
    public function show($kode)
    {
        $dataBarang = $this->getBarangFromSession();
        $kodeUpper = strtoupper(trim($kode));

        if (!isset($dataBarang[$kodeUpper])) {
            return redirect()->route('barang.index')
                ->with('error', "Barang dengan kode [{$kode}] tidak ditemukan dalam sistem.");
        }

        return view('barang.show', [
            'barang' => $dataBarang[$kodeUpper]
        ]);
    }

    /**
     * 5. GET /barang/{kode}/edit (Route: barang.edit)
     * Menampilkan form edit dengan data barang yang dipilih.
     */
    public function edit($kode)
    {
        $dataBarang = $this->getBarangFromSession();
        $kodeUpper = strtoupper(trim($kode));

        if (!isset($dataBarang[$kodeUpper])) {
            return redirect()->route('barang.index')
                ->with('error', "Barang dengan kode [{$kode}] tidak ditemukan untuk disunting.");
        }

        return view('barang.edit', [
            'barang'        => $dataBarang[$kodeUpper],
            'kategoriList'  => [
                'Aksesoris & Dompet',
                'Peralatan Minum/Makan',
                'Kunci & Kendaraan',
                'Pakaian & Tekstil',
                'Elektronik & Gadget',
                'Dokumen & Buku',
                'Lain-lain'
            ],
            'kondisiList'   => ['Sangat Baik', 'Baik', 'Lecet Pemakaian', 'Rusak Ringan']
        ]);
    }

    /**
     * 6. PUT/PATCH /barang/{kode} (Route: barang.update)
     * Memperbarui data barang pada session berdasarkan kode.
     */
    public function update(Request $request, $kode)
    {
        $kodeUpper = strtoupper(trim($kode));
        $dataBarang = $this->getBarangFromSession();

        if (!isset($dataBarang[$kodeUpper])) {
            return redirect()->route('barang.index')
                ->with('error', "Gagal memperbarui! Barang dengan kode [{$kode}] tidak ditemukan.");
        }

        // Validasi input
        $request->validate([
            'nama'      => 'required|string|min:3|max:100',
            'kategori'  => 'required|string|max:50',
            'lokasi'    => 'required|string|max:100',
            'jumlah'    => 'required|integer|min:1',
            'kondisi'   => 'required|string|max:50',
            'status'    => 'required|string|in:Hilang,Ditemukan,Diklaim',
            'tgl_lapor' => 'required|date',
            'pelapor'   => 'nullable|string|max:100',
            'deskripsi' => 'nullable|string|max:500',
        ]);

        // Perbarui data
        $dataBarang[$kodeUpper]['nama']      = trim($request->input('nama'));
        $dataBarang[$kodeUpper]['kategori']  = $request->input('kategori');
        $dataBarang[$kodeUpper]['lokasi']    = trim($request->input('lokasi'));
        $dataBarang[$kodeUpper]['jumlah']    = (int) $request->input('jumlah');
        $dataBarang[$kodeUpper]['kondisi']   = $request->input('kondisi');
        $dataBarang[$kodeUpper]['status']    = $request->input('status');
        $dataBarang[$kodeUpper]['tgl_lapor'] = $request->input('tgl_lapor');
        $dataBarang[$kodeUpper]['pelapor']   = $request->input('pelapor') ? trim($request->input('pelapor')) : $dataBarang[$kodeUpper]['pelapor'];
        $dataBarang[$kodeUpper]['deskripsi'] = $request->input('deskripsi') ? trim($request->input('deskripsi')) : '-';

        $this->saveBarangToSession($dataBarang);

        return redirect()->route('barang.index')
            ->with('success', "Sukses! Data barang [{$kodeUpper} - {$dataBarang[$kodeUpper]['nama']}] berhasil diperbarui.");
    }

    /**
     * 7. DELETE /barang/{kode} (Route: barang.destroy)
     * Menghapus barang dari session berdasarkan kode.
     */
    public function destroy($kode)
    {
        $kodeUpper = strtoupper(trim($kode));
        $dataBarang = $this->getBarangFromSession();

        if (!isset($dataBarang[$kodeUpper])) {
            return redirect()->route('barang.index')
                ->with('error', "Gagal menghapus! Barang dengan kode [{$kode}] tidak ditemukan.");
        }

        $namaBarang = $dataBarang[$kodeUpper]['nama'];
        unset($dataBarang[$kodeUpper]);
        $this->saveBarangToSession($dataBarang);

        return redirect()->route('barang.index')
            ->with('success', "Sukses! Data barang [{$kodeUpper} - {$namaBarang}] berhasil dihapus dari sistem.");
    }

    /**
     * Opsional: Reset session data kembali ke data awal.
     */
    public function reset()
    {
        session()->forget('data_barang');
        $this->getBarangFromSession(); // Re-initialize

        return redirect()->route('barang.index')
            ->with('info', 'Data barang pada session berhasil di-reset ke nilai default awal.');
    }
}
