-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 30-Mar-2020 às 10:36
-- Versão do servidor: 10.4.11-MariaDB
-- versão do PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `bd`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `pessoas`
--

CREATE TABLE `pessoas` (
  `cpf` varchar(18) DEFAULT NULL,
  `name` varchar(200) DEFAULT NULL,
  `nascimento` date DEFAULT NULL,
  `profissao` varchar(200) DEFAULT NULL,
  `cep` varchar(150) DEFAULT NULL,
  `number` varchar(200) DEFAULT NULL,
  `complement` varchar(200) DEFAULT NULL,
  `comp_cnpj` varchar(200) DEFAULT NULL,
  `comp_name` varchar(200) DEFAULT NULL,
  `phones` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `pessoas`
--

INSERT INTO `pessoas` (`cpf`, `name`, `nascimento`, `profissao`, `cep`, `number`, `complement`, `comp_cnpj`, `comp_name`, `phones`) VALUES
('644.183.780-30', 'Adriano da Silva Souza', '1992-02-03', 'Engenheiro da Computação', '29160510', '14', 'APP 201', '06.990.590/0001-23', 'GOOGLE LTDA', '55279818299 - 0279818288 - 27981828822'),
('474.669.350-10', 'Paulo Souza Cruz', '1978-10-03', 'Empreendedor', '29090-290', '22', 'CASA', '975276040001-22', 'CACAU SHOW', '1181818292'),
('363.780.800-54', 'Maria da Juda Mendes', '1991-04-20', 'Professora', '24717250', '1002', 'CONDOMINIO', '10.475.363/0001-37', 'PROG INFORMATICA LTDA PROG-INFO', '27981882222');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
