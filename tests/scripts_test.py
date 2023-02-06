import scripts

test = scripts.Data()
""" 
ДЛЯ ЗАПУСКА ТЕСТОВ НЕОБХОДИМО ИЗМЕНИТЬ ПУТЬ:
В 14 СТРОКЕ НА: 
self.transaction_data = open('../data/operations.json', 'rt', encoding="UTF-8")

Рабочее состояние программы:
self.transaction_data = open('data/operations.json', 'rt', encoding="UTF-8")

Для запуска ввести в терминале: pytest --cov

"""
class Tests:
     def test_user_search(self):
         # Тест на вывод информации по номеру транзакции
         assert test.user_search("5") == ('\nВремя операции: 04.04.2019 23:20:05 || Тип операции: Перевод со счета на счет\n'
                                          'Перевод от: Счет 19708645243227258542 -> Перевод кому: Счет 75651667383060284188\n'
                                          'Сумма перевода: 79114.93 USD')

         # Тест на вывод информации по ID транзакции
         assert test.user_search("441945886") == ('\nВремя операции: 26.08.2019 10:50:58 || Тип операции: Перевод организации\n'
                                                 'Перевод от: Maestro **** **** **** 5199 -> Перевод кому: Счет ''64686473678894779589\n'
                                                 'Сумма перевода: 31957.58 руб.')

         # Тест на неправильный чис
         assert test.user_search("123") == ('Введеный номер операции или ID не найдены.')

         # Тест на вывод 5 последних операций
         assert test.user_search('last') == ('For test')

         assert test.user_search("asdadasd") == ('Введеный номер операции или ID не найдены.')



    # def test_operations_count(self):
    #     assert interface.Interface().operations_count(100) == 100
