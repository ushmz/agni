CREATE TABLE IF NOT EXISTS entire_session (
    user_id INT(11) NOT NULL,
    started_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ended_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    KEY fk_search_session_user_id (user_id),
    CONSTRAINT fk_search_session_user_id
        FOREIGN KEY (user_id) REFERENCES users(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

