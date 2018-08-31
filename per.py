#PERMUTATIONA AND COMBNATIONS
from colorama import *
import math
pre = int(input("Please enter the first part:"))
intialNo = int(input("Please enter the second part:"))
main = "P"
# print(Fore.RED + "The structure of the input is", pre,main,intialNo)
def permutation():
  """
  this is the function that now calculates the numbers of the permutations
  permutations = Pre! / (pre - in6itialNo)!
  math module to be used is  math.factorial
  """
  factor1 = math.factorial(pre)
  diff =  pre - intialNo
  factor2  = math.factorial(diff)
  Ans = factor1 / factor2
  Answer = Fore.GREEN +"The permutation  of {} and {} are {}".format(pre,intialNo,Ans)
  print(Answer)

def  combinations():
  """
  This is a program that gets the combinations of  two numbers in the form of  6C2
  it uses the math module of factorial
  combinations = pre! / (pre -intialNo)! * intialNo!
  """
  factor3 = math.factorial(pre)
  diff2  = pre -intialNo
  factor4 = math.factorial(diff2)
  factor5 = math.factorial(intialNo)
  Ans2 = factor3 / (factor4 * factor5)
  Answer2 =Fore.MAGENTA + "The combination of {} and {} is {}".format(pre,intialNo,Ans2)
  print(Answer2)

def permutationOfWords():
  """
  This is a function that get the number of permutations in a  string of the entered text
  example Stringinput = "Oloo"
  permutations = numbers of words in oloo / numbers of times to be taken
  if input  = john
  len (john)! /numberOfTimesTaken
  """
  StringInput = str(input("Please enter a string:"))
  prewords = len(StringInput)
  numberOfTimesTaken = int(input("Please enter the number of times the word is to be taken:"))
  Answ3  = math.factorial(prewords) / math.factorial(numberOfTimesTaken)
  Answer3 = Fore.YELLOW + "The permutation in the word {} taken {} is {}".format(StringInput,numberOfTimesTaken,Answ3)
  print(Answer3)

print(Fore.BLUE + "What do you want to do:")
print(Fore.YELLOW + "1.Get the permutations in this form  3P2:")
print(Fore.YELLOW + "2.Get the combination in this form  3C2:")
print(Fore.YELLOW + "3.Get the permutations  in the StringInput:")
Operationchoice = int(input(Fore.RED + "Please enter the operation you want to accomplish:"))
if Operationchoice == 1:
  permutation()
elif Operationchoice == 2:
  combinations()
elif Operationchoice == 3:
  permutationOfWords()
