def bagMaker(size):
   "Depending input, makes an array with a patron AB repeating size times"

   arr = []  # Creates a List
   count = ((size*2)*(-1))+1 #Defines a count from size-1 negative to size

   while count <= 0:  #Adds 0 as empty spaces and possible moves
       arr.append([0,count])
       count +=1

   while count < size*2: #Adds A-B patron
       arr.append(["B",count])
       count += 1

       arr.append(["A",count])
       count += 1

   return arr; #Returns finished List


inputValue = int(input("Puts a number between 3 and 100 : "))
bagArr=bagMaker(inputValue)
print(bagArr)
