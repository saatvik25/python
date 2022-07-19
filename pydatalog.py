


from pyDatalog import pyDatalog
pyDatalog.create_terms('bear,elephant,cat,big,small,black, brown,dark,size,color,X,Y')
+size("bear","big")
+size("elephant","big")
+size("cat","small")
+color("bear","brown")
+color("cat","black")
+color("elephant","gray")
dark(x)<= color(X,"black")
dark(x)<= color(X,"brown")
light(x)<= color(X,"gray")
print(dark(X) & size(x,"small"))
