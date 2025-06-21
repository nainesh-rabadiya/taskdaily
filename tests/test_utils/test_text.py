"""Tests for text utilities."""

from taskdaily.utils.text import clean_section_header, split_into_sections


def test_clean_section_header():
    """Test cleaning section headers."""
    # Test basic emoji and name
    emoji, name = clean_section_header("\U0001F3E0 Personal")  # 🏠
    assert emoji == "\U0001F3E0"
    assert name == "Personal"

    # Test with multiple spaces
    emoji, name = clean_section_header("\U0001F4DA  Learning")  # 📚
    assert emoji == "\U0001F4DA"
    assert name == "Learning"

    # Test with trailing spaces
    emoji, name = clean_section_header("\U0001F4BC Work  ")  # 💼
    assert emoji == "\U0001F4BC"
    assert name == "Work"


def test_split_into_sections():
    """Test splitting content into sections."""
    content = """\U0001F3E0 Personal
- [ ] Task 1 \U0001F4DD
- [ ] Task 2 \U00002705

\U0001F4BC Work
- [ ] Task 3 \U000026A1
- [ ] Task 4 \U0001F6A7

\U0001F4DA Learning
- [ ] Task 5 \U0001F4DD"""

    sections = split_into_sections(content)

    # Check section count
    assert len(sections) == 3

    # Check section names
    assert "\U0001F3E0 Personal" in sections
    assert "\U0001F4BC Work" in sections
    assert "\U0001F4DA Learning" in sections

    # Check task count per section
    assert len(sections["\U0001F3E0 Personal"]) == 2
    assert len(sections["\U0001F4BC Work"]) == 2
    assert len(sections["\U0001F4DA Learning"]) == 1


def test_split_into_sections_empty():
    """Test splitting empty content."""
    sections = split_into_sections("")
    assert len(sections) == 0


def test_split_into_sections_no_tasks():
    """Test splitting content with empty sections."""
    content = """\U0001F3E0 Personal

\U0001F4BC Work

\U0001F4DA Learning"""

    sections = split_into_sections(content)

    # All sections should exist but be empty
    assert len(sections) == 3
    assert len(sections["\U0001F3E0 Personal"]) == 0
    assert len(sections["\U0001F4BC Work"]) == 0
    assert len(sections["\U0001F4DA Learning"]) == 0


def test_split_into_sections_mixed():
    """Test splitting content with mixed empty and non-empty sections."""
    content = """\U0001F3E0 Personal
- [ ] Task 1 \U0001F4DD

\U0001F4BC Work

\U0001F4DA Learning
- [ ] Task 2 \U00002705
- [ ] Task 3 \U000026A1"""

    sections = split_into_sections(content)

    # Check section content
    assert len(sections["\U0001F3E0 Personal"]) == 1
    assert len(sections["\U0001F4BC Work"]) == 0
    assert len(sections["\U0001F4DA Learning"]) == 2
