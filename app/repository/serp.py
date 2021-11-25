from infra.mysql import get_connection
from domain.serp import SearchResult
from typing import List
from domain.repository.serp import SerpRepository


class SerpRepositoryImpl(SerpRepository):
    def get_serp(self, task_id: int, offset: int) -> List[SearchResult]:
        """
        Get search result pages by given task INIT_DB

        args:
            task_id(int) : Task ID
            offset(int)  : Offset number of pages
        returns:
            serps(List[Serp]) : Listed result page objects
        """

        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        try:
            cur.execute(
                "SELECT * FROM search_pages WHERE task_id = %s LIMIT %s, 10"
                % (
                    task_id,
                    offset * 10,
                )
            )
            result = cur.fetchall()
            return result
        except Exception as e:
            print(f"[ERROR] {e}")
            return []
        finally:
            cur.close()
            conn.close()
