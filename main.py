'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici

  if n<2:
    return False
  for i in range(2, n//2+1):

      if n % i == 0:
        return False

  return True



'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici

  p=1
  for i in range(len(lst)):
    p=p * lst[i]
  print(p)

'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici

  while x!=y:
    if x<y:
      y=y-x
    else: x=x-y
  print(x)

  # comentariu

'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici

  while y!=0:
      rest=x%y
      x=y
      y=rest

  print(x)

def main():
  # interfata de tip consola aici

  while True:
    print("1. Primalitatea lui n")
    print("2. Produsul numerelor")
    print("3. Cmmdc a 2 numere in prima metoda")
    print("4. Cmmdc a 2 numere in a doua metoda")
    print("x. Iesire din program")

    optiune=input("Alege optiune:")

    if optiune == '1':
      numar=int(input("Introdu numarul: "))
      if is_prime(numar):
        print(f'{numar} este numar prim')
      else: print(f'{numar} nu este numar prim')

    elif optiune =='2':
      nr_str=input("Introduceti numerele cu cate un spatiu intre ele: ")
      nr_str_lst=nr_str.split(' ')
      nr_int_lst=[]
      for nr_str in nr_str_lst:
          nr_int_lst.append(int(nr_str))
      get_product(nr_int_lst)

    elif optiune == '3':
      primul_nr=int(input("introduceti primul nr: "))
      al_doilea_nr=int(input("introduceti al doilea nr: "))
      get_cmmdc_v1(primul_nr,al_doilea_nr)

    elif optiune == '4':
      primul_nr = int(input("introduceti primul nr: "))
      al_doilea_nr = int(input("introduceti al doilea nr: "))
      get_cmmdc_v2(primul_nr, al_doilea_nr)

    elif optiune == 'x':
        break
    else: print("Optiune invalida")

if __name__ == '__main__':
  main()
