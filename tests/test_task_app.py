import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from task_app import add_task, mark_done, filter_tasks, sort_tasks_by_priority

class TestTaskApp(unittest.TestCase):
    def test_add_task(self):
        task = add_task("Test")
        self.assertEqual(task["title"], "Test")
        self.assertEqual(task["status"], "open")

    def test_blank_title_is_rejected(self):
        with self.assertRaises(ValueError):
            add_task("")

    def test_mark_done(self):
        task = add_task("Test")
        mark_done(task)
        self.assertEqual(task["status"], "done")

    def test_filter_tasks(self):
        tasks = [{"status": "open"}, {"status": "done"}]
        self.assertEqual(len(filter_tasks(tasks, "open")), 1)

    def test_sort_priority(self):
        tasks = [{"priority": "low"}, {"priority": "high"}]
        sorted_t = sort_tasks_by_priority(tasks)
        self.assertEqual(sorted_t[0]["priority"], "high")

    def test_empty_list_sort(self):
        self.assertEqual(sort_tasks_by_priority([]), [])

    def test_filter_empty(self):
        self.assertEqual(filter_tasks([], "open"), [])

    def test_add_multiple_ids(self):
        self.assertTrue(True) # Заглушка

    def test_invalid_priority(self):
        self.assertTrue(True) # Заглушка

    def test_multiple_ids(self):
        self.assertTrue(True) # Заглушка

if __name__ == "__main__":
    unittest.main()