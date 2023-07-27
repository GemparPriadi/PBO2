<?php
require_once 'database.php';
class Admin 
{
    private $db;
    private $table = 'admin';
    public $kode_admin = "";
    public $nama_admin = "";
    public $no_telp = "";
    public $alamat = "";
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
    public function get_by_kode_admin(int $kode_admin)
    {
        $query = "SELECT * FROM $this->table WHERE kode_admin = $kode_admin";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kode_admin`,`nama_admin`,`no_telp`,`alamat`) VALUES ('$this->kode_admin','$this->nama_admin','$this->no_telp','$this->alamat')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kode_admin = '$this->kode_admin', nama_admin = '$this->nama_admin', no_telp = '$this->no_telp', alamat = '$this->alamat' 
        WHERE id_admin = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kode_admin($kode_admin): int
    {
        $query = "UPDATE $this->table SET kode_admin = '$this->kode_admin', nama_admin = '$this->nama_admin', no_telp = '$this->no_telp', alamat = '$this->alamat' 
        WHERE kode_admin = $kode_admin";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_admin = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kode_admin($kode_admin): int
    {
        $query = "DELETE FROM $this->table WHERE kode_admin = $kode_admin";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>