# Python code to print Nano prioritization buckets (V27)
# Based on: https://github.com/nanocurrency/nano-node/pull/4661/files

# Column headers:
print ( f'{"Bucket Number":<15}' + f'{"Bucket Region":<15}' + f'{"Bucket Range (Nano)":<33}' + f'{"Bucket Range (Raw)":<30}' )

# Initialize lists
minimums_list = []
maximums_list = []
exponent_list = []

def build_region(begin, end, count):
    # Determine how wide a single sub-region (bucket) is:
    width = ((1<<end) - (1<<begin)) / count
    
    # Loop through the number of buckets in each region:
    i = 0    
    while i < count:
        minimums_list.append((1<<begin) + i * width)
        maximums_list.append((1<<begin) + (i+1) * width)
        exponent_list.append("2^" + str(begin) + "-" + "2^" + str(end))
        i += 1

minimums_list.append(0)
maximums_list.append((1<<79))
exponent_list.append("0-2^79")
build_region(79, 88, 1)
build_region(88, 92, 2)
build_region(92, 96, 4)
build_region(96, 100, 8)
build_region(100, 104, 16)
build_region(104, 108, 16)
build_region(108, 112, 8)
build_region(112, 116, 4)
build_region(116, 120, 2)
build_region(120, 128, 1)

x = 0
while x < len(minimums_list):
    #Get the minimum range in float, convert to string, truncate to 15 chars
    minimum_float_truncated = str(f'{minimums_list[x]/(10**30):,.17f}')[:15]

    #Get the maximum range in float, convert to string, truncate to 15 chars
    maximum_float_truncated = str(f'{maximums_list[x]/(10**30):,.17f}')[:15]
    
    print(f'{str(x):<15}' \
            f'{exponent_list[x]:<14}', \
            f"{minimum_float_truncated + '-' + maximum_float_truncated:<32}", \
            str(int(minimums_list[x])) + "-" + str(int((maximums_list[x]))) )
    x += 1

print("Total length:", len(minimums_list))
