p = [0,1,1]#empty
p[0] = p[0] + p[1]
p[1] = p[0] + p[2]
p[2] = p[0] + p[1]
print(p)#should be [1,2,3]