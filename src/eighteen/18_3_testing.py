class Main {
    n = int(input())
    count3,count5 = 1,1
    for i in range(1,n+1):
      if count3 == 3 and count5 == 5:
          print("FizzBuzz")
          count3,count5 = 0,0
      elif count3 == 3:
        print("Fizz")
        count3 = 0
      elif count5 == 5:
        print("Buzz")
        count5= 0
      else:
        print(i)
      count3 += 1
      count5 += 1
}