<?php
	#conectando com o banco de dados
	require_once('connect.php');

	#selecionando o campo de filtro
	$cpf = $_POST['cpf'];
	#pesquisando no banco através do CPF

	$pesq = " SELECT * FROM pessoas WHERE cpf='".$cpf."'";
	$result = $conn->query($pesq);

	$row = $result->fetch_assoc();

	echo json_encode($row);
    
?>