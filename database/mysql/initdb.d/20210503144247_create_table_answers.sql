-- migrate:up
CREATE TABLE IF NOT EXISTS answers (
    id INT(11) NOT NULL AUTO_INCREMENT,
    user_id INT(11),
    task_id INT(11),
    condition_id INT(11),
    answer LONGTEXT DEFAULT NULL,
    reason LONGTEXT DEFAULT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY fk_click_user_id (user_id),
    CONSTRAINT fk_click_user_id FOREIGN KEY (user_id) REFERENCES users(id),
    KEY fk_click_task_id (task_id),
    CONSTRAINT fk_click_task_id FOREIGN KEY (task_id) REFERENCES tasks(id),
    KEY fk_click_condition_id (condition_id),
    CONSTRAINT fk_click_condition_id FOREIGN KEY (condition_id) REFERENCES conditions(id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

-- migrate:down
DROP TABLE IF EXISTS answers;
