CREATE TABLE `Admin` (
	`id_admin` INT(15) NOT NULL AUTO_INCREMENT,
	`kode_admin` char(20) NOT NULL UNIQUE,
	`nama_admin` varchar(40) NOT NULL,
	`no_telp` char(15) NOT NULL,
	`alamat` varchar(50) NOT NULL,
	PRIMARY KEY (`id_admin`)
);

CREATE TABLE `Anggota` (
	`id_anggota` INT(15) NOT NULL AUTO_INCREMENT,
	`kode_anggota` char(20) NOT NULL UNIQUE,
	`nama_anggota` varchar(50) NOT NULL,
	`jenis_kelamin` enum('P','L') NOT NULL,
	`prodi` char(10) NOT NULL,
	`no_tlp` char(15) NOT NULL,
	`alamat` varchar(50) NOT NULL,
	PRIMARY KEY (`id_anggota`)
);

CREATE TABLE `Buku` (
	`id_buku` INT(15) NOT NULL AUTO_INCREMENT,
	`kode_buku` char(20) NOT NULL UNIQUE,
	`judul_buku` varchar(50) NOT NULL,
	`penulis_buku` varchar(50) NOT NULL,
	`penerbit_buku` varchar(50) NOT NULL,
	`tahun_penerbit` char(15) NOT NULL,
	`kategori_buku` enum('Pendidikan','Cerpen','Komik','Fiksi','Novel') NOT NULL,
	PRIMARY KEY (`id_buku`)
);

CREATE TABLE `Peminjaman` (
	`id_peminjaman` INT(15) NOT NULL AUTO_INCREMENT,
	`kode_peminjaman` char(20) NOT NULL UNIQUE,
	`tanggal_pinjam` DATE NOT NULL,
	`tanggal_kembali` DATE NOT NULL,
	`id_anggota` INT(15) NOT NULL,
	`id_buku` INT(15) NOT NULL,
	`id_admin` INT(15) NOT NULL,
	PRIMARY KEY (`id_peminjaman`)
);

CREATE TABLE `Pengembalian` (
	`id_pengembalian` INT(15) NOT NULL AUTO_INCREMENT,
	`kode_anggota` char(20) NOT NULL UNIQUE,
	`tanggal_pengembalian` DATE NOT NULL,
	`denda` INT(15) NOT NULL,
	`id_buku` INT(15) NOT NULL,
	`id_anggota` INT(15) NOT NULL,
	`id_admin` INT(15) NOT NULL,
	PRIMARY KEY (`id_pengembalian`)
);

ALTER TABLE `Peminjaman` ADD CONSTRAINT `Peminjaman_fk0` FOREIGN KEY (`id_anggota`) REFERENCES `Anggota`(`id_anggota`);

ALTER TABLE `Peminjaman` ADD CONSTRAINT `Peminjaman_fk1` FOREIGN KEY (`id_buku`) REFERENCES `Buku`(`id_buku`);

ALTER TABLE `Peminjaman` ADD CONSTRAINT `Peminjaman_fk2` FOREIGN KEY (`id_admin`) REFERENCES `Admin`(`id_admin`);

ALTER TABLE `Pengembalian` ADD CONSTRAINT `Pengembalian_fk0` FOREIGN KEY (`id_buku`) REFERENCES `Buku`(`id_buku`);

ALTER TABLE `Pengembalian` ADD CONSTRAINT `Pengembalian_fk1` FOREIGN KEY (`id_anggota`) REFERENCES `Anggota`(`id_anggota`);

ALTER TABLE `Pengembalian` ADD CONSTRAINT `Pengembalian_fk2` FOREIGN KEY (`id_admin`) REFERENCES `Admin`(`id_admin`);






