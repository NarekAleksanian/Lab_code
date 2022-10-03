class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        binary = []
        for i in arr:
            binary.append(bin(i).count('1'))
        if ''.join(str(x) for x in binary).count(str(binary[0])) == len(binary):
            return sorted(arr)
        i = 1
        while i < len(binary):
            tmp = binary[i]
            tm = arr[i]
            j = i-1
            while j >= 0 and tmp < binary[j]:
                arr[j+1] = arr[j]
                binary[j+1] = binary[j]
                j -= 1
            arr[j+1] = tm
            binary[j+1] = tmp
            i += 1
       
        i = 0
        j = 1
        start = 0
        end = 0
        while i < len(binary):
            j = i+1
            while j < len(binary) and binary[j] == binary[i]:
                end = j
                j += 1
            else:
                start = i
                arr[start:end+1] = sorted(arr[start:end+1])
            i = j
        return arr
