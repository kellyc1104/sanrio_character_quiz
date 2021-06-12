"""Tests for my functions."""

import pytest

def test_question_answer():
    """Tests for the `question_answer` function."""
    
    # Tests if function is callable.
    assert callable(final_score)
    
    # Tests if function returns an integer.
    assert isinstance(question_answer(), int)

    
def test_final_score():
    """Tests for the `final_score` function."""
    
    # Tests if function is callable.
    assert callable(final_score)
    
    # Tests if function returns a float.
    assert isinstance(final_score(), float)

    
def test_max_score():
    """Tests for the `max_score` function."""
    
    # Tests if function is callable.
    assert callable(max_score)
    
    # Tests if function returns a string.
    assert isinstance(max_score({'a': 5, 'b': 7}), str)
    
    # Tests if indicated inputs will output the correct statement.
    assert max_score({'a': 5, 'b': 7}) == "The results are out! You are most like b!"
    assert max_score({'a': 5, 'b': 7, 'c': 7}) == "The results are out! You are most like b!"