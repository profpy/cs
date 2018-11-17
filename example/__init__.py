import check50 # import the check50 module
2
3 @check50.check() # tag the function below as check50 check
4 def exists(): # the name of the check
5 """description""" # this is what you will see when running check50
6 check50.exists("hello.py") # the actual check
7
8 @check50.check(exists) # only run this check if the exists check has passed
9 def prints_hello():
10 """prints "hello, world\\n" """
11 check50.run("python3 hello.py").stdout("[Hh]ello, world!?\n", regex=True).exit(0)
