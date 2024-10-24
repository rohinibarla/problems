
import check50

@check50.check()
def exists():
    """q1.py exists"""
    check50.exists("q1.py")
    check50.include("../../q1/1.in", "../../q1/1.out")
    check50.include("../../q1/1.in", "../../q1/1.out")

@check50.check(exists)
def q1_2():
    """q1_1"""
    test_input_output("1.in", "1.out")


@check50.check(exists)
def q1_1():
    """q1_2"""
    test_input_output("1.in", "1.out")


# Helpers
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    executable = "python3 q1.py"
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()