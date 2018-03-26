/*
SQLyog Enterprise v12.5.1 (64 bit)
MySQL - 5.7.21-log : Database - stock_market
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`stock_market` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `stock_market`;

/*View structure for view idc.keltner_channels */

/*!50001 DROP TABLE IF EXISTS `idc.keltner_channels` */;
/*!50001 DROP VIEW IF EXISTS `idc.keltner_channels` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`michael`@`%` SQL SECURITY DEFINER VIEW `idc.keltner_channels` AS select `ema`.`symbol` AS `symbol`,`ema`.`effective_date` AS `effective_date`,`ema`.`ema20` AS `ema20`,`atr`.`atr14` AS `atr14`,(`ema`.`ema20` + `atr`.`atr14`) AS `atr1_upper`,(`ema`.`ema20` - `atr`.`atr14`) AS `atr1_lower`,(`ema`.`ema20` + (`atr`.`atr14` * 2)) AS `atr2_upper`,(`ema`.`ema20` - (`atr`.`atr14` * 2)) AS `atr2_lower`,(`ema`.`ema20` + (`atr`.`atr14` * 3)) AS `atr3_upper`,(`ema`.`ema20` - (`atr`.`atr14` * 3)) AS `atr3_lower` from (((select `stock_market`.`idc.ema`.`symbol` AS `symbol`,`stock_market`.`idc.ema`.`effective_date` AS `effective_date`,`stock_market`.`idc.ema`.`ema` AS `ema20` from `stock_market`.`idc.ema` where (`stock_market`.`idc.ema`.`period` = 20))) `ema` left join (select `stock_market`.`idc.atr`.`symbol` AS `symbol`,`stock_market`.`idc.atr`.`effective_date` AS `effective_date`,`stock_market`.`idc.atr`.`atr` AS `atr14` from `stock_market`.`idc.atr` where (`stock_market`.`idc.atr`.`period` = 14)) `atr` on(((`atr`.`symbol` = `ema`.`symbol`) and (`atr`.`effective_date` = `ema`.`effective_date`)))) */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
