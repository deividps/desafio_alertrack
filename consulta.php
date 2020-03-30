<html>
    <head>

	    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
	  	
	  	<script src="config.js"></script>

	  	<center><img src="https://www.alertrack.com.br/img/Alertrack%20logo.png" height="53" width="233" border="0" alt="Logo Alertrack"></center>
	  	
	  	<style type="text/css">
	  		body {
	  			background-color: #B0C4DE
	  		}
	  	</style>

</head>
<body>

	<h1>CONSULTA PESSOA FÍSICA</h1>

	<input type="text" id="input__cpf" placeholder="DIGITE O CPF">
	<button onclick="searchCPF()">Consultar</button>


	<div class="response" style="display: none"> 
		<br>
		<strong>CPF: </strong><span id="cpf"></span><br>
		<strong>NOME: </strong><span id="name"></span><br>
		<strong>NASCIMENTO: </strong><span id="nascimento"></span><br>
		<strong>PROFISSÃO: </strong><span id="profissao"></span><br>
		<strong>CEP DA MORADIA: </strong><span id="cep"></span><br>
		<strong>NUMERO DO ENDEREÇO: </strong><span id="number"></span><br>
		<strong>COMPLEMENTO: </strong><span id="complement"></span><br>
		<strong>CNPJ DA EMPRESA: </strong><span id="comp_cnpj"></span><br>
		<strong>NOME DA EMPRESA QUE TRABALHA: </strong><span id="comp_name"></span><br>
		<strong>TELEFONES DE CONTATO: </strong><span id="phones"></span><br>

	</div>

            
</body>
</html>
