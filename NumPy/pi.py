plane = NumberPlane()
pi_creature  = PiCreature(color = PINK)
plane.prepare_for_nonlinear_transformation()
plane.add(pi_creature)
def homotopy(x,y,z,t):
	norm = np.linalg.norm([x,y])
	tau = interpolate(5,-5,t)+ norm/SPACE_WIDTH
	