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

    # def all_operations_count(self):
    #     """
    #     Для вывода общего количества транзакций
    #     :return:
    #     """
    #     self.ids = []
    #     for i in self.operations_dict:
    #         for x in i:
    #             if x == 'id':
    #                 self.ids.append(i)
    #     return len(self.ids)

    def user_search(self, user_input):

        if user_input.isnumeric():
            if int(user_input) not in range(1,100) and int(user_input) not in self.ids:
                return print(f'{error.wrong_id()}')

            else:
                if len(user_input) > 3:
                    for i in self.operations_dict:
                        for x in i:
                            if int(user_input) == i['id']:
                                self.information(i)
                                return

                if len(user_input) < 4:
                    return print(f'{self.ids[int(user_input)-1]}')
        else:
            if user_input == "last":
                return print(f'{self.ids[0:6]}')

    def information(self, i):
        self.description = i['description']
        number_of_card = str(i['from'])
        splitted = number_of_card.split()
        date = i['date']
        self.date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
        return print(f'\n{interface.date_of_operation(self.date)} || {self.description}\n'
                     f'{interface.operation_from(splitted)} -> {interface.operation_to(i["to"])}\n'
                     f'{interface.amount(i["operationAmount"]["amount"])} {i["operationAmount"]["currency"]["name"]}')


