universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_size(unis):
    enrolled = []
    tuitions = []
    for x in unis:
        enrolled.append(x[1])
        tuitions.append(x[2])
    return enrolled, tuitions

def mean(nums):
    return sum(nums)/len(nums)

def median(nums):
    nums.sort()
    return nums[(len(nums)-1)//2]

enrolled, tuitions = enrollment_size(universities)

print(f'Total students: {sum(enrolled)}')
print(f'Total tuition: $ {sum(tuitions)}')

print(f'\nStudent mean: {mean(enrolled):.2f}')
print(f'Student median: {median(enrolled)}')

print(f'\nTuition mean: {mean(tuitions):.2f}')
print(f'Tuition median: {median(tuitions)}')

