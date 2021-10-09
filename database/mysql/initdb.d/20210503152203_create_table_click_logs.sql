-- migrate:up
CREATE TABLE IF NOT EXISTS click_logs  (
    id VARCHAR(200) NOT NULL,
    user_id INT(11) NOT NULL,
    task_id INT(11) NOT NULL,
    condition_id INT(11) NOT NULL,
    dwell_time INT(11) NOT NULL DEFAULT 0,
    url VARCHAR(512) NOT NULL,
    referrer VARCHAR(512),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY fk_click_user_id (user_id),
    CONSTRAINT fk_click_user_id FOREIGN KEY (user_id) REFERENCES users(id),
    KEY fk_click_task_id (task_id),
    CONSTRAINT fk_click_task_id FOREIGN KEY (task_id) REFERENCES tasks(id),
    KEY fk_click_condition_id (condition_id),
    CONSTRAINT fk_click_condition_id FOREIGN KEY (condition_id) REFERENCES conditions(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- migrate:down
DROP TABLE IF EXISTS click_logs;
