"""
tests/test_display.py
---------------------
Unit tests for the cursor-position logic in display.render_typing_panel().

We call the real function and inspect the Rich Text it produces to verify
that the cursor highlight lands on the correct character position.
"""

import pytest
from rich.text import Text
from display import render_typing_panel
from config import DEFAULT_THEME


def _cursor_positions(target: str, typed: list[str]) -> list[int]:
    """
    Call the real render_typing_panel() and return every character index
    that carries the cursor style.  The panel contains a Text object whose
    spans encode the style for each character.
    """
    theme = DEFAULT_THEME
    panel = render_typing_panel(
        target=target,
        typed=typed,
        elapsed=0.0,
        gross_wpm=0.0,
        net_wpm=0.0,
        accuracy=100.0,
        word_count_done=0,
        total_words=len(target.split()),
        theme=theme,
    )

    # The panel's renderable is a Text assembled from characters + stats.
    # Walk its spans to find which positions carry the cursor style.
    body: Text = panel.renderable
    positions = []
    char_idx = 0
    for span in body.spans:
        if theme.cursor in str(span.style):
            positions.append(span.start)
    return positions


class TestCursorPosition:
    def test_cursor_on_first_char_when_nothing_typed(self):
        """Before typing anything the cursor must sit on character index 0."""
        positions = _cursor_positions("hello", [])
        assert positions == [0], (
            f"Expected cursor at index 0, got {positions}. "
            f"Likely cause: 'len(typed) + 1' shifts the cursor one position too far."
        )

    def test_cursor_advances_after_two_chars(self):
        """After typing 'he' the cursor must sit on index 2 ('l')."""
        positions = _cursor_positions("hello", ["h", "e"])
        assert positions == [2], (
            f"Expected cursor at index 2, got {positions}."
        )

    def test_no_cursor_when_text_complete(self):
        """Once all characters are typed there is no cursor."""
        positions = _cursor_positions("hi", ["h", "i"])
        assert positions == [], (
            f"Expected no cursor when text is complete, got {positions}."
        )
