import functools
login = True


def logindecorator(func):
    functools.wraps(func)
    def upper_wrapper():
      if(login == True):
          func()
      else:
          print("Please login first")
    return upper_wrapper

@logindecorator
def myfunc():
    print("Profile page")
myfunc()