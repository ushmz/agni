CREATE TABLE IF NOT EXISTS dwell_times (
    user_id INT(11) NOT NULL,
    task_id INT(11) NOT NULL,
    condition_id INT(11) NOT NULL,
    dwell_time INT(11) NOT NULL DEFAULT 0,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, task_id),
    KEY fk_dwell_time_user_id (user_id),
    CONSTRAINT fk_dwell_time_user_id
        FOREIGN KEY (user_id) REFERENCES users (id),
    KEY fk_dwell_time_task_id (task_id),
    CONSTRAINT fk_dwell_time_task_id
        FOREIGN KEY (task_id) REFERENCES tasks (id),
    KEY fk_dwell_time_condition_id (condition_id),
    CONSTRAINT fk_dwell_time_condition_id
        FOREIGN KEY (condition_id) REFERENCES conditions (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;
