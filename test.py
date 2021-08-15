def say_scores(score0, score1):
    """A commentary function that announces the score for each player."""
    print("Player 0 now has", score0, "and Player 1 now has", score1)
    return say_scores

def announce_lead_changes(last_leader=None):
    """Return a commentary function that announces lead changes.

    >>> f0 = announce_lead_changes()
    >>> f1 = f0(5, 0)
    Player 0 takes the lead by 5
    >>> f2 = f1(5, 12)
    Player 1 takes the lead by 7
    >>> f3 = f2(8, 12)
    >>> f4 = f3(8, 13)
    >>> f5 = f4(15, 13)
    Player 0 takes the lead by 2
    """
    def say(score0, score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader != None and leader != last_leader:
            print('Player', leader, 'takes the lead by', abs(score0 - score1))
        return announce_lead_changes(leader)
    return say
    
def both(f, g):
    """Return a commentary function that says what f says, then what g says.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> h0 = both(say_scores, announce_lead_changes())
    >>> h1 = h0(10, 0)
    Player 0 now has 10 and Player 1 now has 0
    Player 0 takes the lead by 10
    >>> h2 = h1(10, 6)
    Player 0 now has 10 and Player 1 now has 6
    >>> h3 = h2(6, 17)
    Player 0 now has 6 and Player 1 now has 17
    Player 1 takes the lead by 11
    """
    def say(score0, score1):
        return both(f(score0, score1), g(score0, score1))
    return say

"""Disc04    Disc04    Disc04    Disc04    Disc04    Disc04"""
def count_stair_ways(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return count_stair_ways(n-1)+count_stair_ways(n-2)

def count_k(n,k):
    if n==0 or n==1:
        return 1
    if n<0:
        return 0
    i, count = 1, 0
    while i <k:
        count += count_k(n-i, k)
        i += 1
    return count
    

def max_products(s):
    if not s:
        return 1
    return max(s[0]*max_products(s[2:]), max_products(s[1:]))

def check_hole_number_listed(n): 
    """ n is a list of numbers splited"""
    if len(n)==3:
        return (True if n[1]<min(n[0],n[2]) else False)
    return (True if n[1]<min(n[0],n[2]) else False) and check_hole_number_listed(n[2:])

def check_hole_number(n):
    if n//1000 == 0:
        return (True if n//10%10 < min(n//100%10, n%10) else False)
    return (True if n//10%10 < min(n//100%10, n%10) else False) and check_hole_number(n//100)

def check_mountain_number(n):
    def helper(n, has_turned):
        if n // 10 == 0:
            return  True
        if has_turned and n%10<n//10%10:
            return False
        return helper(n//10,~has_turned) if (~has_turned and n%10>n//10%10) else helper(n//10,has_turned)
    return helper(n,False)

"""Disc05    Disc05    Disc05    Disc05    Disc05    Disc05"""
def group_by(s, fn):
    dict = {}
    for i in s:
        k = fn(i)
        if k not in dict.keys():
            dict[k] = [i]
        else:
            dict[k].append(i)

    return dict

def partition_options(total, biggest):
    if  total == 0:
        return [[]]
    elif total<0 or biggest == 0:
        return []
    else:
        with_biggest = partition_options(total-biggest, biggest)
        without_biggest = partition_options(total, biggest-1)
        with_biggest = [[biggest] + i for i in with_biggest]
        return with_biggest + without_biggest 

"""Disc06    Disc06    Disc06    Disc06    Disc06    Disc06"""

def nonlocalist():
    get = lambda x: "Index out of range!"
    def prepend(value):
        nonlocal get
        f = get
        def get(i):
            if i == 0:
                return value
            return f(i-1)
        
    return prepend, lambda x:get(x)

# f = lambda x: x and (f(x-1) or print(x))
# 


def memory(x, f):
    def g(h):
        print(f(x))
        return memory(x, h)
    return g

def subset_sum(seq, k):
    if not seq:
        return False
    if k in seq:
        return True
    for i in seq:
        s = seq
        s.remove(i)
        if subset_sum(s,k-i):
            return True
    return False


''''''''''''''''''''''''''''''''''''''''''''''''''

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted
    
def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

''''''''''''''''''''''''''''''''''''
"""
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font', size=16)

from timeit import repeat
from numpy import median, percentile

def plot_times(name, xs, n=15):
    f = lambda x: name + '(' + str(x) + ')'
    g = globals()

    samples = []
    for _ in range(n):
        times = lambda x: repeat(f(x), globals=g, number=1, repeat=n)
        samples.append(median(times(x)) for x in xs)
    ys = [10e3 * median(sample) for sample in samples]

    plt.figure(figsize=(8, 8))
    plt.plot(xs, ys)
    plt.xlabel('n')
    plt.ylabel('milliseconds')

exp_2 = lambda n: exp(2, n)
plot_times('exp_2', range(20, 1600, 10))

"""