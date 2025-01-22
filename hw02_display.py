"""Visualization module for HW02 simulating planar rotational
 kinematics for a 3-link mechanism."""

# =============================================================================
# VISUALIZE 3-LINK JOINT TRAJECTORIES
# =============================================================================
def plot_3_trajectories(RR, L):
    """Plot the joint trajectories for a planar rotational 3-link mechanism.

    INPUT:  RR - 3D ndarray of Cartesian coordinates for joints
                 0th dimension:  time steps
                 1th dimension:  four joints (O, A, B, C for three links)
                 2th dimension:  x, y, z coordinates of joint in meters
            L  - 1D ndarray of link lengths in meters
    OUTPUT: None

    Note that plt.show() is invoked in this function to display the plot.
    """
    import numpy as np
    import matplotlib.pyplot as plt

    plt.figure(figsize=(8, 6))

    plt.scatter(0, 0, color="black", label="fixed point O")
    plt.plot(RR[:,1,0], RR[:,1,1], 'g-', label="trajectory of joint A")
    plt.plot(RR[:,2,0], RR[:,2,1], 'b-', label="trajectory of joint B")
    plt.plot(RR[:,3,0], RR[:,3,1], 'r-', label="trajectory of joint C")

    plt.title("Trajectory of joints for three planar rotating links")
    plt.xlabel("x coordinate [m]")
    plt.ylabel("y coordinate [m]")
    margin = 1.03         # add a 3% margin around the plot
    plt.xlim(-np.sum(L)*margin, np.sum(L)*margin)
    plt.ylim(-np.sum(L)*margin, np.sum(L)*margin)

    plt.axis("equal")
    plt.legend()
    plt.grid()
    plt.show()

    return None

# =============================================================================
# ANIMATE 3-LINK MECHANISM
# =============================================================================
def animate_3_links(RR, L, dt):
    """Animate the links for a planar rotational 3-link mechanism.

    INPUT:  RR - 3D ndarray of Cartesian coordinates for joints
                 0th dimension:  time steps
                 1th dimension:  four joints (O, A, B, C for three links)
                 2th dimension:  x, y, z coordinates of joint in meters
            L  - 1D ndarray of link lengths in meters

    OUTPUT: anim - the animation object

    Note that plt.show() must be invoked by the calling script
    to display the animation.

    Proper display requires invoking the following command at the
    command prompt:
        >>> %matplotlib qt
    This will produce the animation (and any previous plots) in
    an external window.  Use <Consoles> <Restart kernel> to return
    to the usual behavior.
    """
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    fig, ax = plt.subplots(figsize=(8, 6))
    margin = 1.05         # add a 5% margin around the plot
    ax.set_xlim(-np.sum(L)*margin, np.sum(L)*margin)
    ax.set_ylim(-np.sum(L)*margin, np.sum(L)*margin)
    ax.set_aspect('equal')
    ax.grid()
    pointC, = ax.plot([], [], 'ro', label='point C')
    line3,  = ax.plot([], [], 'ro-', lw=2, label='link 3')
    line2,  = ax.plot([], [], 'bo-', lw=2, label='link 2')
    line1,  = ax.plot([], [], 'go-', lw=2, label='link 1')
    pointO, = ax.plot([], [], 'ko', label='point O')
    ax.legend()

    def update(frame):
        x3, y3 = RR[frame,3,0], RR[frame,3,1]
        x2, y2 = RR[frame,2,0], RR[frame,2,1]
        x1, y1 = RR[frame,1,0], RR[frame,1,1]
        x0, y0 = RR[frame,0,0], RR[frame,0,1]
        
        pointC.set_data([x3], [y3])
        line3.set_data([x2, x3], [y2, y3])
        line2.set_data([x1, x2], [y1, y2])
        line1.set_data([ 0, x1], [ 0, y1])
        pointO.set_data([x0], [y0])
        return pointC, line3, line2, line1, pointO

    nsteps = RR.shape[0]    # number of simulation steps
    convert_ms_to_s = 1000.0
    interval = dt * convert_ms_to_s
    anim = animation.FuncAnimation(fig, update, frames=nsteps, blit=True, interval=interval, repeat=True)
    plt.show()
    return anim

