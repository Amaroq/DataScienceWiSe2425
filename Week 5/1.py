import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

# all rectangles
"""
plt.rc("axes", axisbelow=True)
plt.xticks(np.arange(-1, 14, step=1))
plt.yticks(np.arange(-1, 14, step=1))
plt.grid(linestyle="-", linewidth=1)

rectangles = [Rectangle((x,y), xW, yW, facecolor="white", edgecolor="black", fill=True, linewidth=2.0) for (x,y,xW,yW) in [
    (10, 0, 2, 3),
    (7, 6, 1, 3),
    (8, 3, 3, 4),
    (4, 1, 2, 2),
    (2, 9, 2, 2),
    (4, 5, 2, 5),
    (9, 9, 3, 3)
]]
for i in range(len(rectangles)):
    r = rectangles[i]
    rx, ry = r.get_xy()
    cx = rx + r.get_width()/2.0
    cy = ry + r.get_height()/2.0

    plt.gca().add_patch(r)
    plt.annotate("R" + str(i + 1), (cx,cy))

plt.title("All rectangles")
plt.show()
"""

# first 3 iterations (there will be a split)
"""
plt.rc("axes", axisbelow=True)
plt.xticks(np.arange(-1, 14, step=1))
plt.yticks(np.arange(-1, 14, step=1))
plt.grid(linestyle="-", linewidth=1)

rectangles = [Rectangle((x,y), xW, yW, facecolor="white", edgecolor="black", fill=True, linewidth=2.0) for (x,y,xW,yW) in [
    (10, 0, 2, 3),
    (7, 6, 1, 3),
    (8, 3, 3, 4),
]]

# add the tree rectangle
rectangles += [Rectangle((7,0), 5, 9, edgecolor="green", facecolor=("green", 0.2), fill=True, linewidth=2.0, linestyle="--")]
for i in range(len(rectangles)):
    r = rectangles[i]
    rx, ry = r.get_xy()
    cx = rx + r.get_width()/2.0
    cy = ry + r.get_height()/2.0

    plt.gca().add_patch(r)
    if (i != 3):
        plt.annotate("R" + str(i + 1), (cx,cy))
    else:
        plt.annotate("T0", (cx,cy), color="green")



plt.title("First 3 iterations, just before the split.\nThe root T0 was scaled in the last insertions.")
plt.show()
"""

# 4th iteration (there was a split)
"""
plt.rc("axes", axisbelow=True)
plt.xticks(np.arange(-1, 14, step=1))
plt.yticks(np.arange(-1, 14, step=1))
plt.grid(linestyle="-", linewidth=1)

rectangles = [Rectangle((x,y), xW, yW, facecolor="white", edgecolor="black", fill=True, linewidth=2.0) for (x,y,xW,yW) in [
    (10, 0, 2, 3),
    (7, 6, 1, 3),
    (8, 3, 3, 4),
    (4, 1, 2, 2),
]]

# add the tree rectangles
rectangles += [
    Rectangle((4,0), 8, 9, edgecolor="green", facecolor=("green", 0.2), fill=True, linewidth=2.0, linestyle="--"),
    Rectangle((4,1), 4, 8, edgecolor="orange", facecolor=("orange", 0.2), fill=True, linewidth=2.0, linestyle="--"),
    Rectangle((8,0), 4, 7, edgecolor="orange", facecolor=("orange", 0.2), fill=True, linewidth=2.0, linestyle="--")
    ]
for i in range(len(rectangles)):
    r = rectangles[i]
    rx, ry = r.get_xy()
    cx = rx + r.get_width()/2.0
    cy = ry + r.get_height()/2.0

    plt.gca().add_patch(r)
    if (i < 4):
        plt.annotate("R" + str(i + 1), (cx,cy))
    else:
        c = "green"
        if (i - 4 > 0):
            c = "orange"
        plt.annotate("T" + str(i - 4), (cx,cy), color=c)



plt.title("4. Iteration, after splitting.\nR3 and R4 had the MBR with largest dead space. After that we had to add R1 to T2 and then R2 to T1")
plt.show()
"""

"""
# 5th iteration (there will be a split)
plt.rc("axes", axisbelow=True)
plt.xticks(np.arange(-1, 14, step=1))
plt.yticks(np.arange(-1, 14, step=1))
plt.grid(linestyle="-", linewidth=1)

rectangles = [Rectangle((x,y), xW, yW, facecolor="white", edgecolor="black", fill=True, linewidth=2.0) for (x,y,xW,yW) in [
    (10, 0, 2, 3),
    (7, 6, 1, 3),
    (8, 3, 3, 4),
    (4, 1, 2, 2),
    (2, 9, 2, 2),
]]

# add the tree rectangles
rectangles += [
    Rectangle((2,0), 10, 11, edgecolor="green", facecolor=("green", 0.2), fill=True, linewidth=2.0, linestyle="--"),
    Rectangle((2,1), 6, 10, edgecolor="orange", facecolor=("orange", 0.2), fill=True, linewidth=2.0, linestyle="--"),
    Rectangle((8,0), 4, 7, edgecolor="orange", facecolor=("orange", 0.2), fill=True, linewidth=2.0, linestyle="--")
    ]
for i in range(len(rectangles)):
    r = rectangles[i]
    rx, ry = r.get_xy()
    cx = rx + r.get_width()/2.0
    cy = ry + r.get_height()/2.0

    plt.gca().add_patch(r)
    if (i < 5):
        plt.annotate("R" + str(i + 1), (cx,cy))
    else:
        c = "green"
        if (i - 5 > 0):
            c = "orange"
        plt.annotate("T" + str(i - 5), (cx,cy), color=c)



plt.title("Iteration 5: R5 -> T1, after this we will have to split since R6 should also go into T1")
plt.show()
"""

"""
# 6th iteration (there was a split)
plt.rc("axes", axisbelow=True)
plt.xticks(np.arange(-1, 14, step=1))
plt.yticks(np.arange(-1, 14, step=1))
plt.grid(linestyle="-", linewidth=1)

rectangles = [Rectangle((x,y), xW, yW, facecolor="white", edgecolor="black", fill=True, linewidth=2.0) for (x,y,xW,yW) in [
    (10, 0, 2, 3),
    (7, 6, 1, 3),
    (8, 3, 3, 4),
    (4, 1, 2, 2),
    (2, 9, 2, 2),
    (4, 5, 2, 5)
]]

# add the tree rectangles
rectangles += [
    Rectangle((2,0), 10, 11, edgecolor="green", facecolor=("green", 0.2), fill=True, linewidth=2.0, linestyle="--"),
    Rectangle((8,0), 4, 7, edgecolor="orange", facecolor=("orange", 0.2), fill=True, linewidth=2.0, linestyle="--"),
    Rectangle((2,6), 6, 5, edgecolor="purple", facecolor=("purple", 0.2), fill=True, linewidth=2.0, linestyle="--"),
    Rectangle((4,1), 2, 9, edgecolor="purple", facecolor=("purple", 0.2), fill=True, linewidth=2.0, linestyle="--")
    ]
for i in range(len(rectangles)):
    r = rectangles[i]
    rx, ry = r.get_xy()
    cx = rx + r.get_width()/2.0
    cy = ry + r.get_height()/2.0

    plt.gca().add_patch(r)
    if (i < 6):
        plt.annotate("R" + str(i + 1), (cx,cy))
    else:
        c = ["green", "orange", "purple", "purple"][i-6]
        txt = "T" + str(i - 6 + int(i == 7))
        if i in [8,9]:
            txt = "T1" + str(i - 7)
        plt.annotate(txt, (cx,cy), color=c)



plt.title("Iteration 6: R6 -> T1, we had to split.\nR5 and R4 form T11 and T12 which are additionally filled with R2 and R6 accordingly.\nAs you can see, T11 and T12 overlap on parts of R6")
plt.show()
"""

# last iteration
plt.rc("axes", axisbelow=True)
plt.xticks(np.arange(-1, 14, step=1))
plt.yticks(np.arange(-1, 14, step=1))
plt.grid(linestyle="-", linewidth=1)

rectangles = [Rectangle((x,y), xW, yW, facecolor="white", edgecolor="black", fill=True, linewidth=2.0) for (x,y,xW,yW) in [
    (10, 0, 2, 3),
    (7, 6, 1, 3),
    (8, 3, 3, 4),
    (4, 1, 2, 2),
    (2, 9, 2, 2),
    (4, 5, 2, 5),
    (9, 9, 3, 3)
]]

# add the tree rectangles
rectangles += [
    Rectangle((2,0), 10, 12, edgecolor="green", facecolor=("green", 0.2), fill=True, linewidth=2.0, linestyle="--"),
    Rectangle((8,0), 4, 12, edgecolor="orange", facecolor=("orange", 0.2), fill=True, linewidth=2.0, linestyle="--"),
    Rectangle((2,6), 6, 5, edgecolor="purple", facecolor=("purple", 0.2), fill=True, linewidth=2.0, linestyle="--"),
    Rectangle((4,1), 2, 9, edgecolor="purple", facecolor=("purple", 0.2), fill=True, linewidth=2.0, linestyle="--")
    ]
for i in range(len(rectangles)):
    r = rectangles[i]
    rx, ry = r.get_xy()
    cx = rx + r.get_width()/2.0
    cy = ry + r.get_height()/2.0

    plt.gca().add_patch(r)
    if (i < 7):
        plt.annotate("R" + str(i + 1), (cx,cy))
    else:
        c = ["green", "orange", "purple", "purple"][i-7]
        txt = "T" + str(i - 7 + int(i == 8))
        if i in [9,10]:
            txt = "T1" + str(i - 8)
        plt.annotate(txt, (cx,cy), color=c)



plt.title("Iteration 7: R7 -> T2 and not to T11 or T12, which means that there was no split necessary.")
plt.show()