import re
print("PASSWORD STRENGTH CHECKER SIMPLE PY CLI PROGRAM")
print("BASED ON SCORE OUT OF 10")
print("--------------------")
def passw_check(passw):
    errors = []
    score = 10
    if len(passw) < 8:
        errors.append("This Password doesn't contains required minimum characters (-2)")
        score -= 2
    if not re.search("[a-z]",passw):
        errors.append("This Password contains no small letters (-2)")
        score -= 2
    if not re.search("[A-Z]",passw):
        errors.append("This Password contains no CAPTIAL LETTERS (-2)")
        score -= 2
    if not re.search("[0-9]",passw):
        errors.append("This Password contains no digits (-2)")
        score -= 2
    if not re.search("[^A-Z0-9a-z]",passw):
        errors.append("This Password contains no special characters (-2)")
        score -= 2

    if len(errors) == 0:
        print("This Password meets required specs. \n CONGRATS")
        print("The Test score out of 10 is: ",score)
    else:
        print("This Password contains weakness.")
        print("The Test score out of 10 is: ",score)
        print("Errors are:")
        print("\n".join(errors))

while True:
  passw = input("Enter the password: ")
  passw_check(passw)
  print("----------")
  checkr = input("Do u want to check another password: (y/yes)|(n/no) :")
  if checkr in ("n","no","exit","N","NO","No"):
      print("Simple Program Exiting")
      print("changed to the main file")
      break
  else:
      continue
