-- MySQL dump 10.13  Distrib 8.1.0, for macos13.3 (arm64)
--
-- Host: localhost    Database: temp
-- ------------------------------------------------------
-- Server version	8.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Assigned`
--

DROP TABLE IF EXISTS `Assigned`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Assigned` (
  `Soldier_id` int DEFAULT NULL,
  `Mess_id` int DEFAULT NULL,
  `Duty_s_no` int DEFAULT NULL,
  `Shift_s_no` int DEFAULT NULL,
  KEY `Soldier_id` (`Soldier_id`),
  KEY `Mess_id` (`Mess_id`),
  KEY `Duty_s_no` (`Duty_s_no`),
  KEY `Shift_s_no` (`Shift_s_no`),
  CONSTRAINT `assigned_ibfk_1` FOREIGN KEY (`Soldier_id`) REFERENCES `Soldiers` (`Soldier_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `assigned_ibfk_2` FOREIGN KEY (`Mess_id`) REFERENCES `Mess` (`Mess_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `assigned_ibfk_3` FOREIGN KEY (`Duty_s_no`) REFERENCES `Duties` (`Duty_s_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `assigned_ibfk_4` FOREIGN KEY (`Shift_s_no`) REFERENCES `Shifts` (`Shift_s_no`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Assigned`
--

LOCK TABLES `Assigned` WRITE;
/*!40000 ALTER TABLE `Assigned` DISABLE KEYS */;
INSERT INTO `Assigned` VALUES (12,2,121,121),(13,1,122,122),(14,1,123,123),(15,3,124,124),(16,3,125,125);
/*!40000 ALTER TABLE `Assigned` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Barracks`
--

DROP TABLE IF EXISTS `Barracks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Barracks` (
  `Barrack_id` int NOT NULL,
  `Last_maintainance_date` date DEFAULT NULL,
  `Landline_no` bigint DEFAULT NULL,
  `Security_prsnl_id` int DEFAULT NULL,
  `Sector_id` int DEFAULT NULL,
  `Commander_id` int DEFAULT NULL,
  PRIMARY KEY (`Barrack_id`),
  KEY `Sector_id` (`Sector_id`),
  KEY `Commander_id` (`Commander_id`),
  KEY `Security_prsnl_id` (`Security_prsnl_id`),
  CONSTRAINT `barracks_ibfk_1` FOREIGN KEY (`Sector_id`) REFERENCES `Sectors` (`Sector_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `barracks_ibfk_2` FOREIGN KEY (`Commander_id`) REFERENCES `Soldiers` (`Soldier_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `barracks_ibfk_3` FOREIGN KEY (`Security_prsnl_id`) REFERENCES `Security_personnel` (`Security_prsnl_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `barracks_chk_1` CHECK ((length(`Landline_no`) = 10))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Barracks`
--

LOCK TABLES `Barracks` WRITE;
/*!40000 ALTER TABLE `Barracks` DISABLE KEYS */;
INSERT INTO `Barracks` VALUES (1,'2023-10-02',1876543621,20,11,14),(2,'2023-10-05',8376452122,21,11,14),(3,'2023-02-10',1239876523,22,22,14),(4,'2023-02-09',1276342564,23,22,14),(5,'2023-02-15',1298765345,24,33,14);
/*!40000 ALTER TABLE `Barracks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Bunk_bed`
--

DROP TABLE IF EXISTS `Bunk_bed`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Bunk_bed` (
  `Barrack_id` int NOT NULL,
  `Bb_s_no` int NOT NULL,
  `Status` enum('empty','occupied') DEFAULT NULL,
  `Room_no` int NOT NULL,
  `Floor_no` int NOT NULL,
  `Soldier_id` int DEFAULT NULL,
  PRIMARY KEY (`Barrack_id`,`Bb_s_no`,`Floor_no`,`Room_no`),
  KEY `Soldier_id` (`Soldier_id`),
  CONSTRAINT `bunk_bed_ibfk_1` FOREIGN KEY (`Barrack_id`) REFERENCES `Barracks` (`Barrack_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `bunk_bed_ibfk_2` FOREIGN KEY (`Soldier_id`) REFERENCES `Soldiers` (`Soldier_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bunk_bed`
--

LOCK TABLES `Bunk_bed` WRITE;
/*!40000 ALTER TABLE `Bunk_bed` DISABLE KEYS */;
INSERT INTO `Bunk_bed` VALUES (1,121,'empty',3,302,16),(2,122,'occupied',3,303,13),(3,123,'occupied',3,304,12),(4,124,'empty',4,402,15),(5,125,'occupied',4,405,14);
/*!40000 ALTER TABLE `Bunk_bed` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Complaints`
--

DROP TABLE IF EXISTS `Complaints`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Complaints` (
  `Complaint_no` int NOT NULL,
  `Type` enum('Mess','Infrastructure','Officials') DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Status` enum('solved','pending') DEFAULT NULL,
  `Soldier_id` int NOT NULL,
  PRIMARY KEY (`Complaint_no`,`Soldier_id`),
  KEY `Soldier_id` (`Soldier_id`),
  CONSTRAINT `complaints_ibfk_1` FOREIGN KEY (`Soldier_id`) REFERENCES `Soldiers` (`Soldier_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Complaints`
--

LOCK TABLES `Complaints` WRITE;
/*!40000 ALTER TABLE `Complaints` DISABLE KEYS */;
/*!40000 ALTER TABLE `Complaints` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Credentials`
--

DROP TABLE IF EXISTS `Credentials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Credentials` (
  `Govt_email_id` varchar(255) NOT NULL,
  `Username` varchar(30) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `User_type` enum('Admin','User') NOT NULL,
  `Soldier_id` int NOT NULL,
  PRIMARY KEY (`Govt_email_id`),
  KEY `Soldier_id` (`Soldier_id`),
  CONSTRAINT `credentials_ibfk_1` FOREIGN KEY (`Soldier_id`) REFERENCES `Soldiers` (`Soldier_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `credentials_chk_1` CHECK ((`Govt_email_id` like _utf8mb4'%@%.gov.in'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Credentials`
--

LOCK TABLES `Credentials` WRITE;
/*!40000 ALTER TABLE `Credentials` DISABLE KEYS */;
INSERT INTO `Credentials` VALUES ('ketaki.shetye@2.gov.in','k.s','k.s','User',13),('maitreya.chitale@5.gov.in','m.c','m.c','User',16),('prabhav.shetty@4.gov.in','p.s','p.s','User',15),('sujal.deoda@3.gov.in','s.d','s.d','User',14),('vinit.mehta@1.gov.in','v.m','v.m','Admin',12);
/*!40000 ALTER TABLE `Credentials` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Dependen_ph_no`
--

DROP TABLE IF EXISTS `Dependen_ph_no`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Dependen_ph_no` (
  `Soldier_id` int NOT NULL,
  `Phone_no` bigint NOT NULL,
  PRIMARY KEY (`Phone_no`,`Soldier_id`),
  KEY `Soldier_id` (`Soldier_id`),
  CONSTRAINT `dependen_ph_no_ibfk_1` FOREIGN KEY (`Soldier_id`) REFERENCES `Soldiers` (`Soldier_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `dependen_ph_no_chk_1` CHECK ((length(`Phone_no`) = 10))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dependen_ph_no`
--

LOCK TABLES `Dependen_ph_no` WRITE;
/*!40000 ALTER TABLE `Dependen_ph_no` DISABLE KEYS */;
INSERT INTO `Dependen_ph_no` VALUES (12,8987654484),(13,4204209876),(14,6969987654),(15,6876596969),(16,6942087653);
/*!40000 ALTER TABLE `Dependen_ph_no` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Dependents`
--

DROP TABLE IF EXISTS `Dependents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Dependents` (
  `Soldier_id` int NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Sex` enum('M','F') DEFAULT NULL,
  `House_no` int DEFAULT NULL,
  `Street_no` int DEFAULT NULL,
  `Area` varchar(50) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  `State` varchar(50) DEFAULT NULL,
  `Pin_code` int DEFAULT NULL,
  `Relationship` enum('Mother','Father','Son','Daughter','Sister','Brother','Uncle','Aunt','Guardian') DEFAULT NULL,
  PRIMARY KEY (`Name`,`Soldier_id`),
  KEY `Soldier_id` (`Soldier_id`),
  CONSTRAINT `dependents_ibfk_1` FOREIGN KEY (`Soldier_id`) REFERENCES `Soldiers` (`Soldier_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `dependents_chk_1` CHECK ((length(`Pin_code`) = 6))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dependents`
--

LOCK TABLES `Dependents` WRITE;
/*!40000 ALTER TABLE `Dependents` DISABLE KEYS */;
INSERT INTO `Dependents` VALUES (16,'Asmi','F',201,16,'AS','KIA','SING',400057,'Daughter'),(15,'Khoooshi','M',503,15,'MG','HECTOR','BRIT',900085,'Brother'),(14,'Medha','F',502,14,'GG','AHM','GJ',800056,'Sister'),(13,'Parrsaad','M',203,13,'FG','HYD','TS',500032,'Father'),(12,'Sujal','F',202,12,'FG','MUM','MH',200014,'Uncle');
/*!40000 ALTER TABLE `Dependents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Duties`
--

DROP TABLE IF EXISTS `Duties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Duties` (
  `Duty_s_no` int NOT NULL,
  `Type` enum('Cleaning Duty','Serving Duty') DEFAULT NULL,
  PRIMARY KEY (`Duty_s_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Duties`
--

LOCK TABLES `Duties` WRITE;
/*!40000 ALTER TABLE `Duties` DISABLE KEYS */;
INSERT INTO `Duties` VALUES (121,'Cleaning Duty'),(122,'Cleaning Duty'),(123,'Cleaning Duty'),(124,'Serving Duty'),(125,'Serving Duty');
/*!40000 ALTER TABLE `Duties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Issue_log`
--

DROP TABLE IF EXISTS `Issue_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Issue_log` (
  `Equipment_id` int NOT NULL,
  `Issue_date` date NOT NULL,
  `Return_date` date NOT NULL,
  PRIMARY KEY (`Equipment_id`,`Return_date`,`Issue_date`),
  CONSTRAINT `issue_log_ibfk_1` FOREIGN KEY (`Equipment_id`) REFERENCES `Military_equipment` (`Equipment_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Issue_log`
--

LOCK TABLES `Issue_log` WRITE;
/*!40000 ALTER TABLE `Issue_log` DISABLE KEYS */;
INSERT INTO `Issue_log` VALUES (1,'2023-01-02','2023-12-31'),(2,'2023-01-02','2023-12-31'),(3,'2023-01-02','2023-04-04'),(4,'2023-01-02','2023-12-31'),(5,'2023-01-02','2023-02-03');
/*!40000 ALTER TABLE `Issue_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Menu_items`
--

DROP TABLE IF EXISTS `Menu_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Menu_items` (
  `Mess_id` int NOT NULL,
  `Week_day` enum('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday') NOT NULL,
  `Breakfast_item` varchar(255) NOT NULL,
  `Lunch_item` varchar(255) NOT NULL,
  `Dinner_item` varchar(255) NOT NULL,
  PRIMARY KEY (`Week_day`,`Mess_id`,`Breakfast_item`,`Lunch_item`,`Dinner_item`),
  KEY `Mess_id` (`Mess_id`),
  CONSTRAINT `menu_items_ibfk_1` FOREIGN KEY (`Mess_id`) REFERENCES `Mess` (`Mess_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Menu_items`
--

LOCK TABLES `Menu_items` WRITE;
/*!40000 ALTER TABLE `Menu_items` DISABLE KEYS */;
INSERT INTO `Menu_items` VALUES (1,'Monday','Dosa','Paneer Non Veg','Sujal Bhurji'),(1,'Tuesday','Idli','Paneer Veg','Sujal Masala'),(2,'Tuesday','Poha','Utappam','Rice');
/*!40000 ALTER TABLE `Menu_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Mess`
--

DROP TABLE IF EXISTS `Mess`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Mess` (
  `Mess_id` int NOT NULL,
  `Mess_name` varchar(20) DEFAULT NULL,
  `Chef_id` int DEFAULT NULL,
  `Capacity` int DEFAULT NULL,
  `Sector_id` int DEFAULT NULL,
  PRIMARY KEY (`Mess_id`),
  KEY `Sector_id` (`Sector_id`),
  CONSTRAINT `mess_ibfk_1` FOREIGN KEY (`Sector_id`) REFERENCES `Sectors` (`Sector_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Mess`
--

LOCK TABLES `Mess` WRITE;
/*!40000 ALTER TABLE `Mess` DISABLE KEYS */;
INSERT INTO `Mess` VALUES (1,'Kadamb',17,200,11),(2,'North',18,300,22),(3,'South',19,300,33);
/*!40000 ALTER TABLE `Mess` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Military_equipment`
--

DROP TABLE IF EXISTS `Military_equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Military_equipment` (
  `Equipment_id` int NOT NULL,
  `Type` enum('weapon','gear','uniform') DEFAULT NULL,
  `Status` enum('issued','not issued') DEFAULT NULL,
  `Late_fine` int DEFAULT NULL,
  `Soldier_id` int DEFAULT NULL,
  PRIMARY KEY (`Equipment_id`),
  KEY `Soldier_id` (`Soldier_id`),
  CONSTRAINT `military_equipment_ibfk_1` FOREIGN KEY (`Soldier_id`) REFERENCES `Soldiers` (`Soldier_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Military_equipment`
--

LOCK TABLES `Military_equipment` WRITE;
/*!40000 ALTER TABLE `Military_equipment` DISABLE KEYS */;
INSERT INTO `Military_equipment` VALUES (1,'weapon','issued',200,12),(2,'gear','issued',200,13),(3,'gear','not issued',200,14),(4,'uniform','issued',200,15),(5,'weapon','not issued',200,16);
/*!40000 ALTER TABLE `Military_equipment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Rooms`
--

DROP TABLE IF EXISTS `Rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Rooms` (
  `Barrack_id` int NOT NULL,
  `Room_no` int NOT NULL,
  `Floor_no` int NOT NULL,
  `Cleaning_schedule` enum('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday') DEFAULT NULL,
  PRIMARY KEY (`Room_no`,`Floor_no`,`Barrack_id`),
  KEY `Barrack_id` (`Barrack_id`),
  CONSTRAINT `rooms_ibfk_1` FOREIGN KEY (`Barrack_id`) REFERENCES `Barracks` (`Barrack_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Rooms`
--

LOCK TABLES `Rooms` WRITE;
/*!40000 ALTER TABLE `Rooms` DISABLE KEYS */;
INSERT INTO `Rooms` VALUES (1,302,3,'Wednesday'),(2,303,3,'Wednesday'),(3,304,3,'Wednesday'),(4,402,4,'Thursday'),(5,405,4,'Thursday');
/*!40000 ALTER TABLE `Rooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Sectors`
--

DROP TABLE IF EXISTS `Sectors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Sectors` (
  `Sector_id` int NOT NULL,
  `Sector_name` varchar(30) DEFAULT NULL,
  `Street_no` int DEFAULT NULL,
  `Area` varchar(50) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  `State` varchar(50) DEFAULT NULL,
  `Pin_code` int DEFAULT NULL,
  `Sector_head_id` int DEFAULT NULL,
  PRIMARY KEY (`Sector_id`),
  CONSTRAINT `sectors_chk_1` CHECK ((length(`Pin_code`) = 6))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Sectors`
--

LOCK TABLES `Sectors` WRITE;
/*!40000 ALTER TABLE `Sectors` DISABLE KEYS */;
INSERT INTO `Sectors` VALUES (11,'Jay',20,'A','F','H',200876,12),(22,'Mata',30,'S','G','N',201987,13),(33,'Di',40,'D','H','F',202321,14),(44,'Hare',50,'E','I','G',203123,15),(55,'Ram',60,'G','J','Y',204234,16);
/*!40000 ALTER TABLE `Sectors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Security_personnel`
--

DROP TABLE IF EXISTS `Security_personnel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Security_personnel` (
  `Security_prsnl_id` int NOT NULL,
  `Name` varchar(30) DEFAULT NULL,
  `Date_posted` date DEFAULT NULL,
  `Ph_no` bigint DEFAULT NULL,
  PRIMARY KEY (`Security_prsnl_id`),
  CONSTRAINT `security_personnel_chk_1` CHECK ((length(`Ph_no`) = 10))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Security_personnel`
--

LOCK TABLES `Security_personnel` WRITE;
/*!40000 ALTER TABLE `Security_personnel` DISABLE KEYS */;
INSERT INTO `Security_personnel` VALUES (20,'Balram','2023-02-25',2987654312),(21,'Jairam','2020-06-25',1276543763),(22,'Sitaraman','2018-03-12',9653427123),(23,'Venkat','2022-08-09',7645327123),(24,'Sujal','2023-12-02',6942026457);
/*!40000 ALTER TABLE `Security_personnel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Shifts`
--

DROP TABLE IF EXISTS `Shifts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Shifts` (
  `Shift_s_no` int NOT NULL,
  `Type` enum('Breakfast Shift','Lunch Shift','Snacks Shift','Dinner Shift') DEFAULT NULL,
  PRIMARY KEY (`Shift_s_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Shifts`
--

LOCK TABLES `Shifts` WRITE;
/*!40000 ALTER TABLE `Shifts` DISABLE KEYS */;
INSERT INTO `Shifts` VALUES (121,'Lunch Shift'),(122,'Lunch Shift'),(123,'Dinner Shift'),(124,'Dinner Shift'),(125,'Breakfast Shift');
/*!40000 ALTER TABLE `Shifts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Shifts_and_duties`
--

DROP TABLE IF EXISTS `Shifts_and_duties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Shifts_and_duties` (
  `Soldier_id` int NOT NULL,
  `Duty_s_no` int NOT NULL,
  `Shift_s_no` int NOT NULL,
  `Mess_id` int NOT NULL,
  PRIMARY KEY (`Shift_s_no`,`Duty_s_no`,`Mess_id`,`Soldier_id`),
  KEY `Duty_s_no` (`Duty_s_no`),
  KEY `Mess_id` (`Mess_id`),
  KEY `Soldier_id` (`Soldier_id`),
  CONSTRAINT `shifts_and_duties_ibfk_1` FOREIGN KEY (`Shift_s_no`) REFERENCES `Shifts` (`Shift_s_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `shifts_and_duties_ibfk_2` FOREIGN KEY (`Duty_s_no`) REFERENCES `Duties` (`Duty_s_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `shifts_and_duties_ibfk_3` FOREIGN KEY (`Mess_id`) REFERENCES `Mess` (`Mess_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `shifts_and_duties_ibfk_4` FOREIGN KEY (`Soldier_id`) REFERENCES `Soldiers` (`Soldier_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Shifts_and_duties`
--

LOCK TABLES `Shifts_and_duties` WRITE;
/*!40000 ALTER TABLE `Shifts_and_duties` DISABLE KEYS */;
INSERT INTO `Shifts_and_duties` VALUES (12,121,121,1),(13,122,122,1),(14,123,123,2),(15,124,124,2),(16,125,125,3);
/*!40000 ALTER TABLE `Shifts_and_duties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Soldier_ph_no`
--

DROP TABLE IF EXISTS `Soldier_ph_no`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Soldier_ph_no` (
  `Soldier_id` int NOT NULL,
  `Phone_no` bigint NOT NULL,
  PRIMARY KEY (`Phone_no`,`Soldier_id`),
  KEY `Soldier_id` (`Soldier_id`),
  CONSTRAINT `soldier_ph_no_ibfk_1` FOREIGN KEY (`Soldier_id`) REFERENCES `Soldiers` (`Soldier_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `soldier_ph_no_chk_1` CHECK ((length(`Phone_no`) = 10))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Soldier_ph_no`
--

LOCK TABLES `Soldier_ph_no` WRITE;
/*!40000 ALTER TABLE `Soldier_ph_no` DISABLE KEYS */;
INSERT INTO `Soldier_ph_no` VALUES (12,7865342584),(13,4207653623),(14,6978654384),(15,6968765498),(16,6942098765);
/*!40000 ALTER TABLE `Soldier_ph_no` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Soldiers`
--

DROP TABLE IF EXISTS `Soldiers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Soldiers` (
  `Soldier_id` int NOT NULL,
  `Mname` varchar(30) NOT NULL,
  `Fname` varchar(30) NOT NULL,
  `Lname` varchar(30) NOT NULL,
  `Birth_day` int NOT NULL,
  `Birth_month` enum('JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC') NOT NULL,
  `Birth_year` int NOT NULL,
  `Soldier_rank` enum('Field Marshal','General','Lieutenant General','Major General','Brigadier','Colonel','Lieutenant Colonel','Major','Captain','Lieutenant') DEFAULT NULL,
  `House_no` int DEFAULT NULL,
  `Street_no` int DEFAULT NULL,
  `Area` varchar(50) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  `State` varchar(50) DEFAULT NULL,
  `Pin_code` int DEFAULT NULL,
  `Aadhar_no` bigint DEFAULT NULL,
  `Sex` enum('M','F') DEFAULT NULL,
  `Salary` int DEFAULT NULL,
  `Unit_id` int DEFAULT NULL,
  `Mess_id` int DEFAULT NULL,
  `Barrack_id` int DEFAULT NULL,
  `Officer_id` int DEFAULT NULL,
  PRIMARY KEY (`Soldier_id`),
  KEY `Unit_id` (`Unit_id`),
  KEY `Mess_id` (`Mess_id`),
  KEY `Officer_id` (`Officer_id`),
  KEY `fk_barrack_id` (`Barrack_id`),
  CONSTRAINT `fk_barrack_id` FOREIGN KEY (`Barrack_id`) REFERENCES `Barracks` (`Barrack_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `soldiers_ibfk_1` FOREIGN KEY (`Unit_id`) REFERENCES `Units` (`Unit_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `soldiers_ibfk_2` FOREIGN KEY (`Mess_id`) REFERENCES `Mess` (`Mess_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `soldiers_ibfk_3` FOREIGN KEY (`Officer_id`) REFERENCES `Soldiers` (`Soldier_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `soldiers_chk_1` CHECK ((`Birth_day` between 1 and 31)),
  CONSTRAINT `soldiers_chk_2` CHECK ((length(`Pin_code`) = 6)),
  CONSTRAINT `soldiers_chk_3` CHECK ((length(`Aadhar_no`) = 12))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Soldiers`
--

LOCK TABLES `Soldiers` WRITE;
/*!40000 ALTER TABLE `Soldiers` DISABLE KEYS */;
INSERT INTO `Soldiers` VALUES (12,'Gandhi','Vinit','Mehta',12,'JUN',2004,'Captain',69,70,'Hi','bye','Gujarat',600251,123465439176,'M',80000,1,1,1,NULL),(13,'Mangesh','Ketaki','Shetye',19,'JUN',2004,'Colonel',78,80,'hello','hi','Maharashtra',500042,123576538765,'F',80000,2,1,1,12),(14,'Maitreya','Sujal','Deoda',29,'FEB',2004,'Brigadier',76,82,'hello','bye','Gujarat',600014,123674629347,'F',80000,3,3,3,12),(15,'Annadurai','Prabhav','Shetty',30,'NOV',2004,'Major',57,83,'hi','hello','Kerala',700036,187653456237,'M',80000,4,3,3,12),(16,'Prafulla','Maitreya','Chitale',17,'JUL',2004,'Colonel',67,68,'bye','hello','Maharashtra',400057,126836975338,'M',80000,5,2,3,12);
/*!40000 ALTER TABLE `Soldiers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Training_grounds`
--

DROP TABLE IF EXISTS `Training_grounds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Training_grounds` (
  `Ground_id` int NOT NULL,
  `Ground_name` varchar(20) DEFAULT NULL,
  `Start_time` time DEFAULT NULL,
  `Close_time` time DEFAULT NULL,
  `Type` enum('indoor','outdoor') DEFAULT NULL,
  `Sector_id` int DEFAULT NULL,
  PRIMARY KEY (`Ground_id`),
  KEY `Sector_id` (`Sector_id`),
  CONSTRAINT `training_grounds_ibfk_1` FOREIGN KEY (`Sector_id`) REFERENCES `Sectors` (`Sector_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Training_grounds`
--

LOCK TABLES `Training_grounds` WRITE;
/*!40000 ALTER TABLE `Training_grounds` DISABLE KEYS */;
INSERT INTO `Training_grounds` VALUES (1,'Felicity','18:00:00','00:00:00','outdoor',11),(2,'Football','14:00:00','00:00:00','outdoor',22),(3,'Jai Mata Di','06:00:00','14:00:00','indoor',33);
/*!40000 ALTER TABLE `Training_grounds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Units`
--

DROP TABLE IF EXISTS `Units`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Units` (
  `Unit_id` int NOT NULL,
  `Unit_name` varchar(30) DEFAULT NULL,
  `Role` enum('Infantry','Armored','Artillery','Cavalry','Engineer','Signals','Mechanized Infantry','Air Defense','Special Forces','Military Police','Medical','Supply','Transport') DEFAULT NULL,
  PRIMARY KEY (`Unit_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Units`
--

LOCK TABLES `Units` WRITE;
/*!40000 ALTER TABLE `Units` DISABLE KEYS */;
INSERT INTO `Units` VALUES (1,'Kanda','Infantry'),(2,'Batata','Armored'),(3,'Bhaji','Cavalry'),(4,'Rules','Signals'),(5,'Forever','Transport'),(6,'Love','Supply');
/*!40000 ALTER TABLE `Units` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-02 20:00:51
