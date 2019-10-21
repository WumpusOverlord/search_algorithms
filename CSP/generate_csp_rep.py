#
# def get_var(i, cell):
#     return i

def generate_constraints(var_a, a_val, var_b, b_val):
    if a_val != b_val:
        return True
    return False


def check_constraint(a_val, b_val):
    if a_val == b_val:
        return False

    return True


def generate_variables(sudoku):
    var_list = []
    for i, cell in enumerate(sudoku):
        var_list.append(i)

    return var_list


def get_same_row(i, cell, sudoku):
    row_list = []

    cell_position = cell.position

    for j, c in enumerate(sudoku):

        if (i != j) and (c.position[0] == cell_position[0]):
            row_list.append(j)

        elif (i != j) and (c.position[1] == cell_position[1]):
            row_list.append(j)

        elif (i != j) and (c.position[2] == cell_position[2]):
            row_list.append(j)

    return row_list


def generate_neigbours(sudoku):
    neightbors_dicts = {}
    for i, cell in enumerate(sudoku):

        neightbors_dicts[i] = get_same_row(i, cell, sudoku)
        # var_list.append(i)

    return neightbors_dicts


def generate_domains(sudoku):
    domain_dict = {}
    for i, cell in enumerate(sudoku):

        domain_dict[i] = list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    return domain_dict


def geneerate_labelled_and_unlabelled_lists(sudoku, var_list, domain_dicts):
    labelled_list = []
    unlabelled_list = list(var_list)

    for i, cell in enumerate(sudoku):
        if cell.solved:
            domain_dicts[i] = [cell.answer]
            labelled_list.append(i)
            unlabelled_list.remove(i)
    return labelled_list, unlabelled_list
