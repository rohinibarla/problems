
import check50

@check50.check()
def exists():
    """q0.py exists"""
    check50.exists("q0.py")
    check50.include("../../q0/1.in", "../../q0/1.out")
    check50.include("../../q0/2.in", "../../q0/2.out")

@check50.check(exists)
def q0_2():
    """q0_1"""
    test_input_output("1.in", "1.out")


@check50.check(exists)
def q0_1():
    """q0_2"""
    test_input_output("1.in", "1.out")


# Helpers
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    executable = "python3 q0.py"
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()