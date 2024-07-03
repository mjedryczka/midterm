import pytest
from app import App

def test_app_arithmetic_commands(capfd, monkeypatch):
    inputs = iter(['history_clear', 'add 2 2', 'subtract 6 2', 'multiply 2 2', 'divide 8 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    captured = capfd.readouterr()
    assert "4" in captured.out, "Command(s) did not return the correct value of 4"
    assert str(e.value) == "0", "The app did not exit as expected"