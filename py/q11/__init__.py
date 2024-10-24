
import check50

@check50.check()
def exists():
    """q11.py exists"""
    check50.exists("q11.py")
    check50.include("../../q11/1.in", "../../q11/1.out")
    check50.include("../../q11/1.in", "../../q11/1.out")

@check50.check(exists)
def q11_2():
    """q11_1"""
    test_input_output("1.in", "1.out")


@check50.check(exists)
def q11_1():
    """q11_2"""
    test_input_output("1.in", "1.out")


# Helpers
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    executable = "python3 q11.py"
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()