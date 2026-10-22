def tenth_line(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        
    if len(lines) >= 10:
        print(lines[9], end="")
        
tenth_line("file.txt")