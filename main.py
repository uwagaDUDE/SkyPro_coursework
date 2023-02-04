import scripts, interface

data = scripts.Data()
interface = interface.Interface()

def main():
    interface.greetings()
    interface.operations_count(data.counts)
    data.user_search(interface.find_operaiton())
main()