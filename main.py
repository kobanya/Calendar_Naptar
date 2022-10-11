# Python program , naptár nyomtatására
import calendar

# Enter in format - 2018, 1997, 2003 etc.
ev = int(input("Enter Year/ Add meg az évszámot: "))

# Enter in format / ilyen formátumban add meg- 01, 06, 12 etc.
honap = int(input("Enter Month/ add meg a hónap számát: "))

# printing Calendar/ a Maptár nyomtatása
print("   ")
print(calendar.month(ev, honap))