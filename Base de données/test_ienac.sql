-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le :  lun. 26 mars 2018 à 12:50
-- Version du serveur :  10.1.26-MariaDB
-- Version de PHP :  7.1.9



--
-- Base de données :  `test_ienac`
--
CREATE DATABASE IF NOT EXISTS `test_ienac` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `test_ienac`;

-- --------------------------------------------------------

--
-- Structure de la table `commentaires`
--

CREATE TABLE `commentaires` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `comment` text NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `commentaires`
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

CREATE TABLE `identification` (
  `id` int(11) NOT NULL,
  `login` varchar(30) CHARACTER SET latin1 NOT NULL,
  `mdp` varchar(30) CHARACTER SET latin1 NOT NULL,
  `nom` varchar(100) CHARACTER SET latin1 NOT NULL,
  `prenom` varchar(100) CHARACTER SET latin1 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `identification`
--

INSERT INTO `identification` (`id`, `login`, `mdp`, `nom`, `prenom`) VALUES
(1, 'coco', 'coco', 'cortes', 'didier'),
(2, 'dada', 'dad', 'dalmau', 'jean-louis');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `commentaires`
--
ALTER TABLE `commentaires`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `identification`
--
ALTER TABLE `identification`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `commentaires`
--
ALTER TABLE `commentaires`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `identification`
--
ALTER TABLE `identification`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;


