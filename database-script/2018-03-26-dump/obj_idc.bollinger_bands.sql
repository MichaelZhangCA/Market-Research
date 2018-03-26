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

/*View structure for view idc.bollinger_bands */

/*!50001 DROP TABLE IF EXISTS `idc.bollinger_bands` */;
/*!50001 DROP VIEW IF EXISTS `idc.bollinger_bands` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`michael`@`%` SQL SECURITY DEFINER VIEW `idc.bollinger_bands` AS select `idc.sma`.`sma_id` AS `sma_id`,`idc.sma`.`symbol` AS `symbol`,`idc.sma`.`effective_date` AS `effective_date`,`idc.sma`.`adj_close` AS `adj_close`,`idc.sma`.`period` AS `period`,`idc.sma`.`sma` AS `sma`,`idc.sma`.`stdev` AS `stdev`,`idc.sma`.`create_timestamp` AS `create_timestamp`,(`idc.sma`.`sma` + (2 * `idc.sma`.`stdev`)) AS `band_upper`,(`idc.sma`.`sma` - (2 * `idc.sma`.`stdev`)) AS `band_lower` from `idc.sma` where (`idc.sma`.`period` = 20) */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
