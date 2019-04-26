<?php

// Output download headers
header("Cache-Control: no-cache");
header("Content-Description: File Transfer");
header("Content-Disposition: attachment; filename=result.csv");
header("Content-Type: text/csv");
header("Content-Transfer-Encoding: binary");

session_start();

if (isset($_POST['json'])){
    $_SESSION['arr'] = json_decode($_POST["json"], true);
}

foreach ($_SESSION['arr'] as $k => $v){
    echo $k.",".$v."\n";
}