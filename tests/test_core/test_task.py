"""Tests for Task model."""

from datetime import datetime
from taskdaily.core.models.task import Task


def test_task_creation():
    """Test basic task creation."""
    task = Task("Test task", "Personal")
    assert task.content == "Test task"
    assert task.project_name == "Personal"
    assert task.status_emoji == "📝"  # Default status


def test_task_status_properties():
    """Test task status properties."""
    task = Task("Test task", "Personal", "✅")
    assert task.is_completed is True
    assert task.is_planned is False
    assert task.is_cancelled is False

    task = Task("Test task", "Personal", "📝")
    assert task.is_completed is False
    assert task.is_planned is True
    assert task.is_cancelled is False

    task = Task("Test task", "Personal", "🚫")
    assert task.is_completed is False
    assert task.is_planned is False
    assert task.is_cancelled is True


def test_task_markdown_conversion():
    """Test markdown conversion."""
    task = Task("Test task", "Personal", "✅")
    markdown = task.to_markdown()
    assert markdown == "- [ ] Test task ✅"

    # Test parsing markdown
    parsed_task = Task.from_markdown(markdown, "Personal")
    assert parsed_task.content == "Test task"
    assert parsed_task.status_emoji == "✅"
    assert parsed_task.project_name == "Personal"


def test_task_carry_forward():
    """Test task carry forward behavior."""
    status_info = {
        "completed": {"emoji": "✅", "carry_forward": False},
        "planned": {"emoji": "📝", "carry_forward": True},
        "cancelled": {"emoji": "🚫", "carry_forward": False},
    }

    # Completed task should not carry forward
    task = Task("Completed task", "Personal", "✅")
    carried = task.carry_forward(status_info)
    assert carried is None

    # Planned task should carry forward
    task = Task("Planned task", "Personal", "📝")
    carried = task.carry_forward(status_info)
    assert carried is not None
    assert carried.content == "Planned task"
    assert carried.status_emoji == "➡️"

    # Cancelled task should not carry forward
    task = Task("Cancelled task", "Personal", "🚫")
    carried = task.carry_forward(status_info)
    assert carried is None


def test_task_show_in_report():
    """Test task show in report behavior."""
    status_info = {
        "completed": {"emoji": "✅", "show_in_report": True},
        "planned": {"emoji": "📝", "show_in_report": False},
        "cancelled": {"emoji": "🚫", "show_in_report": True},
    }

    # Completed task should show in report
    task = Task("Completed task", "Personal", "✅")
    assert task.should_show_in_report(status_info) is True

    # Planned task should not show in report
    task = Task("Planned task", "Personal", "📝")
    assert task.should_show_in_report(status_info) is False

    # Cancelled task should show in report
    task = Task("Cancelled task", "Personal", "🚫")
    assert task.should_show_in_report(status_info) is True
