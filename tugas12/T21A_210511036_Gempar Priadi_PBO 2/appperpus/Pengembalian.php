<?php
require_once 'database.php';
class Pengembalian 
{
    private $db;
    private $table = 'pengembalian';
    public $kode_anggota = "";
    public $tanggal_pengembalian = "";
    public $denda = "";
    public $id_buku = "";
    public $id_anggota = "";
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
    public function get_by_kode_anggota(int $kode_anggota)
    {
        $query = "SELECT * FROM $this->table WHERE kode_anggota = $kode_anggota";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kode_anggota`,`tanggal_pengembalian`,`denda`,`id_buku`,`id_anggota`,`id_admin`) VALUES ('$this->kode_anggota','$this->tanggal_pengembalian','$this->denda','$this->id_buku','$this->id_anggota','$this->id_admin')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kode_anggota = '$this->kode_anggota', tanggal_pengembalian = '$this->tanggal_pengembalian', denda = '$this->denda', id_buku = '$this->id_buku', id_anggota = '$this->id_anggota', id_admin = '$this->id_admin' 
        WHERE id_pengembalian = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kode_anggota($kode_anggota): int
    {
        $query = "UPDATE $this->table SET kode_anggota = '$this->kode_anggota', tanggal_pengembalian = '$this->tanggal_pengembalian', denda = '$this->denda', id_buku = '$this->id_buku', id_anggota = '$this->id_anggota', id_admin = '$this->id_admin' 
        WHERE kode_anggota = $kode_anggota";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_pengembalian = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kode_anggota($kode_anggota): int
    {
        $query = "DELETE FROM $this->table WHERE kode_anggota = $kode_anggota";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>