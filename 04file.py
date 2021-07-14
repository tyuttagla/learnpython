# Learning about file read and write

# # countline, count cgarecter
# infile=open("d:/lernpython/learnpython/data.txt","r")
# line_count=0
# char_count=0

# for line in infile:
#     line_count+=1
#     char_count+=len(line)
#     print(line)

# infile.close()

# # avg score
# infile=open("d:/lernpython/learnpython/data1.txt","r")
# sum_scores=0
# num_student=0

# for line in infile:
#     score= float(line.strip()[10:])
#     sum_scores+=score
#     num_student+=1
# infile.close()
# avg=sum_scores/num_student
# print("Average Score =",avg)

# #minimum score
# infile=open("d:/lernpython/learnpython/data1.txt","r")
# min_score=99999


# for line in infile:
#     score=float(line.strip()[10:])
#     if score<min_score:
#         min_score=score
# infile.close()
# print("Min score=",score)

# #max and ID
# infile=open("d:/lernpython/learnpython/data1.txt","r")
# max_score=0
# max_id=""
# for line in infile:
#     score=float(line.strip()[10:])  # strip ตัดช่องว่าง [:-1]ตัด \n
#     if score>max_score:
#         max_score=score
#         max_id=line.strip()[:10]
# infile.close()
# print("Max Score= ",max_score,"ID=",max_id)

# # write and close file
# outfile= open("d:\lernpython\learnpython\doc.txt","w")

# outfile.write("12345\n")
# outfile.write("teerayuth Yuttagla\n")

# outfile.close()

# # copy file
# src= input("Enter Source file name: ")
# dest=input("Enter destination file name : ")

# infile=open(src,"r")
# outfile=open(dest,"w")

# for line in infile:
#     outfile.write(line)

# infile.close()
# outfile.close()


#rot-13 in for File
filename= input("Enter File name:")
infile=open(filename,"r")
outfile=open(filename+"rot-13","w")

for line in infile:
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower=upper.lower()
    rot13=""
    for k in line:
       
       if k in upper:
              rot13+=upper[(upper.find(k)+13)%26]
       elif k in lower:
              rot13+=lower[(lower.find(k)+13)%26]
       else:
              rot13+=k
    outfile.write(rot13)

infile.close()
outfile.close()



