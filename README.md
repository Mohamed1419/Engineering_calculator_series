# Engineering_calculator_series

A series of Python-based engineering calculators built as portfolio projects 
during the summer of 2026.
Each calculator combines engineering theory with Python to model and visualise 
real physical systems.

---

## 1. Pipe Flow Calculator

### What it does
Calculates key fluid flow parameters for a fluid flowing through a pipe:
- Reynolds Number and flow regime (laminar, transitional, or turbulent)
- Darcy friction factor using the Swamee-Jain approximation
- Pressure drop across the pipe length using the Darcy-Weisbach equation
- Volumetric flow rate

Generates a pressure drop vs velocity graph showing how pressure loss 
scales with flow velocity across the full operating range.

### Engineering concepts
- **Reynolds Number**: dimensionless ratio of inertial to viscous forces, 
  used to predict flow regime
- **Darcy-Weisbach equation**: relates pressure drop to friction factor, 
  pipe geometry, and flow velocity
- **Swamee-Jain equation**: explicit approximation of the Colebrook-White 
  equation for turbulent friction factor

### Motivation
Inspired by a site visit to Ebury Bridge Estate in London, a large 
residential regeneration project, where I observed building services 
infrastructure including pump systems, heating pipework, and mechanical plant 
at various stages of installation. The calculator models the kind of fluid 
flow analysis that underpins the design of those systems.

### How to run
```bash
pip3 install matplotlib numpy
python3 pipe_flow_calculator.py
```

### Example inputs (water in a copper pipe)
| Parameter | Value |
|---|---|
| Diameter | 0.05 m |
| Length | 10 m |
| Velocity | 1.5 m/s |
| Density | 1000 kg/m³ |
| Viscosity | 0.001 Pa·s |
| Roughness | 0.0000015 m |