#
# AC3 - BT

"""CSP (Constraint Satisfaction Problems) problems and solvers. (Chapter 5)."""

from __future__ import generators


# from utils import *
# import search

class Backtrack:
    nodes_searched = 0

    @staticmethod
    def check_valid_solution(labelled, domain_dictionary, neighbors_dicts, constraints):
        for position in labelled:

            cell_value = domain_dictionary[position][0]

            adjacent_cells = neighbors_dicts[position]

            for cell in adjacent_cells:

                val_b = domain_dictionary[cell][0]

                for constraint in constraints:
                    valid_value = constraint(cell_value, val_b)
                    if valid_value is False:
                        print("INVALID SOLUTION")
                        return False
        return True

    @staticmethod
    def check_consistent(var_a, val_a, domain_dict, neighbors_dicts, labelled, constraints):
        ok = True
        for constraint in constraints:
            for neighbour in neighbors_dicts[var_a]:
                if neighbour in labelled:
                    var_b = neighbour
                    val_b = domain_dict[var_b][0]
                    if not constraint(val_a, val_b):
                        ok = False
                        return False

        return True

    def back_track_search(self, unlabelled, labelled, domain_dictionary, constraints, neighbors_dicts, var_a=None,
                          val_1=None):

        self.nodes_searched = self.nodes_searched + 1

        # print("Nodes searched:" + str(nodes_searched))

        unlabelled = [i for i in unlabelled]
        labelled = [i for i in labelled]
        constraints = list(constraints)
        domain_dict = {}
        for key in domain_dictionary.keys():
            domain_dict[key] = []
            for val in domain_dictionary[key]:
                domain_dict[key].append(val)

        if var_a is not None:
            domain_dict[var_a] = [val_1]

        if (len(unlabelled) == 0) and (Backtrack.check_valid_solution(labelled, domain_dict, neighbors_dicts,
                                                                      constraints)):
            return domain_dict
        elif len(unlabelled) == 0:
            return None
        var_a = unlabelled.pop()
        labelled.append(var_a)

        for val_a in list(domain_dict[var_a]):
            if Backtrack.check_consistent(var_a, val_a, domain_dict, neighbors_dicts, labelled, constraints):
                result = self.back_track_search(unlabelled, labelled, domain_dict, constraints, neighbors_dicts, var_a,
                                                val_a)
                if result != None:
                    return result

        return None


class BackJumpSearch(Backtrack):
    conflict_set = {}

    def add_conflict(self, conflict_set, var_a, var_b):
        conflict_set[var_a] = {var_b}

    @staticmethod
    def check_consistent(var_a, val_a, domain_dict, neighbors_dicts, labelled, constraints):
        ok = True
        for constraint in constraints:
            for neighbour in neighbors_dicts[var_a]:
                if neighbour in labelled:
                    var_b = neighbour
                    val_b = domain_dict[var_b][0]
                    if not constraint(val_a, val_b):
                        ok = False
                        # conflict_set[var_a] =
                        return False

        return True

    def back_track_search(self, unlabelled, labelled, domain_dictionary, constraints, neighbors_dicts, var_a=None,
                          val_1=None):

        self.nodes_searched = self.nodes_searched + 1

        # print("Nodes searched:" + str(nodes_searched))

        unlabelled = [i for i in unlabelled]
        labelled = [i for i in labelled]
        constraints = list(constraints)
        domain_dict = {}
        for key in domain_dictionary.keys():
            domain_dict[key] = []
            for val in domain_dictionary[key]:
                domain_dict[key].append(val)

        if var_a is not None:
            domain_dict[var_a] = [val_1]


        else:
            # Get last from conflict set

            last_var_assigned = next(reversed(labelled))
            max_check = self.conflict_set[last_var_assigned]

            self.conflict_set[last_var_assigned] = []
            previous_variable = labelled.pop(last_var_assigned)

        #     IF assigned at least 1 variable:
        #     Add the last variable assigned to conflict set of current variable
        #     Also add the conflict set of the last variable to the current variable
        # ELSE:
        # ??? add conflict set of conflict set of last variable assigned to conflict set of current variable
        # ???Remove the last var from conflict set
        # set current var as last_var

        if (len(unlabelled) == 0) and (Backtrack.check_valid_solution(labelled, domain_dict, neighbors_dicts,
                                                                      constraints)):
            return domain_dict
        elif len(unlabelled) == 0:
            return None
        var_a = unlabelled.pop()
        labelled.append(var_a)

        for val_a in list(domain_dict[var_a]):
            if Backtrack.check_consistent(var_a, val_a, domain_dict, neighbors_dicts, labelled, constraints):
                result = self.back_track_search(unlabelled, labelled, domain_dict, constraints, neighbors_dicts, var_a,
                                                val_a)
                if result != None:
                    return result

        return None
