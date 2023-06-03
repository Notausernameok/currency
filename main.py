C=CurrencyConverter()

try:

   def Currency():
      money = float(input("how much do you have?: "))
      yours = input("Your currency:").upper()
      them = input("to change:").upper()
      a=(float(C.convert(money,yours,them)))
      return a
   print(Currency())
except ValueError:
    print("Please enter a number")

