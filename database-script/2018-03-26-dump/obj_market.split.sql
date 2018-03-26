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

/*Table structure for table `market.split` */

DROP TABLE IF EXISTS `market.split`;

CREATE TABLE `market.split` (
  `split_id` int(11) NOT NULL AUTO_INCREMENT,
  `symbol` varchar(10) DEFAULT NULL,
  `exdate` date DEFAULT NULL,
  `declare_date` date DEFAULT NULL,
  `record_date` date DEFAULT NULL,
  `payment_date` date DEFAULT NULL,
  `ratio` decimal(10,6) DEFAULT NULL,
  `to_factor` decimal(4,2) DEFAULT NULL,
  `for_factor` decimal(4,2) DEFAULT NULL,
  `create_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`split_id`),
  UNIQUE KEY `idx_unique` (`symbol`,`exdate`),
  KEY `idx_symbol` (`symbol`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

/*Data for the table `market.split` */

insert  into `market.split`(`split_id`,`symbol`,`exdate`,`declare_date`,`record_date`,`payment_date`,`ratio`,`to_factor`,`for_factor`,`create_timestamp`) values 
(21,'HSIC','2017-09-15','2017-08-16','2017-09-01','2017-09-14',0.500000,2.00,1.00,'2018-03-26 17:24:39'),
(22,'ISRG','2017-10-06','2017-08-11','2017-09-29','2017-10-05',0.333333,3.00,1.00,'2018-03-26 17:24:39'),
(23,'BF.B','2018-03-01','2018-01-23','2018-02-07','2018-02-28',0.800000,5.00,4.00,'2018-03-26 17:24:40'),
(24,'LEN','2017-11-09','2017-10-30','2017-11-10','2017-11-27',0.980392,51.00,50.00,'2018-03-26 17:24:41');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
