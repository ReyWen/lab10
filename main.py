from linked_list import LinkedList, Resistor


def main():
    resistor1 = Resistor(1000, 10, 0.8)
    resistor2 = Resistor(500, 10, 0.9)
    resistor3 = Resistor(600, 10, 0.7)
    resistor4 = Resistor(700, 10, 0.6)
    resistor5 = Resistor(800, 10, 0.75)
    linked = LinkedList()
    # Додати резістори до списку
    linked.add(resistor1)
    linked.add(resistor2)
    linked.add(resistor3)
    linked.add(resistor4)
    linked.add(resistor5)
    # Вивід всього списку
    print("Весь список")
    for node in linked.iterator():
        print(node)
    print("Весь список після видалення 700")
    linked.delete_element(resistor4)
    for node in linked.iterator():
        print(node)

    # Вивід резисторів з точністю вище 0.75
    print('Резистори з точністю вище 0.75')
    linked.print_by_precision(0.75)

    # Видалити список
    linked.delete_list()

if __name__ == '__main__':
    main()
