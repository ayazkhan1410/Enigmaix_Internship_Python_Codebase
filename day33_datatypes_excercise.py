def print_alternate_elements(list1):
  """Prints the alternate elements of the given list."""
  alternate_elements = []
  for i in range(0, len(list1), 2):
    alternate_elements.append(list1[i])
  print("Alternate elements are: ", alternate_elements)
def main():
  """The main function."""
  list1 = []
  size = int(input("Enter the number of elements in the list: "))
  for i in range(size):
    element = int(input("Enter element {}: ".format(i + 1)))
    list1.append(element)
  print_alternate_elements(list1)
if __name__ == "__main__":
  main()
