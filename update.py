
import csv
import json

with open('/home/tobiuo0203/Book3.csv') as ff:
    reader = csv.reader(ff)
    l = [row for row in reader]
    
data1=l[-1]
data1.pop(0)
data1=[int(s) for s in data1]
data1=sum(data1)*300
data2=l[-2]
data2.pop(0)
data2=[int(s) for s in data2]
data2=sum(data2)*300
data3=l[-3]
data3.pop(0)
data3=[int(s) for s in data3]
data3=sum(data3)*300
data4=l[-4]
data4.pop(0)
data4=[int(s) for s in data4]
data4=sum(data4)*300
data5=l[-5]
data5.pop(0)
data5=[int(s) for s in data5]
data5=sum(data5)*300
data6=l[-6]
data6.pop(0)
data6=[int(s) for s in data6]
data6=sum(data6)*300
data7=l[-7]
data7.pop(0)
data7=[int(s) for s in data7]
data7=sum(data7)*300
data8=l[-8]
data8.pop(0)
data8=[int(s) for s in data8]
data8=sum(data8)*300
data9=l[-9]
data9.pop(0)
data9=[int(s) for s in data9]
data9=sum(data9)*300
data10=l[-10]
data10.pop(0)
data10=[int(s) for s in data10]
data10=sum(data10)*300
data11=l[-11]
data11.pop(0)
data11=[int(s) for s in data11]
data11=sum(data11)*300
data12=l[-12]
data12.pop(0)
data12=[int(s) for s in data12]
data12=sum(data12)*300
data13=l[-13]
data13.pop(0)
data13=[int(s) for s in data13]
data13=sum(data13)*300
data14=l[-14]
data14.pop(0)
data14=[int(s) for s in data14]
data14=sum(data14)*300
data15=l[-15]
data15.pop(0)
data15=[int(s) for s in data15]
data15=sum(data15)*300
data16=l[-16]
data16.pop(0)
data16=[int(s) for s in data16]
data16=sum(data16)*300
data17=l[-17]
data17.pop(0)
data17=[int(s) for s in data17]
data17=sum(data17)*300
data18=l[-18]
data18.pop(0)
data18=[int(s) for s in data18]
data18=sum(data18)*300
data19=l[-19]
data19.pop(0)
data19=[int(s) for s in data19]
data19=sum(data19)*300
data20=l[-20]
data20.pop(0)
data20=[int(s) for s in data20]
data20=sum(data20)*300
data21=l[-21]
data21.pop(0)
data21=[int(s) for s in data21]
data21=sum(data21)*300
data22=l[-22]
data22.pop(0)
data22=[int(s) for s in data22]
data22=sum(data22)*300
data23=l[-23]
data23.pop(0)
data23=[int(s) for s in data23]
data23=sum(data23)*300
data24=l[-24]
data24.pop(0)
data24=[int(s) for s in data24]
data24=sum(data24)*300


data=data1+data2+data3+data4+data5+data6+data7+data8+data9+data10+data11+data12+data13+data14+data15+data16+data17+data18+data19+data20+data21+data22+data23+data24

with open("/home/tobiuo0203/static/data.json", mode='ab+') as f:
    f.seek(-1, 2)
    f.truncate()
    f.write(','.encode())
    f.write(json.dumps(data).encode())
    f.write(']'.encode())




