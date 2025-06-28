-- MySQL dump 10.9
--
-- Host: localhost    Database: ASV-Wortschatz-DB-Schema
-- ------------------------------------------------------
-- Server version	4.1.14-max ???
-- Based on default schema, default for corpora exports
-- tables: co_n, co_s, inv_w, inv_s, words, sentences, sentences_tok, sources, meta


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- CREATE Database
--

CREATE DATABASE `tur_wikipedia_2021_10K`;

USE `tur_wikipedia_2021_10K`;

--
-- Table structure for table `co_n`
--

DROP TABLE IF EXISTS `co_n`;
CREATE TABLE `co_n` (
  `w1_id` int(10) unsigned NOT NULL default '0',
  `w2_id` int(10) unsigned NOT NULL default '0',
  `freq` int(8) unsigned default NULL,
  `sig` float(8) default NULL,
  PRIMARY KEY `w1_w2` (`w1_id`,`w2_id`),
  KEY `w1_sig` (`w1_id`,`sig`),
  KEY `w2_sig` (`w2_id`,`sig`)
) ENGINE=MyISAM CHARSET=utf8mb4;


--
-- Table structure for table `co_s`
--

DROP TABLE IF EXISTS `co_s`;
CREATE TABLE `co_s` (
  `w1_id` int(10) unsigned NOT NULL default '0',
  `w2_id` int(10) unsigned NOT NULL default '0',
  `freq` int(8) unsigned default NULL,
  `sig` float(8) default NULL,
  PRIMARY KEY `w1_w2` (`w1_id`,`w2_id`),
  KEY `w1_sig` (`w1_id`,`sig`),
  KEY `w2_sig` (`w2_id`,`sig`)
) ENGINE=MyISAM CHARSET=utf8mb4;


--
-- Table structure for table `inv_so`
--

DROP TABLE IF EXISTS `inv_so`;
CREATE TABLE `inv_so` (
  `so_id` int(10) unsigned NOT NULL default '0',
  `s_id` int(10) unsigned NOT NULL default '0',
  KEY  `s_id` (`s_id`),
  KEY  `so_id` (`so_id`)
) ENGINE=MyISAM CHARSET=utf8mb4;


--
-- Table structure for table `inv_w`
--

DROP TABLE IF EXISTS `inv_w`;
CREATE TABLE `inv_w` (
  `w_id` int(10) unsigned NOT NULL default '0',
  `s_id` int(10) unsigned NOT NULL default '0',
  `pos` mediumint(2) unsigned NOT NULL default '0',
  KEY `w_id` (`w_id`),
  KEY `s_id` (`s_id`),
  KEY `w_s` (`w_id`,`s_id`)
) ENGINE=MyISAM CHARSET=utf8mb4;


--
-- Table structure for table `sentences`
--

DROP TABLE IF EXISTS `sentences`;
CREATE TABLE `sentences` (
  `s_id` int(10) unsigned NOT NULL auto_increment,
  `sentence` text NOT NULL,
  PRIMARY KEY `s_id` (`s_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;


--
-- Table structure for table `sources`
--

DROP TABLE IF EXISTS `sources`;
CREATE TABLE `sources` (
  `so_id` int(10) unsigned NOT NULL auto_increment,
  `source` varchar(255) default NULL,
  `date` date default NULL,
  PRIMARY KEY `so_id` (`so_id`),
  KEY `date` (`date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;


--
-- Table structure for table `words`
--

DROP TABLE IF EXISTS `words`;
CREATE TABLE `words` (
  `w_id` int(10) unsigned NOT NULL auto_increment,
  `word` varchar(255) character set utf8mb4 collate utf8mb4_bin NOT NULL,
  `freq` int(10) unsigned default NULL,
  PRIMARY KEY `w_id` (`w_id`),
  UNIQUE KEY `word` (`word`(250))
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;


--
-- Table structure for table `sentences_tagged`
--

DROP TABLE IF EXISTS `sentences_tagged`;
CREATE TABLE `sentences_tagged` (
  `s_id` int(10) unsigned NOT NULL,
  `sentence` text,
  PRIMARY KEY `s_id` (`s_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;


--
-- Table structure for table `words_pos_base`
--

DROP TABLE IF EXISTS `words_pos_base`;
CREATE TABLE `words_pos_base` (
  `w_id` int(10) unsigned NOT NULL DEFAULT '0',
  `word` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `pos` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `pos_ud17` varchar(64) SET utf8mb4 COLLATE utf8mb4_bin DEFAULT '',
  `base_form` varchar(256) SET utf8mb4 COLLATE utf8mb4_bin DEFAULT '',
  `freq` int(8) unsigned DEFAULT NULL,
  UNIQUE KEY `w_id` (`w_id`, `word`(128), `pos`, `base_form`(128)),
  KEY `i_w_id` (`w_id`),
  KEY `i_word` (`word`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;


--
-- Disable keys for import
--

ALTER TABLE `co_n` DISABLE KEYS;
ALTER TABLE `co_s` DISABLE KEYS;
ALTER TABLE `inv_so` DISABLE KEYS;
ALTER TABLE `inv_w` DISABLE KEYS;
ALTER TABLE `sentences` DISABLE KEYS;
ALTER TABLE `sources` DISABLE KEYS;
ALTER TABLE `words` DISABLE KEYS;
ALTER TABLE `sentences_tagged` DISABLE KEYS;
ALTER TABLE `words_pos_base` DISABLE KEYS;

--
-- Load data from local files
--

LOAD DATA LOCAL INFILE 'tur_wikipedia_2021_10K-words.txt' INTO TABLE words;
LOAD DATA LOCAL INFILE 'tur_wikipedia_2021_10K-sentences.txt' INTO TABLE sentences;
LOAD DATA LOCAL INFILE 'tur_wikipedia_2021_10K-co_s.txt' INTO TABLE co_s;
LOAD DATA LOCAL INFILE 'tur_wikipedia_2021_10K-co_n.txt' INTO TABLE co_n;
LOAD DATA LOCAL INFILE 'tur_wikipedia_2021_10K-inv_w.txt' INTO TABLE inv_w;
LOAD DATA LOCAL INFILE 'tur_wikipedia_2021_10K-inv_so.txt' INTO TABLE inv_so;
LOAD DATA LOCAL INFILE 'tur_wikipedia_2021_10K-sources.txt' INTO TABLE sources;

--
-- Enable keys after import
--

ALTER TABLE `co_n` ENABLE KEYS;
ALTER TABLE `co_s` ENABLE KEYS;
ALTER TABLE `inv_so` ENABLE KEYS;
ALTER TABLE `inv_w` ENABLE KEYS;
ALTER TABLE `sentences` ENABLE KEYS;
ALTER TABLE `sources` ENABLE KEYS;
ALTER TABLE `words` ENABLE KEYS;
ALTER TABLE `sentences_tagged` ENABLE KEYS;
ALTER TABLE `words_pos_base` ENABLE KEYS;


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
