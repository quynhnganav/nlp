filepath = 'data.csv'
data2=open("data.csv",'w',encoding = 'utf-8')
with open(filepath,encoding = 'utf-8') as fp:
   for line in fp:
       line1 = line.split(",")[0]
       line2 = line.split(",")[1].strip('\n')
       data2.writelines('"{0}","{1}"\n'.format(line1,line2))
      