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

/*Table structure for table `study.jc_squeeze` */

DROP TABLE IF EXISTS `study.jc_squeeze`;

CREATE TABLE `study.jc_squeeze` (
  `jc_squeeze_id` int(11) NOT NULL AUTO_INCREMENT,
  `para_name` varchar(20) DEFAULT NULL,
  `symbol` varchar(10) DEFAULT NULL,
  `effective_date` date DEFAULT NULL,
  `bb_middle` decimal(12,4) DEFAULT NULL,
  `bb_upper` decimal(12,4) DEFAULT NULL,
  `bb_lower` decimal(12,4) DEFAULT NULL,
  `kc_middle` decimal(12,4) DEFAULT NULL,
  `kc_upper` decimal(12,4) DEFAULT NULL,
  `kc_lower` decimal(12,4) DEFAULT NULL,
  `trend` decimal(12,4) DEFAULT NULL,
  `wavea` decimal(12,4) DEFAULT NULL,
  `waveb` decimal(12,4) DEFAULT NULL,
  `wavec` decimal(12,4) DEFAULT NULL,
  `create_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`jc_squeeze_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3352972 DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
