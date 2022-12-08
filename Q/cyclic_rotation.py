def solution(A, K):
    if not A:
        return A

    rotate = K % len(A)
    return A[-rotate:] + A[:-rotate]
