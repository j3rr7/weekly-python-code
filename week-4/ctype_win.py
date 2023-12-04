import ctypes
import sys

# Constants and types
MB_OK = 0x00000000
MB_ICONINFORMATION = 0x00000040
MB_ICONWARNING = 0x00000030
MB_ICONERROR = 0x00000010
MB_YESNOCANCEL = 0x00000003
IDYES = 6
IDNO = 7
IDCANCEL = 2

# Function prototypes
MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox.argtypes = (ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_uint)
MessageBox.restype = ctypes.c_int

# Helper function to show a message box
def show_message_box(message, title, style):
    return MessageBox(None, message, title, style)

# Usage examples
message = "Hello, this is a message box example!"
title = "Message Box Example"

# Show a simple OK message box
show_message_box(message, title, MB_OK | MB_ICONINFORMATION)

# Show a yes/no/cancel message box
response = show_message_box(message, title, MB_YESNOCANCEL | MB_ICONWARNING)
if response == IDYES:
    print("User clicked 'Yes'")
elif response == IDNO:
    print("User clicked 'No'")
elif response == IDCANCEL:
    print("User clicked 'Cancel'")
else:
    print("Unknown response:", response)
