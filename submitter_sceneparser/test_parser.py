import parser
"""
Tests if parser outputs expected results in the provided example scenes. Relies on pytest module.

Run testing with:
    $ pytest
"""

def test_1():
    with open("example_scenes/1.fract") as f:
            content = f.readlines()
    
    expoected_dict = {
        "version" : "2.14",
        "out_folder" : "S:\\020_Preproduction\\050_RND\\450_m2_tests\\aboxmod1_001\\",
        "seq_start" : 0,
        "seq_end" : 1,
        "renderer" : "Flight"
    }
    parsed_dict = parser.parse_mandelbulber(content)

    assert expoected_dict == parsed_dict

def test_2():
    with open("example_scenes/2.fract") as f:
            content = f.readlines()
    
    expoected_dict = {
        "version" : "2.14",
        "out_folder" : "S:\\020_Preproduction\\050_RND\\450_m2_tests\\aboxmod1_001_anim\\",
        "seq_start" : 0,
        "seq_end" : 600,
        "renderer" : "Keyframe"
    }
    parsed_dict = parser.parse_mandelbulber(content)

    assert expoected_dict == parsed_dict

def test_3():
    with open("example_scenes/3.fract") as f:
            content = f.readlines()
    
    expoected_dict = {
        "version" : "2.14",
        "out_folder" : "S:\\020_Preproduction\\050_RND\\450_m2_tests\\aboxmod1_001_anim\\",
        "seq_start" : 0,
        "seq_end" : 61,
        "renderer" : "Flight"
    }
    parsed_dict = parser.parse_mandelbulber(content)

    assert expoected_dict == parsed_dict