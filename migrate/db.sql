create table UserInformation
(
    email       varchar(128)                                            not null
        primary key,
    nickname    varchar(100) charset utf8 default '未设置昵称'               null,
    password    varchar(128)                                            not null,
    type        int                       default 0                     null,
    create_time datetime                  default '1999-09-09 09:09:09' not null,
    phone       varchar(128)                                            null
);

create table Files
(
    Fno       varchar(128)                               not null,
    filename  varchar(128) charset utf8 default '未命名'    null,
    file_info varchar(128) charset utf8 default '没有描述信息' null,
    file_time datetime                                   null,
    email     varchar(128)                               null,
    constraint Files_Fno_uindex
        unique (Fno),
    constraint Files_UserInformation_email_fk
        foreign key (email) references UserInformation (email)
);

alter table Files
    add primary key (Fno);

create table Issue
(
    Ino        varchar(128) not null,
    email      varchar(128) not null,
    title      text         null,
    issue_time datetime     null,
    constraint Issue_Ino_uindex
        unique (Ino),
    constraint Issue_UserInformation_email_fk
        foreign key (email) references UserInformation (email)
);

alter table Issue
    add primary key (Ino);

create table Comment
(
    Cno          varchar(128)                           not null,/*
Navicat MySQL Data Transfer

Source Server         : studypython
Source Server Version : 80026
Source Host           : localhost:3306
Source Database       : onlineforumplatform

Target Server Type    : MYSQL
Target Server Version : 80026
File Encoding         : 65001

Date: 2022-02-20 10:05:58
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `Cno` varchar(128) NOT NULL,
  `Ino` varchar(128) NOT NULL,
  `comment` text,
  `comment_time` datetime NOT NULL DEFAULT '1999-09-09 09:09:09',
  `email` varchar(128) DEFAULT NULL,
  `shop` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Cno`,`Ino`),
  KEY `Comment_Issue_Ino_fk` (`Ino`),
  KEY `Comment_UserInformation_email_fk` (`email`),
  CONSTRAINT `Comment_Issue_Ino_fk` FOREIGN KEY (`Ino`) REFERENCES `issue` (`Ino`),
  CONSTRAINT `Comment_UserInformation_email_fk` FOREIGN KEY (`email`) REFERENCES `userinformation` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of comment
-- ----------------------------
INSERT INTO `comment` VALUES ('1', 'UQKNLQTOHPDZGAJBDNSQQVWPULWWOJWXXUBJHGWOVQGMYWXAVDBCJFJAXHHCWKGOPKGKYHSDMRJQEQENOHEUQRWBYIDNKLXZPLIYZXBBFHKYGRQDITMTVOXCPLFAUYAK', '<p>1223</p>', '2022-02-08 14:20:38', '1379255913@qq.com', '1234@qq.com');
INSERT INTO `comment` VALUES ('2', 'UQKNLQTOHPDZGAJBDNSQQVWPULWWOJWXXUBJHGWOVQGMYWXAVDBCJFJAXHHCWKGOPKGKYHSDMRJQEQENOHEUQRWBYIDNKLXZPLIYZXBBFHKYGRQDITMTVOXCPLFAUYAK', '<p>122334556<br/></p>', '2022-02-08 14:21:02', '1379255913@qq.com', null);
INSERT INTO `comment` VALUES ('3', 'UQKNLQTOHPDZGAJBDNSQQVWPULWWOJWXXUBJHGWOVQGMYWXAVDBCJFJAXHHCWKGOPKGKYHSDMRJQEQENOHEUQRWBYIDNKLXZPLIYZXBBFHKYGRQDITMTVOXCPLFAUYAK', '<p>订单 的</p>', '2022-02-08 14:49:31', '1379255913@qq.com', null);

-- ----------------------------
-- Table structure for issue
-- ----------------------------
DROP TABLE IF EXISTS `issue`;
CREATE TABLE `issue` (
  `Ino` varchar(128) NOT NULL,
  `email` varchar(128) NOT NULL,
  `title` text,
  `issue_time` datetime DEFAULT NULL,
  `shop` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Ino`),
  UNIQUE KEY `Issue_Ino_uindex` (`Ino`),
  KEY `Issue_UserInformation_email_fk` (`email`),
  CONSTRAINT `Issue_UserInformation_email_fk` FOREIGN KEY (`email`) REFERENCES `userinformation` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of issue
-- ----------------------------
INSERT INTO `issue` VALUES ('UQKNLQTOHPDZGAJBDNSQQVWPULWWOJWXXUBJHGWOVQGMYWXAVDBCJFJAXHHCWKGOPKGKYHSDMRJQEQENOHEUQRWBYIDNKLXZPLIYZXBBFHKYGRQDITMTVOXCPLFAUYAK', '1379255913@qq.com', '123', '2022-02-08 14:20:38', '1234@qq.com');

-- ----------------------------
-- Table structure for orderdata
-- ----------------------------
DROP TABLE IF EXISTS `orderdata`;
CREATE TABLE `orderdata` (
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `information` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `shop` varchar(255) DEFAULT NULL,
  `submit_time` datetime DEFAULT NULL,
  `arrive_time` datetime DEFAULT NULL,
  `ino` varchar(255) DEFAULT NULL,
  `horseman` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of orderdata
-- ----------------------------
INSERT INTO `orderdata` VALUES ('1379255913@qq.com', '黄金鸡块/13.5/1%奥尔良鸡腿堡/20/1%老北京鸡肉卷/19/1%55.5', '1234@qq.com', '2022-02-07 13:58:22', '2022-02-19 18:24:12', 'True', 'e@qq.com');
INSERT INTO `orderdata` VALUES ('1379255913@qq.com', '薯条/11/1%香辣鸡腿堡/18.5/1%32.5', '1234@qq.com', '2022-02-07 14:23:18', '2022-02-08 11:32:31', 'True', 'e@qq.com');
INSERT INTO `orderdata` VALUES ('1379255913@qq.com', '薯条/11/1%香辣鸡腿堡/18.5/1%32.5', '1234@qq.com', '2022-02-19 19:34:03', '2022-02-19 20:05:51', 'False', null);
INSERT INTO `orderdata` VALUES ('1379255913@qq.com', '薯条/11/1%香辣鸡腿堡/18.5/1%奥尔良鸡腿堡/20/1%52.5', '1234@qq.com', '2022-02-19 19:38:33', '2022-02-19 20:36:15', 'False', null);
INSERT INTO `orderdata` VALUES ('1379255913@qq.com', '薯条/11/1%香辣鸡腿堡/18.5/1%32.5', '1234@qq.com', '2022-02-19 19:40:02', '2022-02-19 20:36:09', 'Get', null);
INSERT INTO `orderdata` VALUES ('2950422403@qq.com', '黄金鸡块/13.5/1%老北京鸡肉卷/19/1%35.5', '1234@qq.com', '2022-02-19 19:41:18', '2022-02-19 20:18:55', 'Go', 'e@qq.com');

-- ----------------------------
-- Table structure for ordermoney
-- ----------------------------
DROP TABLE IF EXISTS `ordermoney`;
CREATE TABLE `ordermoney` (
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `shop` varchar(255) DEFAULT NULL,
  `horseman` varchar(255) DEFAULT NULL,
  `submit_time` datetime DEFAULT NULL,
  `money_shop` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `money_horse` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of ordermoney
-- ----------------------------
INSERT INTO `ordermoney` VALUES ('1379255913@qq.com', '1234@qq.com', 'e@qq.com', '2022-02-07 14:23:18', '29.5', '246915.0');
INSERT INTO `ordermoney` VALUES ('1379255913@qq.com', '1234@qq.com', 'e@qq.com', '2022-02-07 13:58:22', '52.5', '3');

-- ----------------------------
-- Table structure for shopdata
-- ----------------------------
DROP TABLE IF EXISTS `shopdata`;
CREATE TABLE `shopdata` (
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `price` varchar(255) DEFAULT NULL,
  `information` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `likes` int DEFAULT NULL,
  `fav` int DEFAULT NULL,
  `repeats` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of shopdata
-- ----------------------------
INSERT INTO `shopdata` VALUES ('1234@qq.com', '黄金鸡块', '13.5', '1234567', '/static/img/2022012919252008.jpg', '0', '0', '0', '0');
INSERT INTO `shopdata` VALUES ('1234@qq.com', '薯条', '11.0', '12345678', '/static/img/2022012919294763.jpg', '0', '0', '0', '0');
INSERT INTO `shopdata` VALUES ('1234@qq.com', '老北京鸡肉卷', '19.0', '135323213535', '/static/img/2022020323161028.jpg', '2', '0', '0', '0');
INSERT INTO `shopdata` VALUES ('1234@qq.com', '香辣鸡腿堡', '18.5', '拉爆', '/static/img/2022020323163940.jpg', '1', '0', '0', '0');
INSERT INTO `shopdata` VALUES ('1234@qq.com', '奥尔良鸡腿堡', '20.0', '考堡', '/static/img/2022020323170327.jpg', '1', '0', '0', '0');

-- ----------------------------
-- Table structure for shoptype
-- ----------------------------
DROP TABLE IF EXISTS `shoptype`;
CREATE TABLE `shoptype` (
  `email` varchar(255) NOT NULL,
  `type0` varchar(255) DEFAULT NULL,
  `type1` varchar(255) DEFAULT NULL,
  `type2` varchar(255) DEFAULT NULL,
  `type3` varchar(255) DEFAULT NULL,
  `type4` varchar(255) DEFAULT NULL,
  `type5` varchar(255) DEFAULT NULL,
  `type6` varchar(255) DEFAULT NULL,
  `type7` varchar(255) DEFAULT NULL,
  `type8` varchar(255) DEFAULT NULL,
  `type9` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of shoptype
-- ----------------------------
INSERT INTO `shoptype` VALUES ('1234@qq.com', '小吃', '', '', '', '', '', '', '', '', '');

-- ----------------------------
-- Table structure for userinformation
-- ----------------------------
DROP TABLE IF EXISTS `userinformation`;
CREATE TABLE `userinformation` (
  `email` varchar(128) NOT NULL,
  `nickname` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT '未设置昵称',
  `password` varchar(128) NOT NULL,
  `type` int DEFAULT '0',
  `create_time` datetime NOT NULL DEFAULT '1999-09-09 09:09:09',
  `phone` varchar(128) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `information` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of userinformation
-- ----------------------------
INSERT INTO `userinformation` VALUES ('1234@qq.com', '肯德基', 'pbkdf2:sha256:260000$F2D5J95v$1a486cb90dcfd40733a4eb439391d5a1d76eed16df088215dcd67a7913611cf3', '1', '2022-01-25 20:32:32', '122344556', '浙江省安吉县地铺镇桃园老区31号', '“生活如此多娇” “尽情自在肯德基”', '/static/img/2022012916132440.jpg');
INSERT INTO `userinformation` VALUES ('12345256@163.com', '沙县小吃', 'pbkdf2:sha256:260000$0TcflUnq$d921671108708ab6cf7a2d5265e26c223ee099a0f8be93e6cce817d6ae85c49f', '1', '2022-01-29 16:05:29', '15682353202', '河南省商水县李埠口乡郭河村九组', '沙县小吃源远流长，历史悠久，起源于夏商周、晋、宋中原黄河流域中华饮食文化，在民间具有浓厚的历史文化基础，尤以品种繁多风味独特和经济实惠著称。', '/static/img/2022012916071359.jpg');
INSERT INTO `userinformation` VALUES ('123456789@qq.com', '永和大王', 'pbkdf2:sha256:260000$aDO0wt13$ce001d01d442ca7ae1e92069b36c48b91d19bbad6ed0c6f82adbe0defa628d7c', '1', '2022-01-29 16:09:54', '15268520865', '浙江省永康市西溪镇西山村下马6号', '多年来，永和大王坚守对食品安全的零容忍，从产品的源头开发到餐厅操作，都进行系统化管理，坚持每一个产品的黄金标准，加强餐厅的服务训练，不断优化系统和操作流程，实现产品品质一致性。', '/static/img/2022012916103723.jpg');
INSERT INTO `userinformation` VALUES ('1379255913@qq.com', 'zyy1234567', 'pbkdf2:sha256:260000$X9uLETtd$7a21bb713861ac0463d70b2e5a24afd4da93c036db5cb31b27791cfadffdaa99', '0', '2022-01-24 21:52:42', '187680757054', 'Fzua', '12345678', '/static/img/2022012821023266.jpg');
INSERT INTO `userinformation` VALUES ('2950422402@qq.com', 'zyy', 'pbkdf2:sha256:260000$a3hC4YE7$c6bd8064e7d32f3cff09a5818e78268f86eafcdc291fa8c6645627d24f932cb6', '1', '2022-01-25 20:31:34', '18768075734', 'aet', '欢迎光临本店,本店新开张,诚 信经营,只赚信誉不赚钱,谢谢', '/static/img/None.jpg');
INSERT INTO `userinformation` VALUES ('2950422403@qq.com', 'zyy123', 'pbkdf2:sha256:260000$Wogvk84E$9ff359cf1e03a1f758743df899898744e736b472d9a6665da016e16a0bc3da13', '0', '2022-01-25 20:04:13', '15957068485', 'adg', '', '/static/img/None.jpg');
INSERT INTO `userinformation` VALUES ('e@qq.com', 'zyy343', 'pbkdf2:sha256:260000$mZhjU2PT$6d192f18a2991af3c6b644c3778cad00992cd8a11e2b7ca1cdc3c512b781a934', '2', '2022-01-25 20:33:04', '1234', '123', '', '/static/img/None.jpg');

    Ino          varchar(128)                           not null,
    comment      text                                   null,
    comment_time datetime default '1999-09-09 09:09:09' not null,
    email        varchar(128)                           null,
    primary key (Cno, Ino),
    constraint Comment_Issue_Ino_fk
        foreign key (Ino) references Issue (Ino),
    constraint Comment_UserInformation_email_fk
        foreign key (email) references UserInformation (email)
);

