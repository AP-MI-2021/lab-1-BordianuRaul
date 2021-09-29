'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici

  n=int(input("Introdu numarul: "))

  prim= true
  for i in range(2, n/2):

      if (n % i) == 0:
        prim= false
        break;

  return prim



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

if __name__ == '__main__':
  main()
