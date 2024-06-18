#PARTICAL 7
#PATTERN MATCHING IN THE LIT
#PATTERN MATCHING USING BRUTE FORCE TECHNIQUE
print(""">>> PATTERN MATCHING IN THE STRING USING BRUTE FORCE\n
     this founds the pattern in the below text
     text = "abc beababcabc"
     pattern = "abc" """)
print("")#..space

def brute_force_pattern_matching(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m +1):
        j = 0
        while j < m and text [i + j] == pattern[j]:
            j += 1
        if j == m:
            return i
        return -1

text = "abc beababcabc"
pattern = "abc"
result = brute_force_pattern_matching(text, pattern)

if result != -1:
    print(f"--- Pattern found at index {result}")
else:
    print(f"--- Pattern not found in the text")
    
