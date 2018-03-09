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

/*View structure for view index_symbollist */

/*!50001 DROP TABLE IF EXISTS `index_symbollist` */;
/*!50001 DROP VIEW IF EXISTS `index_symbollist` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`michael`@`%` SQL SECURITY DEFINER VIEW `index_symbollist` AS select `idx`.`symbol` AS `symbol`,`sp`.`index_name` AS `SP`,`tsx`.`index_name` AS `tsx`,`dow`.`index_name` AS `dow`,`nas`.`index_name` AS `Nasdaq`,`price`.`max_effective_date` AS `max_effective_date` from (((((((select distinct `stock_market`.`market.index_constituent`.`symbol` AS `symbol` from `stock_market`.`market.index_constituent` where ((`stock_market`.`market.index_constituent`.`start_date` <= curdate()) and (`stock_market`.`market.index_constituent`.`end_date` >= curdate()) and (`stock_market`.`market.index_constituent`.`index_name` <> 'TSX 60')))) `idx` left join `stock_market`.`market.index_constituent` `sp` on(((`idx`.`symbol` = `sp`.`symbol`) and (`sp`.`index_name` = 'S&P 500')))) left join `stock_market`.`market.index_constituent` `tsx` on(((`idx`.`symbol` = `tsx`.`symbol`) and (`tsx`.`index_name` = 'TSX 60')))) left join `stock_market`.`market.index_constituent` `dow` on(((`idx`.`symbol` = `dow`.`symbol`) and (`dow`.`index_name` = 'DOW 30')))) left join `stock_market`.`market.index_constituent` `nas` on(((`idx`.`symbol` = `nas`.`symbol`) and (`nas`.`index_name` = 'NASDAQ 100')))) left join (select `stock_market`.`market.stock_price`.`symbol` AS `symbol`,max(`stock_market`.`market.stock_price`.`effective_date`) AS `max_effective_date` from `stock_market`.`market.stock_price` group by `stock_market`.`market.stock_price`.`symbol`) `price` on((`idx`.`symbol` = `price`.`symbol`))) */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
