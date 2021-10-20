CREATE TABLE IF NOT EXISTS search_session (
    user_id INT(11) NOT NULL,
    task_id INT(11) NOT NULL,
    condition_id INT(11) NOT NULL,
    started_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ended_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, task_id),
    KEY fk_search_session_user_id (user_id),
    CONSTRAINT fk_search_session_user_id
        FOREIGN KEY (user_id) REFERENCES users(id),
    KEY fk_search_session_task_id (task_id),
    CONSTRAINT fk_search_session_task_id
        FOREIGN KEY (task_id) REFERENCES tasks(id),
    KEY fk_search_session_condition_id (condition_id),
    CONSTRAINT fk_search_session_condition_id
        FOREIGN KEY (condition_id) REFERENCES conditions(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

