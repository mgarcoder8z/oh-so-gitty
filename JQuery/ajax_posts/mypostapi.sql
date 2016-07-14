-- MySQL dump 10.13  Distrib 5.7.12, for osx10.9 (x86_64)
--
-- Host: localhost    Database: mypostapi
-- ------------------------------------------------------
-- Server version	5.5.42

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
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=204 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES (1,'This is a sample post','0000-00-00 00:00:00','0000-00-00 00:00:00'),(2,'this is an updated second message post','0000-00-00 00:00:00','0000-00-00 00:00:00'),(3,'tis is a third post','0000-00-00 00:00:00','0000-00-00 00:00:00'),(4,'type a message here','2016-07-12 18:54:50','2016-07-12 18:54:50'),(5,'type a post','2016-07-12 18:56:10','2016-07-12 18:56:10'),(6,'type a message here','2016-07-12 18:56:57','2016-07-12 18:56:57'),(7,'type a post here','2016-07-12 18:57:27','2016-07-12 18:57:27'),(8,'type a post here','2016-07-12 19:00:18','2016-07-12 19:00:18'),(9,'type a post','2016-07-12 19:00:58','2016-07-12 19:00:58'),(10,'type a post here','2016-07-12 19:11:13','2016-07-12 19:11:13'),(11,'type a message and see if it gets in the box','2016-07-12 19:20:36','2016-07-12 19:20:36'),(12,'type a messahe','2016-07-12 19:22:41','2016-07-12 19:22:41'),(13,'type a new message hope it works','2016-07-12 19:25:10','2016-07-12 19:25:10'),(14,'this is a post','2016-07-12 19:39:05','2016-07-12 19:39:05'),(15,'post a very new message','2016-07-12 20:03:08','2016-07-12 20:03:08'),(16,'try this again','2016-07-12 20:04:30','2016-07-12 20:04:30'),(17,'test this again','2016-07-12 20:10:09','2016-07-12 20:10:09'),(18,'type a new message','2016-07-12 20:10:47','2016-07-12 20:10:47'),(19,'try this again','2016-07-12 20:11:31','2016-07-12 20:11:31'),(20,'please work','2016-07-12 20:12:34','2016-07-12 20:12:34'),(200,'ok try this again','2016-07-13 22:19:07','2016-07-13 22:19:07'),(201,'a new post should appear first','2016-07-13 22:23:36','2016-07-13 22:23:36'),(202,'new post','2016-07-13 22:24:35','2016-07-13 22:24:35'),(203,'add a note july 13','2016-07-13 22:26:55','2016-07-13 22:26:55');
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-07-13 22:28:23
