-- drop database building;
-- create  database `building` character set utf8mb4; use building;
-- drop table building;
CREATE TABLE `building` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    `full_name` varchar(255) NOT NULL,
    `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '0=正在正常施工 1=正常施工完成 -1=已烂尾 -2=业主停止还贷',
    `address` varchar(255) NOT NULL,
    `city` varchar(255) NOT NULL,
    `province` varchar(255) NOT NULL,
    `telephone` varchar(255) NOT NULL,
    `photos` text NOT NULL,
    `position_longitude` varchar(255) NOT NULL,
    `position_latitude` varchar(255) NOT NULL,
    `description` text NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `name_province_city_UNIQUE` (`name`, `province`, `city`),
    UNIQUE KEY `longitude_latitude_UNIQUE` (`position_longitude`,`position_latitude`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into building (name, full_name, status, address, city, province, telephone, photos, position_longitude, position_latitude, description) values
('江苏省南京市玄武区玄武大道', '江苏省南京市玄武区玄武大道', 1, '玄武大道', '南京', '江苏', '025-82888888', '', '', '', ''),


CREATE TABLE `building2` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



CREATE TABLE `test-utf8mb4` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
insert into `test-utf8mb4` (name) values ('我');
select * from `test-utf8mb4`;
