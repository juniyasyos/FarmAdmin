-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: sql12.freemysqlhosting.net
-- Generation Time: Nov 22, 2023 at 08:57 AM
-- Server version: 5.5.62-0ubuntu0.14.04.1
-- PHP Version: 7.0.33-0ubuntu0.16.04.16


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



CREATE TABLE `Hasil_Panen` (
  `id` int(11) NOT NULL,
  `lahan_id` int(11) DEFAULT NULL,
  `jenis_tanaman` varchar(255) DEFAULT NULL,
  `jumlah_hasil_panen` int(11) DEFAULT NULL,
  `waktu_mulai` datetime DEFAULT NULL,
  `waktu_panen` datetime DEFAULT NULL,
  `judul_panen` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


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

CREATE TABLE `Pengeluaran` (
  `id` int(11) NOT NULL,
  `tanggal` date NOT NULL,
  `jenis_aktivitas` varchar(255) DEFAULT NULL,
  `total_pengeluaran` decimal(10,2) DEFAULT NULL,
  `keterangan` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `User` (
  `id` int(11) NOT NULL,
  `email` varchar(30) NOT NULL,
  `Nama_Lengkap` varchar(80) DEFAULT NULL,
  `Nama_Penggilan` varchar(30) DEFAULT NULL,
  `Nomor_Telepon` varchar(20) DEFAULT NULL,
  `Password` varchar(255) NOT NULL,
  `Bio` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



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
