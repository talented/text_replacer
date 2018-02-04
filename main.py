"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    longone = 0
    shortone = 0
    count = 0

    if len(line1) > len(line2):
        longone, shortone = len(line1), len(line2)
    elif len(line1) < len(line2):
        longone, shortone = len(line2), len(line1)
    else:
        for i in range(0, len(line1)):
            if not line1[i] == line2[i]:
                return i

    for i in range(0, longone):
        if count == shortone:
            return i
        elif not line1[i] == line2[i]:
            return i
        count += 1

    return IDENTICAL

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index of first difference between the lines
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if idx != singleline_diff(line1, line2):
        return ""

    if ("\n" in line1) or ("\r" in line1) or ("\n" in line2) or ("\r" in line2) or not (isinstance(idx, int)) or (idx < 0):
        return ""

    template = "=" * idx + "^"

    return (line1+"\n"+template+"\n"+line2+"\n")

# first_line = "abcd"
# second_line = "abef"
# print(singleline_diff_format(first_line, second_line, singleline_diff(first_line, second_line)))
# # print(singleline_diff("abc", "abcdefg"))

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if lines1 == lines2:
        return (IDENTICAL, IDENTICAL)

    if len(lines1) == len(lines2):
        for item in lines1:
            if not item == lines2[lines1.index(item)]:
                res = singleline_diff(item, lines2[lines1.index(item)])
                return(lines1.index(item), res)
    elif len(lines1) > len(lines2):
        return (len(lines2), 0)
    else:
        return (len(lines1), 0)

# print(multiline_diff(["a", "b", "cap"], ["a", "b", "cak"]))
# print(multiline_diff(['line1', 'line2'], ['line1', 'line2', 'line3']))


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    return []


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    return ""
