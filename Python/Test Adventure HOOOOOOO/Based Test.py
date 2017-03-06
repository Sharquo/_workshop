from automa.api import *
import difflib

# Uses Automa to run VClay and then output the three main curves to ASCII.
start("Interactive Petrophysics")
wait_until(Text("Interpretation").exists)
click("Interpretation", MenuItem("Clay Volume Ctrl+Alt+C"))
click("Output Set", MenuItem("Create New Set"))
write("VCL")
click("Update Sets")
click("Close")
click("Run")
click("No")
click("Input / Output", MenuItem("Save Data"), MenuItem("ASCII Write"))
write("C:\Test Outputs")
click("BVW")
scroll_down(51)
drag("VCL:VCLGR", to="Curve Name Output Name")  # Why are these operations so slow?
click("OK")
click("Close")

# Beginning the diff sequence.
diff = difflib.context_diff(open("C:\Test Outputs\ASCOut_W1.asc").readlines(), open("C:\Test Outputs\Base VCL Test.asc").readlines())

with open("C:\Test Outputs\Results.txt", 'w') as file:
    for line in diff:
        file.write(line)



