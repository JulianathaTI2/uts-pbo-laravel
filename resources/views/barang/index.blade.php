@extends('layouts.app')

@section('title', 'Daftar Barang Kehilangan & Temuan (CRUD Session)')

@section('content')
<div class="space-y-6">

    <!-- Header Section -->
    <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4 bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
        <div>
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold bg-blue-100 text-blue-800 mb-2">
                <i class="fa-solid fa-database"></i> Penyimpanan Session File Laravel 13
            </div>
            <h1 class="text-2xl font-black text-slate-800 tracking-tight">Manajemen Data Barang Kehilangan & Temuan</h1>
            <p class="text-sm text-slate-500 mt-1">
                Implementasi CRUD lengkap menggunakan Session driver file sesuai Soal No. 1, 2, dan 3 UTS PBO.
            </p>
        </div>
        <div class="flex items-center gap-3">
            <form action="{{ route('barang.reset') }}" method="POST" onsubmit="return confirm('Reset seluruh data session ke default mock data?');">
                @csrf
                <button type="submit" class="inline-flex items-center gap-2 px-3.5 py-2.5 rounded-lg border border-slate-300 text-slate-700 bg-white hover:bg-slate-50 text-sm font-semibold transition shadow-sm" title="Kembalikan data session ke mock awal">
                    <i class="fa-solid fa-arrows-rotate text-slate-500"></i> Reset Default
                </button>
            </form>
            <a href="{{ route('barang.create') }}" class="inline-flex items-center gap-2 px-4 py-2.5 rounded-lg bg-blue-600 hover:bg-blue-700 text-white text-sm font-bold shadow-md hover:shadow-lg transition">
                <i class="fa-solid fa-circle-plus"></i> Tambah Barang Baru
            </a>
        </div>
    </div>

    <!-- Quick Stats Cards -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
            <div class="w-12 h-12 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center text-xl font-bold">
                <i class="fa-solid fa-boxes-stacked"></i>
            </div>
            <div>
                <p class="text-xs font-medium text-slate-500 uppercase tracking-wider">Total Barang</p>
                <p class="text-2xl font-black text-slate-800">{{ $totalBarang }}</p>
            </div>
        </div>
        <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
            <div class="w-12 h-12 rounded-lg bg-rose-50 text-rose-600 flex items-center justify-center text-xl font-bold">
                <i class="fa-solid fa-triangle-exclamation"></i>
            </div>
            <div>
                <p class="text-xs font-medium text-slate-500 uppercase tracking-wider">Status Hilang</p>
                <p class="text-2xl font-black text-rose-600">{{ $totalHilang }}</p>
            </div>
        </div>
        <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
            <div class="w-12 h-12 rounded-lg bg-emerald-50 text-emerald-600 flex items-center justify-center text-xl font-bold">
                <i class="fa-solid fa-hand-holding-hand"></i>
            </div>
            <div>
                <p class="text-xs font-medium text-slate-500 uppercase tracking-wider">Status Ditemukan</p>
                <p class="text-2xl font-black text-emerald-600">{{ $totalDitemukan }}</p>
            </div>
        </div>
        <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
            <div class="w-12 h-12 rounded-lg bg-indigo-50 text-indigo-600 flex items-center justify-center text-xl font-bold">
                <i class="fa-solid fa-shield-check"></i>
            </div>
            <div>
                <p class="text-xs font-medium text-slate-500 uppercase tracking-wider">Status Diklaim</p>
                <p class="text-2xl font-black text-indigo-600">{{ $totalDiklaim }}</p>
            </div>
        </div>
    </div>

    <!-- Search & Filter Bar -->
    <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-3">
        <form action="{{ route('barang.index') }}" method="GET" class="flex items-center gap-2 flex-grow max-w-lg">
            <div class="relative w-full">
                <i class="fa-solid fa-magnifying-glass absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400 text-sm"></i>
                <input type="text" name="q" value="{{ $searchQuery ?? '' }}" placeholder="Cari nama barang, kode, lokasi, atau kategori..." 
                       class="w-full pl-10 pr-4 py-2 text-sm border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition">
            </div>
            <button type="submit" class="px-4 py-2 bg-slate-800 hover:bg-slate-900 text-white text-sm font-semibold rounded-lg transition">
                Cari
            </button>
            @if(!empty($searchQuery))
                <a href="{{ route('barang.index') }}" class="px-3 py-2 bg-slate-100 hover:bg-slate-200 text-slate-600 text-sm font-medium rounded-lg transition">
                    Reset
                </a>
            @endif
        </form>
        <div class="text-xs text-slate-500">
            Menampilkan <strong>{{ count($dataBarang) }}</strong> data barang aktif
        </div>
    </div>

    <!-- Main Table Section (Sesuai Soal 3: Kode, Nama Barang, Kategori, Lokasi, Jumlah, Kondisi, Aksi) -->
    <div class="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
        <div class="px-6 py-4 border-b border-slate-200 bg-slate-50/70 flex items-center justify-between">
            <h2 class="font-bold text-slate-800 text-base flex items-center gap-2">
                <i class="fa-solid fa-table-list text-blue-600"></i> Tabel Data Barang (Session Storage)
            </h2>
            <span class="text-xs bg-slate-200 text-slate-700 px-2.5 py-1 rounded-full font-mono font-semibold">
                SESSION_DRIVER=file
            </span>
        </div>

        <div class="overflow-x-auto">
            <table class="w-full text-left border-collapse text-sm">
                <thead>
                    <tr class="bg-slate-100/80 text-slate-700 text-xs uppercase tracking-wider border-b border-slate-200">
                        <th class="py-3.5 px-4 font-bold text-center w-28">Kode</th>
                        <th class="py-3.5 px-4 font-bold">Nama Barang</th>
                        <th class="py-3.5 px-4 font-bold">Kategori</th>
                        <th class="py-3.5 px-4 font-bold">Lokasi</th>
                        <th class="py-3.5 px-4 font-bold text-center w-20">Jumlah</th>
                        <th class="py-3.5 px-4 font-bold text-center w-32">Kondisi</th>
                        <th class="py-3.5 px-4 font-bold text-center w-48">Aksi</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-200">
                    @if(count($dataBarang) > 0)
                        @foreach($dataBarang as $item)
                            <tr class="hover:bg-blue-50/40 transition">
                                <!-- 1. Kode -->
                                <td class="py-3.5 px-4 font-mono font-bold text-blue-700 text-center">
                                    <span class="px-2.5 py-1 bg-blue-50 border border-blue-200 rounded-md">
                                        {{ $item['kode'] }}
                                    </span>
                                </td>

                                <!-- 2. Nama Barang & Status Badge -->
                                <td class="py-3.5 px-4">
                                    <div class="font-bold text-slate-900">{{ $item['nama'] }}</div>
                                    <div class="flex items-center gap-2 mt-1">
                                        @if(strtolower($item['status']) === 'hilang')
                                            <span class="inline-flex items-center gap-1 text-[11px] font-semibold px-2 py-0.5 rounded-full bg-rose-100 text-rose-800">
                                                <i class="fa-solid fa-circle-exclamation text-[9px]"></i> Hilang
                                            </span>
                                        @elseif(strtolower($item['status']) === 'ditemukan')
                                            <span class="inline-flex items-center gap-1 text-[11px] font-semibold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800">
                                                <i class="fa-solid fa-circle-check text-[9px]"></i> Ditemukan
                                            </span>
                                        @else
                                            <span class="inline-flex items-center gap-1 text-[11px] font-semibold px-2 py-0.5 rounded-full bg-indigo-100 text-indigo-800">
                                                <i class="fa-solid fa-handshake text-[9px]"></i> {{ $item['status'] }}
                                            </span>
                                        @endif
                                        <span class="text-xs text-slate-400">
                                            <i class="fa-regular fa-calendar-days text-[10px]"></i> {{ $item['tgl_lapor'] ?? '-' }}
                                        </span>
                                    </div>
                                </td>

                                <!-- 3. Kategori -->
                                <td class="py-3.5 px-4 text-slate-600">
                                    <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-xs font-medium bg-slate-100 text-slate-700 border border-slate-200">
                                        <i class="fa-solid fa-tag text-slate-400"></i> {{ $item['kategori'] }}
                                    </span>
                                </td>

                                <!-- 4. Lokasi -->
                                <td class="py-3.5 px-4 text-slate-600 text-xs">
                                    <div class="flex items-start gap-1.5">
                                        <i class="fa-solid fa-location-dot text-rose-500 mt-0.5"></i>
                                        <span>{{ $item['lokasi'] }}</span>
                                    </div>
                                </td>

                                <!-- 5. Jumlah -->
                                <td class="py-3.5 px-4 text-center font-bold text-slate-800">
                                    {{ $item['jumlah'] }}
                                </td>

                                <!-- 6. Kondisi -->
                                <td class="py-3.5 px-4 text-center">
                                    <span class="inline-flex items-center px-2 py-1 rounded text-xs font-medium bg-amber-50 text-amber-800 border border-amber-200">
                                        {{ $item['kondisi'] }}
                                    </span>
                                </td>

                                <!-- 7. Aksi (Detail, Edit, Hapus) -->
                                <td class="py-3.5 px-4 text-center">
                                    <div class="flex items-center justify-center gap-1.5">
                                        <!-- Tombol Detail -->
                                        <a href="{{ route('barang.show', $item['kode']) }}" 
                                           class="inline-flex items-center px-2.5 py-1.5 rounded-md bg-blue-50 text-blue-700 hover:bg-blue-100 text-xs font-bold transition border border-blue-200" 
                                           title="Lihat Detail Barang">
                                            <i class="fa-solid fa-eye mr-1"></i> Detail
                                        </a>

                                        <!-- Tombol Edit -->
                                        <a href="{{ route('barang.edit', $item['kode']) }}" 
                                           class="inline-flex items-center px-2.5 py-1.5 rounded-md bg-amber-50 text-amber-700 hover:bg-amber-100 text-xs font-bold transition border border-amber-200" 
                                           title="Ubah Data Barang">
                                            <i class="fa-solid fa-pen-to-square mr-1"></i> Edit
                                        </a>

                                        <!-- Form Hapus dengan Konfirmasi (@csrf dan @method('DELETE')) -->
                                        <form action="{{ route('barang.destroy', $item['kode']) }}" 
                                              method="POST" 
                                              onsubmit="return confirm('Apakah Anda yakin ingin menghapus data barang [{{ $item['kode'] }} - {{ $item['nama'] }}]? Data akan dihapus dari session.');"
                                              class="inline-block">
                                            @csrf
                                            @method('DELETE')
                                            <button type="submit" 
                                                    class="inline-flex items-center px-2.5 py-1.5 rounded-md bg-rose-50 text-rose-700 hover:bg-rose-100 text-xs font-bold transition border border-rose-200" 
                                                    title="Hapus Barang dari Session">
                                                <i class="fa-solid fa-trash-can mr-1"></i> Hapus
                                            </button>
                                        </form>
                                    </div>
                                </td>
                            </tr>
                        @endforeach
                    @else
                        <tr>
                            <td colspan="7" class="py-12 text-center text-slate-400">
                                <i class="fa-solid fa-box-open text-4xl mb-3 text-slate-300"></i>
                                <p class="text-base font-semibold text-slate-600">Tidak ada data barang yang tersedia.</p>
                                <p class="text-xs text-slate-400 mt-1">Data pada session kosong atau tidak cocok dengan pencarian.</p>
                                <a href="{{ route('barang.create') }}" class="inline-flex items-center gap-1.5 mt-4 px-4 py-2 bg-blue-600 text-white rounded-lg text-xs font-bold hover:bg-blue-700 transition">
                                    <i class="fa-solid fa-plus"></i> Tambah Data Baru Sekarang
                                </a>
                            </td>
                        </tr>
                    @endif
                </tbody>
            </table>
        </div>
    </div>

    <!-- Info Box: Ketentuan Pengerjaan UTS -->
    <div class="bg-blue-50 border border-blue-200 rounded-xl p-5 text-sm text-blue-900 flex flex-col md:flex-row gap-4 items-start">
        <div class="text-blue-600 text-2xl pt-1">
            <i class="fa-solid fa-circle-info"></i>
        </div>
        <div class="space-y-1">
            <h4 class="font-bold text-blue-950">Catatan Arsitektur Sistem (UTS PBO TI033015)</h4>
            <p class="text-xs text-blue-800 leading-relaxed">
                Aplikasi ini mengimplementasikan pola <strong>Route &rarr; Controller &rarr; Blade</strong> tanpa database. 
                Data disimpan pada session file driver (<code>SESSION_DRIVER=file</code>) yang tersimpan di direktori <code>storage/framework/sessions/</code>. 
                Seluruh 7 route RESTful telah terdaftar dengan named routes konsisten, form menggunakan proteksi <code>@csrf</code>, serta HTTP spoofing <code>@method('PUT')</code> dan <code>@method('DELETE')</code>.
            </p>
        </div>
    </div>

</div>
@endsection
