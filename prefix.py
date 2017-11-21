def calculate (N):
    
    count = 0
    for i in range(len(N)-1):
        a = int("".join(N[:i+1]))
        if N[i+1] == "0":
            continue
        b = int("".join(N[i+1:]))
        a_b = a % b
        if a == a_b or b == a_b:
            count += 1
            continue
        b_a = b % a 
        if a == b_a or a == b_a:
            count += 1
    
    print count


N = raw_input()
out_ = calculate(N)
