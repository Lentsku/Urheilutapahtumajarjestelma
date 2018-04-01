def formatName(param):
    if '-' in param:
        paramSplit = param.split('-')
        result = ''
        for item in paramSplit:
            result += item[:1].upper() + item[1:] + '-'
        return result[:-1]

    return param[:1].upper() + param[1:]
