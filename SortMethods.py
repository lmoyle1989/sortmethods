import heapq

class SortMethods:
    def __init__(self):
        None

    def quicksort(self, arr: list[int]) -> list[int]:
    
        def partition(arr: list[int], l: int, r: int):
            if l < r:
                swapidx = l
                for i in range(l, r+1):
                    if arr[i] < arr[r]:
                        arr[i], arr[swapidx] = arr[swapidx], arr[i]
                        swapidx += 1
                arr[r], arr[swapidx] = arr[swapidx], arr[r]
                partition(arr, l, swapidx-1)
                partition(arr, swapidx+1, r)

        partition(arr, 0, len(arr)-1)
        
        return arr

    def mergesort(self, arr: list[int]) -> list[int]:
        
        def splitandmerge(arr: list[int], l: int, r: int) -> list[int]:
            if l == r:
                return [arr[l]]
            else:
                m = (l+r) // 2
                left = splitandmerge(arr, l, m)
                right = splitandmerge(arr, m+1, r)
                pl = 0
                pr = 0
                lsize = len(left)
                rsize = len(right)
                newarr = []
                while pl < lsize or pr < rsize:
                    while pl < lsize and pr < rsize:
                        if left[pl] < right[pr]:
                            newarr.append(left[pl])
                            pl += 1
                        else:
                            newarr.append(right[pr])                
                            pr += 1
                    if pl < lsize:
                        newarr.append(left[pl])
                        pl += 1
                    if pr < rsize:
                        newarr.append(right[pr])                
                        pr += 1
                return newarr

        return splitandmerge(arr, 0, len(arr)-1)
    
    def heapsort(self, arr: list[int]) -> list[int]:
        h = arr.copy()
        heapq.heapify(h)
        newarr = []
        while h:
            newarr.append(heapq.heappop(h))
        
        return newarr


if __name__ == "__main__":
    test = SortMethods()
    arr = [77, 9, 5, 8, 3, 11, 13, 2, 55, 7, 62, 1, 9]
    print("Quicksort")
    print(test.quicksort(arr.copy()))
    print("Mergesort")
    print(test.mergesort(arr.copy()))
    print("Heapsort")
    print(test.heapsort(arr.copy()))