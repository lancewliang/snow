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
-- Table structure for table `income`
--

DROP TABLE IF EXISTS `income`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `income` (
  `symbol` varchar(25) COLLATE utf8_bin NOT NULL,
  `compcode` varchar(25) COLLATE utf8_bin DEFAULT NULL,
  `publishdate` int(11) DEFAULT NULL,
  `begindate` int(11) DEFAULT NULL,
  `enddate` int(11) DEFAULT NULL,
  `reporttype` varchar(15) COLLATE utf8_bin DEFAULT NULL,
  `adjustdate` int(11) DEFAULT NULL,
  `accstacode` varchar(15) COLLATE utf8_bin DEFAULT NULL,
  `accstaname` varchar(15) COLLATE utf8_bin DEFAULT NULL,
  `biztotinco` double DEFAULT NULL,
  `bizinco` double DEFAULT NULL COMMENT '营业收入',
  `inteinco` double DEFAULT NULL COMMENT '利息收入',
  `earnprem` double DEFAULT NULL COMMENT '已赚保费',
  `pouninco` double DEFAULT NULL COMMENT '手续费及佣金收入',
  `realsale` double DEFAULT NULL COMMENT '房地产销售收入',
  `otherbizinco` double DEFAULT NULL COMMENT '其他业务收入	',
  `biztotincoitse` double DEFAULT NULL COMMENT '特殊处理本身不平营业总收入',
  `biztotincoform` double DEFAULT NULL COMMENT ' 特殊处理格式不同营业总收入',
  `biztotcost` double DEFAULT NULL COMMENT ' 营业总成本',
  `bizcost` double DEFAULT NULL COMMENT '营业成本',
  `inteexpe` double DEFAULT NULL COMMENT ' 利息支出',
  `pounexpe` double DEFAULT NULL COMMENT '手续费及佣金支出',
  `realsalecost` double DEFAULT NULL COMMENT '房地产销售成本',
  `deveexpe` double DEFAULT NULL COMMENT '研发费用',
  `surrgold` double DEFAULT NULL COMMENT '退保金',
  `compnetexpe` double DEFAULT NULL COMMENT ' 赔付支出净额',
  `contress` double DEFAULT NULL COMMENT '提取保险合同准备金净额',
  `polidiviexpe` double DEFAULT NULL COMMENT '保单红利支出',
  `reinexpe` double DEFAULT NULL COMMENT ' 分保费用',
  `otherbizcost` double DEFAULT NULL COMMENT '其他业务成本',
  `biztax` double DEFAULT NULL COMMENT '营业税金及附加',
  `salesexpe` double DEFAULT NULL COMMENT '销售费用',
  `manaexpe` double DEFAULT NULL COMMENT '管理费用',
  `finexpe` double DEFAULT NULL COMMENT '财务费用',
  `asseimpaloss` double DEFAULT NULL COMMENT '资产减值损失',
  `biztotcostitse` double DEFAULT NULL COMMENT '特殊处理本身不平营业总成本',
  `biztotcostform` double DEFAULT NULL COMMENT '特殊处理格式不同营业总成本',
  `valuechgloss` double DEFAULT NULL COMMENT '公允价值变动收益',
  `inveinco` double DEFAULT NULL COMMENT '投资收益',
  `assoinveprof` double DEFAULT NULL COMMENT '其中:对联营企业和合营企业的投资收益',
  `exchggain` double DEFAULT NULL COMMENT '汇兑收益',
  `futuloss` double DEFAULT NULL COMMENT '期货损益',
  `custinco` double DEFAULT NULL COMMENT '托管收益',
  `subsidyincome` double DEFAULT NULL COMMENT '补贴收入',
  `otherbizprof` double DEFAULT NULL COMMENT '其他业务利润',
  `bizprofitse` double DEFAULT NULL COMMENT '特殊处理本身不平营业利润,',
  `operprofform` double DEFAULT NULL COMMENT '特殊处理格式不同营业利润,',
  `perprofit` double DEFAULT NULL COMMENT '营业利润',
  `nonoreve` double DEFAULT NULL COMMENT '营业外收入',
  `nonoexpe` double DEFAULT NULL COMMENT '营业外支出,',
  `noncassetsdisl` double DEFAULT NULL COMMENT '非流动资产处置损失,',
  `proftotitse` double DEFAULT NULL COMMENT '特殊处理本身不平利润总额,',
  `proftotform` double DEFAULT NULL COMMENT '特殊处理格式不同利润总额,',
  `totprofit` double DEFAULT NULL COMMENT '利润总额,',
  `incotaxexpe` double DEFAULT NULL COMMENT '所得税费用,',
  `netpro1itse` double DEFAULT NULL COMMENT '特殊处理本身不平净利润,',
  `netpro1form` double DEFAULT NULL COMMENT '特殊处理格式不同净利润,',
  `netprofit` double DEFAULT NULL COMMENT '净利润',
  `parenetp` double DEFAULT NULL COMMENT '归属于母公司所有者的净利润',
  `mergeformnetprof` double DEFAULT NULL COMMENT '被合并方在合并前实现净利润',
  `unreinveloss` double DEFAULT NULL COMMENT '未确认投资损失,',
  `minysharrigh` double DEFAULT NULL COMMENT '少数股东损益',
  `netpro2itse` double DEFAULT NULL COMMENT ' 特殊处理本身不平净利润',
  `netpro2form` double DEFAULT NULL COMMENT ' 特殊处理格式不同净利润',
  `basiceps` double DEFAULT NULL COMMENT '基本每股收益',
  `dilutedeps` double DEFAULT NULL COMMENT '稀释每股收益',
  `compincoamt` double DEFAULT NULL COMMENT '综合收益总额',
  `parecompincoamt` double DEFAULT NULL COMMENT '归属于母公司所有者的综合收益总额',
  `minysharincoamt` double DEFAULT NULL COMMENT '归属于少数股东的综合收益总额'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='综合损益表';
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
