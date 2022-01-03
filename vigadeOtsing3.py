from random import *
s=[]
pos=[]
neg=[]
nol=[]
def arvud_loendis():
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:
        mini,maxi=vahetus(mini,maxi)
    generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    jagamine(s,pos,neg,nol)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",nol)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    s.sort()
    print(s)

def vahetus(a:int,b:int):
    """Kui a>b siis vahetame neid
    :param int a:arv, mis on suurem kui b
    :param int b:arv, mis on vaiksem kui a
    :rtype:int, int
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """Generiruet cisla ot a do b v n kolicestve
    :param int n:kol-vo generiruemih cisel
    :param int a:minimalnoe cislo v diapazone
    :param int b:maksimalnoe cislo v diapozone
    :param list loend:spisok cisel
    """
    for i in range (n):
        loend.append(randint(a,b))


def jagamine(loend:list,p:list,n:list,nol:list):
    """sortiruet otricatelnie i polozitelnie cisla
    :param list loend:spisok vseh cisel
    :param list p:spisok polozitelnih cisel
    :param list n:spisok otricatelnih cisel
    :param list nol:spisok nulei
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend:list):
    """nahodit srednee iz cisel v spiske
    :param list loend:spisok cisel
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)#round okruglaet do celogo
    return kesk

def lisamine(loend:list,el:int):
    """

    """
    loend.append(el)
    loend.sort()

arvud_loendis()
