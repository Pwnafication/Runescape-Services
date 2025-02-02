#2strings:
first_string = "hellooo##"
second_string = "hee#lll#o"



class Solution():
    def check_arrays_equal(arr1,arr2):
        check_arr1 = []
        check_arr2 = []
        for each1 in arr1:
            if each1 == "#":
                check_arr1.pop()
            else:
                check_arr1.append(each1)

        for each2 in arr2:
            if each2 == "#":
                check_arr2.pop()
            else:
                check_arr2.append(each2)
        if check_arr2 == check_arr1:
            return True    
        return False
    
print(Solution.check_arrays_equal(first_string,second_string))