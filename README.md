# CS230_Project

Team: **Cherry Blossom**

| Name| Roll Number |
| --- | ----------- |
| Ameya Prashant Deshmukh | 210050011 |
| Harsh Poonia | 210050063 |
|Tanay Vineet Tayal | 210050155 |


## Instructions to run

- `ChampSim/inc/champsim.h` has two macros: `INCLUSIVE` and `EXCLUSIVE` defined, these can be commented/uncommented to achieve the 3 cache inclusion policies: Inclusive, Exclusive and Non-Inclusive Non-Exclusive.
- `ChampSim/inc/cache.h` has the macro `LLC_SETS` which can be modified to achieve the desired LLC size.
- The replacement policy can be chosen among `lru`, `lfu`, `fifo`, `random`, `ship`, `srrip`, `mru`, `lifo` as an argument to the script `build_champsim.sh`.
- Graph Analytics traces are hosted [here](https://utexas.app.box.com/s/2k54kp8zvrqdfaa8cdhfquvcxwh7yn85/folder/132804598561).
- To run the simulation, run the command `./run_champsim.h N_WARMUP N_SIM trace_name` where `N_WARMUP` and `N_SIM` are units of million instructions.
