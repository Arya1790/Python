def new(name,place='goa'):
    print("Hello, my name is {} and place is {}".format(name,place))

new("Jane")

def sample(*args,**kargs):
    print(args)
    print(kargs)

sample(1,4,12,10,age=33)