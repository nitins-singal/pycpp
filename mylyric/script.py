import mylyric.lib.lyric_module as m

def calculate():
    import debugpy
    debugpy.listen(5678)
    debugpy.wait_for_client()
    print("Visual Debugging inside container with debugpy and gdb")
    a = 10
    b = 20

    result = m.simple_cpp_function(a, b)

    print(f"a = {a}, b = {b}, result = {result}")

    # Create an instance of the Calculator class
    calc = m.Calculator()

    # Call the add method
    result_add = calc.addnum(5, 3)
    print("Addition Result:", result_add)

    # Call the multiply method
    result_multiply = calc.multnum(5, 3)
    print("Multiplication Result:", result_multiply)


if __name__ == "__main__":
    calculate()