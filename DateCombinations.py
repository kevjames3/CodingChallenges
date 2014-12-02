#Of x, y, and z, which are valid orderings?
def answer(x, y, z):
    import datetime
    from itertools import permutations

    values = [x, y, z]
    combos = set(map(tuple, permutations(values, len(values))))

    answer = None
    for combo in combos:
        century = 1900
        year = combo[0] + century
        month = combo[1]
        day = combo[2]

        try:
            currDate = datetime.date(year, month, day)
            formattedString = "%02d/%02d/%02d" % (currDate.month, currDate.day, currDate.year - century) 
            if not answer:
                answer = formattedString
            else: 
                answer = "Ambiguous"
            	break
        except ValueError:
            pass 

    return answer

if __name__ == '__main__':
	#Example test cases
	print answer(19,19,3)
	print answer(10,20,3)
	print answer(1,1,99)
	print answer(2,30,3)
	print answer(12,20,30)
    