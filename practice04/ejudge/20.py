g = 0

def outer():
    n = 0 
    
    def inner():
        nonlocal n
        global g
        local_vars = {} 
        
        for scope, val in commands:
            val = int(val)
            if scope == "global":
                g += val
            elif scope == "nonlocal":
                n += val
            elif scope == "local":
                local_vars["x"] = local_vars.get("x", 0) + val

    inner()
    return n


N = int(input())
commands = [input().split() for _ in range(N)]

n_final = outer()
print(g, n_final)