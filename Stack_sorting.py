def sort():
    s1 = stack()
    while !s.isEmpty():
        temp = s.pop()
        if s1.isEmpty() || temp > s.peek():
            s.push(temp)
        else:
            while s1.peek() > temp:
                s.push(s1.pop())
                if s1.isEmpty():
                    break
           s1.push(temp)
    return s1