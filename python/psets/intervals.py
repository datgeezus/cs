
def minrooms(schedules):
    print(schedules)
    print( schedules.sort(key=lambda tup: tup[0]) )

if __name__ == '__main__':
    print(minrooms([(9,10), (9.5, 10), (9, 9.5), (10, 11)]))
