<?php
$myServer = "localhost\sqlexpress";
$myUser = "sa";
$myPass = "nimp2017";
$myDB = "teste";

$serverName = "localhost\sqlexpress"; 
$connectionInfo = array( "Database"=>"teste", "UID"=>"sa", "PWD"=>"nimp2017");
$conn = sqlsrv_connect( $serverName, $connectionInfo);
  
  
  $qryAC = "SELECT [teste]
  FROM [dbo].[tabela]";
		  
$stmtAC = sqlsrv_query( $conn, $qryAC );	


  echo "<meta http-equiv='refresh' content='0;url=http://10.200.52.232/test.php'>";
  while( $item = sqlsrv_fetch_array($stmtAC)){
    echo $item['teste']."<br>";
}
?>