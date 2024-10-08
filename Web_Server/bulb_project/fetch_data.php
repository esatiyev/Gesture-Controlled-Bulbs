<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json");

include 'db_connect.php';

$sql = "SELECT * FROM bulb_data";
$result = $conn->query($sql);

$data = [];

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }
}

echo json_encode($data);

$conn->close();
?>