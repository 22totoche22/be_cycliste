-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Client :  127.0.0.1
-- Généré le :  Ven 10 Février 2017 à 15:52
-- Version du serveur :  10.1.10-MariaDB
-- Version de PHP :  5.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `test_ienac`
--
CREATE DATABASE IF NOT EXISTS `test_ienac` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `test_ienac`;

-- --------------------------------------------------------

--
-- Structure de la table `commentaires`
--

CREATE TABLE IF NOT EXISTS `commentaires` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `comment` text NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=6 ;

--
-- Contenu de la table `commentaires`
--

INSERT INTO `commentaires` (`id`, `nom`, `comment`, `email`) VALUES
(1, 'test', 'test\r\n', 'test'),
(2, 'test2', 'test2', 'test2'),
(3, 'test2', 'test2', 'test2'),
(4, 'test2', 'test2', 'test2'),
(5, 'test2', 'test2', 'test2');

-- --------------------------------------------------------

--
-- Structure de la table `identification`
--

CREATE TABLE IF NOT EXISTS `identification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(30) NOT NULL,
  `mdp` varchar(30) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Contenu de la table `identification`
--

INSERT INTO `identification` (`id`, `login`, `mdp`, `nom`, `prenom`) VALUES
(1, 'coco', 'coco', 'cortes', 'didier'),
(2, 'dada', 'dad', 'dalmau', 'jean-louis');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
