; FSL Auto Test generated G-code
; generated_at=2026-08-25T20:53:27
; hotend_profile=P350 + Goliath
; material=PLA
; target_temperature_C=230
; Q_start=15 Q_end=16 Q_step=1
; extrusions_per_Q=1
; gap_duration_ms=0
; gap_flow_Q=0
; post_extrusion_record_s=5
; extrusion_rules=[{"q_min":0.0,"q_max":15.0,"E_mm":150.0},{"q_min":15.0,"q_max":20.0,"E_mm":200.0},{"q_min":20.0,"q_max":30.0,"E_mm":250.0},{"q_min":30.0,"q_max":40.0,"E_mm":300.0},{"q_min":40.0,"q_max":50.0,"E_mm":350.0},{"q_min":50.0,"q_max":null,"E_mm":400.0}]
; filament_diameter_mm=1.75
M83 ; relative extrusion
M104 S230.0
M155 S1 ; auto temperature report
; SEGMENT id=1 Q=15 E=200.0000 V=481.0564 F=374.177 start=0.000000 end=32.070425 duration=32.070425 repeat=1/1 gap_after_ms=0 gap_flow_Q=0 gap_E=0.0000
G1 E200.0000 F374.2
; SEGMENT id=2 Q=16 E=200.0000 V=481.0564 F=399.122 start=32.070425 end=62.136448 duration=30.066023 repeat=1/1 gap_after_ms=0 gap_flow_Q=0 gap_E=0.0000
G1 E200.0000 F399.1
M400 ; wait for final extrusion motion
; END FSL Auto Test
