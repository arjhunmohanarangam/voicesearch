from googlesearch import search

search_list = []


def searching(item):
    searching = search(item, num_results=5)
    for i in searching:
        search_list.append(i)
    return search_list
