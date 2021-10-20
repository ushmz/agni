CREATE TABLE IF NOT EXISTS click_counts (
  id INT(11) NOT NULL,
  user_id INT(11) NOT NULL,
  task_id INT(11) NOT NULL,
  condition_id INT(11) NOT NULL,
  url VARCHAR(512) NOT NULL,
  referrer VARCHAR(512),
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  KEY fk_click_counts_user_id (user_id),
  CONSTRAINT fk_click_counts_user_id
    FOREIGN KEY (user_id) REFERENCES users (id),
  KEY fk_click_counts_task_id (task_id),
  CONSTRAINT fk_click_counts_task_id
    FOREIGN KEY (task_id) REFERENCES tasks (id),
  KEY fk_click_counts_condition_id (condition_id),
  CONSTRAINT fk_click_counts_condition_id
    FOREIGN KEY (condition_id) REFERENCES conditions (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
