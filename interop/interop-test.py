# export CLASSPATH=/vagrant/interop/target/:/vagrant/interop/lib/*
from jnius import autoclass

Fib = autoclass('Fib')

print Fib.fib(1)
print Fib.fib(2)
print Fib.fib(3)
print Fib.fib(4)
print Fib.fib(5)
