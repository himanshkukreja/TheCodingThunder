-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 29, 2020 at 06:31 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `users_inotes`
--

-- --------------------------------------------------------

--
-- Table structure for table `users_inotes`
--

CREATE TABLE `users_inotes` (
  `sno` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(255) NOT NULL,
  `dt` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users_inotes`
--

INSERT INTO `users_inotes` (`sno`, `username`, `password`, `dt`) VALUES
(1, 'admin', '$2y$10$9FX1dgoAMBCA4di0SBE9EOffNJivchRQF5Js5efDDcO5JCFA1gfRW', '2020-06-29 16:45:42'),
(2, 'himanshu', '$2y$10$mDC7B2jur/JJslnn9yMMZ.jy9maNeP.fomBegSWjzu8rlC4KtFIu6', '2020-06-29 16:46:47'),
(3, 'TU101903252', '$2y$10$0ztS/01oFIj5q3oskAGAVunxKFr2ekduZXq3YVczeUmPm2HTJez3C', '2020-06-29 17:16:44'),
(4, 'rohan', '$2y$10$jcW91C0KAZoUSr5Ibhg8.eC5ZTiOqM82YnVENehf71f1uQ3MT7hli', '2020-06-29 20:50:07');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users_inotes`
--
ALTER TABLE `users_inotes`
  ADD PRIMARY KEY (`sno`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users_inotes`
--
ALTER TABLE `users_inotes`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
