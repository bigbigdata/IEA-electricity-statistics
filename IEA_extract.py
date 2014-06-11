import xlrd
import pandas 
import matplotlib.pyplot as plt
from pandas import DataFrame 

OrgIndex=[]    # index of organization 
CombustibuleYear=[]
NuclearYear=[]
HydroYear=[]
GWSOYear=[] #Geothermal + wind + solar + other 
CombustibuleMonth=[]
NuclearMonth=[]
HydroMonth=[]
GWSOMonth=[] #Geothermal + wind + solar + other 
yrcol=[]

yr = range(2007,2014)
month = range(1,13)
for i in yr:
    for j in month[-1:]:
        if j<10:
            date = str(i)+'0'+ str(j)
        else:
            date = str(i)+ str(j)
    filename =date+'.xls'
    wb = xlrd.open_workbook(filename)  
    SheetNames=wb.sheet_names()

    for i in SheetNames:
        if i[0:5]=='Table':
            sh = wb.sheet_by_name(i)  
            # Extract yearly data first 
            OrgIndex.append(sh.cell_value(3,0).encode('ascii','ignore'))
            yrcol.append(int(sh.cell_value(7,15)))
            CombustibuleYear.append(sh.cell_value(9,15))
            NuclearYear.append(sh.cell_value(10,15))
            HydroYear.append(sh.cell_value(11,15))
            GWSOYear.append(sh.cell_value(12,15))  

df = DataFrame([OrgIndex,yrcol,CombustibuleYear,NuclearYear,HydroYear,GWSOYear])
df = df.transpose()
df.columns=['Org','date','Comb','Nuclear','Hydro','GWSO']

#print US as an example
df1 = df[df.Org=="UNITED STATES"]
df2 = df1.GWSO
df2.index=df1.date.values

#plot
fig=plt.figure(); ax=fig.add_subplot(1,1,1)
df2.plot(kind='bar')
ax.set_xlabel('Year')
ax.set_ylabel('GSWO Energy (GWh)')
plt.legend(loc='upper center',bbox_to_anchor=(0.5,-0.05),fancybox=True,shadow=True,ncol=6)
plt.savefig('IEA_US_GSWO_Annual.tiff')
