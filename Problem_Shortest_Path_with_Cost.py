def problem1(source, target, original, changed, cost):
    # total minimum cost to convert source string to target string
    sum = 0

    # function to check whether conversion is possible or not
    def conversion_check(source_char, target_char):
        '''
            if conversion is not possible:
                return -1
            return 1
        '''
        pass

    # function to give the min cost
    # cost_min can be -1
    def min_cost(source_char, target_char):

        # check whether the conversion is possible or not
        if conversion_check(source_char, target_char) == -1:
            return -1

        # min_cost logic
        cost_min = 0
        # you have to write the code to complete the logic
        pass
        return cost_min

    # source.length=target.length
    for i in range(len(source)):
        # if source charater is same as target character the cost for conversion is 0
        if source[i] == target[i]:
            sum += 0
        elif min_cost(source[i], target[i]) == -1:
            sum = -1
            break
        else:
            sum += min_cost(source[i], target[i])

    return sum