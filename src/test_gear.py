'''
Copyright 2024 Gergely Bencsik
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import gggears.gggears_core as gg
import matplotlib.pyplot as plt
import gggears.curve as crv
from gggears.defs import *
n = 19
gamma = PI/2 *0.0


param = gg.InvoluteGearParam(n_teeth=n,
                              module=2.0,
                              cone_angle=gamma*2,
                              h_d=1.2,
                              tip_fillet=0.1,
                              profile_reduction=0.001,
                              enable_undercut=True)

param1 = gg.InvoluteGearParamManager(z_vals=[0, 2],
                                     n_teeth=19,
                                     n_cutout_teeth=0, 
                                     module=4.0, 
                                     pressure_angle=0.3490658503988659, 
                                     cone_angle=0.0, 
                                     axis_offset=0, 
                                     center=np.asarray([ 0.        ,  0.        , 10.66666667]), 
                                     angle=0.0, 
                                     axis=np.asarray([0., 0., 1.]), 
                                     h_a=1.2, h_d=1.4, h_o=2, profile_shift=0.0, 
                                     profile_reduction=0.7742636826811271, 
                                     tip_fillet=0.0, root_fillet=0.0, 
                                     tip_reduction=0.1, inside_teeth=False, enable_undercut=True)

param1 = gg.InvoluteGearParamManager(z_vals=[0, 1, 2],
                                     n_teeth=19, n_cutout_teeth=0, 
                                     module=3.8666236292003906, 
                                     pressure_angle=0.3490658503988659, 
                                     cone_angle=0.3141592653589793, axis_offset=0, 
                                     center=np.asarray([ 0.,  0., 16.]), angle=0.0, 
                                     axis=np.asarray([0., 0., 1.]), h_a=1.2, h_d=1.4, h_o=2, 
                                     profile_shift=0.0, profile_reduction=0.1, 
                                     tip_fillet=0.0, root_fillet=0.0, tip_reduction=0.1, 
                                     inside_teeth=False, enable_undercut=True)

# param1 = gg.InvoluteGearParamManager(z_vals=[0,2],
#                                     n_teeth=n,
#                                     module=lambda z: 1-np.tan(gamma)*z/n*2,
#                                     center=lambda z: z*OUT,
#                                     angle=0,
#                                     axis=RIGHT,
#                                     cone_angle=gamma*2,
#                                     h_d=1.2,
#                                     h_o=2.5,
#                                     profile_reduction=0.2,
#                                     root_fillet=0,
#                                     tip_fillet=0,
#                                     enable_undercut=False)

param2 = gg.InvoluteGearParamManager()
for key in param2.__dict__.keys():
    param2.__dict__[key] = param2.__dict__[key]*0
param2.h_d = lambda z: -0.1 + 0.4*z

# param3 = param1+param2
profile1 = gg.InvoluteFlankGenerator(pitch_angle=2*PI/n,
                                     h_d=1.2,
                                     profile_reduction=0.001,
                                     cone_angle=gamma*2,
                                     enable_undercut=True)


# curvgen = gg.GearCurveGenerator(reference_tooth_curve=profile1.tooth_curve.copy(),**param1.__dict__)
# curvgen.generate_profile_closed()

gear = gg.InvoluteGear(params=param1)
curvgen = gear.setup_generator(param1(0))
profile_full = curvgen.generate_gear_pattern(curvgen.generate_profile_closed(rd_coeff_right=0.5,rd_coeff_left=0.5))
profile_closed = curvgen.generate_profile_closed(rd_coeff_right=1,rd_coeff_left=0)

points1 = curvgen.rp_circle(np.linspace(0,1,300))
points2 = curvgen.ra_circle(np.linspace(0,1,300))
points3 = curvgen.rd_circle(np.linspace(0,1,300))
points4 = curvgen.ro_circle(np.linspace(0,1,300))
points5 = profile1.tooth_curve(np.linspace(0,1,300))
points5 = profile_full(np.linspace(0,1,300*n))
# points5 = crv.convert_curve_nurbezier(profile1.tooth_curve)(np.linspace(0,1,300))
convert1 = crv.convert_curve_nurbezier(profile_closed.get_curves())
points5 = crv.convert_curve_nurbezier(profile_closed)(np.linspace(0,1,300*n))

ax = plt.axes(projection='3d')

ax.plot(points1[:,0],points1[:,1], points1[:,2], marker='',linestyle='-', color='red')
ax.plot(points2[:,0],points2[:,1], points2[:,2], marker='',linestyle='-', color='green')
ax.plot(points3[:,0],points3[:,1], points3[:,2], marker='',linestyle='-', color='blue')
ax.plot(points4[:,0],points4[:,1], points4[:,2], marker='',linestyle='-', color='black')
ax.plot(points5[:,0],points5[:,1], points5[:,2], marker='.',linestyle='-', color='orange')

ax.axis('equal')
plt.show()