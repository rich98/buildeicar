p1 = "X5O!P%%@"
p2 = "AP[4\PZX54(P"
p4 = ")7CC)7}$EICAR"
p5 = "-STANDARD"
p6 = "-ANTIVIRUS-"
p7 = "TEST-"
p8 = "FILE!$H+"
p9 = "H*"

output_text = p1 + p2 + "^^" + p4 + p5 + p6 + p7 + p8 + p9

with open("buildeicar.txt", "w") as file:
    file.write(output_text)
