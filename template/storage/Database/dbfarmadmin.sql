-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 15 Okt 2023 pada 22.17
-- Versi server: 10.4.28-MariaDB
-- Versi PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbfarmadmin`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `aktivitas_lahan`
--

CREATE TABLE `aktivitas_lahan` (
  `id` int(11) NOT NULL,
  `lahan_id` int(11) DEFAULT NULL,
  `jenis_aktivitas` varchar(255) NOT NULL,
  `tanggal` date DEFAULT NULL,
  `jenis_aktivitas_id` int(11) NOT NULL,
  `catatan` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `aktivitas_lahan`
--

INSERT INTO `aktivitas_lahan` (`id`, `lahan_id`, `jenis_aktivitas`, `tanggal`, `jenis_aktivitas_id`, `catatan`) VALUES
(1, 1, 'Penyiapan Lahan', '2023-08-02', 1, 'Pembersihan lahan'),
(2, 1, 'Penyiapan Lahan', '2023-08-05', 1, 'Pembajakan tanah'),
(3, 1, 'Penanaman', '2023-08-10', 2, 'Penanaman padi'),
(4, 1, 'Pemupukan', '2023-09-01', 3, 'Pemupukan pertama'),
(5, 1, 'Pemupukan', '2023-09-15', 3, 'Pemupukan kedua'),
(6, 1, 'Pemanenan', '2023-10-15', 4, 'Panen padi'),
(7, 1, 'Pengendalian Hama', '2023-09-25', 5, 'Pengendalian hama ulat padi'),
(8, 1, 'Pengolahan Tanah', '2023-08-01', 6, 'Pengolahan tanah sebelum penanaman'),
(9, 1, 'Penyiraman', '2023-08-12', 7, 'Penyiraman pertama'),
(10, 1, 'Penyiraman', '2023-09-05', 7, 'Penyiraman selama pertumbuhan padi'),
(11, 2, 'Penyiapan Lahan', '2023-08-10', 1, 'Pembersihan lahan'),
(12, 2, 'Penyiapan Lahan', '2023-08-14', 1, 'Pembajakan tanah'),
(13, 2, 'Penanaman', '2023-08-20', 2, 'Penanaman jagung'),
(14, 2, 'Pemupukan', '2023-09-05', 3, 'Pemupukan pertama'),
(15, 2, 'Pemupukan', '2023-09-20', 3, 'Pemupukan kedua'),
(16, 2, 'Pemanenan', '2023-10-16', 4, 'Panen jagung'),
(17, 2, 'Pengendalian Hama', '2023-09-15', 5, 'Pengendalian hama ulat jagung'),
(18, 2, 'Pengolahan Tanah', '2023-08-02', 6, 'Pengolahan tanah sebelum penanaman'),
(19, 2, 'Penyiraman', '2023-08-15', 7, 'Penyiraman pertama'),
(20, 2, 'Penyiraman', '2023-09-08', 7, 'Penyiraman selama pertumbuhan jagung'),
(21, 3, 'Penyiapan Lahan', '2023-08-03', 1, 'Pembersihan lahan'),
(22, 3, 'Penyiapan Lahan', '2023-08-06', 1, 'Pembajakan tanah'),
(23, 3, 'Penanaman', '2023-08-12', 2, 'Penanaman tomat'),
(24, 3, 'Pemupukan', '2023-09-02', 3, 'Pemupukan pertama'),
(25, 3, 'Pemupukan', '2023-09-16', 3, 'Pemupukan kedua'),
(26, 3, 'Pemanenan', '2023-10-17', 4, 'Panen tomat'),
(27, 3, 'Pengendalian Hama', '2023-09-26', 5, 'Pengendalian hama ulat tomat'),
(28, 3, 'Pengolahan Tanah', '2023-08-03', 6, 'Pengolahan tanah sebelum penanaman'),
(29, 3, 'Penyiraman', '2023-08-13', 7, 'Penyiraman pertama'),
(30, 3, 'Penyiraman', '2023-09-06', 7, 'Penyiraman selama pertumbuhan tomat'),
(31, 4, 'Penyiapan Lahan', '2023-08-01', 1, 'Pembersihan lahan'),
(32, 4, 'Penyiapan Lahan', '2023-08-03', 1, 'Pembajakan tanah'),
(33, 4, 'Penanaman', '2023-08-08', 2, 'Penanaman kentang'),
(34, 4, 'Pemupukan', '2023-09-01', 3, 'Pemupukan pertama'),
(35, 4, 'Pemupukan', '2023-09-15', 3, 'Pemupukan kedua'),
(36, 4, 'Pemanenan', '2023-10-18', 4, 'Panen kentang'),
(37, 4, 'Pengendalian Hama', '2023-09-24', 5, 'Pengendalian hama ulat kentang'),
(38, 4, 'Pengolahan Tanah', '2023-08-01', 6, 'Pengolahan tanah sebelum penanaman'),
(39, 4, 'Penyiraman', '2023-08-10', 7, 'Penyiraman pertama'),
(40, 4, 'Penyiraman', '2023-09-05', 7, 'Penyiraman selama pertumbuhan kentang'),
(41, 5, 'Penyiapan Lahan', '2023-08-02', 1, 'Pembersihan lahan'),
(42, 5, 'Penyiapan Lahan', '2023-08-05', 1, 'Pembajakan tanah'),
(43, 5, 'Penanaman', '2023-08-10', 2, 'Penanaman kentang'),
(44, 5, 'Pemupukan', '2023-09-01', 3, 'Pemupukan pertama'),
(45, 5, 'Pemupukan', '2023-09-15', 3, 'Pemupukan kedua'),
(46, 5, 'Pengendalian Hama', '2023-09-25', 5, 'Pengendalian hama ulat kentang'),
(47, 5, 'Pengolahan Tanah', '2023-08-01', 6, 'Pengolahan tanah sebelum penanaman'),
(48, 5, 'Penyiraman', '2023-08-12', 7, 'Penyiraman pertama'),
(49, 5, 'Penyiraman', '2023-09-05', 7, 'Penyiraman selama pertumbuhan kentang'),
(50, 6, 'Penyiapan Lahan', '2023-08-03', 1, 'Pembersihan lahan'),
(51, 6, 'Penyiapan Lahan', '2023-08-06', 1, 'Pembajakan tanah'),
(52, 6, 'Penanaman', '2023-08-12', 2, 'Penanaman tomat'),
(53, 6, 'Pemupukan', '2023-09-02', 3, 'Pemupukan pertama'),
(54, 6, 'Pemupukan', '2023-09-16', 3, 'Pemupukan kedua'),
(55, 6, 'Pengendalian Hama', '2023-09-26', 5, 'Pengendalian hama ulat tomat'),
(56, 6, 'Pengolahan Tanah', '2023-08-03', 6, 'Pengolahan tanah sebelum penanaman'),
(57, 6, 'Penyiraman', '2023-08-13', 7, 'Penyiraman pertama'),
(58, 6, 'Penyiraman', '2023-09-06', 7, 'Penyiraman selama pertumbuhan tomat');

-- --------------------------------------------------------

--
-- Struktur dari tabel `hasil_panen`
--

CREATE TABLE `hasil_panen` (
  `id` int(11) NOT NULL,
  `lahan_id` int(11) DEFAULT NULL,
  `jenis_tanaman` varchar(255) NOT NULL,
  `jumlah_panen` int(11) DEFAULT NULL,
  `tanggal_panen` date DEFAULT NULL,
  `tanggal_mulai_tanam` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `hasil_panen`
--

INSERT INTO `hasil_panen` (`id`, `lahan_id`, `jenis_tanaman`, `jumlah_panen`, `tanggal_panen`, `tanggal_mulai_tanam`) VALUES
(1, 1, 'Padi', 5000, '2023-10-15', '2023-08-01'),
(2, 2, 'Jagung', 3500, '2023-10-16', '2023-08-15'),
(3, 3, 'Tomat', 1200, '2023-10-17', '2023-09-01'),
(4, 1, 'Padi', 5200, '2023-10-18', '2023-08-01'),
(5, 2, 'Jagung', 3600, '2023-10-19', '2023-08-15'),
(6, 3, 'Tomat', 1300, '2023-10-20', '2023-09-01');

-- --------------------------------------------------------

--
-- Struktur dari tabel `jenis_aktivitas_lahan`
--

CREATE TABLE `jenis_aktivitas_lahan` (
  `id` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `deskripsi` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `jenis_aktivitas_lahan`
--

INSERT INTO `jenis_aktivitas_lahan` (`id`, `nama`, `deskripsi`) VALUES
(1, 'Penanaman', 'Aktivitas menanam tanaman pertanian.'),
(2, 'Penyiraman', 'Aktivitas penyiraman tanaman.'),
(3, 'Pemupukan', 'Aktivitas memberikan pupuk pada tanaman.'),
(4, 'Pembersihan', 'Aktivitas membersihkan lahan dari gulma dan sampah.'),
(5, 'Pemangkasan', 'Aktivitas pemangkasan tanaman.'),
(6, 'Pemanenan', 'Aktivitas memanen tanaman yang sudah matang.'),
(7, 'Pengendalian Hama', 'Aktivitas mengendalikan hama dan penyakit tanaman.'),
(8, 'Pengolahan Tanah', 'Aktivitas pengolahan tanah untuk persiapan tanam.');

-- --------------------------------------------------------

--
-- Struktur dari tabel `jenis_material`
--

CREATE TABLE `jenis_material` (
  `id` int(11) NOT NULL,
  `jenis` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `jenis_material`
--

INSERT INTO `jenis_material` (`id`, `jenis`) VALUES
(1, 'Pupuk Cair'),
(2, 'Benih Padi'),
(3, 'Herbisida'),
(4, 'Pupuk Padat'),
(5, 'Benih Jagung');

-- --------------------------------------------------------

--
-- Struktur dari tabel `lahan`
--

CREATE TABLE `lahan` (
  `id` int(11) NOT NULL,
  `nama_lahan` varchar(255) NOT NULL,
  `luas` double NOT NULL,
  `lokasi` varchar(255) DEFAULT NULL,
  `pemilik_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `lahan`
--

INSERT INTO `lahan` (`id`, `nama_lahan`, `luas`, `lokasi`, `pemilik_id`) VALUES
(1, 'Lahan Pertanian A', 10, 'Jl. Contoh No. 123', 1),
(2, 'Lahan Pertanian B', 15, 'Jl. Contoh No. 456', 2),
(3, 'Lahan Pertanian C', 8, 'Jl. Contoh No. 789', 3),
(4, 'Lahan Pertanian D', 20, 'Jl. Contoh No. 1011', 1),
(5, 'Lahan Pertanian E', 12, 'Jl. Contoh No. 1213', 2),
(6, 'Lahan Pertanian F', 6, 'Jl. Contoh No. 1415', 3);

-- --------------------------------------------------------

--
-- Struktur dari tabel `material`
--

CREATE TABLE `material` (
  `id` int(11) NOT NULL,
  `nama_material` varchar(255) NOT NULL,
  `deskripsi` text DEFAULT NULL,
  `harga` double NOT NULL,
  `satuan` varchar(50) DEFAULT NULL,
  `tanggal` date DEFAULT NULL,
  `jenis_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `material`
--

INSERT INTO `material` (`id`, `nama_material`, `deskripsi`, `harga`, `satuan`, `tanggal`, `jenis_id`) VALUES
(1, 'Pupuk NPK', 'Pupuk padat untuk meningkatkan pertumbuhan tanaman.', 10.5, 'Kg', '2023-10-15', 1),
(2, 'Bibit Padi', 'Bibit padi unggul untuk ditanam di lahan sawah.', 5.75, 'Biji', '2023-10-15', 2),
(3, 'Insektisida', 'Pestisida untuk mengendalikan serangga dan hama pada tanaman.', 15.25, 'L', '2023-10-15', 3),
(4, 'Pupuk Padat', 'Pupuk padat organik untuk meningkatkan kesuburan tanah.', 8.99, 'Kg', '2023-10-15', 4),
(5, 'Benih Jagung', 'Benih jagung berkualitas tinggi untuk ditanam di lahan pertanian.', 3.25, 'Biji', '2023-10-15', 5),
(6, 'Pestisida', 'Bahan kimia untuk melindungi tanaman dari serangga dan penyakit.', 12.75, 'L', '2023-10-15', 3),
(7, 'Bibit Tomat', 'Bibit tomat unggul untuk kebun dan pertanian.', 6.5, 'Biji', '2023-10-15', 2),
(8, 'Pupuk Organik', 'Pupuk alami untuk meningkatkan kesuburan tanah.', 7.99, 'Kg', '2023-10-15', 1),
(9, 'Benih Cabai', 'Benih cabai pedas untuk ditanam di kebun.', 4.25, 'Biji', '2023-10-15', 5),
(10, 'Herbisida', 'Bahan kimia untuk mengendalikan pertumbuhan gulma pada lahan pertanian.', 9.85, 'L', '2023-10-15', 3),
(11, 'Pupuk Cair', 'Pupuk cair untuk penyiraman tanaman.', 6.99, 'L', '2023-10-15', 1),
(12, 'Benih Gandum', 'Benih gandum untuk lahan pertanian.', 5.25, 'Biji', '2023-10-15', 2),
(13, 'Insektisida', 'Pestisida untuk melindungi tanaman dari serangga.', 13.75, 'L', '2023-10-15', 3),
(14, 'Pupuk Organik', 'Pupuk alami untuk kebun dan pertanian organik.', 11.99, 'Kg', '2023-10-15', 1),
(15, 'Benih Kentang', 'Benih kentang unggul untuk pertanian.', 5.5, 'Biji', '2023-10-15', 2),
(16, 'Herbisida', 'Herbisida untuk mengendalikan pertumbuhan gulma.', 9.5, 'L', '2023-10-15', 3),
(17, 'Pupuk Cair', 'Pupuk cair untuk penyiraman tanaman hias.', 7.99, 'L', '2023-10-15', 1),
(18, 'Benih Jeruk', 'Benih jeruk berkualitas untuk pertanian.', 6.25, 'Biji', '2023-10-15', 2),
(19, 'Pestisida', 'Bahan kimia untuk melindungi tanaman dari hama.', 14.75, 'L', '2023-10-15', 3);

-- --------------------------------------------------------

--
-- Struktur dari tabel `pengeluaran`
--

CREATE TABLE `pengeluaran` (
  `id` int(11) NOT NULL,
  `lahan_id` int(11) DEFAULT NULL,
  `biaya` double NOT NULL,
  `tanggal` date DEFAULT NULL,
  `keterangan` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `pengeluaran`
--

INSERT INTO `pengeluaran` (`id`, `lahan_id`, `biaya`, `tanggal`, `keterangan`) VALUES
(1, 1, 150, '2023-08-05', 'Pembelian pupuk'),
(2, 1, 80, '2023-08-15', 'Pengeluaran untuk penyewaan alat pertanian'),
(3, 1, 200, '2023-09-02', 'Pengeluaran untuk bahan pestisida'),
(4, 1, 100, '2023-09-12', 'Pengeluaran untuk pembayaran pekerja'),
(5, 1, 50, '2023-10-10', 'Pengeluaran untuk pemeliharaan lahan'),
(6, 2, 120, '2023-08-12', 'Pembelian pupuk'),
(7, 2, 70, '2023-08-22', 'Pengeluaran untuk penyewaan alat pertanian'),
(8, 2, 180, '2023-09-05', 'Pengeluaran untuk bahan pestisida'),
(9, 2, 90, '2023-09-15', 'Pengeluaran untuk pembayaran pekerja'),
(10, 2, 60, '2023-10-12', 'Pengeluaran untuk pemeliharaan lahan'),
(11, 3, 130, '2023-08-04', 'Pembelian pupuk'),
(12, 3, 75, '2023-08-14', 'Pengeluaran untuk penyewaan alat pertanian'),
(13, 3, 190, '2023-09-03', 'Pengeluaran untuk bahan pestisida'),
(14, 3, 95, '2023-09-13', 'Pengeluaran untuk pembayaran pekerja'),
(15, 3, 55, '2023-10-11', 'Pengeluaran untuk pemeliharaan lahan'),
(16, 4, 140, '2023-08-02', 'Pembelian pupuk'),
(17, 4, 85, '2023-08-16', 'Pengeluaran untuk penyewaan alat pertanian'),
(18, 4, 210, '2023-09-04', 'Pengeluaran untuk bahan pestisida'),
(19, 4, 110, '2023-09-14', 'Pengeluaran untuk pembayaran pekerja'),
(20, 4, 65, '2023-10-13', 'Pengeluaran untuk pemeliharaan lahan'),
(21, 5, 150, '2023-08-05', 'Pembelian pupuk'),
(22, 5, 80, '2023-08-15', 'Pengeluaran untuk penyewaan alat pertanian'),
(23, 5, 200, '2023-09-02', 'Pengeluaran untuk bahan pestisida'),
(24, 5, 100, '2023-09-12', 'Pengeluaran untuk pembayaran pekerja'),
(25, 5, 50, '2023-10-10', 'Pengeluaran untuk pemeliharaan lahan'),
(26, 6, 120, '2023-08-12', 'Pembelian pupuk'),
(27, 6, 70, '2023-08-22', 'Pengeluaran untuk penyewaan alat pertanian'),
(28, 6, 180, '2023-09-05', 'Pengeluaran untuk bahan pestisida'),
(29, 6, 90, '2023-09-15', 'Pengeluaran untuk pembayaran pekerja'),
(30, 6, 60, '2023-10-12', 'Pengeluaran untuk pemeliharaan lahan'),
(31, 1, 240, '2022-03-01', 'Pengeluaran 1'),
(32, 1, 583, '2022-09-01', 'Pengeluaran 2'),
(33, 1, 909, '2022-05-01', 'Pengeluaran 3'),
(34, 1, 14, '2022-07-01', 'Pengeluaran 4'),
(35, 1, 87, '2022-10-01', 'Pengeluaran 5'),
(36, 1, 526, '2022-05-01', 'Pengeluaran 6'),
(37, 1, 205, '2022-05-01', 'Pengeluaran 7'),
(38, 1, 152, '2021-12-01', 'Pengeluaran 8'),
(39, 1, 48, '2022-05-01', 'Pengeluaran 9'),
(40, 1, 537, '2021-11-01', 'Pengeluaran 10'),
(41, 1, 765, '2021-09-01', 'Pengeluaran 11'),
(42, 1, 698, '2021-07-01', 'Pengeluaran 12'),
(43, 1, 381, '2021-01-01', 'Pengeluaran 13'),
(44, 1, 943, '2022-03-01', 'Pengeluaran 14'),
(45, 1, 478, '2021-09-01', 'Pengeluaran 15'),
(46, 1, 592, '2022-05-01', 'Pengeluaran 16'),
(47, 1, 951, '2021-12-01', 'Pengeluaran 17'),
(48, 1, 732, '2021-03-01', 'Pengeluaran 18'),
(49, 1, 347, '2021-09-01', 'Pengeluaran 19'),
(50, 1, 5, '2022-06-01', 'Pengeluaran 20'),
(51, 1, 960, '2021-10-01', 'Pengeluaran 21'),
(52, 1, 187, '2022-04-01', 'Pengeluaran 22'),
(53, 1, 908, '2021-11-01', 'Pengeluaran 23'),
(54, 1, 567, '2021-11-01', 'Pengeluaran 24'),
(55, 1, 603, '2022-02-01', 'Pengeluaran 25'),
(56, 1, 352, '2022-07-01', 'Pengeluaran 26'),
(57, 1, 262, '2022-04-01', 'Pengeluaran 27'),
(58, 1, 808, '2022-08-01', 'Pengeluaran 28'),
(59, 1, 994, '2021-07-01', 'Pengeluaran 29'),
(60, 1, 607, '2021-02-01', 'Pengeluaran 30'),
(62, 2, 512, '2021-01-01', 'Pengeluaran 1'),
(63, 2, 485, '2021-09-01', 'Pengeluaran 2'),
(64, 2, 590, '2022-04-01', 'Pengeluaran 3'),
(65, 2, 845, '2021-02-01', 'Pengeluaran 4'),
(66, 2, 733, '2021-12-01', 'Pengeluaran 5'),
(67, 2, 320, '2021-02-01', 'Pengeluaran 6'),
(68, 2, 487, '2021-04-01', 'Pengeluaran 7'),
(69, 2, 367, '2021-08-01', 'Pengeluaran 8'),
(70, 2, 576, '2022-08-01', 'Pengeluaran 9'),
(71, 2, 640, '2022-01-01', 'Pengeluaran 10'),
(72, 2, 965, '2021-03-01', 'Pengeluaran 11'),
(73, 2, 580, '2022-02-01', 'Pengeluaran 12'),
(74, 2, 328, '2022-06-01', 'Pengeluaran 13'),
(75, 2, 7, '2022-03-01', 'Pengeluaran 14'),
(76, 2, 186, '2021-01-01', 'Pengeluaran 15'),
(77, 2, 453, '2021-06-01', 'Pengeluaran 16'),
(78, 2, 941, '2022-09-01', 'Pengeluaran 17'),
(79, 2, 798, '2021-05-01', 'Pengeluaran 18'),
(80, 2, 686, '2022-06-01', 'Pengeluaran 19'),
(81, 2, 848, '2022-08-01', 'Pengeluaran 20'),
(82, 2, 939, '2021-01-01', 'Pengeluaran 21'),
(83, 2, 208, '2021-01-01', 'Pengeluaran 22'),
(84, 2, 490, '2021-09-01', 'Pengeluaran 23'),
(85, 2, 443, '2021-02-01', 'Pengeluaran 24'),
(86, 2, 996, '2022-06-01', 'Pengeluaran 25'),
(87, 2, 935, '2021-08-01', 'Pengeluaran 26'),
(88, 2, 803, '2021-02-01', 'Pengeluaran 27'),
(89, 2, 833, '2021-01-01', 'Pengeluaran 28'),
(90, 2, 590, '2022-08-01', 'Pengeluaran 29'),
(91, 2, 704, '2022-07-01', 'Pengeluaran 30'),
(93, 3, 158, '2022-02-01', 'Pengeluaran 1'),
(94, 3, 706, '2022-02-01', 'Pengeluaran 2'),
(95, 3, 992, '2021-03-01', 'Pengeluaran 3'),
(96, 3, 492, '2021-04-01', 'Pengeluaran 4'),
(97, 3, 406, '2021-11-01', 'Pengeluaran 5'),
(98, 3, 281, '2022-08-01', 'Pengeluaran 6'),
(99, 3, 680, '2022-04-01', 'Pengeluaran 7'),
(100, 3, 388, '2022-08-01', 'Pengeluaran 8'),
(101, 3, 249, '2022-02-01', 'Pengeluaran 9'),
(102, 3, 228, '2021-08-01', 'Pengeluaran 10'),
(103, 3, 95, '2021-09-01', 'Pengeluaran 11'),
(104, 3, 739, '2021-11-01', 'Pengeluaran 12'),
(105, 3, 185, '2021-11-01', 'Pengeluaran 13'),
(106, 3, 867, '2022-08-01', 'Pengeluaran 14'),
(107, 3, 805, '2021-09-01', 'Pengeluaran 15'),
(108, 3, 484, '2021-07-01', 'Pengeluaran 16'),
(109, 3, 944, '2022-08-01', 'Pengeluaran 17'),
(110, 3, 571, '2021-05-01', 'Pengeluaran 18'),
(111, 3, 345, '2021-02-01', 'Pengeluaran 19'),
(112, 3, 416, '2022-06-01', 'Pengeluaran 20'),
(113, 3, 785, '2021-12-01', 'Pengeluaran 21'),
(114, 3, 168, '2021-08-01', 'Pengeluaran 22'),
(115, 3, 123, '2022-03-01', 'Pengeluaran 23'),
(116, 3, 829, '2021-05-01', 'Pengeluaran 24'),
(117, 3, 633, '2021-11-01', 'Pengeluaran 25'),
(118, 3, 555, '2021-07-01', 'Pengeluaran 26'),
(119, 3, 841, '2021-07-01', 'Pengeluaran 27'),
(120, 3, 980, '2022-10-01', 'Pengeluaran 28'),
(121, 3, 39, '2021-05-01', 'Pengeluaran 29'),
(122, 3, 923, '2022-10-01', 'Pengeluaran 30');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pengguna`
--

CREATE TABLE `pengguna` (
  `id` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  `tanggal_lahir` date DEFAULT NULL,
  `jenis_kelamin` enum('Laki-laki','Perempuan') DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `telepon` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `pengguna`
--

INSERT INTO `pengguna` (`id`, `nama`, `alamat`, `tanggal_lahir`, `jenis_kelamin`, `email`, `telepon`) VALUES
(1, 'John Doe', 'Jl. Contoh No. 123', '1980-05-15', 'Laki-laki', 'johndoe@email.com', '123-456-7890'),
(2, 'Jane Smith', 'Jl. Contoh No. 456', '1992-08-25', 'Perempuan', 'janesmith@email.com', '987-654-3210'),
(3, 'Alice Johnson', 'Jl. Contoh No. 789', '1985-12-10', 'Perempuan', 'alicejohnson@email.com', '555-123-4567');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `aktivitas_lahan`
--
ALTER TABLE `aktivitas_lahan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `lahan_id` (`lahan_id`),
  ADD KEY `jenis_aktivitas_id` (`jenis_aktivitas_id`);

--
-- Indeks untuk tabel `hasil_panen`
--
ALTER TABLE `hasil_panen`
  ADD PRIMARY KEY (`id`),
  ADD KEY `lahan_id` (`lahan_id`);

--
-- Indeks untuk tabel `jenis_aktivitas_lahan`
--
ALTER TABLE `jenis_aktivitas_lahan`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `jenis_material`
--
ALTER TABLE `jenis_material`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `lahan`
--
ALTER TABLE `lahan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pemilik_id` (`pemilik_id`);

--
-- Indeks untuk tabel `material`
--
ALTER TABLE `material`
  ADD PRIMARY KEY (`id`),
  ADD KEY `jenis_id` (`jenis_id`);

--
-- Indeks untuk tabel `pengeluaran`
--
ALTER TABLE `pengeluaran`
  ADD PRIMARY KEY (`id`),
  ADD KEY `lahan_id` (`lahan_id`);

--
-- Indeks untuk tabel `pengguna`
--
ALTER TABLE `pengguna`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `aktivitas_lahan`
--
ALTER TABLE `aktivitas_lahan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- AUTO_INCREMENT untuk tabel `hasil_panen`
--
ALTER TABLE `hasil_panen`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `jenis_aktivitas_lahan`
--
ALTER TABLE `jenis_aktivitas_lahan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT untuk tabel `jenis_material`
--
ALTER TABLE `jenis_material`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `lahan`
--
ALTER TABLE `lahan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `material`
--
ALTER TABLE `material`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT untuk tabel `pengeluaran`
--
ALTER TABLE `pengeluaran`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=123;

--
-- AUTO_INCREMENT untuk tabel `pengguna`
--
ALTER TABLE `pengguna`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `aktivitas_lahan`
--
ALTER TABLE `aktivitas_lahan`
  ADD CONSTRAINT `aktivitas_lahan_ibfk_1` FOREIGN KEY (`lahan_id`) REFERENCES `lahan` (`id`),
  ADD CONSTRAINT `aktivitas_lahan_ibfk_2` FOREIGN KEY (`jenis_aktivitas_id`) REFERENCES `jenis_aktivitas_lahan` (`id`);

--
-- Ketidakleluasaan untuk tabel `hasil_panen`
--
ALTER TABLE `hasil_panen`
  ADD CONSTRAINT `hasil_panen_ibfk_1` FOREIGN KEY (`lahan_id`) REFERENCES `lahan` (`id`);

--
-- Ketidakleluasaan untuk tabel `lahan`
--
ALTER TABLE `lahan`
  ADD CONSTRAINT `lahan_ibfk_1` FOREIGN KEY (`pemilik_id`) REFERENCES `pengguna` (`id`);

--
-- Ketidakleluasaan untuk tabel `material`
--
ALTER TABLE `material`
  ADD CONSTRAINT `material_ibfk_1` FOREIGN KEY (`jenis_id`) REFERENCES `jenis_material` (`id`);

--
-- Ketidakleluasaan untuk tabel `pengeluaran`
--
ALTER TABLE `pengeluaran`
  ADD CONSTRAINT `pengeluaran_ibfk_1` FOREIGN KEY (`lahan_id`) REFERENCES `lahan` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
