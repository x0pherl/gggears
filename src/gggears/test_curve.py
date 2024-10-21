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

from curve import *
import matplotlib.pyplot as plt
# curve1 = Curve(arc_from_2_point_center,params={'p0': DOWN,'p1':RIGHT,'center':ORIGIN})
# curve2 = Curve(arc_from_2_point_center,params={'p0': RIGHT,'p1':RIGHT*2+DOWN,'center':RIGHT*2})

curve1 = ArcCurve.from_radius_center_angle(radius=0.5,center=RIGHT*0.5,angle_start=-PI/2,angle_end=0)
curve2 = ArcCurve2(radius=1,angle=-PI/2,center=RIGHT+DOWN,yaw=PI/2)

curve3 = ArcCurve2(radius=1,angle=PI/2,center=ORIGIN,yaw=-PI/2,roll=PI/2)

chain1 = CurveChain(curve1,curve2)

chain1(0.2)
chain1(0.8)

print(len(chain1))
p1 = curve3(np.linspace(0,1,101))

props=chain1.get_length_portions()
chain2 = chain1.fillet(radius=0.05,location=props[1])
# chain2.set_start_on(0.5,preserve_inactive_curves=True)
# chain2.set_end_on(0.8)

chain3 = MirroredCurve(chain2)
print(curve1)
# chain2[1].active=0
# chain2(0.8)
p2 = chain1(np.linspace(0,1,101))

plt.plot(p1[:,0],p1[:,2])
# plt.plot(p2[:,0],p2[:,1])
plt.show()