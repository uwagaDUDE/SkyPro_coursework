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

    def operation_to_card(self, card):
        if "Счет" in card:
            return f"Перевод кому: {card}"
        else:
            splitted_card = card.split()
            if len(splitted_card) > 2:
                card_name = splitted_card[0,1]
                card_number = splitted_card[2]
                return f"Перевод кому: {card_name} **** **** **** {card_number[-4:]}"
            else:
                card_name = splitted_card[0]
                card_number = splitted_card[1]
            return f"Перевод кому: {card_name} **** **** **** {card_number[-4:]}"

    def amount(self, amount):
        return f'Сумма перевода: {amount}'

    def open_new_wallet(self, wallet):
        return f'Номер счета: {wallet}'

class Errors:
    def wrong_id(self):
        return f'Введеный номер операции или ID не найдены.'
