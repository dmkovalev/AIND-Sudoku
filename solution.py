assignments = []

rows = 'ABCDEFGHI'
cols = '123456789'

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    

    # Find all instances of naked twins
    naked_twins = list()
    for k, v in values.items():
        naked = False
        if len(v) == 2:
            for p in peers[k]:
                if values[p] == v:
                    naked = True
            if naked:
                naked_twins.append(k)
    # Eliminate the naked twins as possibilities for their peers
    for nt in naked_twins:
        for p in peers[nt]:
            if p not in set(naked_twins):
                if len(values[p]) > 2:
                    assign_value(values, p, values[p].replace(values[nt][0],'').replace(values[nt][1],''))

    display(values)
    return values

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in A for t in B]

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    s = dict(zip(boxes,grid))
    for key, value in s.items():
        if s[key] == '.':
            s[key] = '123456789'
    return s

def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
            for c in cols))
        if r in 'CF': print(line)
    print

def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """

    for k,v in values.items():
        if len(v) == 1:
            for p in peers[k]:
                assign_value(values,p,values[p].replace(v,''))

    return values

def only_choice(values):
    for unit in unitlist:
        sub = ''
        for k in unit:
            sub += values[k]
        con = [l for l in cols if sub.count(l) == 1]
        for k in unit:
            for el in con:
                if el in values[k]:
                    assign_value(values,k,el)
    return values

def reduce_puzzle(values):
    solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

#    values = naked_twins(values)
    # Your code here: Use the Eliminate Strategy
    values = eliminate(values)
    # Your code here: Use the Only Choice Strategy
    values = only_choice(values)
    # Check how many boxes have a determined value, to compare
    solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
    # If no new values were added, stop the loop.
    stalled = solved_values_before == solved_values_after
    # Sanity check, return False if there is a box with zero available values:
    if len([box for box in values.keys() if len(values[box]) == 0]):
        return False
    return values

def search(values):
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    # Choose one of the unfilled squares with the fewest possibilities
    key = ''

    if values is False:
        return False

    if all(len(values[s]) == 1 for s in boxes):
        return values ## Solved!

    for k,v in values.items():
        if len(v) > 1:
            key = k

    for k,v in values.items():
        if len(values[key]) > len(v) and len(v) > 1:
            key = k

    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for v in values[key]:
        new_v = values.copy()
        new_v[key] = v
        r = search(new_v)
        if r:
            return r

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    
    values = grid_values(diag_sudoku_grid)
    return search(values)

boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))
    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
