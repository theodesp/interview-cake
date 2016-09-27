import itertools
import operator

def condense_meeting_times(list_of_tiples):
    if len(list_of_tiples) <= 0:
        return
    
    # Create an empty stack of intervals
    stack = []

    # sort the intervals in increasing order of start time
    sorted_intervals = sorted(list_of_tiples, key=lambda tup: tup[0])

    # push the first interval to stack
    stack.append(sorted_intervals[0])

    # Start from the next interval and merge if necessary
    for interval in itertools.islice(sorted_intervals, 1, None):

        # if we have not overlap just push this interval to the stack
        if stack[-1][1] < interval[0]:
            stack.append(interval)
        # if we have overlap merge the new inteval with the one on top of the stack
        elif stack[-1][1] < interval[1]:
            newtop = (stack[-1][0], interval[1],)
            stack.pop()
            stack.append(newtop)

    return stack