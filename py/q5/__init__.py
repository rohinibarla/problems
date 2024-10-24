
import check50

@check50.check()
def exists():
    """q5.py exists"""
    check50.exists("q5.py")
    check50.include("../../q5/1.in", "../../q5/1.out")
    check50.include("../../q5/1.in", "../../q5/1.out")

@check50.check(exists)
def q5_2():
    """q5_1"""
    test_input_output("1.in", "1.out")


@check50.check(exists)
def q5_1():
    """q5_2"""
    test_input_output("1.in", "1.out")


# Helpers
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    executable = "python3 q5.py"
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()