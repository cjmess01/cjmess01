import InsightCrimeFunctions
import xlwt

#Add strings to searchTerms to include more search terms in search
searchTerms = ["Cocaine","Transatlantic"]

#Change this number to modify which page you want to start at. Minumum must be 1
pageToStartAt = 1

#Change this number to modify how many pages in you want to search. Must be greater than or equal to pageToStartAt
pagesToSearch = 3


#------------------------------------------------
#   12/10/21
#   Don't modify below this line for regular usage
#
#------------------------------------------------


workbook = xlwt.Workbook()
sheet = workbook.add_sheet("InsightCrimeLinks")



#Give title-confirmed construct to this, adds to sheet
def addConstrToExcel(startRow,sheet,constr,searchTerm,pageNum):
    
    currentRow = startRow

    style = xlwt.easyxf('font: bold 1')

    ConstrID = "Search Term: " + str(searchTerm) + ". Page Num: "+str(pageNum)


    sheet.write(currentRow,0,ConstrID,style)
    currentRow = currentRow + 1

    for x in range(0,len(constr)):
        sheet.write(currentRow,0,constr[x])
        currentRow = currentRow + 1


    workbook.save('Links.xls')
    return currentRow
#
def getArticleTitle(link):

    return 0

def keywordIsntSubstring(link,keyword):

    return 0


startRow = 0
currentRow = startRow
for x in range(0,len(searchTerms)):
    for y in range(pageToStartAt,pagesToSearch):
        #creates a URL in the following format
        #url = https://insightcrime.org/page/y/?s=searchTerms[x]"
        url = "https://insightcrime.org/page/"
        url = url +                       str(y)
        url = url +                           "/?s="
        url = url +                                searchTerms[x]
    
        constr = InsightCrimeFunctions.returnLinks(url)
        #print(constr)

        currentRow = addConstrToExcel(currentRow,sheet,constr,searchTerms[x],y)
        print("Added Construct to Sheet")
        
        

