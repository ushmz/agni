CREATE TABLE IF NOT EXISTS allocations (
    task_id INT(11) NOT NULL,
    condition_id INT(11) NOT NULL,
    user_count INT(11) NOT NULL,
    PRIMARY KEY (task_id, condition_id),
    KEY fk_entire_session_task_id (task_id),
    CONSTRAINT fk_entire_session_task_id
        FOREIGN KEY (task_id) REFERENCES tasks(id),
    KEY fk_entire_session_condition_id (condition_id),
    CONSTRAINT fk_entire_session_condition_id
        FOREIGN KEY (condition_id) REFERENCES conditions(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
