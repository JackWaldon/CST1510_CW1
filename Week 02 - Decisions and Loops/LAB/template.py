"""
RECORD CHECK  -  my version
===========================

Name  : Jack Waldon
Lane  : Cyber     (delete two)
Date  : 20/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

ip = input("Enter in the IP adress of the mashine you are checking:     ")        # replace with an input() call
failed = float(input("Enter the ammount of attempted FAILED logins:     "))        # replace with an input() call, converted with float()
total = float(input("Enter the total amount of logins:                  "))      # replace with an input() call, converted with float()


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

difference =  total - failed   # replace with your calculation
percent_og = (failed/total) * 100      # replace with your calculation
percent_90 = (total/failed) * 90
percent_50 = (total/failed) * 50
percent_30 = (total/failed) * 30
percent_20 = (total/failed) * 20
percent_10 = (total/failed) * 10
percent = 100 - percent_og
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"

if percent > 100: # replace with your if / else (or if / elif / else)
    lable = "error - try again"
elif percent == 100:
    lable = "System Emergancy"
elif percent >= 90:
    lable ="Immediate action needed"
elif percent >= 50:
    lable ="action should be taken"
elif percent >= 30:
    lable ="above average activity"
elif percent >= 20:
    lable ="regular but still need to be sorted"
elif percent >= 10:
    lable ="almost excpetion"
elif percent >= 5:
    lable ="almost excpetional"
elif percent >= 1:
    lable ="practially perfect"
elif percent == 1:
    lable ="exception"
elif percent == 0:
    lable ="flawless"
elif percent < 0:
    lable ="error - try again"





# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print()
print("=" * 68)
print(f"    IP CHECK              -               {ip}")
print("=" * 68)
print(f"    Failed entries                    :{failed}")
print(f"    Total entries                     :{total}")
print(f"    Sucessful entries                 :{difference}")
print(f"    percent that failed entries       :{percent:.2f}")
print(f"    Status                            :{lable}")

# your report lines go here

print("=" * 68)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
