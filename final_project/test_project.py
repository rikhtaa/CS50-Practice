import pytest
from project import add_movie, view_movies, update_movie

def test_view_movies(capsys):
    view_movies()
    captured = capsys.readouterr()
    assert "title" in captured.out

def test_update_movie(capsys):
    update_movie("happy together", "rating", "9")
    captured = capsys.readouterr()
    assert "updated" in captured.out

def test_add_movie(monkeypatch, capsys):
    inputs = iter(["happy together", "romance", "watched", "10"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    add_movie()
    captured = capsys.readouterr()
    assert "added" in captured.out