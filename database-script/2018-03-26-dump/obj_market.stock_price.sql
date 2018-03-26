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

/*Table structure for table `market.stock_price` */

DROP TABLE IF EXISTS `market.stock_price`;

CREATE TABLE `market.stock_price` (
  `stock_price_id` int(11) NOT NULL AUTO_INCREMENT,
  `symbol` varchar(10) DEFAULT NULL,
  `effective_date` date DEFAULT NULL,
  `open` decimal(12,6) DEFAULT NULL,
  `high` decimal(12,6) DEFAULT NULL,
  `low` decimal(12,6) DEFAULT NULL,
  `close` decimal(12,6) DEFAULT NULL,
  `volume` decimal(12,2) DEFAULT NULL,
  `ex_dividend` decimal(6,2) DEFAULT NULL,
  `split_ratio` decimal(4,2) DEFAULT NULL,
  `adj_open` decimal(12,6) DEFAULT NULL,
  `adj_high` decimal(12,6) DEFAULT NULL,
  `adj_low` decimal(12,6) DEFAULT NULL,
  `adj_close` decimal(12,6) DEFAULT NULL,
  `adj_volume` decimal(12,2) DEFAULT NULL,
  `create_timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`stock_price_id`),
  UNIQUE KEY `idx_unique` (`symbol`,`effective_date`),
  KEY `idx_symbol` (`symbol`)
) ENGINE=InnoDB AUTO_INCREMENT=4150166 DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
