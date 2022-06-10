from linked_list import DoublyLinkedList
from transistor import Transistor


lst = DoublyLinkedList()

lst.push_back(Transistor("p-n-p", "Antoniy", 1, 1))
lst.push_back(Transistor("a", "Avreliy", -1, 1))
lst.push_back(Transistor("ddd", "Henry", 5, 1))
lst.push_back(Transistor("d", "Kutsevalov", 224, 1))
lst.push_back(Transistor("a", "Ruffalo", 3, 1))
lst.push_back(Transistor("d", "Avreliy", 11, 1))
lst.push_back(Transistor("aboba", "Avreliy", -1, 1))
lst.push_back(Transistor("p-n-p", "Lenard", 3, 1))

print("Starting list of transistors:")
lst.print_list()
print()
print("Transistors of mark Avreliy:")
lst.print_by_mark("Avreliy")
print()
lst.sort_by_selection()
print("Transistors sorted by type and Imax:")
lst.print_list()