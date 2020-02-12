CREATE DATABASE  IF NOT EXISTS `snow` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
USE `snow`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: snow
-- ------------------------------------------------------
-- Server version	5.7.20-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `pricemonth`
--

DROP TABLE IF EXISTS `pricemonth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pricemonth` (
  `symbol` varchar(20) COLLATE utf8_bin NOT NULL,
  `year` int(10) NOT NULL,
  `month` int(10) NOT NULL,
  `firstday` int(10) DEFAULT NULL,
  `lastday` int(10) NOT NULL,
  `begin` double DEFAULT NULL,
  `high` double DEFAULT NULL,
  `low` double DEFAULT NULL,
  `end` double DEFAULT NULL,
  `amount` double DEFAULT NULL COMMENT '交易金额(元)',
  `pe` double DEFAULT NULL COMMENT '市盈率\n',
  `p` double DEFAULT NULL COMMENT '盈利率=1/pe',
  `basiceps` double DEFAULT NULL,
  `naps` double DEFAULT NULL,
  `totassgrowrate` double DEFAULT NULL,
  `netincgrowrate` double DEFAULT NULL,
  `mainbusincgrowrate` double DEFAULT NULL,
  `totalshare` double DEFAULT NULL COMMENT '总股本 万股',
  `circskamt` double DEFAULT NULL,
  UNIQUE KEY `index1` (`symbol`,`month`,`year`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-12 10:19:08
