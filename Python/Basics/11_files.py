f = open('sample.txt', 'r')  # r mode in which file open and bydefault mode is r
data = f.read(5);  # only read first 5 charater
# readline se pheli line and fir se readline likha to agli line read
#diffretn modes go to notes or refernce
print(data)
f.close()

# differtn modes
# w = write but first it will delete all data then write from start
# x  = create new file and open in write mode
# a = open file and append to end of file
# b = binary mode
# t = text mode  // by deafult text hi open hai eg r ya rt same hi hai , t implicity call hota hai
# + = open file disk for updating perfform two operation


# f.read  reads all file
# f.readline() reads only single line

# if we read forst fulll file so pointer end par puch gya hai to readline se empty print hoga as pointer already end par hai
