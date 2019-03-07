def sumModFunc(count : float, fArray : list, sArray : list):
    data = []
    i = 0
    for f in fArray:
        data.append(f + sArray[i])
        i+=1
    return data

def MinOfTwo(count : float, fArr : list, sArr : list):    
    return ([f if f<f1 else f1 for f,f1 in zip(fArr, sArr)])

def MinOfThree(count : float, fArr,sArr,tArr : list):    
    return ([f if f<f1 and f<f2 else f1 if f1<f2 and f1<f else f2 if f2<f and f2<f1 else 0 for f,f1,f2 in zip(fArr, sArr,tArr)])

def MinAndMax(data : list):
    return max(data),min(data)

def CreateListOfThreeArray(data : list):
    fArr = []
    sArr = []
    tArr = []
    for f in range(0, len(data), 3):
        fArr.append(data[f])

    for f in range(1, len(data), 3):
        sArr.append(data[f])
        
    for f in range(2, len(data), 3):
        tArr.append(data[f])
        
    return    fArr,sArr,tArr
        
        

l0 = [-433462, 978021, -4816849, -6169927, -1755212, -7016768, 489843, 5068167, 6855515, -41334, 8642551, -1036407, 6101802, -4247098, -7991845, 5334270, -7603652, 5634029, 3032656, -1264566, 8743826, 7574864, -9675855, -7031222]
l1 = [-1177353, -6081759, 9895354, 3637405, 4204102, -1042684, 2346486, 2556231, 141464, 3839614, -6593847, 4384174, 9567324, -6602602, 1642186, 4625418, -4884739, -9816571, 7038944, -3002390, -4359839, 4603753, 705556, 6458457]
l2 = [321041, -2861790, -348901, 6255252, 3326116, -2937922, 3237681, 7398627, 5702778, 8392, 8831038, -7250720, -7355366, 6282038, 486141, 9443456, 1789943, -5653825, 4487638, -1672747, 1733405, -3882421, -4315096, -917698]

a0 = [
63064,31585,-10755,11440,-38291,-44652,-40655,-65686,-2545,-54034,67951,-29504,-22328,-52553,-33436,-27237,26979,3130,73302,-70332,-14987,-41482,-33504,-20018,3300,42109,20167,63967,-31880,-1066,58030,-48815,-49480,-32725,42625,-7772,
2623,-78030,6541,-79921,-52064,-5508,-29426,5607,21938,17138,58369,-31082,-59732,51672,-21414,5281,-69810,25081,65263,13490,-12809,5431,-2543,35311,-75635,-24512,66496,-45116,22762,29121,27112,-54615,31090,-46347,-54536,59025,28145,
-3962,-15367,-29916,-66824,-36998,19001,-46557,-65326,77587,38724,-55136,22669,23987,38353,-70140,-50582,-44190,45171,-46217,11297,31667,-11333,-45940,-19211,-64221,-20555,-68120,-30568,4908,70905,77576,-79054,-24462,-32339,-65879,
18540,66661,-32436,33213,64249,-73712,58076,6918,30275,16430,16777,59693,52239,-18051,-66523,-16463,-66383,2144,17597,-5595,17923,77041,6285,67354,1949,-2810,64931,2895,52728,-47408,17015,-8732,-60746,64579,-55518,-76497,70867,-77442,
10420,21143,18988,-52802,836,-8773,9147,14313,54764,22763,-63543,-7638,-62831,34379,-10597,23453,21734,71352,-59356,6666,-5753,73371,39258,-68737,-15360,58512,75841,9121,62015,66708,11679,-7564,7852,-49333,19634,-71312,21894,-51219,
23001,-3341,51543,39457,69020,68712,-6163,-21577,12166,-64428,-30224,32809,22237,44022,26181,-18504,55284,-69178,-39992,51126,19942,-57977,37835,-48379,14459,-34313,-17712,-45907,-25625,-75818,-17127,77375,840,-45583,36833,-10139,
-56871,-49329,48284,35294,-33758,-61940,-11896,68479,62082,-65714,-30024,37367,-54893,9983,8493,45048,32006,-33672,76669,-33535,12015,-21042,558,66389,-16861,63430,63765,63979,-62153,20598,-26159,-39024,51268,-57875,76270,-62489,
-39816,-15626,-74009,-57733,-1340,-24034,59633,23766,65949,-11873,-11185,17956,34455,-14515,64421,-33530,44442,-15021,-47140,-52418,-31591,-63375,-68438,-13744,37222,-14598,27231,8491,7526,23501,26002,47710,-72124,31992,69976,6535,
-72041,49610,-49698,73907,-42263,19117,11863,72191]



#print(sumModFunc(13, l3, l4))
#print(MinOfTwo(21, l5, l6))
#print(MinOfThree(12, l0, l1, l2))
#print(CreateListOfThreeArray(a0))
#print (MinAndMax(a0))


# Time converter
#Output in 'hh:mm a.m' format
#if < 10 - without 0 before it
#input format "hh:mm"
def TimeConverter(time):
    newtime = str(int(time[:2])- 12) + time[2:] +' p.m.' if int(time[:2]) > 12 else time +' p.m.' if int(time[:2]) == 12 else '12' + time[2:] +' a.m.' if int(time[:2]) == 0 else time[1:2]+ time[2:] +' a.m.'
    return newtime



#Most Frequency symbol
#In: List, Out: List

#sorted key(on count)
def sort_Count(item):
    return item[0]

#create list of value    
def Iterable(data):
    tempList = list()
    howMuch = list()
    i = 0
    while i < len(data):  #add to dict and show how much        
        tempList.append(data.count(data[i]))
        tempList.append(data[i])     
        howMuch.append(tempList[:])
        tempList.clear()
        
        i +=1
    
    howMuch =(sorted(howMuch,key = sort_Count, reverse = True))[:]
    finalList = list()
    
    for b in howMuch: 
        i = 0
        while  i < b[0]:   #add element to new list in an her amount
            finalList.append(b[1])
            i+=1
        
        
        if howMuch.count(b) > 1:  #delete nedless value from list
            j = b[0]            
            while j > 1:
                howMuch.remove(b)
                j-=1    
    return(howMuch,'\n', finalList)       


#Multiplication table
def MultTable():
    for i in range(1,10):
        for j in range(1,10):
            print(i*j, end='\t')
        print ("\n")
    
            
#Long repeat(search longest substring of the same letter
def LongRepeat(strData):
    i = j = 0
    tempStr = ''
    tempCount = [0]
    while i < len(strData):
        if not strData[i] == tempStr:
            tempStr = strData[i]
            tempCount.append(1)
            j+=1
        else:
            tempCount[j] +=1

        i+=1
    
    return(max(tempCount), tempCount)       

#Flatten list            
#Input data: A nested list with integers.
#Output data: The one-dimensional list with integers.            
def FlattenList(dataL):
    flatStr = str(str(dataL).split(']'))
    flatStr = str(flatStr.split('\'')) #create splitted str
    i = 0
    finalL = list()
    print(flatStr)
    while i < len(flatStr): #run on all symb       
        
        if flatStr[i].isdigit():    #we need digit
            tempS = ''
            while flatStr[i].isdigit(): #go foreward and search end sumbol
                tempS += flatStr[i]
                i+=1
            finalL.append(int(tempS))
            
        elif flatStr[i] == '-': #and negative number            
            if flatStr[i+1].isdigit():
                tempS = flatStr[i]
                i+=1    #we have already took the number
            while flatStr[i].isdigit(): #go foreward and search end sumbol
                tempS += flatStr[i]
                i+=1
            finalL.append(int(tempS))
            
        i+=1
    
    return(finalL)

#All the Same
def AllTheSame(data):
    try:
        return(True if len(data) == 0 or min(data) == max(data) else False)
    except:
        return False
    #return True if len(set(data))<=1 else False

#Sun angle
def SunAngle(time):
    nightMess = 'I don\'t see the sun!'

    try:
        if int(time[:2]) >= 18 and int(time[3:]) >= 1: #we don't see sun after 18:00
            return nightMess
        elif int(time[3:]) > 59:    #and minute can't be more 59
            return nightMess
        elif int(time[:2]) < 6: #don't see sun before 6:00
            return nightMess
        else:               #calculate angle
            timeM = ((int(time[:2])-6)*60 + int(time[3:]))/4 
            return '{:.0f}'.format(timeM)
    except:
        return nightTime
            


#Bird language
def BirdTranslater(data):
    vowels = "aeiouy"
    try:
        data = data.lower()
        i = 0
        while i < len(data)-1: #can't be ending symbol
            if data[i] == ' ':
                i+=1
                
          
            elif data[i].isalpha() and not data[i] in vowels:
              
                data = data[:i+1]+data[i+2:]
                i+=1
                print(data[i], i, '\n')
            else:
                 data = data[:i]+data[i+2:]
                 i+=1
            
            print(data)
            
        return(data)
    except:
        return(data)
     

       
def main():
    #print(MultTable())    
    #print(TimeConverter('12:30'))
    #print(Iterable(['alex','alex', 'bob', 'bob', 'carl', 'carl', 'bob']))
    #print(LongRepeat('ddvvrwwwrggg'))
    #print(FlattenList([100,99,98,97,-96,95,94,93,92,91,90,89,88,87,86,]))
    #print(AllTheSame([]))
    #print(SunAngle('18:01'))
    print(BirdTranslater('hoooowe yyyooouuu duoooiiine'))
    print(BirdTranslater('aaa bo cy da eee fe'))


main()    
    




