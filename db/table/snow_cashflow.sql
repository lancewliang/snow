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
-- Table structure for table `cashflow`
--

DROP TABLE IF EXISTS `cashflow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cashflow` (
  `compcode` varchar(25) COLLATE utf8_bin NOT NULL,
  `symbol` varchar(25) COLLATE utf8_bin DEFAULT NULL,
  `publishdate` int(11) DEFAULT NULL,
  `begindate` int(11) DEFAULT NULL,
  `enddate` int(11) DEFAULT NULL,
  `reporttype` varchar(15) COLLATE utf8_bin DEFAULT NULL,
  `adjustdate` int(11) DEFAULT NULL,
  `accstacode` varchar(15) COLLATE utf8_bin DEFAULT NULL,
  `accstaname` varchar(15) COLLATE utf8_bin DEFAULT NULL COMMENT '新会计准则',
  `laborgetcash` double DEFAULT NULL COMMENT '销售商品、提供劳务收到的现金,',
  `deponetr` double DEFAULT NULL COMMENT '客户存款和同业存放款项净增加额,',
  `bankloannetincr` double DEFAULT NULL COMMENT '向中央银行借款净增加额,',
  `fininstnetr` double DEFAULT NULL COMMENT '向其他金融机构拆入资金净增加额,',
  `inspremcash` double DEFAULT NULL COMMENT '收到原保险合同保费取得的现金,',
  `insnetc` double DEFAULT NULL COMMENT '收到再保险业务现金净额,',
  `savinetr` double DEFAULT NULL COMMENT '保户储金及投资款净增加额,',
  `disptradnetincr` double DEFAULT NULL COMMENT '处置交易性金融资产净增加额,',
  `charintecash` double DEFAULT NULL COMMENT '收取利息、手续费及佣金的现金,',
  `fdsborrnetr` double DEFAULT NULL COMMENT '拆入资金净增加额,',
  `repnetincr` double DEFAULT NULL COMMENT ' 回购业务资金净增加额,',
  `taxrefd` double DEFAULT NULL COMMENT '收到的税费返还,',
  `receotherbizcash` double DEFAULT NULL COMMENT ' 收到的其他与经营活动有关的现金,',
  `bizinflitse` double DEFAULT NULL COMMENT '特殊处理本身不平经营流入,',
  `bizinflform` double DEFAULT NULL COMMENT '特殊处理格式不同经营流入,',
  `bizcashinfl` double DEFAULT NULL COMMENT '经营活动现金流入小计,',
  `labopayc` double DEFAULT NULL COMMENT '购买商品、接受劳务支付的现金,',
  `loansnetr` double DEFAULT NULL COMMENT '客户贷款及垫款净增加额,',
  `tradepaymnetr` double DEFAULT NULL COMMENT '存放中央银行和同业款项净增加额,',
  `paycompgold` double DEFAULT NULL COMMENT ' 支付原保险合同赔付款项的现金,',
  `payintecash` double DEFAULT NULL COMMENT '支付利息、手续费及佣金的现金,',
  `payworkcash` double DEFAULT NULL COMMENT ' 支付给职工以及为职工支付的现金,',
  `paytax` double DEFAULT NULL COMMENT '支付的各项税费,',
  `payacticash` double DEFAULT NULL COMMENT '支付的其他与经营活动有关的现金,',
  `bizoutfitse` double DEFAULT NULL COMMENT '特殊处理本身不平经营流出,',
  `bizoutfform` double DEFAULT NULL COMMENT '特殊处理格式不同经营流出,',
  `bizcashoutf` double DEFAULT NULL COMMENT '经营活动现金流出小计,',
  `biznetitse` double DEFAULT NULL COMMENT '特殊处理本身不平经营净额',
  `biznetform` double DEFAULT NULL COMMENT '特殊处理格式不同经营净额',
  `mananetr` double DEFAULT NULL COMMENT '经营活动产生的现金流量净额,',
  `withinvgetcash` double DEFAULT NULL COMMENT '收回投资所收到的现金,',
  `inveretugetcash` double DEFAULT NULL COMMENT '取得投资收益收到的现金,',
  `fixedassetnetc` double DEFAULT NULL COMMENT '处置固定资产、无形资产和其他长期资产所回收的现金净额,',
  `subsnetc` double DEFAULT NULL COMMENT '处置子公司及其他营业单位收到的现金净额,',
  `receinvcash` double DEFAULT NULL COMMENT '收到的其他与投资活动有关的现金,',
  `reducashpled` double DEFAULT NULL COMMENT '减少质押和定期存款所收到的现金,',
  `invinflitse` double DEFAULT NULL COMMENT '特殊处理本身不平投资流入,',
  `invinffrom` double DEFAULT NULL COMMENT '特殊处理格式不同投资流入,',
  `invcashinfl` double DEFAULT NULL COMMENT ' 投资活动现金流入小计,',
  `acquassetcash` double DEFAULT NULL COMMENT '购建固定资产、无形资产和其他长期资产所支付的现金,',
  `invpayc` double DEFAULT NULL COMMENT ' 投资所支付的现金,',
  `loannetr` double DEFAULT NULL COMMENT '质押贷款净增加额,',
  `subspaynetcash` double DEFAULT NULL COMMENT '取得子公司及其他营业单位支付的现金净额,',
  `payinvecash` double DEFAULT NULL COMMENT '支付的其他与投资活动有关的现金,',
  `incrcashpled` double DEFAULT NULL COMMENT '增加质押和定期存款所支付的现金,',
  `invoutfitse` double DEFAULT NULL COMMENT '特殊处理本身不平投资流出,',
  `invoutfform` double DEFAULT NULL COMMENT ' 特殊处理格式不同投资流出,',
  `invcashoutf` double DEFAULT NULL COMMENT '投资活动现金流出小计,',
  `netinvitse` double DEFAULT NULL COMMENT '特殊处理本身不平投资净额,',
  `netinvform` double DEFAULT NULL COMMENT ' 特殊处理格式不同投资净额,',
  `invnetcashflow` double DEFAULT NULL COMMENT '投资活动产生的现金流量净额,',
  `invrececash` double DEFAULT NULL COMMENT ' 吸收投资收到的现金,',
  `subsrececash` double DEFAULT NULL COMMENT '其中：子公司吸收少数股东投资收到的现金,',
  `recefromloan` double DEFAULT NULL COMMENT '取得借款收到的现金,',
  `issbdrececash` double DEFAULT NULL COMMENT ' 发行债券收到的现金,',
  `recefincash` double DEFAULT NULL COMMENT '收到其他与筹资活动有关的现金,',
  `fininflitse` double DEFAULT NULL COMMENT '特殊处理本身不平筹资流入,',
  `fininflform` double DEFAULT NULL COMMENT '特殊处理格式不同筹资流入,',
  `fincashinfl` double DEFAULT NULL COMMENT '筹资活动现金流入小计,',
  `debtpaycash` double DEFAULT NULL COMMENT '偿还债务支付的现金,',
  `diviprofpaycash` double DEFAULT NULL COMMENT '分配股利、利润或偿付利息所支付的现金,',
  `subspaydivid` double DEFAULT NULL COMMENT '其中：子公司支付给少数股东的股利，利润,',
  `finrelacash` double DEFAULT NULL COMMENT ' 支付其他与筹资活动有关的现金,',
  `finoutfitse` double DEFAULT NULL COMMENT '特殊处理本身不平筹资流出,',
  `finoutfform` double DEFAULT NULL COMMENT '特殊处理格式不同筹资流出,',
  `fincashoutf` double DEFAULT NULL COMMENT '筹资活动现金流出小计,',
  `finnetitse` double DEFAULT NULL COMMENT '特殊处理本身不平筹资净额,',
  `finnetform` double DEFAULT NULL COMMENT ' 特殊处理格式不同筹资净额,',
  `finnetcflow` double DEFAULT NULL COMMENT '筹资活动产生的现金流量净,',
  `chgexchgchgs` double DEFAULT NULL COMMENT '汇率变动对现金及现金等价物的影响,',
  `netcashitse` double DEFAULT NULL COMMENT '特殊处理本身不平现金净额,',
  `netcashform` double DEFAULT NULL COMMENT '特殊处理格式不同现金净额,',
  `cashnetr` double DEFAULT NULL COMMENT '现金及现金等价物净增加额,',
  `inicashbala` double DEFAULT NULL COMMENT '期初现金及现金等价物余额,',
  `cashfinalitse` double DEFAULT NULL COMMENT '特殊处理本身不平现金期末,',
  `cashfinalform` double DEFAULT NULL COMMENT '特殊处理格式不同现金期末,',
  `finalcashbala` double DEFAULT NULL COMMENT '期末现金及现金等价物余额,',
  `netprofit` double DEFAULT NULL COMMENT '净利润,',
  `minysharrigh` double DEFAULT NULL COMMENT '少数股东权益,',
  `unreinveloss` double DEFAULT NULL COMMENT '未确认的投资损失,',
  `asseimpa` double DEFAULT NULL COMMENT ' 资产减值准备,',
  `assedepr` double DEFAULT NULL COMMENT ' 固定资产折旧、油气资产折耗、生产性物资折旧,',
  `realestadep` double DEFAULT NULL COMMENT ' 投资性房地产折旧、摊销,',
  `intaasseamor` double DEFAULT NULL COMMENT '无形资产摊销,',
  `longdefeexpenamor` double DEFAULT NULL COMMENT '长期待摊费用摊销,',
  `prepexpedecr` double DEFAULT NULL COMMENT '待摊费用的减少,',
  `accrexpeincr` double DEFAULT NULL COMMENT ' 预提费用的增加,',
  `dispfixedassetloss` double DEFAULT NULL COMMENT '处置固定资产、无形资产和其他长期资产的损失,',
  `fixedassescraloss` double DEFAULT NULL COMMENT ' 固定资产报废损失,',
  `valuechgloss` double DEFAULT NULL COMMENT '公允价值变动损失,',
  `defeincoincr` double DEFAULT NULL COMMENT '递延收益增加（减：减少）,',
  `estidebts` double DEFAULT NULL COMMENT '预计负债,',
  `finexpe` double DEFAULT NULL COMMENT ' 财务费用,',
  `inveloss` double DEFAULT NULL COMMENT '投资损失,',
  `defetaxassetdecr` double DEFAULT NULL COMMENT '递延所得税资产减少,',
  `defetaxliabincr` double DEFAULT NULL COMMENT ' 递延所得税负债增加,',
  `inveredu` double DEFAULT NULL COMMENT '存货的减少,',
  `receredu` double DEFAULT NULL COMMENT '经营性应收项目的减少,',
  `payaincr` double DEFAULT NULL COMMENT '经营性应付项目的增加,',
  `unseparachg` double DEFAULT NULL COMMENT '已完工尚未结算款的减少(减:增加)	,',
  `unfiparachg` double DEFAULT NULL COMMENT ' 已结算尚未完工款的增加(减:减少)	,',
  `other` double DEFAULT NULL COMMENT '其他,',
  `biznetscheitse` double DEFAULT NULL COMMENT ' 特殊处理本身不平经营净额附表,',
  `biznetscheform` double DEFAULT NULL COMMENT '特殊处理格式不同经营净额附表,',
  `biznetcflow` double DEFAULT NULL COMMENT '经营活动产生现金流量净额,',
  `debtintocapi` double DEFAULT NULL COMMENT '债务转为资本,',
  `expiconvbd` double DEFAULT NULL COMMENT '一年内到期的可转换公司债券,',
  `finfixedasset` double DEFAULT NULL COMMENT ' 融资租入固定资产,',
  `cashfinalbala` double DEFAULT NULL COMMENT '现金的期末余额,',
  `cashopenbala` double DEFAULT NULL COMMENT '现金的期初余额,',
  `equfinalbala` double DEFAULT NULL COMMENT ' 现金等价物的期末余额,',
  `equopenbala` double DEFAULT NULL COMMENT ' 现金等价物的期初余额,',
  `netcashscheitse` double DEFAULT NULL COMMENT '特殊处理本身不平现金净额附表,',
  `netcashscheform` double DEFAULT NULL COMMENT '特殊处理格式不同现金净额附表,',
  `cashneti` double DEFAULT NULL,
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP
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

-- Dump completed on 2020-02-12 10:19:07
