def answer(N, L, Q):
    while(Q > 0):
        q = int(input())
        Q = Q - 1
        count = 0
        i = 0
        for i in range(N):
            if(int(L[i]) >= q):
                count += 1
            elif(int(L[i]) + 1 == q):
                count += 1
        print(count)

# mapping to integer removed to make it more space efficient
# passing the list of lengths only once to answer function to increase time efficiency
# I think that the time complexity is O(n) and nothing better than this could be acheived
# Sorting is also removed for this purpose.
def main():
    T = int(input())
    while(T > 0):
        N, Q = input().split(' ')
        L = input().split(' ')
        answer(int(N), L, int(Q))
        T = T - 1

if __name__ == "__main__":
    main()
