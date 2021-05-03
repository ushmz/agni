-- migrate:up
CREATE TABLE IF NOT EXISTS behavior_logs  (
    id VARCHAR(200) NOT NULL,
    uid VARCHAR(200) NOT NULL,
    click_count INT(11) DEFAULT 0,
    time_on_page INT(11) NOT NULL DEFAULT 0,
    referrer VARCHAR(512),
    refocus_count INT(11),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    url VARCHAR(512) NOT NULL,
    task_id INT(11) NOT NULL,
    condition_id INT(11) DEFAULT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- migrate:down
DROP TABLE IF EXISTS behavior_logs;
