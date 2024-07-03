import pytest
from app import App

def test_app_menu_command(capfd, monkeypatch):
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
        
    assert str(e.value) == "0", "The app did not exit as expected"

def test_app_exit_command(capfd, monkeypatch):
    inputs = iter(['exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
        
    assert str(e.value) == "0", "The app did not exit as expected"

def test_app_get_by_operation_command(capfd, monkeypatch):
    inputs = iter(['history_clear', 'add 2 2', 'history_get_by_operation add', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    captured = capfd.readouterr()
    assert "[add 2 2 4]" in captured.out, "Command did not return correctly"
    assert str(e.value) == "0", "The app did not exit as expected"
    
def test_app_history_get_command(capfd, monkeypatch):
    inputs = iter(['history_clear', 'add 2 2', 'history_print', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    captured = capfd.readouterr()
    assert "[add 2 2 4]" in captured.out, "Command did not return correctly"
    assert str(e.value) == "0", "The app did not exit as expected"
    
def test_app_get_latest_command(capfd, monkeypatch):
    inputs = iter(['history_clear', 'add 2 2', 'history_print', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    captured = capfd.readouterr()
    assert "[add 2 2 4]" in captured.out, "Command did not return correctly"
    assert str(e.value) == "0", "The app did not exit as expected"
    
def test_app_history_clear_command(capfd, monkeypatch):
    inputs = iter(['history_clear', 'add 2 2', 'history_clear', 'history_print', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    captured = capfd.readouterr()
    assert "[]" in captured.out, "Command did not return correctly"
    assert str(e.value) == "0", "The app did not exit as expected"