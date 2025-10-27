def merge_the_tools(string, k):
    n = len(string)
    for i in range(0,n,k):     
        seen = set()
        result = []
        for ch in string[i:i+k]:
            if ch not in seen:
                seen.add(ch)
                result.append(ch)
        print(''.join(result))        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
