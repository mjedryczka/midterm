from app.commands import Command
import logging

class MenuCommand(Command):
    def execute(self, command_name: str):
        logging.info("Printed Menu Commandsd")
        print(f'Menu Commands')
        print(f'\tMenu')
        print(f'\tExit')

        print(f'Calculator Commands')
        print(f'\tAdd\t\t - add <numberA> <numberB>')
        print(f'\tSubtract\t - subtract <numberA> <numberB>')
        print(f'\tMultiply\t - multiply <numberA> <numberB>')
        print(f'\tDivide\t\t - divide <numberA> <numberB>')

        print(f'History Commands')
        print(f'\tGet History\t - history_get')
        print(f'\tClear History\t - history_clear')
        print(f'\tGet Latest\t - history_print_latest')
        print(f'\tGet By Operation - history_print_by_latest <operation_name>')

        print(f'Save File Commands')
        print(f'\tSave To File\t - save_make')
        print(f'\tLoad Save File\t - save_load')
        print(f'\tClear Save Filet\t - save_clear')
        print(f'\tDelete Last Operation  - save_delete_newest')
        print(f'\tDelete Last Operation  - save_delete_oldest')