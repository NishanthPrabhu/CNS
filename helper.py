__author__ = 'nishanth'

# Helper Functions


# Check if string entered is a number. True if number, False if not
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
