# one line python fizzbuzz
# Author: @CiTRuS93
print("".join(map((lambda x: ("fizzbuzz\n") if x%3==0 and x%5==0 else "fizz\n" if x%3==0 else "buzz\n" if x%5 ==0 else str(x)+"\n"),[x for x in range(101)])))