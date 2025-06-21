"""Tests for Project model."""

from taskdaily.core.models.project import Project
from taskdaily.core.models.task import Task


def test_project_creation():
    """Test basic project creation."""
    project = Project("Personal", "🏠")
    assert project.name == "Personal"
    assert project.emoji == "🏠"
    assert len(project.tasks) == 0


def test_project_add_task():
    """Test adding tasks to project."""
    project = Project("Personal", "🏠")
    task = Task("Test task", "Personal", "📝")
    project.add_task(task)
    assert len(project.tasks) == 1
    assert project.tasks[0].content == "Test task"


def test_project_carry_forward_tasks():
    """Test carrying forward tasks."""
    status_info = {
        "completed": {"emoji": "✅", "carry_forward": False},
        "planned": {"emoji": "📝", "carry_forward": True},
        "cancelled": {"emoji": "🚫", "carry_forward": False},
        "in_progress": {"emoji": "⚡", "carry_forward": True},
    }

    project = Project("Personal", "🏠")

    # Add tasks with different statuses
    project.add_task(Task("Completed task", "Personal", "✅"))
    project.add_task(Task("Planned task", "Personal", "📝"))
    project.add_task(Task("Cancelled task", "Personal", "🚫"))
    project.add_task(Task("In progress task", "Personal", "⚡"))

    # Carry forward tasks
    carried_tasks = project.carry_forward_tasks(status_info)

    # Should only carry forward planned and in-progress tasks
    assert len(carried_tasks) == 2

    # Check carried tasks have correct status
    carried_contents = [task.content for task in carried_tasks]
    assert "Planned task" in carried_contents
    assert "In progress task" in carried_contents

    # Check all carried tasks have carry forward status
    for task in carried_tasks:
        assert task.status_emoji == "➡️"


def test_project_task_filtering():
    """Test task filtering for reports."""
    status_info = {
        "completed": {"emoji": "✅", "show_in_report": True},
        "planned": {"emoji": "📝", "show_in_report": False},
        "cancelled": {"emoji": "🚫", "show_in_report": True},
    }

    project = Project("Personal", "🏠")

    # Add tasks with different statuses
    project.add_task(Task("Completed task", "Personal", "✅"))
    project.add_task(Task("Planned task", "Personal", "📝"))
    project.add_task(Task("Cancelled task", "Personal", "🚫"))

    # Get tasks for report
    report_tasks = [
        task for task in project.tasks if task.should_show_in_report(status_info)
    ]

    # Should only show completed and cancelled tasks
    assert len(report_tasks) == 2

    # Check report tasks have correct content
    report_contents = [task.content for task in report_tasks]
    assert "Completed task" in report_contents
    assert "Cancelled task" in report_contents
    assert "Planned task" not in report_contents
