import scripts, interface

"""
Известные ошибки:
1. Поиск почему-то идет только до !74! операции, дальше выдает Error по ID.
"""

data = scripts.Data()
interface = interface.Interface()

if __name__ == '__main__':
    interface.greetings()
    interface.operations_count(data.counts)
    data.user_search(interface.find_operaiton())

    #инпут для того, чтобы программа не выключалась после вывода информации на экран, если запускать через консоль
    input()

