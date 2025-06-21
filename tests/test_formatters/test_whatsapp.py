"""Tests for WhatsApp formatter."""

from datetime import date
from taskdaily.core.models.project import Project
from taskdaily.core.models.task import Task
from taskdaily.formatters.whatsapp import WhatsAppFormatter


def test_whatsapp_format_basic():
    """Test basic WhatsApp formatting."""
    status_info = {
        "completed": {"emoji": "✅", "show_in_report": True},
        "planned": {"emoji": "📝", "show_in_report": False},
    }

    formatter = WhatsAppFormatter(status_info)
    project = Project("Personal", "🏠")
    project.add_task(Task("Test task", "Personal", "✅"))

    output = formatter.format_tasks([project], date.today())

    # Check header
    assert "*DAILY PLAN" in output
    assert str(date.today()) in output

    # Check project formatting
    assert "*🏠 Personal*" in output

    # Check task formatting
    assert "✓ Test task" in output  # Completed task


def test_whatsapp_format_report():
    """Test WhatsApp report formatting."""
    status_info = {
        "completed": {"emoji": "✅", "show_in_report": True},
        "planned": {"emoji": "📝", "show_in_report": False},
    }

    formatter = WhatsAppFormatter(status_info)
    project = Project("Personal", "🏠")
    project.add_task(Task("Completed task", "Personal", "✅"))
    project.add_task(Task("Planned task", "Personal", "📝"))

    output = formatter.format_tasks([project], date.today(), is_report=True)

    # Check header
    assert "*EOD REPORT" in output

    # Check task filtering
    assert "Completed task" in output
    assert "Planned task" not in output


def test_whatsapp_format_multiple_projects():
    """Test WhatsApp formatting with multiple projects."""
    status_info = {
        "completed": {"emoji": "✅", "show_in_report": True},
        "in_progress": {"emoji": "⚡", "show_in_report": True},
    }

    formatter = WhatsAppFormatter(status_info)

    # Create projects
    personal = Project("Personal", "🏠")
    personal.add_task(Task("Personal task", "Personal", "✅"))

    work = Project("Work", "💼")
    work.add_task(Task("Work task", "Work", "⚡"))

    output = formatter.format_tasks([personal, work], date.today())

    # Check project sections
    assert "*🏠 Personal*" in output
    assert "*💼 Work*" in output

    # Check tasks
    assert "✓ Personal task" in output  # Completed task
    assert "• Work task" in output  # In-progress task


def test_whatsapp_format_empty_project():
    """Test WhatsApp formatting with empty project."""
    formatter = WhatsAppFormatter({})
    project = Project("Empty", "📝")

    output = formatter.format_tasks([project], date.today())

    # Empty project should not appear in output
    assert "Empty" not in output
