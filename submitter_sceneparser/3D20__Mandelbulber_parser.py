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

# TODO: move functionality into a separate file - for easier testing without rr module available
#       update readme

import parser

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
new_job.imageDir = settings_dict["out_file"]
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
