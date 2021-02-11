import vrProjector
#
# eq = vrProjector.EquirectangularProjection()
# # eq.loadImage("images/sidebysidefisheye.png")
# # # eq.set_use_bilinear(True)
# # cb = vrProjector.CubemapProjection()
# eq.initImage(2048,1024)
# # cb.reprojectToThis(eq)
# # cb.saveImages("front.png", "right.png", "back.png", "left.png", "top.png", "bottom.png")
#
#
#
# sbs = vrProjector.SideBySideFisheyeProjection()
# # sbs.initImage(2048, 1024)
# sbs.loadImage("images/sidebysidefisheye.png")
# # sbs.reprojectToThisThreaded(eq, 8)
# sbs.reprojectToThis(eq)
# sbs.saveImage("foo.png")
#
# sbs2 = SideBySideFisheyeProjection()
# sbs2.loadImage("foo.png")
#
# eq2 = EquirectangularProjection()
# eq2.initImage(2048,1024)
# eq2.reprojectToThis(sbs2)
# eq2.saveImage("foo2.png")

# eq = EquirectangularProjection()
# eq.loadImage("cuber.jpg")
# eq.set_use_bilinear(True)
# cb = CubemapProjection()
# cb.initImages(256,256)
# cb.reprojectToThis(eq)
# cb.saveImages("front.png", "right.png", "back.png", "left.png", "top.png", "bottom.png")
#


# cb2 = vrProjector.SideBySideFisheyeProjection()
# cb2.loadImage("images/sidebysidefisheye.png", "images/right.png", "images/back.png", "images/left.png", "images/top.png", "images/bottom.png")
# eq2 = vrProjector.EquirectangularProjection()
# eq2.initImage(2048,1024)
# eq2.reprojectToThis(cb2)
# eq2.saveImage("foo.png")
print("Here1")
cb2 = vrProjector.SideBySideFisheyeProjection()
print("Here2")
cb2.loadImage("images/side-by-side-sketch.png")
print("Here3")
eq2 = vrProjector.EquirectangularProjection()
print("Here4")
eq2.initImage(2048,1024)
print("Here5")
eq2.reprojectToThis(cb2)
print("Here6")
eq2.saveImage("foo.png")
