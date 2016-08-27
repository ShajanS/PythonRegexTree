"""
# Copyright Nick Cheng, Brian Harrington, Danny Heap, Shajan Sivarajah
# 2013, 2014, 2015
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2015
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

# Do not change this import statement, or add any of your own!
from regextree import RegexTree, StarTree, DotTree, BarTree, Leaf

# Do not change anything above this comment except for the copyright
# statement

# Student code below this comment.

# Global Variables For Functions
uno_regex = ["e", "1", "2", "0"]
duo_regex = ["|", "."]
bracket = ["(", ")"]


def is_regex(s):
    ''' (str) -> bool
    Checks if a given string is a valid regex and returns True or False
    >>>is_regex("((1.(1|2)*).0)")
    True
    >>>is_regex("1********")
    True
    >>>is_regex("Regex")
    False
    >>>is_regex("")
    False
    '''
    length = len(s)
    # Base Case
    if len(s) <= 1:
        result = s in uno_regex
    # If there regex ends in "*" check value before
    # to see if it is apart of uno_regex
    elif s[-1] == "*":
        result = is_regex(s[:-1])
    # If regex string is enclosed in parentheses "(" ")"
    elif s[0] == "(" and s[-1] == ")":
        # Set counters
        break_location = 0
        bracket_count = 0
        # Find the location to split the regex into r1 and r2 components
        # Search the elements in range of the regex
        # s[1:-1] Accommodates for the outter brackets
        for element in range(len(s[1:-1])):
            # If element is a left bracket
            if s[1:-1][element] == bracket[0]:
                bracket_count += 1
            # If element is a right bracket
            elif s[1:-1][element] == bracket[1]:
                bracket_count -= 1
            # If there is a set of brackets followed by a | or .
            # Is the location where to split for components
            elif (bracket_count == 0 and s[1:-1][element] in duo_regex):
                # Accomodate for the outer brackets
                break_location = element + 1
        # if the element at the split index is not a | or .
        # Return False
        if (s[break_location] in duo_regex) == False:
            result = False
        else:
            # Call the function again to check if r1 and r2 is a regex
            # [:break_location-1] is done to not include the split node
            if is_regex(s[1:break_location]) and \
               is_regex(s[break_location+1:length-1]):
                result = True
            # Return False if not
            else:
                result = False
    # If any other case occurs return False
    else:
        result = False
    return result


def perms(perm_string):
    ''' (str) -> list
    Function uses the given string and returns all permutations of the string
    >>> perms("abc")
    ['cba', 'bca', 'cab', 'acb', 'bac', 'abc']
    >>> perms("123")
    ['321', '231', '312', '132', '213', '123']
    >>> perms("(1.2)")
    [')2.1(', '2).1(', ').21(', '.)21(', '2.)1(', '.2)1(', ')21.(', '2)1.(',
    ')12.(', '1)2.(', '21).(', '12).(', ').12(', '.)12(', ')1.2(', '1).2(',
    '.1)2(', '1.)2(', '2.1)(', '.21)(', '21.)(', '12.)(', '.12)(', '1.2)(',
    ')2.(1', '2).(1', ').2(1', '.)2(1', '2.)(1', '.2)(1', ')2(.1', '2)(.1',
    ')(2.1', '()2.1', '2().1', '(2).1', ').(21', '.)(21', ')(.21', '().21',
    '.()21', '(.)21', '2.()1', '.2()1', '2(.)1', '(2.)1', '.(2)1', '(.2)1',
    ')21(.', '2)1(.', ')12(.', '1)2(.', '21)(.', '12)(.', ')2(1.', '2)(1.',
    ')(21.', '()21.', '2()1.', '(2)1.', ')1(2.', '1)(2.', ')(12.', '()12.',
    '1()2.', '(1)2.', '21().', '12().', '2(1).', '(21).', '1(2).', '(12).',
    ').1(2', '.)1(2', ')1.(2', '1).(2', '.1)(2', '1.)(2', ').(12', '.)(12',
    ')(.12', '().12', '.()12', '(.)12', ')1(.2', '1)(.2', ')(1.2', '()1.2',
    '1().2', '(1).2', '.1()2', '1.()2', '.(1)2', '(.1)2', '1(.)2', '(1.)2',
    '2.1()', '.21()', '21.()', '12.()', '.12()', '1.2()', '2.(1)', '.2(1)',
    '2(.1)', '(2.1)', '.(21)', '(.21)', '21(.)', '12(.)', '2(1.)', '(21.)',
    '1(2.)', '(12.)', '.1(2)', '1.(2)', '.(12)', '(.12)', '1(.2)', '(1.2)']
    >>> perms("")
    []
    '''
    # base case
    if len(perm_string) == 1:
        return [perm_string[0]]
    # Create a empty list to hold the permutations
    perm = []
    # Loop through every character of string
    for value in range(len(perm_string)):
        # hold back a characeter
        rec = perm_string[:value] + perm_string[value + 1:]
        char = perm_string[value]
        # Recurse on shorter string
        new = perms(rec)
        # add the seperated char
        for element in range(len(new)):
            new[element] += char
        # Insert values into the empty string
        perm.extend(new)

    return perm


def all_regex_permutations(s):
    ''' (str) -> set(str)
    The function uses the given string and permutates it
    Checks if each permutation is a regex
    Returns a set of all the valid regex from the permutation
    >>> all_regex_permutations('(0|1)')
    set(['(1|0)', '(0|1)'])
    >>> all_regex_permutations('(0.2*)')
    set(['(0.2*)', '(0*.2)', '(0.2)*', '(2.0*)', '(2.0)*', '(2*.0)'])
    >>> all_regex_permutations('e')
    set(['e'])
    '''
    # Call helper function
    perm = perms(s)
    # Create a new set for the valid regexs
    new = set()
    # Check elements in the permutation list
    for element in perm:
        # If element is a valid regex insert into the newly created
        # set
        if (is_regex(element) == True):
            new.add(element)
    # Return the new set of valid regex
    return new


def build_regex_tree(regex):
    ''' (str) -> set(str)
    The function takes a valid regex string and produces a regex tree in order
    to return the root.
    REQ: String must be a valid regex
    >>> build_regex_tree("((1.(0|1)*).2)")
    DotTree(DotTree(Leaf('1'), StarTree(BarTree(Leaf('0'), Leaf('1')))),
    Leaf('2'))
    >>> build_regex_tree("(1|2)")
    BarTree(Leaf('1'), Leaf('2'))
    >>> build_regex_tree("(1.2)")
    DotTree(Leaf('1'), Leaf('2'))
    >>>build_regex_tree("1****")
    StarTree(StarTree(StarTree(StarTree(Leaf('1')))))
    '''
    # Base Case
    if len(regex) <= 1:
        return Leaf(regex)

    # If Regex obtains a star in as the last element
    elif regex[-1] == "*":
        # Return the StarTree with the rest of the regex
        # without the last element
        return StarTree(build_regex_tree(regex[:-1]))

    # If regex is in the form of ( + r1 + |/. + r2 + )
    else:
        # Create counter variables
        break_location = 0
        bracket_count = 0
        length = len(regex)

        # Find the location to split the regex into r1 and r2 components
        # Search the elements in range of the regex
        # regex[1:-1] Accommodates for the outter brackets
        for element in range(len(regex[1:-1])):

            # If element is a left bracket
            if regex[1:-1][element] == bracket[0]:
                bracket_count += 1

            # If element is a right bracket
            elif regex[1:-1][element] == bracket[1]:
                bracket_count -= 1
            # If there is a set of brackets followed by a |.
            # Is the location where to split for components
            elif (bracket_count == 0 and regex[1:-1][element] in duo_regex):
                # accomadate for the outer bracket
                break_location += element + 1
        # If the node found after the set of brackets is a "|"
        if regex[break_location] == duo_regex[0]:
            # Return BarTree on the left side "r1" and the right side "r2"
            return BarTree(build_regex_tree(regex[1:break_location]),
                           build_regex_tree(regex[break_location + 1:
                                                  length - 1]))
        # If the node found after the set of brackets is a "."
        elif regex[break_location] == duo_regex[1]:
            # Return DotTree on the left side "r1" and the right side "r2"
            return DotTree(build_regex_tree(regex[1:break_location]),
                           build_regex_tree(regex[break_location + 1:
                                                  length - 1]))


def regex_match(r, s):
    '''(RegexTree, str) -> bool
    The function takes a string and checks if it matches the RegexTree root
    >>> regex_match(build_regex_tree('e'), "")
    True
    >>> regex_match(DotTree(Leaf('1'), DotTree(Leaf('1'), Leaf('e'))),
    "122223")
    False
    >>> regex_match(DotTree(Leaf('1'), DotTree(Leaf('2'), Leaf('0'))), "120")
    True
    '''
    # check base cases if r = Leaf with elements from "0,1,2,e"
    # if its a StarTree
    # if its a BarTree
    # if its a DotTree
    # base case
    pass
