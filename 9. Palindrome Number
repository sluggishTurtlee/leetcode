class Solution:
    def isPalindrome(self, x: int) -> bool:
        lenth=len(str(x))
        tf=True
        palindrome=[]
        if x<0:
            tf=False
        else:

            if lenth==1:
                tf=True
            else:
                if (lenth%2)==0: #even 
                    for i in range(lenth): #0,1,2,3
                        if i==0:
                            k=x%10
                        else:
                            k=x//(10**i)
                            k=k%10

                        palindrome.append(k)
            
                    for j in range(lenth//2): #0,1
                        if palindrome[j]==palindrome[lenth-j-1]:
                            tf=True
                            continue
                        else: 
                            tf=False
                            break
                    


                else:   #odd
                    for i in range(lenth):
                        if i==0:
                            k=x%10
                        else:
                            k=x//(10**i)
                            k=k%10

                        palindrome.append(k)

                    for j in range(lenth//2): #j=0,1,2,3
                        if palindrome[j]==palindrome[lenth-j-1]:
                            tf=True
                            continue
                        else: 
                            tf=False
                            break        
        return tf
