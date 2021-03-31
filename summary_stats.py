import statistics

#error handling for designating precision
try:
    precision=int(input("Please enter the desired precision:")) #ask for integer precision value
except:
    print("Precision must an integer value.") #raise exception for non-integer precision values
    raise

val=input("Please enter a number. Type 'quit' to exit. \n") #ask for first value
running_data=[] #initiate running list of data
while val != 'quit': #look for exit word
    try: #error handling for entering data
        num = float(val) #test if data can convert to float, look for non-numeric entry
        running_data.append(num) #add to running list of data
        if len(running_data)==1: #check if this is the first entry. statistics package cannot calculate the variance of a single entry list
            print(num,0,num)
            val=input("Please enter a number. Type 'quit' to exit. \n") #get second value
        else:
            print(round(statistics.mean(running_data),precision),round(statistics.stdev(running_data),precision),round(statistics.median(running_data),3)) #print mean, standard deviation, and median
            val=input("Please enter a number. Type 'quit' to exit. \n") #get next value
    except:
        print("Non-numeric entry provided. Please try again.") #raise error for non-numeric entry
        raise



