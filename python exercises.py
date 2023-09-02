###############################################
# Python Exercises
###############################################

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################

x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)


l = [1, 2, 3, 4,"String",3.2, False]
type(l)

l[-2]


d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}
type(d)

#########################################################################################################################################


t = ("Machine Learning", "Data Science","Data Analyst","Data Engineer")
type(t)

t[0]= "Machine"
dir(t)

dir(l)
print(t)


coral = ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral')

coral[-4:-2]

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

numbers[1:11:2]

numbers[::3]


coral = ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral')
kelp = (2, 1,3,4)

coral_kelp = (coral + kelp)

print(coral_kelp)


new = list(coral)

tuple(new)

#Yorum
tuple("Machine")
list("Machine")


s = {"Python", "Machine Learning", "Data Science","Python","Machine Learning"}
type(s)


print(s)

s[2]


tuple(s)

list(s)


# tuple ---
x = {42, 'foo', (1, 2, 3), 3.14159}

# list
y = {42, 'foo', [1, 2, 3], 3.14159}

# dictionary
z = {1,2, {'a': 1, 'b': 2},5}


#2 Write a line of code that counts the number of unique characters in a string.
string = "hello world"
set(string)
len(set(string))
# 8

#3  Write a line of code that finds the second smallest element in a list.
my_list = [5, 3, 1, 4,1,1,1,1, 2,12,0,-4]
set(my_list)

sorted(set(my_list))[1]

sorted(my_list)[1]
# 0

#4 Write a line of code that creates a tuple containing the squares of numbers from 1 to 5.

tuple(x**2 for x in range(1,6))
#(1, 4, 9, 16, 25)

###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################

text = "the goal is to turn data into information, and information into insight."
text.upper().replace(","," ").replace("."," ").split()

text.replace(","," ").replace("."," ").upper().split()



###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.
len(lst)

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.
lst[0],lst[10]
lst[10]

# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.

data_list = lst[0:4]

lst

data_list

# Adım 4: Sekizinci index'teki elemanı silin.

lst.pop(8)
lst.remove("C")

# pop- remove difference?

# Adım 5: Yeni bir eleman ekleyin.

lst.append(101)
lst


# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.

lst.insert(8, "N")
lst

# Bonus Uygulama

# Write a line of code that creates a list containing the first 10 Fibonacci numbers.
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
fibonacci = [0,1]

while len(fibonacci)<10:
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
print(fibonacci)


###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}


# Adım 1: Key değerlerine erişiniz.

dict.keys()

# Adım 2: Value'lara erişiniz.

dict.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict.update({"Daisy": ["England",13]})
dict

dict["Daisy"][1] = 14
dict
dict["Daisy"][0] = 15


# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict.update({"Ahmet": ["Turkey", 24]})
dict

# Adım 5: Antonio'yu dictionary'den siliniz.

dict.pop("Antonio")
dict

dict.remove("England")
dir(dict)

dict.items()
dict.clear()

print(dict.keys())

dict.get("Daisy")

dict.popitem()
###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################

yeni_list = [2,13,18,93,22]

def func(list):

    return gurkan(list)


def gurkan(list):
    çift_list = []
    tek_list = []
    for i in list:
        if i % 2 == 0:
            çift_list.append(i)
        else:
            tek_list.append(i)
    return çift_list, tek_list

çift,tek = func(yeni_list)

# Alternative Solution by Melih Calis

even_list =[]
odd_list =[]
def func(list):
   [even_list.append(n) if n % 2 == 0 else odd_list.append(n) for n in list]
   return even_list, odd_list

even_list, odd_list = func(yeni_list)

###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for i,x in enumerate(ogrenciler):
    if i<3:
        i += 1
        print("Mühendislik Fakültesi",i,". öğrenci: ",x)
    else:
        i -= 2
        print("Tıp Fakültesi",i,". öğrenci: ",x)


for index, derece in enumerate(ogrenciler, 1):
    if index < 4:
        print("Mühendislik Fakültesi {} . öğrenci: {}".format(index,derece))
    if index >= 4 :
        print("Tıp Fakültesi {} . öğrenci: {}".format(index -3, derece))

###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

zip(ders_kodu,kredi,kontenjan)
zipped=list(zip(ders_kodu,kredi,kontenjan))

zipped[0]


for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
  print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")


uni = list(zip(ders_kodu, kredi, kontenjan))
for ders in uni:
    print("Kredisi", ders[1], "olan",ders[0],"kodlu dersin kontenjani",ders[2],"kisidir." )


###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kume(set1,set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))

kume(kume1,kume2)

