** Generated for: Finesim


.PARAM blinresistor=2000
.PARAM blresistor=3000

.TRAN 10e-12 200e-9 START=0.0

.TEMP 25.0
.OPTION
+    ARTIST=2
+    INGOLD=2
+    PARHIER=LOCAL
+    PSF=2
.OPTION PROBE=1
.PROBE tran v(l3bl0)
.PROBE tran v(l3bl1)
.PROBE tran v(l3bl2)
.PROBE tran v(l3bl3)
.PROBE tran v(l3bl4)
.PROBE tran v(l3bl5)
.PROBE tran v(l3bl6)
.PROBE tran v(l3bl7)
.PROBE tran v(l3bl8)
.PROBE tran v(l3bl9)
.measure tran avgval0 AVG v(l3bl0) FROM = 199ns TO =200ns
.measure tran avgval1 AVG v(l3bl1) FROM = 199ns TO =200ns
.measure tran avgval2 AVG v(l3bl2) FROM = 199ns TO =200ns
.measure tran avgval3 AVG v(l3bl3) FROM = 199ns TO =200ns
.measure tran avgval4 AVG v(l3bl4) FROM = 199ns TO =200ns
.measure tran avgval5 AVG v(l3bl5) FROM = 199ns TO =200ns
.measure tran avgval6 AVG v(l3bl6) FROM = 199ns TO =200ns
.measure tran avgval7 AVG v(l3bl7) FROM = 199ns TO =200ns
.measure tran avgval8 AVG v(l3bl8) FROM = 199ns TO =200ns
.measure tran avgval9 AVG v(l3bl9) FROM = 199ns TO =200ns
.measure tran bld AVG v(bld) FROM = 99ns TO =100ns
.measure tran bldin AVG v(bldin) FROM = 99ns TO =100ns
.measure tran czabd AVG v(czabd) FROM = 99ns TO =100ns


.INCLUDE "/home/user33/design/rules/rohm180/spice/hspice/bu40n1.mdl"
#.INCLUDE "/home/user33/design/rules/rohm180/spice/hspice/bu40n3.mdl"
.LIB "/home/user33/design/rules/rohm180/spice/hspice/bu40n1.skw" NT
.LIB "/home/user33/design/rules/rohm180/spice/hspice/bu40n1.skw" PT

** Library name: reram
** Cell name: CELLD
** View name: schematic
.subckt CELLD bl sl wl wlb
m1 sl wlb net08 0 N L=180e-9 W=5e-6
m0 sl wl net09 0 N L=180e-9 W=5e-6
r1 net08 bl r1
r0 net09 bl r0
.ends CELLD
** End of subcircuit definition.

** Library name: reram
** Cell name: SAVM2
** View name: schematic
.subckt SAVM2 bl blb dl vdd
m1 dl net19 vdd vdd P L=180e-9 W=1e-6
m0 net19 net19 vdd vdd P L=180e-9 W=1e-6
m3 dl blb 0 0 N L=180e-9 W=1e-6
m2 net19 bl 0 0 N L=180e-9 W=1e-6
.ends SAVM2
** End of subcircuit definition.

** Library name: testRohm_n
** Cell name: INV1
** View name: schematic
.subckt INV1 g in out v
m1 out in v v P L=180e-9 W=5e-6
m0 out in g g N L=180e-9 W=2e-6
.ends INV1
** End of subcircuit definition.

** Library name: reram
** Cell name: CELLDREF
** View name: schematic
.subckt CELLDREF bl sl wl wlb
m1 sl wlb net13 net13 N L=180e-9 W=5e-6
m0 sl wl net14 net14 N L=180e-9 W=5e-6
r8 net018 bl 5.3e3
r7 net13 net018 100e3
r6 net14 net020 5.3e3
r5 net020 bl 100e3

r4 net017 bl 5.3e3
r3 net019 bl 100e3
r1 net13 net017 100e3
r0 net14 net019 5.3e3
.ends CELLDREF
** End of subcircuit definition.

** Library name: reram
** Cell name: XORNET4
** View name: schematic
