from listStack import ListStack

st1 = ListStack()
print(st1.top())
st1.push(100)
st1.push(200)
print("Top is", st1.top())
st1.push('Monday')
st1.printStack()
print("isEmpty?", st1.isEmpty())