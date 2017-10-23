rainfile = open("rainfall.text", "r")
outfile = open("rainfallfmt.txt","w")
for aline in rainfile:
    values = aline.split()
    print(aline)
    city = values(0)
    inches = float(values[1])
    outfile.write("%+25s $5.lf \n"%(city,inches))

rainfile.close()
outfile.close()
    
