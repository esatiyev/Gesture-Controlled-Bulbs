<?php
$servername = "servername";
$username = "username";
$password = "password";
$dbname = "database_name";
$port = 1111; // Your mysql port number 


// Create connection
$conn = new mysqli($servername, $username, $password, $dbname, $port);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>