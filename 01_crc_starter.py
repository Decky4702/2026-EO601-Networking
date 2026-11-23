# ============================================================
# EO601 Networking - Lecture 3: Solving Real Network Problems
# STUDENT TASK: Find interfaces with CRC errors
#
# Each dictionary is one switch interface.
# Complete the loop so that Python reports ONLY the
# interfaces where CRC errors > 0.
#
# Expected output:
# WARNING: SW1 Gi0/2 CRC Errors: 18
# WARNING: SW2 Gi0/2 CRC Errors: 43
# ============================================================

interfaces = [
    {"device": "SW1", "interface": "Gi0/1", "crc_errors": 0},
    {"device": "SW1", "interface": "Gi0/2", "crc_errors": 18},
    {"device": "SW2", "interface": "Gi0/1", "crc_errors": 0},
    {"device": "SW2", "interface": "Gi0/2", "crc_errors": 43}
]

for interface in interfaces:

    # What should Python check?

    # What should Python print?

    pass   # delete this line when you add your code
