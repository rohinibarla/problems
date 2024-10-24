
import check50

@check50.check()
def exists():
    """q6.py exists"""
    check50.exists("q6.py")
    check50.include("../../q6/1.in", "../../q6/1.out")
    check50.include("../../q6/1.in", "../../q6/1.out")

@check50.check(exists)
def q6_2():
    """q6_1"""
    test_input_output("1.in", "1.out")


@check50.check(exists)
def q6_1():
    """q6_2"""
    test_input_output("1.in", "1.out")


# Helpers
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    executable = "python3 q6.py"
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()