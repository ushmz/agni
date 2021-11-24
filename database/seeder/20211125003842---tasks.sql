-- -------------------------------------------------------------
-- TablePlus 4.5.0(396)
--
-- https://tableplus.com/
--
-- Database: agni
-- Generation Time: 0003-11-25 00:38:47.8610
-- -------------------------------------------------------------


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


INSERT INTO `tasks` (`id`, `query`, `title`, `description`, `search_url`, `created_at`, `updated_at`) VALUES
(1, 'task1', 'タスク1', 'これはタスク1の説明文です。', 'task/1', '2021-10-20 23:45:04', '2021-10-20 23:45:04'),
(2, 'task2', 'タスク2', 'これはタスク2の説明文です。', 'task/2', '2021-10-20 23:45:04', '2021-10-20 23:45:04'),
(3, 'task3', 'タスク3', 'これはタスク3の説明文です。', 'task/3', '2021-10-20 23:45:04', '2021-10-20 23:45:04'),
(4, 'task4', 'タスク4', 'これはタスク4の説明文です。', 'task/4', '2021-10-20 23:45:04', '2021-10-20 23:45:04');


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;