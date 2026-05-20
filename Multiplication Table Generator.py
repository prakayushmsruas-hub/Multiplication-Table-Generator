#-------------------------------------------------------------------------------
def Multiplication_Table(num,multiplier=1):
    print(f"Multiplication table of {num} till {m} multiplier\n")
    for multiplier in range(1,m+1):
        print(f"Multiplication of {num}*{multiplier}={num*multiplier}")
#--------------------------------------------------------------------------------    
while True:

    print("\n======== Multiplication Table ========\n")
    print("1.Table generator\n2.Exit\n")
    choice=int(input("Enter (1-2):"))
 
    if choice==1:
        n=int(input("enter a number you want table for:"))
        m=int(input("Enter till where/which number u want to multiply:"))
        Multiplication_Table(n,multiplier=1)
    elif choice==2:
        print("Exiting Program...")
        print("Exit Successful!")
        break
    else:
        print("Invalid Choice!")        
       
#----------------------------------------------------------------------------------   
