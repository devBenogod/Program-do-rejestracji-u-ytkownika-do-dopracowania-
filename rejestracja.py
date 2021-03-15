import time

max_pesel = len("11111111111")

print("Witaj użytkowniku na naszej platformie. Aby się zarejestrować, postępuj zgodnie z następnymi krokami...")

time.sleep(1)

login = input("Wpisz swój login: ")
print("login: ", login)

password = input("Brawo! Wpisz teraz swoje hasło: ")
password_accept = input("Potwierdź swoje hasło :")

while password != password_accept:
    print("Hasła się nie zgadzają, spróbuj jeszcze raz!")
    password = input("Wpisz teraz swoje hasło: ")
    password_accept = input("Potwierdź swoje hasło :")
if password == password_accept:
    pass
    


print("login: ", login)
print("haslo: ", password)



pesel = input("Wpisz swój numer pesel: ")

while len(pesel) != max_pesel:
    print("Pesel musi posiadać 11cyfr, spróbuj jeszcze raz.")
    pesel = input("Wpisz swój numer pesel: ")
if len(pesel) == max_pesel:
    pass


print("login: ", login)
print("haslo: ", password)
print("pesel: ", pesel)

age = input("Wpisz swój wiek: ")

print("Witamy w naszej aplikacji! Oto twoje dane rejestracyjne. Zostały one przesłane również na maila. Dziękujemy za zaufanie.")
print("login: ", login)
print("haslo: ", password)
print("pesel: ", pesel)
print("wiek: ", age)
    
