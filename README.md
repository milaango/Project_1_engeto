# Text Analyzer
První projekt v rámci Python Akademie od ENGETO.
## O projektu
Jedná se o jednoduchou konzolovou aplikaci, která umožňuje registrovanému uživateli přihlásit se a vybrat jeden ze tří předpřipravených textů, který je následně zanalyzován.
## Požadavky na spuštění
Projekt vyžaduje pouze Python 3.x. Není třeba instalovat žádné knihovny; stačí jej spustit v Terminálu či IDE dle vlastního výběru.
## Použití
Po spuštění projekt uživatele vyzve k zadaní uživatelského jména a hesla, čímž ověřuje, zda je uživatel uveden ve slovníku `registered_users`, který obsahuje přihlašovací údaje.
```
registered_users = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"
}
```
V případě úspěšného přihlášení je následně uživatel vyzván k výběru textu k analýze (1-3). 

V případě nesprávných přihlašovacích údajů či neplatné volby textu je program ukončen.

## Výstup projektu

Výstupem projektu je analýza vybraného textu, konkrétně:
- celkový počet slov
- počet slov ve formátu `Titlecase`, `UPPERCASE` a `lowercase`,
- počet čísel (jako `str`) a jejich celkový součet
- grafické znázornění četností jednotlivých slov o daném počtu písmen

## Ukázka použití
```
username: ann
password: pass123
----------------------------------------
Welcome to the app, ann
We have 3 texts to be analyzed.
----------------------------------------
Enter a number btw. 1 and 3 to select: 3
There are 74 words in the selected text.
There are 4 titlecase words.
There are 0 uppercase words.
There are 68 lowercase words.
There are 2 numeric strings.
The sum of all the numbers 8298.
----------------------------------------
LEN|  OCCURENCES  |NR.
----------------------------------------
 1|*                   |1
 2|***********         |11
 3|***************     |15
 4|*********           |9
 5|**********          |10
 6|*****               |5
 7|***********         |11
 8|******              |6
 9|***                 |3
10|***                 |3
```