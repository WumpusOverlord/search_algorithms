from CSP.Backtracking.ac3bt import Backtrack
from CSP.Sudoku.sudoku_generator2 import main, printSudoku
from CSP.generate_csp_rep import check_constraint, geneerate_labelled_and_unlabelled_lists, \
    generate_domains, generate_neigbours, generate_variables

sudoku, answers = main("Easy")

neighbors_dicts = generate_neigbours(sudoku)
var_list = generate_variables(sudoku)
domain_dicts = generate_domains(sudoku)

constraints = [check_constraint]

labelled_list, unlabelled_list = geneerate_labelled_and_unlabelled_lists(sudoku, var_list, domain_dicts)

print("solving")
search = Backtrack()

puzzle_answer = search.back_track_search(unlabelled_list, labelled_list, domain_dicts, constraints, neighbors_dicts)

for i, cell in enumerate(sudoku):
    cell.answer = puzzle_answer[i][0]
    cell.solved = True
    cell.possibleAnswers = puzzle_answer[i]

printSudoku(sudoku)

print("done!")
