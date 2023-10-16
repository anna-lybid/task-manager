from django.test import TestCase
from .models import TaskType, Position, Worker, Task


class TaskManagerModelsTest(TestCase):
    def test_task_type_str(self):
        task_type = TaskType(name="Test Task Type")
        self.assertEqual(str(task_type), "Test Task Type")

    def test_position_str(self):
        position = Position(name="Test Position")
        self.assertEqual(str(position), "Test Position")

    def test_worker_str(self):
        worker = Worker(
            username="test",
            email="test@gmail.com",
            password="test123",
            first_name="test",
            last_name="user",
        )
        self.assertEqual(str(worker), "test (test user)")

    def test_task_str(self):
        task_type = TaskType(name="Memory optimization")
        task = Task(
            name="Test task",
            description="Test description",
            deadline="2021-10-10",
            is_completed=False,
            priority="high",
            task_type=task_type,
        )
        self.assertEqual(str(task), "Test task")


class TaskManagerViewsTest(TestCase):
    def setUp(self):
        self.user = Worker.objects.create_user(
            username="test_user",
            email="test@gmail.com",
            password="qawsed",
            first_name="test",
            last_name="user",
        )
        self.client.login(username="test_user", password="qawsed")

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/index.html")

    def test_positions(self):
        response = self.client.get("/positions/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/position_list.html")

    def test_workers(self):
        response = self.client.get("/workers/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/worker_list.html")

    def test_tasks(self):
        response = self.client.get("/tasks/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/task_list.html")

    def test_task_create(self):
        response = self.client.get("/tasks/create/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/task_form.html")

    def test_task_update(self):
        task_type = TaskType.objects.create(name="Memory optimization")
        task = Task.objects.create(
            name="Test task",
            description="Test description",
            deadline="2021-10-10",
            is_completed=False,
            priority="high",
            task_type=task_type,
        )
        response = self.client.get(f"/tasks/{task.id}/update/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/task_form.html")

    def test_task_delete(self):
        task_type = TaskType.objects.create(name="Memory optimization")
        task = Task.objects.create(
            name="Test task",
            description="Test description",
            deadline="2021-10-10",
            is_completed=False,
            priority="high",
            task_type=task_type,
        )
        response = self.client.get(f"/tasks/{task.id}/delete/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/task_confirm_delete.html")
