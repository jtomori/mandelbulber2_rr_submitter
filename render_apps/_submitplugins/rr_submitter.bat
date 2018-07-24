@echo off
rem RR Submitter for Mandelbulber 2, in Keyframe mode

%RR_ROOT%\bin\win64\rrStartlocal rrSubmitter "%~1" -Software "Mandelbulber" -Version "2.14" -Renderer "Keyframe" -Layer "Scene" -ImageFileName "frame_%%07d" -ImageExtension ".exr" -SeqStart 0 "SequenceDivide=1~1" "SeqDivMIN=1~10" "SeqDivMAX=1~30" "PPSequenceCheck=1~0" "PPCreateSmallVideo=1~0" "RenderPreviewFirst=1~0"