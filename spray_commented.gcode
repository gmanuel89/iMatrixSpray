;;;; x (-60 + 60), y (-80 +80), density 1, height 60, line distance 5, liquid A, speed 150
;Spray file generated on the fly
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; initialisation
G28XYZ ; initialise axes
G28P ; initialise pump
G90 ; absolute reference coordinates







;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; first wash
;go to wash position
G1 Z-35.0 F200 ; initial position
G1 X0.0 Y-110.0 Z-35.0 F200 ; go to the furthest position along the y-axis (speed 200, F)
G1 Z-50.0 ; move the capillary down a little bit

; 5 cycles of washing
G1 V3.5 F200 ; valve position 3-5 (solution A - Waste)
G4 S1 ; wait for 1 second (S)
G1 P4.2 F200 ; aspirate position 4.2 (P) (create vacuum for later)
G4 S1 ; wait for 1 second (S)
G1 V3 F200 ; Valve 3 (solution A) to position 1 (call the liquid from the vial thanks to the vacuum)
G4 S1 ; wait for 1 second (S)
G1 V0 F200 ; Valve 0 (waste) to position 1
G4 S1 ; wait for 1 second (S)
G1 P0 F100 ; empty syringe
G4 S1 ; wait for 1 second (S)

G1 V3.5 F200
G4 S1
G1 P4.2 F200
G4 S1
G1 V3 F200
G4 S1
G1 V0 F200
G4 S1
G1 P0 F100
G4 S1

G1 V3.5 F200
G4 S1
G1 P4.2 F200
G4 S1
G1 V3 F200
G4 S1
G1 V0 F200
G4 S1
G1 P0 F100
G4 S1

G1 V3.5 F200
G4 S1
G1 P4.2 F200
G4 S1
G1 V3 F200
G4 S1
G1 V0 F200
G4 S1
G1 P0 F100
G4 S1

G1 V3.5 F200
G4 S1
G1 P4.2 F200
G4 S1
G1 V3 F200
G4 S1
G1 V0 F200
G4 S1
G1 P0 F100
G4 S1

M106 ; turn the gas on
G1 V3 F200 ; Valve 3 (solution A) to position 1
G4 S1 ; wait (G4) for 1 second (S)
G1 P2 F200 ; aspirates (P) 2 mm (0.02 ml) of solution
G1 V1 F200 ; Valve 1 (spray) to position 1
G4 S1 ; wait (G4) for 1 second (S)
G1 F0.1 ; set speed
G1 P0 ; empty syringe






;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; spray
M106 ; turn the gas on
M82 ; pump in absolute mode
G1 V3 F200 ; Valve 3 (solution A) to position 1 (G) at 200mm/min (F)
G4 S1 ; wait (G4) for 1 second (S)
G1 P13.9760479042 F200 ; aspirates (P) 14 mm of solution A
G1 V1 F200 ; Valve 1 (waste) to position 1 (G) at 200mm/min (F)
G4 S1 ; wait (G4) for 1 second (S)
G1 F0.1 ; set speed of the next command
G1 P11.9760479042 ; set the syringe to the new position (slowly) (the 2mm of solution of difference between 14 and 12 goes into the tubes)

; position where to start spraying
G1 Z-35.0 F200 ; initial position
G1 X-60.0 Y-80.0 F200  ; go to the upper left corner of the spraying area
G1 Z-24.0 F200 ; move the capillary down a little bit (according to how much it has to be from the sample)

M83 ; pump in relative mode
;;; spraying code
G1 X60.0 Y-80.0 P-0.0149700598802 F150.0 ; dispense (negative P) 0.01497 mm of solution (0.125% of Vtot) at 150mm/min of speed (F)
G1 X-60.0 Y-80.0 P-0.359281437126 F150.0 ; dispense (negative P) 0.35928 mm of solution (3% of Vtot) at 150mm/min of speed (F)
G1 X-60.0 Y-75.0 P-0.0149700598802 F150.0
G1 X60.0 Y-75.0 P-0.359281437126 F150.0
G1 X60.0 Y-70.0 P-0.0149700598802 F150.0
G1 X-60.0 Y-70.0 P-0.359281437126 F150.0
G1 X-60.0 Y-65.0 P-0.0149700598802 F150.0
G1 X60.0 Y-65.0 P-0.359281437126 F150.0
G1 X60.0 Y-60.0 P-0.0149700598802 F150.0
G1 X-60.0 Y-60.0 P-0.359281437126 F150.0
G1 X-60.0 Y-55.0 P-0.0149700598802 F150.0
G1 X60.0 Y-55.0 P-0.359281437126 F150.0
G1 X60.0 Y-50.0 P-0.0149700598802 F150.0
G1 X-60.0 Y-50.0 P-0.359281437126 F150.0
G1 X-60.0 Y-45.0 P-0.0149700598802 F150.0
G1 X60.0 Y-45.0 P-0.359281437126 F150.0
G1 X60.0 Y-40.0 P-0.0149700598802 F150.0
G1 X-60.0 Y-40.0 P-0.359281437126 F150.0
G1 X-60.0 Y-35.0 P-0.0149700598802 F150.0
G1 X60.0 Y-35.0 P-0.359281437126 F150.0
G1 X60.0 Y-30.0 P-0.0149700598802 F150.0
G1 X-60.0 Y-30.0 P-0.359281437126 F150.0
G1 X-60.0 Y-25.0 P-0.0149700598802 F150.0
G1 X60.0 Y-25.0 P-0.359281437126 F150.0
G1 X60.0 Y-20.0 P-0.0149700598802 F150.0
G1 X-60.0 Y-20.0 P-0.359281437126 F150.0
G1 X-60.0 Y-15.0 P-0.0149700598802 F150.0
G1 X60.0 Y-15.0 P-0.359281437126 F150.0
G1 X60.0 Y-10.0 P-0.0149700598802 F150.0
G1 X-60.0 Y-10.0 P-0.359281437126 F150.0
G1 X-60.0 Y-5.0 P-0.0149700598802 F150.0
G1 X60.0 Y-5.0 P-0.359281437126 F150.0
G1 X60.0 Y0.0 P-0.0149700598802 F150.0
G1 X-60.0 Y0.0 P-0.359281437126 F150.0
G1 X-60.0 Y5.0 P-0.0149700598802 F150.0
G1 X60.0 Y5.0 P-0.359281437126 F150.0
G1 X60.0 Y10.0 P-0.0149700598802 F150.0
G1 X-60.0 Y10.0 P-0.359281437126 F150.0
G1 X-60.0 Y15.0 P-0.0149700598802 F150.0
G1 X60.0 Y15.0 P-0.359281437126 F150.0
G1 X60.0 Y20.0 P-0.0149700598802 F150.0
G1 X-60.0 Y20.0 P-0.359281437126 F150.0
G1 X-60.0 Y25.0 P-0.0149700598802 F150.0
G1 X60.0 Y25.0 P-0.359281437126 F150.0
G1 X60.0 Y30.0 P-0.0149700598802 F150.0
G1 X-60.0 Y30.0 P-0.359281437126 F150.0
G1 X-60.0 Y35.0 P-0.0149700598802 F150.0
G1 X60.0 Y35.0 P-0.359281437126 F150.0
G1 X60.0 Y40.0 P-0.0149700598802 F150.0
G1 X-60.0 Y40.0 P-0.359281437126 F150.0
G1 X-60.0 Y45.0 P-0.0149700598802 F150.0
G1 X60.0 Y45.0 P-0.359281437126 F150.0
G1 X60.0 Y50.0 P-0.0149700598802 F150.0
G1 X-60.0 Y50.0 P-0.359281437126 F150.0
G1 X-60.0 Y55.0 P-0.0149700598802 F150.0
G1 X60.0 Y55.0 P-0.359281437126 F150.0
G1 X60.0 Y60.0 P-0.0149700598802 F150.0
G1 X-60.0 Y60.0 P-0.359281437126 F150.0
G1 X-60.0 Y65.0 P-0.0149700598802 F150.0
G1 X60.0 Y65.0 P-0.359281437126 F150.0
G1 X60.0 Y70.0 P-0.0149700598802 F150.0
G1 X-60.0 Y70.0 P-0.359281437126 F150.0
G1 X-60.0 Y75.0 P-0.0149700598802 F150.0
G1 X60.0 Y75.0 P-0.359281437126 F150.0
G1 Y-80.0 Z-35.0 F200








;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; wash
;go to wash position
G1 Z-35.0 F200 ; initial position
G1 X0.0 Y-110.0 Z-35.0 F200 ; go to the furthest position along the y-axis (speed 200, F)
G1 Z-50.0 ; move the capillary down a little bit

M82 ; pump in absolute mode
G1 V0 F200 ; open the waste valve (V0)
G4 S1 ; wait (G4) for 1 second (S)
G1 P0 F200 ; empty the syringe
M106 S0 ; turn the gas off
G4 S0.0 ; wait (G4) for 0 seconds (S)










;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; starting cleaning procedure
; go to wash position
M82 ; pump in absolute mode
G90 ; absolute reference coordinates
G1 Z-35.0 F200
G1 X0.0 Y-110.0 Z-35.0 F200
G1 Z-50.0
M106 ; turn the gas on
G1 V0 F200 ; open the waste valve (V0)
G4 S1
; emptying syringe
G1 P0 F100
; rinsing valve  steps 5
;80 microliter each step
;step 1
G1 V1.5 F200 ; set the valve position to 1-5 (spray-waste)
G4 S1 ; wait for 1 second
G1 P4.8 F200 ; aspirate 4.8mm
G1 V2 F200 ; open the rinsing valve (V2)
G4 S2 ; wait for 2 seconds
G1 V0 F200 ; open the waste valve (V0)
G4 S1 ; wait for 1 second
G1 P0 F100 ; empty the syringe
;step2
G1 V1.5 F200
G4 S1
G1 P4.8 F200
G1 V2 F200
G4 S2
G1 V0 F200
G4 S1
G1 P0 F100
;step 3
G1 V1.5 F200
G4 S1
G1 P4.8 F200
G1 V2 F200
G4 S2
G1 V0 F200
G4 S1
G1 P0 F100
;step 4
G1 V1.5 F200
G4 S1
G1 P4.8 F200
G1 V2 F200
G4 S2
G1 V0 F200
G4 S1
G1 P0 F100
;step 5
G1 V1.5 F200
G4 S1
G1 P4.8 F200
G1 V2 F200
G4 S2
G1 V0 F200
G4 S1
G1 P0 F100
; rinsing spray
G1 V1.5 F200
G4 S1
G1 P4 F200
G4 S1
G1 V2 F200
G4 S2
G1 V1 F200
G4 S1
G1 F0.1
G1 P0
M106 S0
; rinsing capillary
G1 V1.5 F200
G4 S1
G1 P3 F200
G1 V2 F200
G4 S2
G1 V1 F200
G4 S1
G1 F0.1
G1 P0
G1 P1
; drying
M106
G1 P0
G4 S2
G4 S2
G4 S2
G4 S2
M106 S0
; parking spray
G1 Z-35.0 F200
G1 X0 Y0 Z-35 F200
G1 Z16.5 F200
; motors off
M18
