
def greet (fx):
    def mfx():
        print("Good Morning")
        fx()
    return mfx

@greet
def hello ():
    print("hello world ")
    
hello()