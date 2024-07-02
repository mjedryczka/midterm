from app.commands import Command

class MenuCommand(Command):
    def execute(self):
        print(f'Menu Commands')
        print(f'\tMenu')
        print(f'\tExit')
        print(f'Calculator Commands')
        print(f'\tAdd')
        print(f'\tSubtract')
        print(f'\tMultiply')
        print(f'\tDivide')
        print(f'History Commands')
        print(f'\tGet History')
        print(f'\tClear History')
        print(f'\tGet Latest')
        print(f'\tGet By Operation')