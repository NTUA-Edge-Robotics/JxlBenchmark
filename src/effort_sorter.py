def effort_sorter(column):
    """Sorts a pandas data frame by effort

    Args:
        column (_type_): The efforts column

    Returns:
        _type_: The data sorted by effort
    """
    efforts = ["lightning", "thunder", "falcon", "cheetah", "hare", "wombat", "squirrel", "kitten"]

    correspondence = {effort: order for order, effort in enumerate(efforts)}
    
    return column.map(correspondence)
