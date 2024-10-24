
import check50

@check50.check()
def exists():
    """q3.py exists"""
    check50.exists("q3.py")
    check50.include("../../q3/1.in", "../../q3/1.out")
    check50.include("../../q3/1.in", "../../q3/1.out")

@check50.check(exists)
def q3_2():
    """q3_1"""
    test_input_output("1.in", "1.out")


@check50.check(exists)
def q3_1():
    """q3_2"""
    test_input_output("1.in", "1.out")


# Helpers
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    executable = "python3 q3.py"
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()