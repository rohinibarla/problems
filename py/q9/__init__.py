
import check50

@check50.check()
def exists():
    """q9.py exists"""
    check50.exists("q9.py")
    check50.include("../../q9/1.in", "../../q9/1.out")
    check50.include("../../q9/1.in", "../../q9/1.out")

@check50.check(exists)
def q9_2():
    """q9_1"""
    test_input_output("1.in", "1.out")


@check50.check(exists)
def q9_1():
    """q9_2"""
    test_input_output("1.in", "1.out")


# Helpers
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    executable = "python3 q9.py"
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()