def happy(n):
 temp=n
 sum=0
 while temp>0:
  digit=temp%10
  sum=digit**2+sum
  temp=temp//10
  return sum
num=int(input("Enter the number:"))
res=num
while res!=1 and res!=4:
 res=(happy(res))
if res==1:
  print("True")
elif res==4:
  print("False")
