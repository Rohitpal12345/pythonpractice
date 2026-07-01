try:
    a=10
    b="2"
    c=a/b
    print(c)
except Exception as e:
    print("Error",e)
    pass
finally:
    print("finally run always")

    
