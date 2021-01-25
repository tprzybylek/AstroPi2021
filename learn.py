print ("siema")
liczba1 = int(input("Podaj pierwszą liczbę "))
liczba2 = int(input("Podaj drugą liczbę "))
mnozenie = liczba1 * liczba2
dzielenie = liczba1 / liczba2
dodawanie = liczba1 + liczba2
odejmowanie = liczba1 - liczba2
potegowanie = liczba1 ** liczba2
print("Wybierz numer działania: ")
print("1. mnozenie")
print("2. dzielenie")
print("3. odejmowanie")
print("4. dodawanie")
odp = (input())

if int(odp) == 1:
	print("Wynik mnożenia to:", mnozenie)
elif int(odp) == 2:
	if liczba1 == 0 or liczba2 == 0:
		print("nie dizelimy przez 0")
	else:
		print("Wynik dzielenia to", dzielenie)
elif int(odp) ==3:
  print("Wynik odejmowania to", odejmowanie)
elif int(odp) ==4:
  print("Wynik dodawania to", dodawanie)
else:
	print("nie ma takiego numeru działania")