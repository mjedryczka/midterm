import pytest
from app import App

def test_app_menu_command(capfd, monkeypatch):
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
        
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_exit_command(capfd, monkeypatch):
    inputs = iter(['exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
        
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_arithmetic_commands(capfd, monkeypatch):
    inputs = iter(['clear_history', 'add 2 2', 'subtract 6 2', 'multiply 2 2', 'divide 8 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    captured = capfd.readouterr()
    assert "4" in captured.out, "Command(s) did not return the correct value of 4"
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_get_by_operation_command(capfd, monkeypatch):
    inputs = iter(['clear_history', 'add 2 2', 'get_by_operation add', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    captured = capfd.readouterr()
    assert "[Calculation(2, 2, add)]" in captured.out, "Command did not return correctly"
    assert str(e.value) == "Exiting...", "The app did not exit as expected"
    
def test_app_get_history_command(capfd, monkeypatch):
    inputs = iter(['clear_history', 'add 2 2', 'get_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    captured = capfd.readouterr()
    assert "[Calculation(2, 2, add)]" in captured.out, "Command did not return correctly"
    assert str(e.value) == "Exiting...", "The app did not exit as expected"
    
def test_app_get_latest_command(capfd, monkeypatch):
    inputs = iter(['clear_history', 'add 2 2', 'get_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    captured = capfd.readouterr()
    assert "[Calculation(2, 2, add)]" in captured.out, "Command did not return correctly"
    assert str(e.value) == "Exiting...", "The app did not exit as expected"
    
def test_app_clear_history_command(capfd, monkeypatch):
    inputs = iter(['clear_history', 'add 2 2', 'clear_history', 'get_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    captured = capfd.readouterr()
    assert "[]" in captured.out, "Command did not return correctly"
    assert str(e.value) == "Exiting...", "The app did not exit as expected"