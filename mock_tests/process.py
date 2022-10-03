

def process(start, load):
    finish = {}
    for idx, each_load in enumerate(load):
        finish[start[idx]] = each_load + start[idx] - 1

    for idx, pro in enumerate(finish.keys()):
        process = pro
