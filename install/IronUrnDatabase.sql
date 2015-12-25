-- --------------------------------------------------------
-- Host:                         10.1.2.11
-- Server version:               5.6.27-0ubuntu0.14.04.1-log - (Ubuntu)
-- Server OS:                    debian-linux-gnu
-- HeidiSQL Version:             9.3.0.4984
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping structure for table iron_urn.ExternalSystem
CREATE TABLE IF NOT EXISTS `ExternalSystem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `urlPrefix` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table iron_urn.ObjectType
CREATE TABLE IF NOT EXISTS `ObjectType` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table iron_urn.UrlRule
CREATE TABLE IF NOT EXISTS `UrlRule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `externalSystem_id` int(11) NOT NULL,
  `objectType_id` int(11) NOT NULL,
  `url` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_UrlRule_ExternalSystem` (`externalSystem_id`),
  KEY `FK_UrlRule_ObjectType` (`objectType_id`),
  CONSTRAINT `FK_UrlRule_ExternalSystem` FOREIGN KEY (`externalSystem_id`) REFERENCES `ExternalSystem` (`id`),
  CONSTRAINT `FK_UrlRule_ObjectType` FOREIGN KEY (`objectType_id`) REFERENCES `ObjectType` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
