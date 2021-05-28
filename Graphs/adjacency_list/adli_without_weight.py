def create_adjacency_list(elist,vlist):
    adli=dict()
    edges=elist.split(',')
    for e in edges:
        fr=e[0]
        to=e[1]
        if fr in adli:
            adli[fr].append(to)
        else:
            adli[fr]=[]
            adli[fr].append(to)
        if to in adli:
            adli[to].append(fr)
        else:
            adli[to]=[]
            adli[to].append(fr)
    return adli