import matplotlib as plt
from stl import mesh
from octree_module import Point, OctBox, OctTree
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from tqdm import trange

# Plot figure
fig = plt.figure(figsize=(8,8))
# ax = plt.axes(projection='3d')
ax = mplot3d.Axes3D(fig,auto_add_to_figure=False)
fig.add_axes(ax)
ax.view_init(elev=0., azim=90)

m1 = mesh.Mesh.from_file('surf.stl')
ax.add_collection3d(mplot3d.art3d.Poly3DCollection(m1.vectors))

ax.set_xlim3d(-0.5, 0.5)
ax.set_ylim3d(-0.5, 0.5)
ax.set_zlim3d(-0.5, 0.5)
# Auto scale to the mesh size
# scale = m1.points.flatten()
# print(scale)
# ax.auto_scale_xyz(-0.5, 0.5, 0.5)

boundary = OctBox(0., 0., 0., 1, 1, 1)
qt = OctTree(boundary,100)

print(len(m1.points))
print(np.shape(m1.points))
points = m1.points.reshape([-1, 3])
print(np.shape(points))

for i in trange(np.shape(points)[0]):
    pnt = Point(points[i,0],points[i,1],points[i,2])
    qt.insertpoint(pnt)
qt.show(plt)
plt.show()