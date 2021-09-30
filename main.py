'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici

  if n<2:
    return False
  for i in range(2, n/2+1):

      if n % i == 0:
        return False

  return True



'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici



'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici


  # comentariu

'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici


def main():
  # interfata de tip consola aici

  while True:
    print("1. Primalitatea lui n")
    print("x. Iesire din program")

    optiune=input("Alege optiune:")

    if optiune == '1':
      numar=int(input("Introdu numarul: "))
      if is_prime(numar):
        print(f'{numar} este numar prim')
      else: print(f'{numar} nu este numar prim')

    elif optiune == 'x':
        break
    else: print("Optiune invalida")

if __name__ == '__main__':
  main()
