# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
import glob
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Unstructured Grid Reader'
full3d_04150200vtu = XMLUnstructuredGridReader(FileName=glob.glob('./vtu_files/*.vtu'))
full3d_04150200vtu.PointArrayStatus = ['f0501', 'f0001']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [2457, 925]

# show data in view
full3d_04150200vtuDisplay = Show(full3d_04150200vtu, renderView1)

# get color transfer function/color map for 'f0001'
f0001LUT = GetColorTransferFunction('f0001')
f0001LUT.RGBPoints = [-302.673369835994, 0.231373, 0.298039, 0.752941, -23.358833573780544, 0.865003, 0.865003, 0.865003, 255.9557026884329, 0.705882, 0.0156863, 0.14902]
f0001LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'f0001'
f0001PWF = GetOpacityTransferFunction('f0001')
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]
f0001PWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
full3d_04150200vtuDisplay.Representation = 'Surface'
full3d_04150200vtuDisplay.ColorArrayName = ['POINTS', 'f0001']
full3d_04150200vtuDisplay.LookupTable = f0001LUT
full3d_04150200vtuDisplay.OSPRayScaleArray = 'f0001'
full3d_04150200vtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
full3d_04150200vtuDisplay.SelectOrientationVectors = 'None'
full3d_04150200vtuDisplay.ScaleFactor = 0.22222036782307916
full3d_04150200vtuDisplay.SelectScaleArray = 'f0001'
full3d_04150200vtuDisplay.GlyphType = 'Arrow'
full3d_04150200vtuDisplay.GlyphTableIndexArray = 'f0001'
full3d_04150200vtuDisplay.GaussianRadius = 0.011111018391153957
full3d_04150200vtuDisplay.SetScaleArray = ['POINTS', 'f0001']
full3d_04150200vtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
full3d_04150200vtuDisplay.OpacityArray = ['POINTS', 'f0001']
full3d_04150200vtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
full3d_04150200vtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
full3d_04150200vtuDisplay.SelectionCellLabelFontFile = ''
full3d_04150200vtuDisplay.SelectionPointLabelFontFile = ''
full3d_04150200vtuDisplay.PolarAxes = 'PolarAxesRepresentation'
full3d_04150200vtuDisplay.ScalarOpacityFunction = f0001PWF
full3d_04150200vtuDisplay.ScalarOpacityUnitDistance = 0.011513878115196685

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
full3d_04150200vtuDisplay.DataAxesGrid.XTitleFontFile = ''
full3d_04150200vtuDisplay.DataAxesGrid.YTitleFontFile = ''
full3d_04150200vtuDisplay.DataAxesGrid.ZTitleFontFile = ''
full3d_04150200vtuDisplay.DataAxesGrid.XLabelFontFile = ''
full3d_04150200vtuDisplay.DataAxesGrid.YLabelFontFile = ''
full3d_04150200vtuDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
full3d_04150200vtuDisplay.PolarAxes.PolarAxisTitleFontFile = ''
full3d_04150200vtuDisplay.PolarAxes.PolarAxisLabelFontFile = ''
full3d_04150200vtuDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
full3d_04150200vtuDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
full3d_04150200vtuDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip1 = Clip(Input=full3d_04150200vtu)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'f0001']
clip1.Value = -23.358833573780544

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [0.0, 0.0, 0.08551762525203843]
clip1.ClipType.Normal = [0.0, 0.0, 1.0]

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [0.0, 0.0, 0.08551762525203843]
clip1.ClipType.Normal = [0.0, 0.0, 1.0]

# show data in view
clip1Display = Show(clip1, renderView1)

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'f0001']
clip1Display.LookupTable = f0001LUT
clip1Display.OSPRayScaleArray = 'f0001'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 0.22222036782307916
clip1Display.SelectScaleArray = 'f0001'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'f0001'
clip1Display.GaussianRadius = 0.011111018391153957
clip1Display.SetScaleArray = ['POINTS', 'f0001']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'f0001']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.SelectionCellLabelFontFile = ''
clip1Display.SelectionPointLabelFontFile = ''
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = f0001PWF
clip1Display.ScalarOpacityUnitDistance = 0.012029766189750477

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip1Display.DataAxesGrid.XTitleFontFile = ''
clip1Display.DataAxesGrid.YTitleFontFile = ''
clip1Display.DataAxesGrid.ZTitleFontFile = ''
clip1Display.DataAxesGrid.XLabelFontFile = ''
clip1Display.DataAxesGrid.YLabelFontFile = ''
clip1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip1Display.PolarAxes.PolarAxisTitleFontFile = ''
clip1Display.PolarAxes.PolarAxisLabelFontFile = ''
clip1Display.PolarAxes.LastRadialAxisTextFontFile = ''
clip1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(full3d_04150200vtu, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
f0001LUT.ApplyPreset('Inferno (matplotlib)', True)

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -198.49659729003906, 0.20108695328235626, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -198.49659729003906, 0.20652174949645996, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -198.49659729003906, 0.2445652186870575, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -198.49659729003906, 0.66847825050354, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -198.49659729003906, 0.864130437374115, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -198.49659729003906, 0.9293478727340698, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -198.49659729003906, 0.97826087474823, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -198.49659729003906, 1.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -187.9279327392578, 1.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.016304347664117813, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.005434782709926367, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.021739130839705467, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.07065217196941376, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.125, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.135869562625885, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.15217392146587372, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.16304348409175873, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.17934782803058624, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.1467391401529312, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -0.7117094397544861, 0.989130437374115, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -0.7117094397544861, 0.9836956858634949, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -0.7117094397544861, 0.967391312122345, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -0.7117094397544861, 0.6630434989929199, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -6.750942707061768, 0.45652174949645996, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -9.770559310913086, 0.364130437374115, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -9.770559310913086, 0.28260868787765503, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -12.790175437927246, 0.21739131212234497, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -12.790175437927246, 0.15760870277881622, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -12.790175437927246, 0.10326087474822998, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -15.809792518615723, 0.05434782803058624, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -15.809792518615723, 0.043478261679410934, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -15.809792518615723, 0.02717391401529312, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -15.809792518615723, 0.021739130839705467, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -17.31960105895996, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -20.339218139648438, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -17.31960105895996, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.05978260934352875, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.07065217196941376, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.08695652335882187, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.10326087474822998, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.11413043737411499, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.09239130467176437, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.08152174204587936, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.07065217196941376, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -252.84970092773438, 0.44565218687057495, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -252.84970092773438, 0.44021740555763245, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -252.84970092773438, 0.4184782803058624, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -240.77122497558594, 0.25, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -228.69276428222656, 0.1467391401529312, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -227.18295288085938, 0.07608696073293686, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -221.1437225341797, 0.010869565419852734, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -212.08486938476562, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -209.0652618408203, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -206.04563903808594, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -203.02601623535156, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -195.4769744873047, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -192.45736694335938, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [-302.673369835994, 0.0, 0.5, 0.0, -190.9475555419922, 0.0, 0.5, 0.0, -183.3985137939453, 1.0, 0.5, 0.0, -18.829408645629883, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Rescale transfer function
f0001LUT.RescaleTransferFunction(0.0255955702688, 255.955702688)

# Rescale transfer function
f0001PWF.RescaleTransferFunction(0.0255955702688, 255.955702688)

# convert to log space
f0001LUT.MapControlPointsToLogSpace()

# Properties modified on f0001LUT
f0001LUT.UseLogScale = 1

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1.ClipType)

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0

# hide color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, False)

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 51.903324127197266, 0.02717391401529312, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 50.51991653442383, 0.09782608598470688, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 37.377559661865234, 0.39673912525177, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 37.377559661865234, 0.42934784293174744, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 37.377559661865234, 0.44021740555763245, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 35.302452087402344, 0.46739131212234497, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 29.76882553100586, 0.5271739363670349, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 24.235200881958008, 0.592391312122345, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 22.851795196533203, 0.60326087474823, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 22.851795196533203, 0.6086956858634949, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 20.77668571472168, 0.6195652484893799, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 20.77668571472168, 0.625, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 20.08498191833496, 0.6630434989929199, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 18.701576232910156, 0.6902173757553101, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 17.31817054748535, 0.7445652484893799, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 15.934764862060547, 0.79347825050354, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 15.243062019348145, 0.820652186870575, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 15.243062019348145, 0.842391312122345, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 13.85965633392334, 0.85326087474823, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 13.85965633392334, 0.8695652484893799, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 12.476249694824219, 0.875, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 12.476249694824219, 0.907608687877655, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 11.092844009399414, 0.9347826242446899, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 10.401141166687012, 0.9510869979858398, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 9.01773452758789, 0.9510869979858398, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 5.559219837188721, 0.967391312122345, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 4.867516994476318, 0.967391312122345, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 4.175813674926758, 0.967391312122345, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 4.175813674926758, 0.97826087474823, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 4.175813674926758, 0.9945652484893799, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 4.175813674926758, 1.0, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 3.4841108322143555, 1.0, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 2.792407751083374, 1.0, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 2.1007046699523926, 1.0, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 3.4841108322143555, 1.0, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# Properties modified on f0001PWF
f0001PWF.Points = [0.02559557026884329, 0.0, 0.5, 0.0, 0.02559557026884329, 1.0, 0.5, 0.0, 54.67013196254605, 1.0, 0.5, 0.0, 130.06575811321886, 0.0, 0.5, 0.0, 255.9557026884329, 1.0, 0.5, 0.0]

# change representation type
clip1Display.SetRepresentationType('Volume')

# current camera placement for renderView1
renderView1.CameraPosition = [-1.8653783685856458, -6.4572079936206634, 3.1801154010943287]
renderView1.CameraViewUp = [-0.2599632209950631, 0.4860258166435079, 0.834384820862582]
renderView1.CameraParallelScale = 1.9244776439536024

# save screenshot
# SaveScreenshot('/home/roldan/Desktop/clip_transfer_313.png', renderView1, ImageResolution=[900, 900])

SaveAnimation('./png_transfer/clip_run_.png', renderView1, ImageResolution=[900, 900],
    FrameWindow=[0, 1499],
    # PNG options
    SuffixFormat='%04d')


#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-1.8653783685856458, -6.4572079936206634, 3.1801154010943287]
renderView1.CameraViewUp = [-0.2599632209950631, 0.4860258166435079, 0.834384820862582]
renderView1.CameraParallelScale = 1.9244776439536024

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
