-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: mysql:3306
-- Generation Time: Feb 17, 2024 at 01:37 PM
-- Server version: 8.3.0
-- PHP Version: 8.2.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `belsimpel_hackathon`
--

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `Description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `EAN` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `Price` float DEFAULT NULL,
  `Stock` int DEFAULT NULL,
  `IMEI` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `Prepaid_sim` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `Prepaid_tel` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `ID` int NOT NULL,
  `identifier` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `location` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `warehouse` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
