def number_lines(filename):
    with open(filename,'r') as f:
        i=1
        for line in f:
            print(f"{i}: {line.strip()}")
            i+=1
number_lines('w4q1.py')