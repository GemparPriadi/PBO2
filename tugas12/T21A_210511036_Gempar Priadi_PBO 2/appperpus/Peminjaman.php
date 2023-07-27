<?php
require_once 'database.php';
class Peminjaman 
{
    private $db;
    private $table = 'peminjaman';
    public $kode_peminjaman = "";
    public $tanggal_pinjam = "";
    public $tanggal_kembali = "";
    public $id_anggota = "";
    public $id_buku = "";
    public $id_admin = "";
    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }
    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }
    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function get_by_kode_peminjaman(int $kode_peminjaman)
    {
        $query = "SELECT * FROM $this->table WHERE kode_peminjaman = $kode_peminjaman";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kode_peminjaman`,`tanggal_pinjam`,`tanggal_kembali`,`id_anggota`,`id_buku`,`id_admin`) VALUES ('$this->kode_peminjaman','$this->tanggal_pinjam','$this->tanggal_kembali','$this->id_anggota','$this->id_buku','$this->id_admin')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kode_peminjaman = '$this->kode_peminjaman', tanggal_pinjam = '$this->tanggal_pinjam', tanggal_kembali = '$this->tanggal_kembali', id_anggota = '$this->id_anggota', id_buku = '$this->id_buku', id_admin = '$this->id_admin' 
        WHERE id_peminjaman = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kode_peminjaman($kode_peminjaman): int
    {
        $query = "UPDATE $this->table SET kode_peminjaman = '$this->kode_peminjaman', tanggal_pinjam = '$this->tanggal_pinjam', tanggal_kembali = '$this->tanggal_kembali', id_anggota = '$this->id_anggota', id_buku = '$this->id_buku', id_admin = '$this->id_admin' 
        WHERE kode_peminjaman = $kode_peminjaman";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_peminjaman = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kode_peminjaman($kode_peminjaman): int
    {
        $query = "DELETE FROM $this->table WHERE kode_peminjaman = $kode_peminjaman";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>