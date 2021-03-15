#################################################Program do rejestracji użytkownika na platformie x##################################################################

import time
import sys

print("Witaj użytkowniku na naszej platformie. Aby się zarejestrować, postępuj zgodnie z następnymi krokami...")

time.sleep(1)

login = input("Wpisz swój login: ")
print("login: ", login)


haslo = input("Brawo! Wpisz teraz swoje hasło: ")
haslo_accept = input("Potwierdź swoje hasło :")

while haslo != haslo_accept:
    print("Hasła się nie zgadzają, spróbuj jeszcze raz!")
    haslo = input("Brawo! Wpisz teraz swoje hasło: ")
    haslo_accept = input("Potwierdź swoje hasło :")

if haslo == haslo_accept:
    pass
    
print("login: ", login)
print("haslo: ", haslo)


pesel = input("Wpisz swój numer pesel: ")

print("login: ", login)
print("haslo: ", haslo)
print("pesel: ", pesel)

wiek = input("Wpisz swój wiek: ")

print("Witamy w naszej aplikacji! Oto twoje dane rejestracyjne. Zostały one przesłane również na maila. Dziękujemy za zaufanie.")
print("login: ", login)
print("haslo: ", haslo)
print("pesel: ", pesel)
print("wiek: ", wiek)
    





