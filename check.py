import os;
import fileinput
import sys
sets = ["2048", "4096", "8192", "16384"]
latency ={}
latency["2048"] = "20"
latency["4096"] = "27"
latency["8192"] = "32"
latency["16384"] = "41"
#done with way = 1

Types = ["lru", "lfu", "random", "fifo"]
hiers = ["incl", "nonincl", "excl"]
Traces = ["bfs-14.trace.gz", "pr-10.trace.gz", "bc-12.trace.gz", "sssp-14.trace.gz"]
for hier in hiers:
    for i, line in enumerate(fileinput.input("./inc/champsim.h", inplace = 1)):
        
        if "#define INCLUSIVE" in line:
            if hier == "incl":
                sys.stdout.write("#define INCLUSIVE\n")
            else:
                sys.stdout.write("// #define INCLUSIVE\n")
        elif "#define EXCLUSIVE" in line:
            if hier == "excl":
                sys.stdout.write("#define EXCLUSIVE\n")
            else:
                sys.stdout.write("// #define EXCLUSIVE\n")
        else:
            sys.stdout.write(line)
        
    for sett in sets:
        for i, line in enumerate(fileinput.input('./inc/cache.h', inplace=1)):
            if "#define LLC_SET " in line: 
                sys.stdout.write("#define LLC_SET NUM_CPUS*" + sett+"\n")
            elif "#define LLC_LATENCY" in line:
                sys.stdout.write("#define LLC_LATENCY " + latency[sett] + "\n")
            else:
                sys.stdout.write(line)
        for mytype in Types:
            os.system("./build_champsim.sh bimodal no no no no " + mytype + " 1 ")
            binary = "bimodal-no-no-no-no-" + mytype + "-1core"
            os.system("mv ./bin/" + binary +" ./bin/" + binary + "_" + hier)
            binary  = binary + "_" + hier
            for trace in Traces:
                os.system("./run_champsim.sh " + binary + " 30 30 " + trace)
                print(hier+sett+mytype+trace)
        os.system("cp -r ./results_30M ../../shared_folder/Desktop/results_30M_"+ sett+"sets_"+hier)
