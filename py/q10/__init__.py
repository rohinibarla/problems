
import check50

@check50.check()
def exists():
    """q10.py exists"""
    check50.exists("q10.py")
    check50.include("../../q10/1.in", "../../q10/1.out")
    check50.include("../../q10/1.in", "../../q10/1.out")

@check50.check(exists)
def q10_2():
    """q10_1"""
    test_input_output("1.in", "1.out")


@check50.check(exists)
def q10_1():
    """q10_2"""
    test_input_output("1.in", "1.out")


# Helpers
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    executable = "python3 q10.py"
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()