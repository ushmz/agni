-- migrate:up
CREATE TABLE IF NOT EXISTS conditions (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `condition` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

-- migrate:down
DROP TABLE IF EXISTS conditions;
