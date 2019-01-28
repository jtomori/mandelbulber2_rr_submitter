def parse_mandelbulber(content):
    """
    Parses Mandelbulber2 .fract file and outputs a dictionoary containing needed info for RoyalRender scene parser:
    
    out_dict = {
        "version" : "",
        "out_folder" : "",
        "seq_start" : 0,
        "seq_end" : 0,
        "renderer" : ""
    }

    This parser is deveoped in parser.py file and then merged with 3D20__Mandelbulber.py file, which is used by RR
    """
    
    # init dict
    out_dict = {
        "version" : "",
        "out_folder" : "",
        "seq_start" : 0,
        "seq_end" : 0,
        "renderer" : ""
    }

    # check if it is a valid Mandelbulber settings file
    if content[0] != "# Mandelbulber settings file\n":
        rr.returnFromPlugin(rrGlobal.pluginReturn.unsupportedFormat)  
        raise rrCleanExit() #I do not want any traceback info
    
    renderer = ""
    # iterate over lines
    for n, line in enumerate(content):
        # strip newline characters
        line = line.replace("\n", "")
        content[n] = line

        if line.startswith("# version "):
            version = line
            version = version.split(" ")[-1]

            out_dict["version"] = version
        
        elif line.startswith("anim_flight_dir ") and renderer != "Keyframe":
            out = line
            out = out.replace(";", "")
            out = out.split(" ")[-1]

            renderer = "Flight"
            out_dict["renderer"] = "Flight"
            out_dict["out_folder"] = out
        
        elif line.startswith("flight_last_to_render ") and renderer != "Keyframe":
            frame = line
            frame = frame.replace(";", "")
            frame = frame.split(" ")[-1]

            out_dict["seq_end"] = int(frame)
        
        elif line.startswith("anim_keyframe_dir "):
            out = line
            out = out.replace(";", "")
            out = out.split(" ")[-1]

            renderer = "Keyframe"
            out_dict["renderer"] = "Keyframe"
            out_dict["out_folder"] = out
        
        elif line.startswith("keyframe_last_to_render ") and renderer != "Flight":
            frame = line
            frame = frame.replace(";", "")
            frame = frame.split(" ")[-1]

            renderer = "Keyframe"
            out_dict["seq_end"] = int(frame)

    return out_dict
