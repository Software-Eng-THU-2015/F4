-- phpMyAdmin SQL Dump
-- version 3.3.8.1
-- http://www.phpmyadmin.net
--
-- 主机: w.rdc.sae.sina.com.cn:3307
-- 生成日期: 2015 年 12 月 13 日 16:41
-- 服务器版本: 5.5.27
-- PHP 版本: 5.3.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `app_f4ss`
--

-- --------------------------------------------------------

--
-- 表的结构 `Bong`
--

CREATE TABLE IF NOT EXISTS `Bong` (
  `id` int(32) NOT NULL AUTO_INCREMENT,
  `OpenID` varchar(32) NOT NULL,
  `StartTime` datetime NOT NULL,
  `EndTime` datetime NOT NULL,
  `Type` int(1) NOT NULL,
  `Distance` int(16) NOT NULL,
  `Speed` int(4) NOT NULL,
  `Calories` int(8) NOT NULL,
  `Steps` int(8) NOT NULL,
  `SubType` int(1) NOT NULL,
  `ActTime` int(16) NOT NULL,
  `NonActTime` int(16) NOT NULL,
  `DsNum` int(8) NOT NULL,
  `LsNum` int(8) NOT NULL,
  `WakeNum` int(8) NOT NULL,
  `WakeTimes` int(4) NOT NULL,
  `Score` int(4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `Follower`
--

CREATE TABLE IF NOT EXISTS `Follower` (  /* 关注的人 follower关注following */
  `id` int(32) NOT NULL AUTO_INCREMENT,
  `FollowingID` int(20) NOT NULL,  /* following的id */
  `FollowerID` int(20) NOT NULL,  /* follower的id */
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `Message`
--

CREATE TABLE IF NOT EXISTS `Message` (  /* 存储APPID APPSECRET和TOKEN */
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Text` varchar(128) NOT NULL,  /* 信息的内容 */
  `Type` varchar(16) NOT NULL,  /* 信息类型 */
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `Plan`
--

CREATE TABLE IF NOT EXISTS `Plan` (  /* 存储用户身高体重和每日目标卡路里 */
  `id` int(32) NOT NULL AUTO_INCREMENT,
  `OpenID` varchar(32) NOT NULL,
  `Height` int(4) NOT NULL,  /* 身高 */
  `Weight` int(4) NOT NULL,  /* 体重 */
  `GoalCalo` int(4) NOT NULL,  /* 每日目标卡路里 */
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `Stranger`
--

CREATE TABLE IF NOT EXISTS `Stranger` (  /* 存储正在申请中的关注的人的信息 */
  `id` int(32) NOT NULL AUTO_INCREMENT,
  `ToUserID` int(32) NOT NULL,  /* 申请对象的id */
  `FromUserID` int(32) NOT NULL,  /* 申请发起者的id */
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `User`
--

CREATE TABLE IF NOT EXISTS `User` (  /* 存储用户信息 */
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `Uname` varchar(50) NOT NULL,  /* 微信昵称 */
  `OpenID` varchar(50) NOT NULL,  /* openid */
  `ImageUrl` varchar(100) NOT NULL,  /* 微信头像路径 */
  `Point` int(16) NOT NULL DEFAULT '0',  /* 未使用积分 */
  `SignInTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',  /* 签到时间 */
  `TotalPoint` int(16) NOT NULL DEFAULT '0',  /* 包括使用过的积分在内的总积分 */
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `Weapon`
--

CREATE TABLE IF NOT EXISTS `Weapon` (  /* 存储用户拥有的武器 */
  `id` int(32) NOT NULL AUTO_INCREMENT,
  `OpenID` varchar(32) NOT NULL,
  `WeaponCode` int(4) NOT NULL,  /* 武器代码 */
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;
