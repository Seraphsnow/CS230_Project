import re
import matplotlib.pyplot as plt
import numpy as np
fullnames = {
    'sssp' : 'sssp-14',
    'bc' : 'bc-12',
    'bfs' : 'bfs-14',
    'pr' : 'pr-10',
}
traces = ['sssp', 'bfs', 'bc', 'pr']
policies = ['lru', 'random', 'ship', 'fifo', 'lfu']
hierarchies = ['excl', 'incl', 'nonincl']
sizes = ['2048', '4096', '8192', '16384']

def get_file(trace, hierarchy, policy, size):
    return open(fullnames[trace] + '.trace.gz-bimodal-no-no-no-no-' + policy + '-1core_' + hierarchy + '_' + str(size) + '.txt', 'r')

def get_IPC(file):
    for i, line in enumerate(file, 1):
        if 'Finished CPU' in line:
            x = re.search('cumulative IPC: ([^\s]*\s)', line)
            return(x.group(1))
def get_LLC(file):
    for i, line in enumerate(file, 1):
        if 'LLC TOTAL' in line:
            x = re.findall('(HIT:[\s]*|ACCESS:[\s]*|MISS:[\s]*)([0-9]+)', line)
            return(x[0][1], x[1][1], x[2][1])

fixed_trace = 'bfs'
for p in policies:
    x = sizes
    y_incl = [get_IPC(get_file(fixed_trace, 'incl', p, size)) for size in x]
    y_excl = [get_IPC(get_file(fixed_trace, 'excl', p, size)) for size in x]
    y_non = [get_IPC(get_file(fixed_trace, 'nonincl', p, size)) for size in x]
    X_axis = np.arange(4)
    plt.bar(X_axis - 0.25, y_incl, 0.25, label = 'Inclusive')
    plt.bar(X_axis, y_non, 0.25, label = 'Non-Inclusive')
    plt.bar(X_axis + 0.25, y_excl, 0.25, label = 'Exclusive')
    plt.xticks(X_axis, x)
    plt.xlabel("LLC Sets")
    plt.ylabel("IPC")
    plt.title(fixed_trace + "- IPC vs LLC Sets, policy = " + p)
    plt.legend()
    plt.show()

for s in sizes:
    x = policies
    y_incl = [get_IPC(get_file(fixed_trace, 'incl', policy, s)) for policy in x]
    y_non = [get_IPC(get_file(fixed_trace, 'nonincl', policy, s)) for policy in x]
    y_excl = [get_IPC(get_file(fixed_trace, 'excl', policy, s)) for policy in x]  
    X_axis = np.arange(5)
    plt.bar(X_axis - 0.25, y_incl, 0.25, label = 'Inclusive')
    plt.bar(X_axis, y_non, 0.25, label = 'Non-Inclusive')
    plt.bar(X_axis + 0.25, y_excl, 0.25, label = 'Exclusive')
    plt.xticks(X_axis, x)
    plt.xlabel("Policies")
    plt.ylabel("IPC")
    plt.title(fixed_trace + "- IPC vs Policies, Sets = " + s)
    plt.legend()
    plt.show()
