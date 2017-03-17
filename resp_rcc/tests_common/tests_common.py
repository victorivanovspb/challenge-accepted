# -*- coding: utf-8 -*-

def get_filenames(path, min_val, max_val):
    """
        Допустим, у нас имеется структура файлов:
            path/
                01
                01.a
                02
                02.a

        В таком случае вызов get_filenames(path, 1, 2) вернёт:
            [(path/01, path/01.a), (path/02, path/02.a)]
    """

    result = []
    for i in xrange(min_val, max_val + 1):
        name = str(i)
        name = "0" + name if len(name) == 1 else name
        result.append((path + name, path + name + ".a"))
    return result
