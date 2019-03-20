class MyClass:
  variable = "blah"

  def function(self):
    print("This is a message inside the class.")

  # creates new object which is a new instance of MyClass
  myobjectx = MyClass()
  
  # accesses a variable defined within MyClass
  myobjectx.variable

  # will print the value of the respective variable in that class
  print(myobjectx.variable)