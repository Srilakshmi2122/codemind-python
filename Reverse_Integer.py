# We have to take the number being -ve into consideration
n = int(input())
# Storing -n if value is negative
# or storing n in a temp variable
temp = -n if n < 0 else n
# Reversing the temp
reverse = 0
while temp:
 reverse = reverse * 10 + temp % 10
 temp = temp // 10
# Checking whether to print -reverse or +reverse
# using n value again
print(-reverse if n < 0 else reverse)