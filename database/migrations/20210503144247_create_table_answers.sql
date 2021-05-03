-- migrate:up
CREATE TABLE IF NOT EXISTS answers (
    id INT(11) NOT NULL AUTO_INCREMENT,
    uid VARCHAR(255) NOT NULL,
    task_id INT(11),
    condition_id INT(11),
    task_condition_relations_id INT(11),
    reason TEXT DEFAULT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

-- migrate:down
DROP TABLE IF EXISTS answers;
