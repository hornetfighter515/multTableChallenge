
def main():
    for i in range(0,11):
        for j in range(0,11):
            operand_i = i
            if(i==0):
                operand_i = 1
            
            operand_j = j
            if(j==0):
                operand_j = 1

            result = operand_i*operand_j
            if(i==0 and j==0):
                result = "X"
            print(str( result)+ '\t', end='')
        print()

if __name__ == "__main__":
    main()