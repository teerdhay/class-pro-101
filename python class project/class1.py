def project():
    filename=input("enter file name")
    count=0
    f=open(filename,'r')
    for i in f:
        words=i.split()
        count=count+len(words)
    print("no.of words")
    print(count)

project()
#inorder to declare a function :def ,name of the function, ()bracketss