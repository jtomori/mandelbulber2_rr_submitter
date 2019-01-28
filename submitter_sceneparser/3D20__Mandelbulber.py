# -*- coding: cp1252 -*-
#
# These lines are just information lines for the plugin loader
# rrPluginName:		Mandelbulber2 Scene parser
# rrPluginAuthor:	Juraj Tomori
# rrPluginVersion:	%rrVersion%
# rrPluginType:		Scene Parser Plugin
# rrRRversion:		8.0
#
#
#
# This setting is important for scene parser job plugins and need to be set.
# 
# rrSupportedFileExt: *.fract;
#
#
#
######################################################################

# TODO:
#       update readme

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

    This parser is deveoped in m2_parser.py file and then merged with 3D20__Mandelbulber.py file, which is used by RR
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

            out_dict["seq_end"] = int(frame)-1
        
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
            out_dict["seq_end"] = int(frame)-1

    return out_dict


# load file, check if loads ok
scene_file = rr.sceneFileToLoad()

try:
    with open(scene_file, "r") as f:
        content = f.readlines()
except Exception as e:
    rrGlobal.writeLog(rrGlobal.logLvL.progress, "Error loading file: "+str(e),"") # info messages will only be shown in the small log window of the rrSubmitter, but do not show a dialog window. As we do not want two dialog windows, see next lint
    rr.returnFromPlugin(rrGlobal.pluginReturn.fileFailedToOpen)  # this shows a general message window
    raise rrCleanExit() # I do not want any traceback info

settings_dict = parse_mandelbulber(content)

# create a render app
render_app = rrJob._RenderAppBasic()
render_app.clear()
render_app.name = "Mandelbulber"
render_app.rendererName = settings_dict["renderer"]
render_app.setVersionBoth(settings_dict["version"])

# create a job
new_job = rr.getNewJob()
new_job.sceneName = scene_file
new_job.renderApp = render_app
new_job.imageDir = settings_dict["out_folder"]
new_job.imageFileName = "frame_"
new_job.imageFramePadding = 7
new_job.imageExtension = ".exr"
new_job.imageSingleOutputFile = False
new_job.splitImageFileInto_DirFileExt(False)
new_job.uiIsChecked = True
new_job.seqStart = settings_dict["seq_start"]
new_job.seqEnd = settings_dict["seq_end"]
new_job.layer = "Scene"
new_job.customSet_Str("rrSubmitterParameter", "SequenceDivide=1~1")
new_job.customSet_Str("rrSubmitterParameter", "SeqDivMIN=1~1")
new_job.customSet_Str("rrSubmitterParameter", "SeqDivMAX=1~5")
new_job.customSet_Str("rrSubmitterParameter", "PPSequenceCheck=1~0")
new_job.customSet_Str("rrSubmitterParameter", "PPCreateSmallVideo=1~0")
new_job.customSet_Str("rrSubmitterParameter", "RenderPreviewFirst=1~0")
#new_job.customSet_Str("rrSubmitterParameter", "CompanyProjectName=0~strandsofmind")

rr.jobAll_set(999,new_job)
rr.returnFromPlugin(rrGlobal.pluginReturn.successful)
