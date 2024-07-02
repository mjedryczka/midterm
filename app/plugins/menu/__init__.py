from app.commands import Command

class MenuCommand(Command):
    def execute(self, command_name: str):
        print(f'Menu Commands')
        print(f'\tMenu')
        print(f'\tExit')
        print(f'Calculator Commands')
        print(f'\tAdd\t\t - add <numberA> <numberB>')
        print(f'\tSubtract\t - subtract <numberA> <numberB>')
        print(f'\tMultiply\t - multiply <numberA> <numberB>')
        print(f'\tDivide\t\t - divide <numberA> <numberB>')
        print(f'History Commands')
        print(f'\tGet History\t - get_history')
        print(f'\tClear History\t - clear_history')
        print(f'\tGet Latest\t - get_latest')
        print(f'\tGet By Operation - get_by_operation <operation_name>')