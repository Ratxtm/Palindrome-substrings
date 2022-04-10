def is_kinda_interesting(s, j, k):
      
  count = 0
  
  while j >= 0 and k < len(s):
    if s[j] != s[k]:
          
      break
      
    else:
          print(s[j: k+1])
    count += 1

    j -= 1
    k += 1
  
  return count
  


def is_interesting(str):
  count = 0
  s = input("Enter a word to check palindromic substrings: ").casefold()
  if s == "":
        print("None")
  elif s != s[::-1]:
    print("False")    
  else:      
        
     for i in range(0, len(s)):
       count += is_kinda_interesting(s, i - len(s)//2, i + len(s)//2)
       count += is_kinda_interesting(s, i-len(s)//2, i+1)

  
  return ""

print(is_interesting(str))  



  






    