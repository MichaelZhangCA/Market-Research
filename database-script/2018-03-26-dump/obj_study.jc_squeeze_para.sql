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

/*Table structure for table `study.jc_squeeze_para` */

DROP TABLE IF EXISTS `study.jc_squeeze_para`;

CREATE TABLE `study.jc_squeeze_para` (
  `para_name` varchar(20) NOT NULL,
  `sma_period` int(11) DEFAULT NULL,
  `dev_mode` varchar(10) DEFAULT NULL,
  `ema_period` int(11) DEFAULT NULL,
  `atr_period` int(11) DEFAULT NULL,
  `atr_mode` varchar(10) DEFAULT NULL,
  `trend_indicator` varchar(10) DEFAULT NULL,
  `trend_period` varchar(20) DEFAULT NULL,
  `wave_indicator` varchar(10) DEFAULT NULL,
  `wave_base_period` int(11) DEFAULT NULL,
  `wave_short_period` int(11) DEFAULT NULL,
  `wave_medium_period` int(11) DEFAULT NULL,
  `wave_long_period` int(11) DEFAULT NULL,
  `create_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`para_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `study.jc_squeeze_para` */

insert  into `study.jc_squeeze_para`(`para_name`,`sma_period`,`dev_mode`,`ema_period`,`atr_period`,`atr_mode`,`trend_indicator`,`trend_period`,`wave_indicator`,`wave_base_period`,`wave_short_period`,`wave_medium_period`,`wave_long_period`,`create_timestamp`) values 
('10 ATR',20,'std',20,10,'atr','MACD','12/26/9','MACD',8,34,89,233,'2018-03-19 22:09:04'),
('10 EMATR',20,'std',20,10,'ematr','MACD','12/26/9','MACD',8,34,89,233,'2018-03-19 22:04:46'),
('10ATR',20,'std',20,10,'atr','MACD','12/26/9','MACD',8,34,89,233,'2018-03-19 22:04:24'),
('14 ATR',20,'std',20,14,'atr','MACD','12/26/9','MACD',8,34,89,233,'2018-03-19 22:10:06'),
('14 EMATR',20,'std',20,14,'ematr','MACD','12/26/9','MACD',8,34,89,233,'2018-03-19 22:05:28'),
('14ATR',20,'std',20,14,'atr','MACD','12/26/9','MACD',8,34,89,233,'2018-03-19 21:56:30'),
('Default',20,'std',20,14,'ematr','MACD','12/26/9','MACD',8,34,89,233,'2018-03-13 09:31:36'),
('PPO',20,'std',20,14,'ematr','PPO','12/26/9','PPO',8,34,89,233,'2018-03-14 23:23:34');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
