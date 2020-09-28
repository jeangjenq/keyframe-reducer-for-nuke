import reduceKeyframes
m = nuke.menu( 'Animation' )
m.addCommand( 'Reduce Keyframes', "reduceKeyframes.doReduceKeyframes()" )
