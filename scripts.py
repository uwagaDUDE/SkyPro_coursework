import json
from datetime import datetime
import interface
error = interface.Errors()
interface = interface.Interface()
class Data:

    def __init__(self):
        """
        Загрузка транзакций
        """
        self.transaction_data = open('data/operations.json', 'rt', encoding="UTF-8")
        self.operations_dict = json.load(self.transaction_data)
        self.ids = []
        for i in self.operations_dict:
            for x in i:
                if x == 'id':
                    self.ids.append(i['id'])
        self.counts = len(self.ids)


    def user_search(self, user_input):
        """
        Обработка и фильтрация запроса пользователя по ID или по номеру транзакции.
        :param user_input: пользовательский ввод.
        :return:
        """
        if user_input.isnumeric():
            if int(user_input) not in range(1,self.counts) and int(user_input) not in self.ids:
                return error.wrong_id()

            else:
                if len(user_input) > 3:
                    for i in self.operations_dict:
                        if int(user_input) == i['id']:
                            self.information(i)
                            return


                if len(user_input) < 4:
                    for i in self.operations_dict:
                        if self.ids[int(user_input)-1] == i['id']:
                            self.information(i)
                            return


        else:
            if user_input == "last":
                ticker = 0
                for i in self.operations_dict:
                    if self.ids[ticker] == i['id']:
                        self.information(i)
                        ticker += 1
                        if ticker == 5:
                            return

            else:
                return error.wrong_id()

    def information(self, i):
        """
        Работа с информацией о карте
        сделано не совсем корректно
        Правильным было бы сделать напрямую через тип операции, а не через наличие в ней 'FROM'
        :param i: Перебор объекта с операциями
        :return:
        """
        self.description = interface.description_of_operation(i['description'])

        date = i['date']
        self.date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')

        if "from" in i:
            number_of_card = i['from']
            card = number_of_card.split()

            if "Счет" in card:
                card_number = card[1]
                card_type = card[0]
                return self.return_fuction(card, card_type, card_number, i)

            elif len(card) == 2:
                card_number = card[1][12:]
                card_type = card[0]
                return self.return_fuction(card, card_type, card_number, i)

            else:
                card_number = card[2][12:]
                card_type=''
                for c in card[0:2]:
                    card_type += c
                return self.return_fuction(card, card_type, card_number, i)

        else:
            card = i['to'].split()
            card_number = card[1]
            return print(f'\n{interface.date_of_operation(self.date)} || {self.description}\n'
                         f'{interface.open_new_wallet(card_number)}')

    def return_fuction(self, card, card_type, card_number, i):
        """
        :param card: Общие данные карты
        :param card_type: Тип карты
        :param card_number: Номер карты
        :param i: Перебор объекта с операциями
        :return:
        """

        print(f'\n{interface.date_of_operation(self.date)} || {self.description}\n'
              f'{interface.operation_from_card(card, card_type, card_number)} -> {interface.operation_to(i["to"])}\n'
              f'{interface.amount(i["operationAmount"]["amount"])} {i["operationAmount"]["currency"]["name"]}')


