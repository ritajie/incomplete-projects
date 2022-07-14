CREATE TABLE `building` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '0=正在正常施工 1=正常施工完成 -1=已烂尾 -2=业主停止还贷',
    `address` varchar(255) NOT NULL,
    `city` varchar(255) NOT NULL,
    `description` text NOT NULL,
    `position_longitude` float NOT NULL,
    `position_latitude` float NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `name_UNIQUE` (`name`),
    UNIQUE KEY `address_UNIQUE` (`address`),
    UNIQUE KEY `longitude_latitude_UNIQUE` (`position_longitude`,`position_latitude`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
