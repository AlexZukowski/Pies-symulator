class Pies:
	def __init__(self,imię = "Pies", wiek = 0):
		self.imię = str(imię)
		self.wiek = float(wiek)
		self.szczęście = 10
	
	def Nakarm(self,jedzenie):
		self.wiek += 0.1
		if (len(str(jedzenie)) % 2) == 0:
			self.szczęście += 10
			print("Woof, woof! (jestem szczęśliwy, bardzo dobre jedzenie)")
		else:
			self.szczęście -= 5
			print("Woof, woof! (jestem nieszczęśliwy, nie lubię tego jedzenia)")

	def Aport(self,odległość):
		self.wiek += 0.1
		if int(odległość) <= 5:
			self.szczęście += 2
			print("Wof, Woof. (Czemu tka blisko? Żadne wyzwanie))")
		elif int(odległość) <= 30:
			self.szczęście += 10
			print("Woof, woof! (Kocham Cię!)")
		elif int(odległość) > 30:
			self.szczęście -= 1
			print("Woof, woof! (Ojej, trochę za daleko, nie mogę znaleźć!)")

	def Pogłaszcz(self):
		self.wiek += 0.1
		self.szczęście += 5
		print("Wooooooof, wooooof (Ale fajnie!)")

	def Szczęście(self):
		self.wiek += 0.1
		return self.szczęście

	def Wiek(self):
		self.wiek += 0.1
		return self.wiek

	def Imię(self):
		self.wiek += 0.1
		return self.imię

	def Zmień_imię(self, imię):
		self.wiek += 0.1
		self.imię = imię

	def Zmień_wiek(self, wiek):
		self.wiek = wiek

	def Szczekaj(self):
		self.wiek += 0.1
		print("Woof, woof!")
		
global psy, numer, numery, do
psy = []
numer = 0
numery = {}
do = True

while do == True:

	command = input("Pies symulator > ")

	if command.lower().strip() == "stwórz":
		imiępsa = input("Podaj imię nowego psa > ")
		wiekpsa = input("Podaj wiek nowego psa > ")
		psy.append(Pies(wiek = wiekpsa.lower().strip(), imię = imiępsa.lower().strip()))
		numery[imiępsa.lower().strip()] = numer
		numer += 1
	elif command.lower().strip() == "szczekaj":
		imiępsa = input("Który pies ma zaszczekać? > ")
		psy[numery[imiępsa.lower().strip()]].Szczekaj()
	elif command.lower().strip() == "aport":
		imiępsa = input("Któremu psu chcesz rzucić patyk? > ")
		odległośćpsa = input("Na jaką odległość chcesz rzucić patyk? > ")
		psy[numery[imiępsa.lower().strip()]].Aport(odległośćpsa)
	elif command.lower().strip() == "nakarm":
		imiępsa = input("Którego psa chcesz nakarmić? > ")
		jedzeniepsa = input("Czym chcesz go nakarmić? > ")
		psy[numery[imiępsa.lower().strip()]].Nakarm(jedzeniepsa)
	elif command.lower().strip() == "pogłaszcz":
		imiępsa = input("Którego psa chcesz pogłaskać? > ")
		psy[numery[imiępsa]].Pogłaszcz()
	elif command.lower().strip() == "wiek":
		imiępsa = input("Którego psa wiek chcesz poznać? > ")
		print(imiępsa,"ma",int(psy[numery[imiępsa.lower().strip()]].Wiek()),"lat")
	elif command.lower().strip() == "szczęście":
		imiępsa = input("Którego psa szczęście chcesz poznać? > ")
		print(imiępsa,"ma",psy[numery[imiępsa.lower().strip()]].Szczęście(),"szczęścia")
	elif command.lower().strip() == "zmień imię":
		imiępsa = input("Którego psa imię chcesz zmienić? > ")
		noweimiępsa = input("Na jakie imię chcesz je zmienić? > ")
		psy[numery[imiępsa.lower().strip()]].Zmień_imię(noweimiępsa)
		numery[noweimiępsa] = numery.pop(imiępsa)
	elif command.lower().strip() == "psy":
		print("Twoje psy to: ")
		for i in range(len(psy)):
			print(psy[i].Imię())
	elif command.lower().strip() == "pomoc":
		print("Lista komend:")
		print('"stwórz" Tworzysz nowego psa.')
		print('"aport" Rzucasz patyk istniejącemu psu. Jeśli odległość rzutu jest za mała,')
		print('pies uzna grę za zbyt łatwą, jeśli odległość jest zbyt duża, nie będzie mógł on')
		print('znaleźć patyka i zacznie się denerwować. Sęk w znalezieniu odpowiedniej odległości, by uszczęśliwić psa')
		print('"nakarm" Karmisz wybranego psa, dowolnym jedzeniem. Niektóre potrawy psy')
		print('odrzucają, a inne lubią. Podpowiedź: Psy to matematyczne nerdy.')
		print('"pogłaszcz" Głaszczesz psa.')
		print('"szczekaj" Wybrany pies zaszczeka.')
		print('"wiek" Pozwala Ci sprawdzić wiek, danego psa. Pies starzeje się, podczas wykonywania')
		print('różnych czynności.')
		print('"szczęście" Pozwala Ci sprawdzic poziom szczęścia danego psa. Szczęście można')
		print('zdobywać poprzez granie w gry, dawaniu psu przekąsek, czy głaskanie go.')
		print('Szczęście można też tracić.')
		print('"zmień imię" Pozwala Ci zmienić imię wybranego psa.')
		print('"psy" Wyświetla listę twoich psów.')
		print('"pomoc" Chyba już wiesz, jak to działa?')
		print('"koniec" Pozwala Ci zakończć grę w Pies symulator.')
	elif command.lower().strip() == "koniec":
		napewno = input("Na pewno chcesz zakończyć (y/n)? > ")
		if napewno.lower().strip() == "y":
			do = False
	else:
		print('Oj! Taka komenda nie istnieje. By dowiedzieć się o wszystkich komendach, wpisz "pomoc".')


