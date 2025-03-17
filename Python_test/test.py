import re
string = input("input : ")
string = re.sub('RT'," ",string)
string = re.sub('@\S+'," ",string)
string = re.sub('#\S+'," ",string)
print(string)