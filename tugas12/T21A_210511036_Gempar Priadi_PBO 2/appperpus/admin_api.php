<?php
require_once 'database.php';
require_once 'Admin.php';
$db = new MySQLDatabase();
$admin = new Admin($db);
$id=0;
$kode_admin=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_admin'])){
            $kode_admin = $_GET['kode_admin'];
        }
        if($id>0){    
            $result = $admin->get_by_id($id);
        }elseif($kode_admin>0){
            $result = $admin->get_by_kode_admin($kode_admin);
        } else {
            $result = $admin->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new admin
        $admin->kode_admin = $_POST['kode_admin'];
        $admin->nama_admin = $_POST['nama_admin'];
        $admin->no_telp = $_POST['no_telp'];
        $admin->alamat = $_POST['alamat'];
       
        $admin->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Admin created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Admin not created.';
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
        if(isset($_GET['kode_admin'])){
            $kode_admin = $_GET['kode_admin'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $admin->kode_admin = $_PUT['kode_admin'];
        $admin->nama_admin = $_PUT['nama_admin'];
        $admin->no_telp = $_PUT['no_telp'];
        $admin->alamat = $_PUT['alamat'];
        if($id>0){    
            $admin->update($id);
        }elseif($kode_admin<>""){
            $admin->update_by_kode_admin($kode_admin);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Admin updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Admin update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_admin'])){
            $kode_admin = $_GET['kode_admin'];
        }
        if($id>0){    
            $admin->delete($id);
        }elseif($kode_admin>0){
            $admin->delete_by_kode_admin($kode_admin);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Admin deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Admin delete failed.';
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