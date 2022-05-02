-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 24, 2021 at 09:06 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `attendence`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `subject` varchar(50) NOT NULL,
  `message` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`id`, `name`, `email`, `subject`, `message`) VALUES
(1, 'manisha', 'manisha@gmail.com', 'whats new', 'hi what are the courses are started');

-- --------------------------------------------------------

--
-- Table structure for table `pregister`
--

CREATE TABLE `pregister` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `mobile` int(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(10) NOT NULL,
  `cpassword` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pregister`
--

INSERT INTO `pregister` (`id`, `name`, `uname`, `mobile`, `email`, `password`, `cpassword`) VALUES
(1, 'manisha', 'manishas', 2147483647, 'manisha@gmail.com', '123456789', '123456789');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `mobile` int(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(10) NOT NULL,
  `cpassword` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `name`, `uname`, `mobile`, `email`, `password`, `cpassword`) VALUES
(1, 'manisha', 'manishas', 2147483647, 'tech@gmail.com', 'manishas', 'manishas'),
(2, 'Mrunal', 'Vmrunal', 2147483647, 'mrunal@gmail.com', 'mrunal@123', 'mrunal@123'),
(3, 'Padmini', 'Mpadmini', 2147483647, 'padmini@gmail.com', '123456789', '123456789'),
(4, 'tushari', 'tusharip', 2147483647, 'tushari@gmail.com', '123456789', '123456789'),
(5, 'madhuri', 'madhurik', 2147483647, 'madhuri@gmail.com', '123456789', '123456789'),
(6, 'riya', 'riyas', 2147483647, 'riya@gmail.com', 'riya@1234', 'riya@1234');

-- --------------------------------------------------------

--
-- Table structure for table `sregister`
--

CREATE TABLE `sregister` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `mobile` int(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(10) NOT NULL,
  `cpassword` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sregister`
--

INSERT INTO `sregister` (`id`, `name`, `uname`, `mobile`, `email`, `password`, `cpassword`) VALUES
(1, 'tushari', 'Ptushari', 2147483647, 'tushari@gmail.com', 'qwertyui', 'qwertyui'),
(2, 'mrunal', 'Vmurnal', 1234567890, 'mrunal@gmail.com', '123456789', '123456789');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pregister`
--
ALTER TABLE `pregister`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sregister`
--
ALTER TABLE `sregister`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `pregister`
--
ALTER TABLE `pregister`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `sregister`
--
ALTER TABLE `sregister`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
