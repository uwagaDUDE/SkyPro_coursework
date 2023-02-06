class Interface:

    def greetings(self):
        return print(f'### История банковских операций ###')

    def operations_count(self, count=0):
        return print(f'Всего операций: {count}\n'
                     f'Чтобы показать 5 последних операций введите: "last"')

    def find_operaiton(self):
        return input('Номер или ID операции: ')

    def description_of_operation(self, description):
        return f"Тип операции: {description}"

    def date_of_operation(self, date):
        return f"Время операции: {date:%d.%m.%Y %H:%M:%S}"

    def operation_from_card(self, card, card_type, card_number):
        if "Счет" in card:
            return f"Перевод от: {card_type} {card_number}"
        else:
            return f"Перевод от: {card_type} **** **** **** {card_number}"

    def operation_to(self, op_to):
        return f"Перевод кому: {op_to}"

    def amount(self, amount):
        return f'Сумма перевода: {amount}'

    def open_new_wallet(self, wallet):
        return f'Номер счета: {wallet}'

class Errors:
    def wrong_id(self):
        return f'Введеный номер операции или ID не найдены.'
