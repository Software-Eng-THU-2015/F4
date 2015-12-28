SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `f4ss`
--

USE f4ss;

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

CREATE TABLE IF NOT EXISTS `Follower` (
  `id` int(32) NOT NULL AUTO_INCREMENT,
  `FollowingID` int(20) NOT NULL,
  `FollowerID` int(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `Message`
--

CREATE TABLE IF NOT EXISTS `Message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Text` varchar(128) NOT NULL,
  `Type` varchar(16) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- 转存表中的数据 `Message`
--

INSERT INTO `Message` (`id`, `Text`, `Type`) VALUES
(1, 'test_token', 'TOKEN');

-- --------------------------------------------------------

--
-- 表的结构 `Plan`
--

CREATE TABLE IF NOT EXISTS `Plan` (
  `id` int(32) NOT NULL AUTO_INCREMENT,
  `OpenID` varchar(32) NOT NULL,
  `Height` int(4) NOT NULL,
  `Weight` int(4) NOT NULL,
  `GoalCalo` int(4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `Stranger`
--

CREATE TABLE IF NOT EXISTS `Stranger` (
  `id` int(32) NOT NULL AUTO_INCREMENT,
  `ToUserID` int(32) NOT NULL,
  `FromUserID` int(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `User`
--

CREATE TABLE IF NOT EXISTS `User` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `Uname` varchar(50) NOT NULL,
  `OpenID` varchar(50) NOT NULL,
  `ImageUrl` varchar(100) NOT NULL,
  `Point` int(16) NOT NULL DEFAULT '0',
  `SignInTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `TotalPoint` int(16) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `Weapon`
--

CREATE TABLE IF NOT EXISTS `Weapon` (
  `id` int(32) NOT NULL AUTO_INCREMENT,
  `OpenID` varchar(32) NOT NULL,
  `WeaponCode` int(4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;