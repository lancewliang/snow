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
-- Table structure for table `mfinancialindex`
--

DROP TABLE IF EXISTS `mfinancialindex`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mfinancialindex` (
  `compcode` varchar(25) COLLATE utf8_bin NOT NULL,
  `symbol` varchar(25) COLLATE utf8_bin DEFAULT NULL,
  `reportdate` int(11) DEFAULT NULL,
  `basiceps` double DEFAULT NULL COMMENT ' 基本每股收益',
  `naps` double DEFAULT NULL COMMENT '每股净资产',
  `opercashpershare` double DEFAULT NULL COMMENT '每股现金流',
  `peropecashpershare` double DEFAULT NULL COMMENT '每股经营性现金流 ',
  `weightedroe` double DEFAULT NULL COMMENT '净资产收益率(加权)(%) ',
  `mainbusincgrowrate` double DEFAULT NULL COMMENT '主营业务收入增长率(%)',
  `netincgrowrate` double DEFAULT NULL COMMENT '净利润增长率(%)',
  `totassgrowrate` double DEFAULT NULL COMMENT '总资产增长率(%)',
  `salegrossprofitrto` double DEFAULT NULL COMMENT '总资产增长率(%)',
  `mainbusiincome` double DEFAULT NULL COMMENT '主营业务收入 ',
  `mainbusiprofit` double DEFAULT NULL COMMENT '主营业务利润',
  `totprofit` double DEFAULT NULL COMMENT '利润总额 ',
  `netprofit` double DEFAULT NULL COMMENT '净利润',
  `totalassets` double DEFAULT NULL COMMENT '资产总额',
  `totalliab` double DEFAULT NULL COMMENT ' 负债总额  ',
  `totsharequi` double DEFAULT NULL COMMENT '股东权益合计 ',
  `operrevenue` double DEFAULT NULL COMMENT '经营活动产生的现金流量净额',
  `invnetcashflow` double DEFAULT NULL COMMENT '投资活动产生的现金流量净额',
  `finnetcflow` double DEFAULT NULL COMMENT '筹资活动产生的现金流量净额',
  `chgexchgchgs` double DEFAULT NULL COMMENT '汇率变动对现金及现金等价物的影响',
  `cashnetr` double DEFAULT NULL COMMENT '现金及现金等价物净增加额',
  `cashequfinbal` double DEFAULT NULL COMMENT '期末现金及现金等价物余额',
  UNIQUE KEY `index1` (`symbol`,`reportdate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='主要财务指标';
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
