class Interface:

    def greetings(self):
        return print(f'### История банковских операций ###')
    def operations_count(self, count=0):
        return print(f'Всего операций: {count}\n'
                     f'Чтобы показать последние 5 операции введите: "last"')

    def find_operaiton(self):
        return input('Номер или ID операции: ')

    def description_of_operation(self, description):
        return f"{description}"

    def date_of_operation(self, date):
        return f"Время операции: {date:%d.%m.%Y %H:%M:%S}"

    def operation_from(self, op_from):
        return f"Перевод от: {op_from}"

    def operation_to(self, op_to):
        return f"Перевод кому: {op_to}"

    def amount(self, amount):
        return f'Сумма перевода {amount}'

class Errors:
    def wrong_id(self):
        return print(f'Введеный номер операции или ID не найдены.')
