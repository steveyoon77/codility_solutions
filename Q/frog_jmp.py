def solution(X, Y, D):
    if D < 0 or X < 0 or Y < 0 or Y < X:
        return 0
    
    dist = Y-X
    steps = dist//D
    if (dist%D) > 0:
        steps += 1
    return steps