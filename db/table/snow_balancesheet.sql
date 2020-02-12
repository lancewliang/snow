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
-- Table structure for table `balancesheet`
--

DROP TABLE IF EXISTS `balancesheet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `balancesheet` (
  `compcode` varchar(25) COLLATE utf8_bin NOT NULL,
  `symbol` varchar(25) COLLATE utf8_bin NOT NULL,
  `publishdate` int(11) DEFAULT NULL COMMENT ' 报表日期     ',
  `reportdate` int(11) DEFAULT NULL,
  `reporttype` varchar(15) COLLATE utf8_bin DEFAULT NULL,
  `adjustdate` int(11) DEFAULT NULL,
  `curfds` double DEFAULT NULL COMMENT ' 货币资金',
  `tradfinasset` double DEFAULT NULL COMMENT '交易性金融资产,',
  `notesrece` double DEFAULT NULL COMMENT '应收票据,',
  `accorece` double DEFAULT NULL COMMENT '应收账款,',
  `prep` double DEFAULT NULL COMMENT '预付款项,',
  `premrece` double DEFAULT NULL COMMENT '应收保费,',
  `dividrece` double DEFAULT NULL COMMENT '应收股利,',
  `otherrece` double DEFAULT NULL COMMENT '其他应收款,',
  `expotaxrebarece` double DEFAULT NULL COMMENT '应收出口退税,',
  `subsrece` double DEFAULT NULL COMMENT '应收补贴款,',
  `margrece` double DEFAULT NULL COMMENT '应收保证金,',
  `intelrece` double DEFAULT NULL COMMENT '内部应收款,',
  `inve` double DEFAULT NULL COMMENT '存货,',
  `prepexpe` double DEFAULT NULL COMMENT '待摊费用,',
  `unseg` double DEFAULT NULL,
  `expinoncurrasset` double DEFAULT NULL COMMENT ' 一年内到期的非流动资产,',
  `othercurrasse` double DEFAULT NULL COMMENT ' 其他流动资产,',
  `currassetitse` double DEFAULT NULL COMMENT '特殊处理本身不平流动资产,',
  `currasseform` double DEFAULT NULL COMMENT '特殊处理格式不同流动资产,',
  `totcurrasset` double DEFAULT NULL COMMENT '流动资产合计,',
  `lendandloan` double DEFAULT NULL COMMENT '发放贷款及垫款,',
  `avaisellasse` double DEFAULT NULL COMMENT '可供出售金融资产,',
  `holdinvedue` double DEFAULT NULL COMMENT '持有至到期投资,',
  `longrece` double DEFAULT NULL COMMENT '长期应收款,',
  `equiinve` double DEFAULT NULL COMMENT '长期股权投资,',
  `otherlonginve` double DEFAULT NULL COMMENT ' 其他长期投资,',
  `inveprop` double DEFAULT NULL COMMENT ' 投资性房地产,',
  `fixedasseimmo` double DEFAULT NULL COMMENT '固定资产原值,',
  `accudepr` double DEFAULT NULL COMMENT '累计折旧,',
  `fixedassenetw` double DEFAULT NULL COMMENT '固定资产净值,',
  `fixedasseimpa` double DEFAULT NULL COMMENT '固定资产减值准备,',
  `fixedassenet` double DEFAULT NULL COMMENT ' 固定资产净额,',
  `consprog` double DEFAULT NULL COMMENT ' 在建工程,',
  `engimate` double DEFAULT NULL COMMENT '工程物资,',
  `fixedasseclea` double DEFAULT NULL COMMENT '固定资产清理,',
  `prodasse` double DEFAULT NULL COMMENT '生产性生物资产,',
  `comasse` double DEFAULT NULL COMMENT '公益性生物资产,',
  `hydrasset` double DEFAULT NULL COMMENT ' 油气资产,',
  `intaasset` double DEFAULT NULL COMMENT '无形资产,',
  `deveexpe` double DEFAULT NULL COMMENT '开发支出,',
  `goodwill` double DEFAULT NULL COMMENT '商誉,',
  `logprepexpe` double DEFAULT NULL COMMENT ' 长期待摊费用,',
  `tradshartrad` double DEFAULT NULL COMMENT '股权分置流通权,',
  `defetaxasset` double DEFAULT NULL COMMENT '递延所得税资产,',
  `othernoncasse` double DEFAULT NULL COMMENT '其他非流动资产,',
  `noncasseitse` double DEFAULT NULL COMMENT ' 特殊处理本身不平非流动资产,',
  `noncasseform` double DEFAULT NULL COMMENT '特殊处理格式不同非流动资产,',
  `totalnoncassets` double DEFAULT NULL COMMENT '非流动资产合计,',
  `totassetitse` double DEFAULT NULL COMMENT '特殊处理本身不平总资产,',
  `totalasseform` double DEFAULT NULL COMMENT '特殊处理格式不同总资产,',
  `totasset` double DEFAULT NULL COMMENT '资产总计,',
  `shorttermborr` double DEFAULT NULL COMMENT '短期借款,',
  `tradfinliab` double DEFAULT NULL COMMENT '交易性金融负债,',
  `notespaya` double DEFAULT NULL COMMENT '应付票据,',
  `accopaya` double DEFAULT NULL COMMENT '应付账款,',
  `advapaym` double DEFAULT NULL COMMENT '预收款项,',
  `copeworkersal` double DEFAULT NULL COMMENT '应付职工薪酬,',
  `taxespaya` double DEFAULT NULL COMMENT '应交税费,',
  `intepaya` double DEFAULT NULL COMMENT ' 应付利息,',
  `divipaya` double DEFAULT NULL COMMENT ' 应付股利,',
  `otherfeepaya` double DEFAULT NULL COMMENT '其他应交款,',
  `margrequ` double DEFAULT NULL COMMENT ' 应付保证金,',
  `intelpay` double DEFAULT NULL COMMENT ' 内部应付款,',
  `otherpay` double DEFAULT NULL COMMENT '其他应付款,',
  `accrexpe` double DEFAULT NULL COMMENT '预提费用,',
  `expecurrliab` double DEFAULT NULL COMMENT ' 预计流动负债,',
  `copewithreinrece` double DEFAULT NULL COMMENT ' 应付分保账款,',
  `inteticksett` double DEFAULT NULL COMMENT ' 国际票证结算,',
  `dometicksett` double DEFAULT NULL COMMENT ' 国内票证结算,',
  `defereve` double DEFAULT NULL COMMENT '一年内的递延收益,',
  `shorttermbdspaya` double DEFAULT NULL COMMENT '应付短期债券,',
  `duenoncliab` double DEFAULT NULL COMMENT '一年内到期的非流动负债,',
  `othercurreliabi` double DEFAULT NULL COMMENT ' 其他流动负债,',
  `currliabitse` double DEFAULT NULL COMMENT '特殊处理本身不平流动负债,',
  `currliabform` double DEFAULT NULL COMMENT '特殊处理格式不同流动负债',
  `totalcurrliab` double DEFAULT NULL COMMENT '流动负债合计,',
  `longborr` double DEFAULT NULL COMMENT '长期借款,',
  `bdspaya` double DEFAULT NULL COMMENT ' 应付债券,',
  `longpaya` double DEFAULT NULL COMMENT '长期应付款,',
  `specpaya` double DEFAULT NULL COMMENT ' 专项应付款,',
  `expenoncliab` double DEFAULT NULL COMMENT '预计非流动负债,',
  `longdefeinco` double DEFAULT NULL COMMENT '长期递延收益,',
  `defeincotaxliab` double DEFAULT NULL COMMENT ' 递延所得税负债,',
  `othernoncliabi` double DEFAULT NULL COMMENT '其他非流动负债,',
  `longliabitse` double DEFAULT NULL COMMENT ' 特殊处理本身不平长期负债,',
  `longliabform` double DEFAULT NULL COMMENT ' 特殊处理格式不同长期负债,',
  `totalnoncliab` double DEFAULT NULL COMMENT '非流动负债合计,',
  `totliabitse` double DEFAULT NULL COMMENT '特殊处理本身不平负债合计,',
  `totliabform` double DEFAULT NULL COMMENT '特殊处理格式不同负债合计,',
  `totliab` double DEFAULT NULL COMMENT '负债合计,',
  `paidincapi` double DEFAULT NULL COMMENT '实收资本(或股本),',
  `capisurp` double DEFAULT NULL COMMENT '资本公积,',
  `treastk` double DEFAULT NULL COMMENT '减：库存股,',
  `specrese` double DEFAULT NULL COMMENT '专项储备,',
  `rese` double DEFAULT NULL COMMENT ' 盈余公积,',
  `generiskrese` double DEFAULT NULL COMMENT '一般风险准备,',
  `unreinveloss` double DEFAULT NULL COMMENT '未确定的投资损失,',
  `undiprof` double DEFAULT NULL COMMENT '未分配利润,',
  `topaycashdivi` double DEFAULT NULL COMMENT '拟分配现金股利,',
  `curtrandiff` double DEFAULT NULL COMMENT ' 外币报表折算差额,',
  `sharrighitse` double DEFAULT NULL COMMENT '特殊处理本身不平股东权益,',
  `sharrightform` double DEFAULT NULL COMMENT '特殊处理格式不同股东权益,',
  `paresharrigh` double DEFAULT NULL COMMENT '归属于母公司股东权益合计,',
  `minysharrigh` double DEFAULT NULL COMMENT '少数股东权益,',
  `righaggritse` double DEFAULT NULL COMMENT '特殊处理本身不平股东权益,',
  `rightaggrform` double DEFAULT NULL COMMENT '特殊处理格式不平股东权益,',
  `righaggr` double DEFAULT NULL COMMENT ' 所有者权益(或股东权益)合计,',
  `rightotitse` double DEFAULT NULL COMMENT '特殊处理本身不平负债及权益,',
  `rightotform` double DEFAULT NULL COMMENT '特殊处理格式不同负债及权益,',
  `totliabsharequi` double DEFAULT NULL COMMENT ' 负债和所有者权益,',
  `settresedepo` double DEFAULT NULL COMMENT '结算备付金,',
  `plac` double DEFAULT NULL COMMENT '拆出资金,',
  `derifinaasset` double DEFAULT NULL COMMENT '衍生金融资产,',
  `reinrece` double DEFAULT NULL COMMENT '应收分保账款,',
  `reincontrese` double DEFAULT NULL COMMENT '应收分保合同准备金,',
  `purcresaasset` double DEFAULT NULL COMMENT ' 买入返售金融资产,',
  `cenbankborr` double DEFAULT NULL COMMENT '向中央银行借款,',
  `deposit` double DEFAULT NULL COMMENT '吸收存款及同业存放,',
  `fdsborr` double DEFAULT NULL COMMENT '拆入资金,',
  `deriliab` double DEFAULT NULL COMMENT ' 衍生金融负债,',
  `sellrepasse` double DEFAULT NULL COMMENT ' 卖出回购金融资产款,',
  `copepoun` double DEFAULT NULL COMMENT '应付手续费及佣金,',
  `insucontrese` double DEFAULT NULL COMMENT '保险合同准备金,',
  `actitradsecu` double DEFAULT NULL COMMENT '代理买卖证券款,',
  `actiundesecu` double DEFAULT NULL COMMENT '代理承销证券款'
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

-- Dump completed on 2020-02-12 10:19:05
