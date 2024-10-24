
import check50

@check50.check()
def exists():
    """q8.py exists"""
    check50.exists("q8.py")
    check50.include("../../q8/1.in", "../../q8/1.out")
    check50.include("../../q8/1.in", "../../q8/1.out")

@check50.check(exists)
def q8_2():
    """q8_1"""
    test_input_output("1.in", "1.out")


@check50.check(exists)
def q8_1():
    """q8_2"""
    test_input_output("1.in", "1.out")


# Helpers
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    executable = "python3 q8.py"
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()