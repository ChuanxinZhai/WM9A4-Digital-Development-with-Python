# Enter your code here. Read input from STDIN. Print output to STDOUT

# Function to generate the door mat design
def generate_door_mat(N, M):

    design = []
    
    # Top 
    for i in range(1, N, 2):
        pattern = (".|." * i).center(M, "-")
        design.append(pattern)
    
    # Middle 
    design.append("WELCOME".center(M, "-"))
    
    # Bottom 
    for i in range(N-2, 0, -2):
        pattern = (".|." * i).center(M, "-")
        design.append(pattern)
    
    for line in design:
        print(line)

if __name__ == '__main__':
    N, M = map(int, input().split())
    generate_door_mat(N, M)
