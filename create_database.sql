/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50709
Source Host           : localhost:3306
Source Database       : student2

Target Server Type    : MYSQL
Target Server Version : 50709
File Encoding         : 65001

Date: 2017-12-17 20:40:26
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `table_comment`
-- ----------------------------
DROP TABLE IF EXISTS `table_comment`;
CREATE TABLE `table_comment` (
  `comt_id` int(20) NOT NULL AUTO_INCREMENT,
  `comt_commenter` char(25) DEFAULT NULL,
  `comt_post_id` int(20) DEFAULT NULL,
  `comt_time` datetime DEFAULT NULL,
  `comt_content` varchar(2000) NOT NULL,
  PRIMARY KEY (`comt_id`),
  KEY `comt_post_id` (`comt_post_id`),
  KEY `comt_commenter` (`comt_commenter`)
) ENGINE=MyISAM AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of table_comment
-- ----------------------------
INSERT INTO `table_comment` VALUES ('31', '涵哥', '4', '2017-12-17 10:43:57', '年');
INSERT INTO `table_comment` VALUES ('29', '林光涵', '3', '2017-12-12 16:32:18', 'nimmm');
INSERT INTO `table_comment` VALUES ('26', '12a', '3', '2017-12-11 08:34:50', 'nima');
INSERT INTO `table_comment` VALUES ('25', '林光涵', '3', '2017-12-11 08:29:34', 'nima');

-- ----------------------------
-- Table structure for `table_feedback`
-- ----------------------------
DROP TABLE IF EXISTS `table_feedback`;
CREATE TABLE `table_feedback` (
  `fbk_receive_time` datetime NOT NULL,
  `fbk_sender` char(25) NOT NULL,
  `fbk_recipient` char(25) NOT NULL,
  `fbk_info_type` char(25) NOT NULL,
  `fbk_info_content` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`fbk_receive_time`,`fbk_sender`,`fbk_recipient`),
  KEY `fbk_sender` (`fbk_sender`),
  KEY `fbk_recipient` (`fbk_recipient`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of table_feedback
-- ----------------------------
INSERT INTO `table_feedback` VALUES ('2017-12-17 11:16:22', '涵哥', 'admin', '1', 'nima');
INSERT INTO `table_feedback` VALUES ('2017-12-17 14:48:42', '12aaa', 'admin', '1', '你阿妈');
INSERT INTO `table_feedback` VALUES ('2017-12-17 14:49:43', '12aaa', 'admin', '1', '你阿妈');

-- ----------------------------
-- Table structure for `table_op_record`
-- ----------------------------
DROP TABLE IF EXISTS `table_op_record`;
CREATE TABLE `table_op_record` (
  `opt_time` datetime NOT NULL,
  `user_login_name` char(25) NOT NULL,
  `opt_type` char(20) NOT NULL,
  `opt_data_route` char(50) DEFAULT NULL,
  PRIMARY KEY (`opt_time`,`user_login_name`),
  KEY `user_login_name` (`user_login_name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of table_op_record
-- ----------------------------

-- ----------------------------
-- Table structure for `table_picture`
-- ----------------------------
DROP TABLE IF EXISTS `table_picture`;
CREATE TABLE `table_picture` (
  `pic_id` varchar(60) DEFAULT NULL,
  `pic_route` char(50) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of table_picture
-- ----------------------------

-- ----------------------------
-- Table structure for `table_poster`
-- ----------------------------
DROP TABLE IF EXISTS `table_poster`;
CREATE TABLE `table_poster` (
  `post_id` int(20) NOT NULL AUTO_INCREMENT,
  `post_user` char(25) DEFAULT NULL,
  `post_time` datetime DEFAULT NULL,
  `post_content` varchar(5000) NOT NULL,
  `post_title` char(80) NOT NULL,
  `post_type` char(20) NOT NULL,
  PRIMARY KEY (`post_id`),
  KEY `post_user` (`post_user`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of table_poster
-- ----------------------------
INSERT INTO `table_poster` VALUES ('6', '涵哥', '2017-12-17 10:45:15', 'asdcasc', 'vcaom', 'guanghanjiba');
INSERT INTO `table_poster` VALUES ('3', '林光涵', '2017-12-10 10:35:31', '11', '11', 'guanghanjiba');
INSERT INTO `table_poster` VALUES ('4', '林光涵', '2017-12-10 10:37:14', '阿花', '你阿妈牛逼', 'guanghanjiba');

-- ----------------------------
-- Table structure for `table_user_info`
-- ----------------------------
DROP TABLE IF EXISTS `table_user_info`;
CREATE TABLE `table_user_info` (
  `user_login_name` char(25) NOT NULL,
  `user_pwd` char(15) DEFAULT NULL,
  `user_Nick_name` char(20) DEFAULT NULL,
  `user_phone` char(11) DEFAULT NULL,
  `user_Email` char(25) DEFAULT NULL,
  `user_pic_url` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_login_name`),
  UNIQUE KEY `user_phone` (`user_phone`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of table_user_info
-- ----------------------------
INSERT INTO `table_user_info` VALUES ('林光涵', '12345678', 'shsaijasio', '15359284261', '1354009873@qq.com', '17.jpg');
INSERT INTO `table_user_info` VALUES ('12a', '123456', '娇滴滴', '13860951435', '1354009873@qq.com', '12a.jpg');
INSERT INTO `table_user_info` VALUES ('尼玛', '123456', '', '13656567645', '', '');
INSERT INTO `table_user_info` VALUES ('12t', '123456', '', '13545467876', '', '');
INSERT INTO `table_user_info` VALUES ('涵哥', '123456', '', '13565656732', '', '');
INSERT INTO `table_user_info` VALUES ('admin', '123456', '管理员', '15359284262', null, null);
INSERT INTO `table_user_info` VALUES ('12abs', '123456', '', '13544545621', '', '12a.jpg');
INSERT INTO `table_user_info` VALUES ('12aaa', '123456', '你哈', '13546565675', '那些', '17.jpg');
INSERT INTO `table_user_info` VALUES ('12eee', '123456', '', '13456565743', '', '17.jpg');

-- ----------------------------
-- Table structure for `table_user_rights`
-- ----------------------------
DROP TABLE IF EXISTS `table_user_rights`;
CREATE TABLE `table_user_rights` (
  `user_login_name` char(25) NOT NULL,
  `user_status` char(15) DEFAULT NULL,
  PRIMARY KEY (`user_login_name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of table_user_rights
-- ----------------------------

-- ----------------------------
-- View structure for `a_post_view`
-- ----------------------------
DROP VIEW IF EXISTS `a_post_view`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `a_post_view` AS (select `u`.`user_login_name` AS `user_login_name`,`u`.`user_Nick_name` AS `user_Nick_name`,`u`.`user_pic_url` AS `user_pic_url`,`up`.`post_id` AS `post_id`,`up`.`post_time` AS `post_time`,`up`.`post_content` AS `post_content`,`up`.`post_title` AS `post_title`,`up`.`post_type` AS `post_type`,`tp`.`pic_id` AS `pic_id`,`tp`.`pic_route` AS `pic_route` from ((`table_poster` `up` left join `table_user_info` `u` on((`u`.`user_login_name` = `up`.`post_user`))) left join `table_picture` `tp` on((`up`.`post_id` = `tp`.`pic_id`)))) ;

-- ----------------------------
-- View structure for `post_comment_view`
-- ----------------------------
DROP VIEW IF EXISTS `post_comment_view`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `post_comment_view` AS (select `u`.`post_id` AS `post_id`,`up`.`comt_id` AS `comt_id`,`up`.`comt_commenter` AS `comt_commenter`,`up`.`comt_time` AS `comt_time`,`up`.`comt_content` AS `comt_content`,`tp`.`pic_id` AS `pic_id`,`tp`.`pic_route` AS `pic_route` from ((`table_poster` `u` left join `table_comment` `up` on((`u`.`post_id` = `up`.`comt_post_id`))) left join `table_picture` `tp` on((`up`.`comt_id` = `tp`.`pic_id`)))) ;
