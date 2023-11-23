-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: sql12.freemysqlhosting.net
-- Generation Time: Nov 22, 2023 at 08:57 AM
-- Server version: 5.5.62-0ubuntu0.14.04.1
-- PHP Version: 7.0.33-0ubuntu0.16.04.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sql12664157`
--

-- --------------------------------------------------------

--
-- Table structure for table `Aktivitas_Lahan`
--

CREATE TABLE `Aktivitas_Lahan` (
  `id` int(11) NOT NULL,
  `lahan_id` int(11) DEFAULT NULL,
  `pengeluaran_id` int(11) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `id_panen` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Aktivitas_Lahan`
--

INSERT INTO `Aktivitas_Lahan` (`id`, `lahan_id`, `pengeluaran_id`, `status`, `id_panen`) VALUES
(41, 6, 1, 'Belum Selesai', NULL),
(42, 7, 2, 'Belum Selesai', NULL),
(43, 8, 3, 'Belum Selesai', NULL),
(44, 9, 4, 'Belum Selesai', NULL),
(45, 10, 5, 'Belum Selesai', NULL),
(46, 6, 6, 'Belum Selesai', NULL),
(47, 7, 7, 'Belum Selesai', NULL),
(48, 8, 8, 'Belum Selesai', NULL),
(49, 9, 9, 'Belum Selesai', NULL),
(50, 10, 10, 'Belum Selesai', NULL),
(51, 6, 11, 'Belum Selesai', NULL),
(52, 7, 12, 'Belum Selesai', NULL),
(53, 8, 13, 'Belum Selesai', NULL),
(54, 9, 14, 'Belum Selesai', NULL),
(55, 10, 15, 'Belum Selesai', NULL),
(56, 6, 16, 'Belum Selesai', NULL),
(57, 7, 17, 'Belum Selesai', NULL),
(58, 8, 18, 'Belum Selesai', NULL),
(59, 9, 19, 'Belum Selesai', NULL),
(60, 10, 20, 'Selesai', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `Hasil_Panen`
--

CREATE TABLE `Hasil_Panen` (
  `id` int(11) NOT NULL,
  `lahan_id` int(11) DEFAULT NULL,
  `jenis_tanaman` varchar(255) DEFAULT NULL,
  `jumlah_hasil_panen` int(11) DEFAULT NULL,
  `waktu_mulai` datetime DEFAULT NULL,
  `waktu_panen` datetime DEFAULT NULL,
  `judul_panen` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Hasil_Panen`
--

INSERT INTO `Hasil_Panen` (`id`, `lahan_id`, `jenis_tanaman`, `jumlah_hasil_panen`, `waktu_mulai`, `waktu_panen`, `judul_panen`) VALUES
(16, 6, 'Padi', 500, '2023-01-01 08:00:00', '2023-01-10 15:00:00', 'Panen Padi 1'),
(17, 7, 'Jagung', 300, '2023-02-05 09:30:00', '2023-02-15 16:45:00', 'Panen Jagung 1'),
(18, 8, 'Tebu', 700, '2023-03-10 10:15:00', '2023-03-20 17:30:00', 'Panen Tebu 1'),
(19, 9, 'Kentang', 400, '2023-04-15 11:45:00', '2023-04-25 18:15:00', 'Panen Kentang 1'),
(20, 10, 'Wortel', 600, '2023-05-20 12:30:00', '2023-05-30 19:00:00', 'Panen Wortel 1');

-- --------------------------------------------------------

--
-- Table structure for table `Lahan`
--

CREATE TABLE `Lahan` (
  `id` int(11) NOT NULL,
  `nama` varchar(255) DEFAULT NULL,
  `lokasi` varchar(255) DEFAULT NULL,
  `deskripsi` text,
  `luas` int(11) DEFAULT NULL,
  `jenis_tanaman` varchar(255) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Lahan`
--

INSERT INTO `Lahan` (`id`, `nama`, `lokasi`, `deskripsi`, `luas`, `jenis_tanaman`, `user_id`) VALUES
(6, 'Lahan 1', 'Location 1', 'Description 1', 180, 'Tanaman A', 1),
(7, 'Lahan 2', 'Location 2', 'Description 2', 150, 'Tanaman B', 1),
(8, 'Lahan 3', 'Location 3', 'Description 3', 200, 'Tanaman C', 1),
(9, 'Lahan 4', 'Location 4', 'Description 4', 120, 'Tanaman D', 1),
(10, 'Lahan 5', 'Location 5', 'Description 5', 180, 'Tanaman E', 1);

-- --------------------------------------------------------

--
-- Table structure for table `Pendapatan`
--

CREATE TABLE `Pendapatan` (
  `id` int(11) NOT NULL,
  `tanggal` date DEFAULT NULL,
  `nama_barang` varchar(255) DEFAULT NULL,
  `harga_barang` decimal(10,2) DEFAULT NULL,
  `jumlah` int(11) DEFAULT NULL,
  `keterangan` text,
  `hasil_panen_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Pendapatan`
--

INSERT INTO `Pendapatan` (`id`, `tanggal`, `nama_barang`, `harga_barang`, `jumlah`, `keterangan`, `hasil_panen_id`) VALUES
(1, '2023-06-01', 'Produk A', '1000.00', 50, 'Penjualan Produk A', 16),
(2, '2023-06-05', 'Produk B', '1200.00', 60, 'Penjualan Produk B', 17),
(3, '2023-06-10', 'Produk C', '1500.00', 70, 'Penjualan Produk C', 18),
(4, '2023-06-15', 'Produk D', '800.00', 40, 'Penjualan Produk D', 19),
(5, '2023-06-20', 'Produk E', '2000.00', 80, 'Penjualan Produk E', 20),
(6, '2023-07-01', 'Produk F', '1100.00', 55, 'Penjualan Produk F', 16),
(7, '2023-07-05', 'Produk G', '1300.00', 65, 'Penjualan Produk G', 17),
(8, '2023-07-10', 'Produk H', '1600.00', 75, 'Penjualan Produk H', 18),
(9, '2023-07-15', 'Produk I', '850.00', 45, 'Penjualan Produk I', 19),
(10, '2023-07-20', 'Produk J', '2100.00', 85, 'Penjualan Produk J', 20),
(11, '2023-08-01', 'Produk K', '900.00', 30, 'Penjualan Produk K', 16),
(12, '2023-08-05', 'Produk L', '1700.00', 90, 'Penjualan Produk L', 17),
(13, '2023-08-10', 'Produk M', '1100.00', 55, 'Penjualan Produk M', 18),
(14, '2023-08-15', 'Produk N', '1200.00', 60, 'Penjualan Produk N', 19),
(15, '2023-08-20', 'Produk O', '1400.00', 70, 'Penjualan Produk O', 20);

-- --------------------------------------------------------

--
-- Table structure for table `Pengeluaran`
--

CREATE TABLE `Pengeluaran` (
  `id` int(11) NOT NULL,
  `tanggal` date NOT NULL,
  `jenis_aktivitas` varchar(255) DEFAULT NULL,
  `total_pengeluaran` decimal(10,2) DEFAULT NULL,
  `keterangan` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Pengeluaran`
--

INSERT INTO `Pengeluaran` (`id`, `tanggal`, `jenis_aktivitas`, `total_pengeluaran`, `keterangan`) VALUES
(1, '2023-06-01', 'Pembelian Benih', '500.00', 'Pembelian benih untuk tanaman'),
(2, '2023-06-05', 'Pupuk', '300.00', 'Pembelian pupuk untuk tanaman'),
(3, '2023-06-10', 'Alat Pertanian', '800.00', 'Pembelian alat pertanian'),
(4, '2023-06-15', 'Irigasi', '200.00', 'Biaya irigasi lahan'),
(5, '2023-06-20', 'Pekerja Harian', '400.00', 'Gaji pekerja harian'),
(6, '2023-07-01', 'Pembelian Benih', '450.00', 'Pembelian benih untuk tanaman'),
(7, '2023-07-05', 'Pupuk', '250.00', 'Pembelian pupuk untuk tanaman'),
(8, '2023-07-10', 'Alat Pertanian', '700.00', 'Pembelian alat pertanian'),
(9, '2023-07-15', 'Irigasi', '150.00', 'Biaya irigasi lahan'),
(10, '2023-07-20', 'Pekerja Harian', '350.00', 'Gaji pekerja harian'),
(11, '2023-08-01', 'Pembelian Benih', '480.00', 'Pembelian benih untuk tanaman'),
(12, '2023-08-05', 'Pupuk', '280.00', 'Pembelian pupuk untuk tanaman'),
(13, '2023-08-10', 'Alat Pertanian', '750.00', 'Pembelian alat pertanian'),
(14, '2023-08-15', 'Irigasi', '120.00', 'Biaya irigasi lahan'),
(15, '2023-08-20', 'Pekerja Harian', '380.00', 'Gaji pekerja harian'),
(16, '2023-09-01', 'Pembelian Benih', '520.00', 'Pembelian benih untuk tanaman'),
(17, '2023-09-05', 'Pupuk', '320.00', 'Pembelian pupuk untuk tanaman'),
(18, '2023-09-10', 'Alat Pertanian', '780.00', 'Pembelian alat pertanian'),
(19, '2023-09-15', 'Irigasi', '170.00', 'Biaya irigasi lahan'),
(20, '2023-09-20', 'Pekerja Harian', '420.00', 'Gaji pekerja harian');

-- --------------------------------------------------------

--
-- Table structure for table `User`
--

CREATE TABLE `User` (
  `id` int(11) NOT NULL,
  `email` varchar(30) NOT NULL,
  `Nama_Lengkap` varchar(80) DEFAULT NULL,
  `Nama_Penggilan` varchar(30) DEFAULT NULL,
  `Nomor_Telepon` varchar(20) DEFAULT NULL,
  `Password` varchar(255) NOT NULL,
  `Bio` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `User`
--

INSERT INTO `User` (`id`, `email`, `Nama_Lengkap`, `Nama_Penggilan`, `Nomor_Telepon`, `Password`, `Bio`) VALUES
(1, 'juniyasyos@gmail.com', 'Ahmad Ilyas', 'Ilyas', '082338172691', 'pbkdf2:sha1:600000$TMwS9ZSp40cRkVXY$836fa084ef285f00f9cfd3cbcc6c51298889e149', 'Hallo Nama Saya Ahmad Ilyas dan merupakan Programmer pemula');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Aktivitas_Lahan`
--
ALTER TABLE `Aktivitas_Lahan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `lahan_id` (`lahan_id`),
  ADD KEY `pengeluaran_id` (`pengeluaran_id`),
  ADD KEY `id_panen` (`id_panen`);

--
-- Indexes for table `Hasil_Panen`
--
ALTER TABLE `Hasil_Panen`
  ADD PRIMARY KEY (`id`),
  ADD KEY `lahan_id` (`lahan_id`);

--
-- Indexes for table `Lahan`
--
ALTER TABLE `Lahan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `Pendapatan`
--
ALTER TABLE `Pendapatan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hasil_panen_id` (`hasil_panen_id`);

--
-- Indexes for table `Pengeluaran`
--
ALTER TABLE `Pengeluaran`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `User`
--
ALTER TABLE `User`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Aktivitas_Lahan`
--
ALTER TABLE `Aktivitas_Lahan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;
--
-- AUTO_INCREMENT for table `Hasil_Panen`
--
ALTER TABLE `Hasil_Panen`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
--
-- AUTO_INCREMENT for table `Lahan`
--
ALTER TABLE `Lahan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `Pendapatan`
--
ALTER TABLE `Pendapatan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT for table `Pengeluaran`
--
ALTER TABLE `Pengeluaran`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
--
-- AUTO_INCREMENT for table `User`
--
ALTER TABLE `User`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `Aktivitas_Lahan`
--
ALTER TABLE `Aktivitas_Lahan`
  ADD CONSTRAINT `Aktivitas_Lahan_ibfk_1` FOREIGN KEY (`lahan_id`) REFERENCES `Lahan` (`id`),
  ADD CONSTRAINT `Aktivitas_Lahan_ibfk_2` FOREIGN KEY (`pengeluaran_id`) REFERENCES `Pengeluaran` (`id`),
  ADD CONSTRAINT `Aktivitas_Lahan_ibfk_3` FOREIGN KEY (`id_panen`) REFERENCES `Hasil_Panen` (`id`);

--
-- Constraints for table `Hasil_Panen`
--
ALTER TABLE `Hasil_Panen`
  ADD CONSTRAINT `Hasil_Panen_ibfk_1` FOREIGN KEY (`lahan_id`) REFERENCES `Lahan` (`id`);

--
-- Constraints for table `Lahan`
--
ALTER TABLE `Lahan`
  ADD CONSTRAINT `Lahan_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`id`);

--
-- Constraints for table `Pendapatan`
--
ALTER TABLE `Pendapatan`
  ADD CONSTRAINT `Pendapatan_ibfk_1` FOREIGN KEY (`hasil_panen_id`) REFERENCES `Hasil_Panen` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
