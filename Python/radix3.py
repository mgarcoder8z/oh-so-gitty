def radix_sort(a):
    "sort list of integers using base-10 radix sort without using n or len"

    if a:
        bins = [ [],[],[],[],[],[],[],[],[],[] ]

        # get largest element to determine when sort is done
        m = max(a)
        # decimal digit currently partitioning on (1,10,100...)
        r = 1

        while m > r:
            # append each element of a to the end of the bin
            # corresponding to the partition digit
            for e in a:
                bins[(e/r)%10].append(e)

            r = r * 10

            # move values from bins back to a single list
            a = []
            for i in range(10):
                a.extend(bins[i])
                bins[i] = []

    return a

print(radix_sort([1,67,192,3000,567,789,34,21,2,8,19]))
