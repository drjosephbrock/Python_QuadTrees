from octree_module import Point, OctBox, OctTree
import numpy as np
# %matplotlib qt
import matplotlib.pyplot as plt

boundary = OctBox(0., 0., 0., 4, 4, 4)
qt = OctTree(boundary,4)

# Plot figure
# fig = plt.figure(figsize=(16,16))
fig = plt.figure()
# e1 = [qt.boundary.x - qt.boundary.w, qt.boundary.
ax = plt.axes(projection='3d')

npts = 80
# xpts = np.random.rand(npts)
# ypts = np.random.rand(npts)
# zpts = np.random.rand(npts)
zpts = np.linspace(-1.5, 1.5, npts)
xpts = np.sin(10*zpts)
ypts = np.cos(10*zpts)

# create simple line plot
for i in range(npts):
    x = xpts[i]
    y = ypts[i]
    z = zpts[i]
    pnt = Point(x,y,z)
    qt.insertpoint(pnt)

ax.scatter3D(xpts,ypts,zpts)
qt.show(plt)
plt.show()