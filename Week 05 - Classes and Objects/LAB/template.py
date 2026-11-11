"""
RECORD CHECK  -  my version
===========================

Name  : Jack Waldon
Lane  : Cyber 
Date  :21/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here



class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
            """Return OVER LIMIT, WARNING or OK based on percent()."""
            p = (self.value / self.limit) * 100
            if p >= 100:
                return "OVER LIMIT"
            elif p >= 90:
                return "WARNING"
            else:
                return "OK"

class Checker:
    def __init__(self):
        self.over_limit_count = 0

    def check(self, value, limit):
        if value > limit:
            self.over_limit_count += 1



# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

  # replace with your code

def load_records(path):
    records = []
    with open(path) as i:
        for line in i:
            line = line.strip()
            if line == "":
                continue
            label, value, limit = line.split(",")
            records.append(Record(label, float(value), float(limit)))
    return records


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

records = load_records(r"C:\Uni applications\CST1510\Week 05 - Classes and Objects\LAB\records_for_lab_Mini_project.txt")

for rec in records:
    print("=" * 34)
    print(f"  RECORD CHECK  -  {rec.label}")
    print("=" * 34)

    # your report lines go here

    print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
