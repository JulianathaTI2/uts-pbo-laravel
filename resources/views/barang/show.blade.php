@extends('layouts.app')

@section('title', 'Detail Barang ' . $barang['kode'] . ' - UTS PBO')

@section('content')
<div class="max-w-3xl mx-auto space-y-6">

    <!-- Header Navigation Back -->
    <div class="flex items-center justify-between">
        <a href="{{ route('barang.index') }}" class="inline-flex items-center gap-2 text-sm font-semibold text-slate-600 hover:text-blue-600 transition">
            <i class="fa-solid fa-arrow-left"></i> Kembali ke Daftar Barang
        </a>
        <span class="text-xs font-mono bg-blue-100 text-blue-800 px-3 py-1 rounded-full font-semibold">
            Route: barang.show [GET]
        </span>
    </div>

    <!-- Main Detail Card -->
    <div class="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
        <!-- Card Top Banner -->
        <div class="px-6 py-5 border-b border-slate-200 bg-gradient-to-r from-slate-50 to-blue-50/50 flex flex-col md:flex-row md:items-center md:justify-between gap-4">
            <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-xl bg-blue-600 text-white flex items-center justify-center text-xl font-bold shadow-md">
                    <i class="fa-solid fa-box-archive"></i>
                </div>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="font-mono text-xs font-black text-blue-700 bg-blue-100 px-2.5 py-0.5 rounded">
                            {{ $barang['kode'] }}
                        </span>
                        @if(strtolower($barang['status']) === 'hilang')
                            <span class="text-xs font-bold px-2.5 py-0.5 rounded-full bg-rose-100 text-rose-800 flex items-center gap-1">
                                <i class="fa-solid fa-circle-exclamation text-[10px]"></i> Hilang
                            </span>
                        @elseif(strtolower($barang['status']) === 'ditemukan')
                            <span class="text-xs font-bold px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 flex items-center gap-1">
                                <i class="fa-solid fa-circle-check text-[10px]"></i> Ditemukan
                            </span>
                        @else
                            <span class="text-xs font-bold px-2.5 py-0.5 rounded-full bg-indigo-100 text-indigo-800 flex items-center gap-1">
                                <i class="fa-solid fa-handshake text-[10px]"></i> {{ $barang['status'] }}
                            </span>
                        @endif
                    </div>
                    <h1 class="text-xl font-black text-slate-800 mt-1">{{ $barang['nama'] }}</h1>
                </div>
            </div>

            <!-- Action Buttons on Header -->
            <div class="flex items-center gap-2">
                <a href="{{ route('barang.edit', $barang['kode']) }}" 
                   class="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-lg bg-amber-500 hover:bg-amber-600 text-white text-xs font-bold transition shadow-sm">
                    <i class="fa-solid fa-pen-to-square"></i> Edit
                </a>
                <form action="{{ route('barang.destroy', $barang['kode']) }}" 
                      method="POST" 
                      onsubmit="return confirm('Apakah Anda yakin ingin menghapus data barang ini dari session?');"
                      class="inline-block">
                    @csrf
                    @method('DELETE')
                    <button type="submit" 
                            class="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-lg bg-rose-600 hover:bg-rose-700 text-white text-xs font-bold transition shadow-sm">
                        <i class="fa-solid fa-trash-can"></i> Hapus
                    </button>
                </form>
            </div>
        </div>

        <!-- Detail Attributes List -->
        <div class="p-6">
            <h2 class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-4">Informasi Rinci Atribut Barang</h2>

            <dl class="grid grid-cols-1 md:grid-cols-2 gap-x-6 gap-y-4 text-sm">
                <!-- Kategori -->
                <div class="p-3 bg-slate-50 rounded-lg border border-slate-100">
                    <dt class="text-xs font-semibold text-slate-500">Kategori Barang</dt>
                    <dd class="text-slate-800 font-bold mt-1 flex items-center gap-1.5">
                        <i class="fa-solid fa-tag text-blue-500"></i> {{ $barang['kategori'] }}
                    </dd>
                </div>

                <!-- Jumlah -->
                <div class="p-3 bg-slate-50 rounded-lg border border-slate-100">
                    <dt class="text-xs font-semibold text-slate-500">Jumlah Unit</dt>
                    <dd class="text-slate-800 font-bold mt-1 flex items-center gap-1.5">
                        <i class="fa-solid fa-layer-group text-blue-500"></i> {{ $barang['jumlah'] }} Unit
                    </dd>
                </div>

                <!-- Lokasi -->
                <div class="p-3 bg-slate-50 rounded-lg border border-slate-100">
                    <dt class="text-xs font-semibold text-slate-500">Lokasi Kejadian / Ditemukan</dt>
                    <dd class="text-slate-800 font-bold mt-1 flex items-center gap-1.5">
                        <i class="fa-solid fa-location-dot text-rose-500"></i> {{ $barang['lokasi'] }}
                    </dd>
                </div>

                <!-- Kondisi -->
                <div class="p-3 bg-slate-50 rounded-lg border border-slate-100">
                    <dt class="text-xs font-semibold text-slate-500">Kondisi Fisik</dt>
                    <dd class="text-slate-800 font-bold mt-1 flex items-center gap-1.5">
                        <i class="fa-solid fa-sparkles text-amber-500"></i> {{ $barang['kondisi'] }}
                    </dd>
                </div>

                <!-- Tanggal Lapor -->
                <div class="p-3 bg-slate-50 rounded-lg border border-slate-100">
                    <dt class="text-xs font-semibold text-slate-500">Tanggal Pelaporan</dt>
                    <dd class="text-slate-800 font-bold mt-1 flex items-center gap-1.5">
                        <i class="fa-regular fa-calendar-check text-emerald-500"></i> {{ $barang['tgl_lapor'] ?? '-' }}
                    </dd>
                </div>

                <!-- Pelapor -->
                <div class="p-3 bg-slate-50 rounded-lg border border-slate-100">
                    <dt class="text-xs font-semibold text-slate-500">Identitas Pelapor / Saksi</dt>
                    <dd class="text-slate-800 font-bold mt-1 flex items-center gap-1.5">
                        <i class="fa-solid fa-user-check text-indigo-500"></i> {{ $barang['pelapor'] ?? 'Anonim' }}
                    </dd>
                </div>
            </dl>

            <!-- Deskripsi Ciri Khusus -->
            <div class="mt-5 p-4 bg-blue-50/50 rounded-lg border border-blue-100">
                <h3 class="text-xs font-bold text-blue-900 uppercase tracking-wider mb-1">
                    <i class="fa-solid fa-align-left mr-1"></i> Deskripsi & Ciri-Ciri Khusus
                </h3>
                <p class="text-sm text-slate-700 leading-relaxed">
                    {{ $barang['deskripsi'] ?? 'Tidak ada catatan deskripsi khusus.' }}
                </p>
            </div>
        </div>

        <!-- Footer Actions -->
        <div class="px-6 py-4 bg-slate-50 border-t border-slate-200 flex items-center justify-between">
            <span class="text-xs text-slate-500">
                Data disimpan dalam session file (<code>storage/framework/sessions</code>)
            </span>
            <a href="{{ route('barang.index') }}" class="px-4 py-2 bg-slate-800 hover:bg-slate-900 text-white rounded-lg text-xs font-bold transition">
                &larr; Kembali ke Daftar
            </a>
        </div>
    </div>

</div>
@endsection
