def delete(list, index=None):
    list.pop(index) if index != None else list.pop()
    return list