# TaskDaily Testing Guide

## Manual Testing Checklist

### 1. Task File Creation
```bash
# Test creating today's file
daily create

# Test creating file for specific date
daily create -d 2025-06-25
```
Expected Results:
- File should be created in correct directory (YYYY/MM/DD/YYYY-MM-DD.md)
- File should contain default sections from config
- Previous day's incomplete tasks should carry forward

### 2. Task Status Testing
Test each status emoji in the markdown file:
- 📝 Planned
- ⚡ In Progress
- 🚧 Blocked
- ➡️ Carried Forward
- ✅ Completed
- 🚫 Cancelled

Example task file format:
```markdown
🏠 Personal
- [ ] Task 1 📝
- [ ] Task 2 ⚡
- [ ] Task 3 🚧
- [ ] Task 4 ✅
- [ ] Task 5 🚫
- [ ] Task 6 ➡️

🔬 Work
- [ ] Another task 📝
```

### 3. Output Format Testing

#### Slack Format
```bash
daily share --format slack
daily share --format slack --report
```
Check:
- Emoji conversion
- Task status indicators (○/●)
- Section formatting
- Report filtering (no 📝 tasks)

#### Teams Format
```bash
daily share --format teams
daily share --format teams --report
```
Check:
- Markdown formatting
- Task checkboxes (☐/☑)
- Header formatting
- Report filtering

#### WhatsApp Format
```bash
daily share --format whatsapp
daily share --format whatsapp --report
```
Check:
- Bold text formatting
- Task bullets (•/✓)
- Emoji display
- Report filtering

### 4. Task Carrying Forward
1. Create a file for day 1 with various task statuses
2. Create next day's file
3. Verify:
   - Completed tasks (✅) don't carry forward
   - Cancelled tasks (🚫) don't carry forward
   - Other tasks carry forward with ➡️ status

### 5. Project Management
Test:
- Multiple projects in same file
- Custom emoji sections
- Unicode emoji handling
- Section ordering

### 6. Configuration
```bash
daily config init
daily config path
```
Verify:
- Config file creation
- Default sections
- Status definitions
- Format settings

## Automated Testing

### Unit Tests Structure
```
tests/
├── test_core/
│   ├── test_task.py
│   └── test_project.py
├── test_formatters/
│   ├── test_slack.py
│   ├── test_teams.py
│   └── test_whatsapp.py
└── test_utils/
    └── test_text.py
```

### Key Test Cases

1. Task Tests:
```python
def test_task_status():
    task = Task("Test task", "Personal", "📝")
    assert not task.is_completed
    assert task.is_planned
    assert not task.is_cancelled

def test_task_markdown():
    task = Task("Test task", "Personal", "✅")
    assert task.to_markdown() == "- [ ] Test task ✅"

def test_task_from_markdown():
    task = Task.from_markdown("- [ ] Test task ✅", "Personal")
    assert task.content == "Test task"
    assert task.status_emoji == "✅"
```

2. Project Tests:
```python
def test_project_tasks():
    project = Project("Personal", "🏠")
    task = Task("Test task", "Personal", "📝")
    project.add_task(task)
    assert len(project.tasks) == 1

def test_project_carry_forward():
    project = Project("Personal", "🏠")
    task1 = Task("Task 1", "Personal", "✅")
    task2 = Task("Task 2", "Personal", "📝")
    project.add_task(task1)
    project.add_task(task2)
    carried = project.carry_forward_tasks(status_info)
    assert len(carried) == 1
```

3. Formatter Tests:
```python
def test_slack_format():
    project = Project("Personal", "🏠")
    task = Task("Test task", "Personal", "✅")
    project.add_task(task)
    formatter = SlackFormatter(status_info)
    output = formatter.format_tasks([project], date.today())
    assert "● Test task" in output

def test_teams_format():
    project = Project("Personal", "🏠")
    task = Task("Test task", "Personal", "✅")
    project.add_task(task)
    formatter = TeamsFormatter(status_info)
    output = formatter.format_tasks([project], date.today())
    assert "☑ Test task" in output
```

## Running Tests
```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests with coverage
pytest --cov=taskdaily tests/

# Generate coverage report
pytest --cov=taskdaily --cov-report=html tests/
```

## Common Issues to Test For

1. Unicode Handling:
- Test with various emoji combinations
- Test with international characters in task names
- Test with special characters in project names

2. Edge Cases:
- Empty task lists
- Missing status emojis
- Invalid date formats
- Non-existent files
- Multiple status emojis in one task

3. Performance:
- Large number of tasks
- Many projects
- Long task descriptions
- Multiple days of history

## Continuous Integration

Recommended GitHub Actions workflow:
```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: |
          pip install -e .
          pip install pytest pytest-cov
      - name: Run tests
        run: pytest --cov=taskdaily tests/
```
