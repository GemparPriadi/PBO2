<?php
require_once 'database.php';
require_once 'Peminjaman.php';
$db = new MySQLDatabase();
$peminjaman = new Peminjaman($db);
$id=0;
$kode_peminjaman=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_peminjaman'])){
            $kode_peminjaman = $_GET['kode_peminjaman'];
        }
        if($id>0){    
            $result = $peminjaman->get_by_id($id);
        }elseif($kode_peminjaman>0){
            $result = $peminjaman->get_by_kode_peminjaman($kode_peminjaman);
        } else {
            $result = $peminjaman->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new peminjaman
        $peminjaman->kode_peminjaman = $_POST['kode_peminjaman'];
        $peminjaman->tanggal_pinjam = $_POST['tanggal_pinjam'];
        $peminjaman->tanggal_kembali = $_POST['tanggal_kembali'];
        $peminjaman->id_anggota = $_POST['id_anggota'];
        $peminjaman->id_buku = $_POST['id_buku'];
        $peminjaman->id_admin = $_POST['id_admin'];
       
        $peminjaman->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'PUT':
        // Update an existing data
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_peminjaman'])){
            $kode_peminjaman = $_GET['kode_peminjaman'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $peminjaman->kode_peminjaman = $_PUT['kode_peminjaman'];
        $peminjaman->tanggal_pinjam = $_PUT['tanggal_pinjam'];
        $peminjaman->tanggal_kembali = $_PUT['tanggal_kembali'];
        $peminjaman->id_anggota = $_PUT['id_anggota'];
        $peminjaman->id_buku = $_PUT['id_buku'];
        $peminjaman->id_admin = $_PUT['id_admin'];
        if($id>0){    
            $peminjaman->update($id);
        }elseif($kode_peminjaman<>""){
            $peminjaman->update_by_kode_peminjaman($kode_peminjaman);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_peminjaman'])){
            $kode_peminjaman = $_GET['kode_peminjaman'];
        }
        if($id>0){    
            $peminjaman->delete($id);
        }elseif($kode_peminjaman>0){
            $peminjaman->delete_by_kode_peminjaman($kode_peminjaman);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
    }
$db->close()
?>