
def minSwapsCouples1(row):
    ## Build a Map of Couple
    couple_map = {person: ind for ind, person in enumerate(row)}
    min_swap = 0
    for ind in range(0, len(row), 2):
        person = row[ind]
        partner = person ^ 1

        if partner != row[ind+1]:
            min_swap += 1
            partner_ind = couple_map[partner]
            ## Swap
            row[ind + 1], row[partner_ind] = row[partner_ind], row[ind + 1]
            ## Update the couple map
            couple_map[row[ind+1]] = ind+1
            couple_map[row[partner_ind]] = partner_ind
    return min_swap


if __name__ == "__main__":
    row = [3, 2, 0, 1]
    result = minSwapsCouples1(row)
    print(result)
