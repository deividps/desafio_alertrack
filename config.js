function searchCPF(){

	let cpfInp = document.getElementById("input__cpf").value;
	$.ajax({
	type: 'POST',
	url: 'pesquisa.php',
	data: {cpf: cpfInp},
	success: function(data){
		console.log(data);
		document.getElementById('cpf').textContent = data.cpf;
		document.getElementById('name').textContent = data.name;
		document.getElementById('nascimento').textContent = data.nascimento;
		document.getElementById('profissao').textContent = data.profissao;
		document.getElementById('cep').textContent = data.cep;
		document.getElementById('number').textContent = data.number;
		document.getElementById('complement').textContent = data.complement;
		document.getElementById('comp_cnpj').textContent = data.comp_cnpj;
		document.getElementById('comp_name').textContent = data.comp_name;
		document.getElementById('phones').textContent = data.phones;
		document.getElementsByClassName("response")[0].style.display = "block";
	},
	dataType: 'json'

});
}

