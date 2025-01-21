def main():
    # Read the number of test cases
    t = int(input())  
    
    for _ in range(t):
        # Read n (chart side length) and k (square side length)
        n, k = map(int, input().split())
        
        # Calculate the number of k×k squares that can fit
        result = (n // k) * (n // k)
        
        # Print the result
        print(result)

# Main guard
if __name__ == "__main__":
    main()