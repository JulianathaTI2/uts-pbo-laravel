@extends('layouts.app')

@section('title', 'Ubah Data Barang ' . $barang['kode'] . ' - UTS PBO')

@section('content')
<div class="max-w-3xl mx-auto space-y-6">

    <!-- Header Navigation Back -->
    <div class="flex items-center justify-between">
        <a href="{{ route('barang.index') }}" class="inline-flex items-center gap-2 text-sm font-semibold text-slate-600 hover:text-blue-600 transition">
            <i class="fa-solid fa-arrow-left"></i> Kembali ke Daftar Barang
        </a>
        <span class="text-xs font-mono bg-amber-100 text-amber-800 px-3 py-1 rounded-full font-semibold">
            Route: barang.edit &rarr; barang.update [PUT/PATCH]
        </span>
    </div>

    <!-- Form Card -->
    <div class="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
        <div class="px-6 py-4 border-b border-slate-200 bg-amber-50/50 flex items-center justify-between">
            <div>
                <h1 class="text-lg font-bold text-slate-800">Ubah Data Barang (Edit Mode)</h1>
                <p class="text-xs text-slate-500 mt-0.5">Memperbarui atribut barang pada session file storage.</p>
            </div>
            <div class="w-10 h-10 rounded-full bg-amber-100 text-amber-700 flex items-center justify-center font-bold">
                <i class="fa-solid fa-pen-to-square text-lg"></i>
            </div>
        </div>

        <form action="{{ route('barang.update', $barang['kode']) }}" method="POST" class="p-6 space-y-5">
            @csrf
            @method('PUT')

            <!-- Baris 1: Kode Barang (Readonly) & Status -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                    <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                        Kode Barang (Kunci Identifikasi)
                    </label>
                    <input type="text" value="{{ $barang['kode'] }}" 
                           class="w-full px-3.5 py-2.5 text-sm font-mono border border-slate-300 rounded-lg bg-slate-100 font-bold text-slate-600 cursor-not-allowed" 
                           readonly>
                    <p class="text-[11px] text-slate-400 mt-1">Kode barang bersifat tetap (immutable key).</p>
                </div>

                <div>
                    <label for="status" class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                        Status Laporan <span class="text-rose-500">*</span>
                    </label>
                    <select name="status" id="status" 
                            class="w-full px-3.5 py-2.5 text-sm border @error('status') border-rose-500 @else border-slate-300 @enderror rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none"
                            required>
                        <option value="Hilang" {{ old('status', $barang['status']) === 'Hilang' ? 'selected' : '' }}>Hilang (Dilaporkan Pemilik)</option>
                        <option value="Ditemukan" {{ old('status', $barang['status']) === 'Ditemukan' ? 'selected' : '' }}>Ditemukan (Ditemukan Penemu)</option>
                        <option value="Diklaim" {{ old('status', $barang['status']) === 'Diklaim' ? 'selected' : '' }}>Diklaim / Selesai</option>
                    </select>
                    @error('status')
                        <p class="text-xs text-rose-600 mt-1">{{ $message }}</p>
                    @enderror
                </div>
            </div>

            <!-- Baris 2: Nama Barang -->
            <div>
                <label for="nama" class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                    Nama Barang <span class="text-rose-500">*</span>
                </label>
                <input type="text" name="nama" id="nama" 
                       value="{{ old('nama', $barang['nama']) }}" 
                       class="w-full px-3.5 py-2.5 text-sm border @error('nama') border-rose-500 ring-1 ring-rose-500 @else border-slate-300 @enderror rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none"
                       required>
                @error('nama')
                    <p class="text-xs text-rose-600 mt-1">{{ $message }}</p>
                @enderror
            </div>

            <!-- Baris 3: Kategori & Jumlah -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="md:col-span-2">
                    <label for="kategori" class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                        Kategori <span class="text-rose-500">*</span>
                    </label>
                    <select name="kategori" id="kategori" 
                            class="w-full px-3.5 py-2.5 text-sm border @error('kategori') border-rose-500 @else border-slate-300 @enderror rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none"
                            required>
                        @foreach($kategoriList as $kat)
                            <option value="{{ $kat }}" {{ old('kategori', $barang['kategori']) === $kat ? 'selected' : '' }}>{{ $kat }}</option>
                        @endforeach
                    </select>
                    @error('kategori')
                        <p class="text-xs text-rose-600 mt-1">{{ $message }}</p>
                    @enderror
                </div>

                <div>
                    <label for="jumlah" class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                        Jumlah <span class="text-rose-500">*</span>
                    </label>
                    <input type="number" name="jumlah" id="jumlah" min="1" 
                           value="{{ old('jumlah', $barang['jumlah']) }}" 
                           class="w-full px-3.5 py-2.5 text-sm border @error('jumlah') border-rose-500 @else border-slate-300 @enderror rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none text-center font-bold"
                           required>
                    @error('jumlah')
                        <p class="text-xs text-rose-600 mt-1">{{ $message }}</p>
                    @enderror
                </div>
            </div>

            <!-- Baris 4: Lokasi & Kondisi -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                    <label for="lokasi" class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                        Lokasi Terakhir / Ditemukan <span class="text-rose-500">*</span>
                    </label>
                    <input type="text" name="lokasi" id="lokasi" 
                           value="{{ old('lokasi', $barang['lokasi']) }}" 
                           class="w-full px-3.5 py-2.5 text-sm border @error('lokasi') border-rose-500 @else border-slate-300 @enderror rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none"
                           required>
                    @error('lokasi')
                        <p class="text-xs text-rose-600 mt-1">{{ $message }}</p>
                    @enderror
                </div>

                <div>
                    <label for="kondisi" class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                        Kondisi Fisik <span class="text-rose-500">*</span>
                    </label>
                    <select name="kondisi" id="kondisi" 
                            class="w-full px-3.5 py-2.5 text-sm border @error('kondisi') border-rose-500 @else border-slate-300 @enderror rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none"
                            required>
                        @foreach($kondisiList as $kon)
                            <option value="{{ $kon }}" {{ old('kondisi', $barang['kondisi']) === $kon ? 'selected' : '' }}>{{ $kon }}</option>
                        @endforeach
                    </select>
                    @error('kondisi')
                        <p class="text-xs text-rose-600 mt-1">{{ $message }}</p>
                    @enderror
                </div>
            </div>

            <!-- Baris 5: Tanggal & Pelapor -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                    <label for="tgl_lapor" class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                        Tanggal Lapor <span class="text-rose-500">*</span>
                    </label>
                    <input type="date" name="tgl_lapor" id="tgl_lapor" 
                           value="{{ old('tgl_lapor', $barang['tgl_lapor']) }}" 
                           class="w-full px-3.5 py-2.5 text-sm border @error('tgl_lapor') border-rose-500 @else border-slate-300 @enderror rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none"
                           required>
                    @error('tgl_lapor')
                        <p class="text-xs text-rose-600 mt-1">{{ $message }}</p>
                    @enderror
                </div>

                <div>
                    <label for="pelapor" class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                        Nama / Identitas Pelapor
                    </label>
                    <input type="text" name="pelapor" id="pelapor" 
                           value="{{ old('pelapor', $barang['pelapor']) }}" 
                           class="w-full px-3.5 py-2.5 text-sm border @error('pelapor') border-rose-500 @else border-slate-300 @enderror rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none">
                    @error('pelapor')
                        <p class="text-xs text-rose-600 mt-1">{{ $message }}</p>
                    @enderror
                </div>
            </div>

            <!-- Baris 6: Deskripsi Ciri Khusus -->
            <div>
                <label for="deskripsi" class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                    Deskripsi & Ciri-Ciri Khusus
                </label>
                <textarea name="deskripsi" id="deskripsi" rows="3" 
                          class="w-full px-3.5 py-2.5 text-sm border @error('deskripsi') border-rose-500 @else border-slate-300 @enderror rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none">{{ old('deskripsi', $barang['deskripsi']) }}</textarea>
                @error('deskripsi')
                    <p class="text-xs text-rose-600 mt-1">{{ $message }}</p>
                @enderror
            </div>

            <!-- Form Actions -->
            <div class="pt-4 border-t border-slate-200 flex items-center justify-end gap-3">
                <a href="{{ route('barang.index') }}" class="px-5 py-2.5 rounded-lg border border-slate-300 text-slate-700 hover:bg-slate-50 text-sm font-semibold transition">
                    Batal
                </a>
                <button type="submit" class="inline-flex items-center gap-2 px-6 py-2.5 rounded-lg bg-amber-600 hover:bg-amber-700 text-white text-sm font-bold shadow-md hover:shadow-lg transition">
                    <i class="fa-solid fa-check"></i> Simpan Perubahan
                </button>
            </div>
        </form>
    </div>

</div>
@endsection
