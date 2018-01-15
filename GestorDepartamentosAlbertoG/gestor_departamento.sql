-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-01-2018 a las 00:12:06
-- Versión del servidor: 10.1.28-MariaDB
-- Versión de PHP: 7.1.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gestor_departamento`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asignatura`
--

CREATE TABLE `asignatura` (
  `Codigo` int(11) NOT NULL,
  `Profesor` int(11) NOT NULL,
  `Nombre_Asignatura` text CHARACTER SET latin1 COLLATE latin1_spanish_ci NOT NULL,
  `Num_Departamento` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `asignatura`
--

INSERT INTO `asignatura` (`Codigo`, `Profesor`, `Nombre_Asignatura`, `Num_Departamento`) VALUES
(0, 0, 'matematicas', 0),
(22, 3, 'mates', 25),
(155, 888, 'Infantil', 500);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamento`
--

CREATE TABLE `departamento` (
  `Nomb_Departamento` text NOT NULL,
  `Num_Departamento` int(11) NOT NULL,
  `Titulacion` text NOT NULL,
  `Edificio` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `departamento`
--

INSERT INTO `departamento` (`Nomb_Departamento`, `Num_Departamento`, `Titulacion`, `Edificio`) VALUES
('string', 0, 'string', 'string'),
('CC', 25, 'informatica', 'politecnica'),
('magisterio', 500, 'magisterio', 'magisterio');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesor`
--

CREATE TABLE `profesor` (
  `Carga_Trabajo` int(11) NOT NULL,
  `DNI_profesor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `profesor`
--

INSERT INTO `profesor` (`Carga_Trabajo`, `DNI_profesor`) VALUES
(0, 0),
(1, 1),
(44, 3),
(140, 10),
(20, 888);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `asignatura`
--
ALTER TABLE `asignatura`
  ADD PRIMARY KEY (`Codigo`),
  ADD KEY `asignatura_ibfk_2` (`Num_Departamento`),
  ADD KEY `asignatura_ibfk_1` (`Profesor`);

--
-- Indices de la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`Num_Departamento`);

--
-- Indices de la tabla `profesor`
--
ALTER TABLE `profesor`
  ADD PRIMARY KEY (`DNI_profesor`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asignatura`
--
ALTER TABLE `asignatura`
  ADD CONSTRAINT `asignatura_ibfk_1` FOREIGN KEY (`Profesor`) REFERENCES `profesor` (`DNI_Profesor`),
  ADD CONSTRAINT `asignatura_ibfk_2` FOREIGN KEY (`Num_Departamento`) REFERENCES `departamento` (`Num_Departamento`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
