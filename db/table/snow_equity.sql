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
-- Table structure for table `equity`
--

DROP TABLE IF EXISTS `equity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `equity` (
  `symbol` varchar(25) COLLATE utf8_bin NOT NULL,
  `reportdate` int(11) NOT NULL,
  `begindate` int(11) NOT NULL,
  `totalshare` double DEFAULT NULL COMMENT '总股本(万股)',
  `skchgexp` varchar(45) COLLATE utf8_bin DEFAULT NULL COMMENT ' 股本变动说明',
  `circskamt` double DEFAULT NULL COMMENT '流通股(万股)  ',
  `ncircamt` double DEFAULT NULL COMMENT ' 未流通股',
  `bsk` double DEFAULT NULL COMMENT 'B股(万股)	  ',
  `bskchg` double DEFAULT NULL COMMENT 'B股变动数量(万股)   ',
  `circbamt` double DEFAULT NULL COMMENT ' 流通B股(万股) ',
  `cfcircbamt` double DEFAULT NULL COMMENT '已流通B股（含高管）(万股)',
  `skchgtype` varchar(45) COLLATE utf8_bin DEFAULT NULL COMMENT '股份变动类别  ',
  `originatorskamt` double DEFAULT NULL COMMENT '发起人股(万股)',
  `pstateamt` double DEFAULT NULL COMMENT ' 国家股(万股)   ',
  `pstatecorpamt` double DEFAULT NULL COMMENT '国有法人股(万股) ',
  `pdomecorpamt` double DEFAULT NULL COMMENT '境内法人股(万股) ',
  `pdomesocicorpamt` double DEFAULT NULL COMMENT '境内社会法人股(万股)  ',
  `exrightdate` int(11) DEFAULT NULL COMMENT ' 除权除息日         ',
  `exrightexp` varchar(45) COLLATE utf8_bin DEFAULT NULL COMMENT ' 除权日期股本说明 ',
  `circskrto` double DEFAULT NULL COMMENT '流通股合计占总股本比例(%)',
  `bsharerto` double DEFAULT NULL COMMENT '流通B股占总股本比例(%) ',
  `totalbsharerto` double DEFAULT NULL COMMENT ' B股合计占总股本比例(%)  ',
  UNIQUE KEY `index1` (`symbol`,`begindate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='股本变更表';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-12 10:19:06
