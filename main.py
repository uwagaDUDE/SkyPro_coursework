import scripts, interface

"""
Известные ошибки:
1. Поиск почему-то идет только до !74! операции, дальше выдает Error по ID.
"""

data = scripts.Data()
interface = interface.Interface()

def main():
    interface.greetings()
    interface.operations_count(data.counts)
    data.user_search(interface.find_operaiton())
main()
input()