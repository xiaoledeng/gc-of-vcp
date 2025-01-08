# 1. Integral kernels of formulas for a vertical cylindrical prism in Table 3

Vrrr = 3*G*r3*rho*(r - r3*cos(lon - lon3))*(3*r**2 - 6*r*r3*cos(lon - lon3) + 3*r3**2 - 5*(r - r3*cos(lon - lon3))**2 + 3*(z - z3)**2)/(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 + (z - z3)**2)**(7/2)

Vrrlon = -3*G*r3**2*rho*(4*r**2 - 8*r*r3*cos(lon - lon3) - 5*r3**2*sin(lon - lon3)**2 + 4*r3**2 - (z - z3)**2)*sin(lon - lon3)/(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 + (z - z3)**2)**(7/2)

Vrrz = 3*G*r3*rho*(z - z3)*(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 - 5*(r - r3*cos(lon - lon3))**2 + (z - z3)**2)/(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 + (z - z3)**2)**(7/2)

Vrlonz = -15*G*r3**2*rho*(r - r3*cos(lon - lon3))*(z - z3)*sin(lon - lon3)/(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 + (z - z3)**2)**(7/2)

Vlonlonr = 3*G*r3*rho*(r - r3*cos(lon - lon3))*(r**2 - 2*r*r3*cos(lon - lon3) - 5*r3**2*sin(lon - lon3)**2 + r3**2 + (z - z3)**2)/(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 + (z - z3)**2)**(7/2)

Vlonlonlon = 3*G*r3**2*rho*(3*r**2 - 6*r*r3*cos(lon - lon3) - 5*r3**2*sin(lon - lon3)**2 + 3*r3**2 + 3*(z - z3)**2)*sin(lon - lon3)/(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 + (z - z3)**2)**(7/2)

Vlonlonz = 3*G*r3*rho*(z - z3)*(r**2 - 2*r*r3*cos(lon - lon3) - 5*r3**2*sin(lon - lon3)**2 + r3**2 + (z - z3)**2)/(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 + (z - z3)**2)**(7/2)

Vzzr = 3*G*r3*rho*(r - r3*cos(lon - lon3))*(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 - 4*(z - z3)**2)/(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 + (z - z3)**2)**(7/2)

Vzzlon = 3*G*r3**2*rho*(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 - 4*(z - z3)**2)*sin(lon - lon3)/(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 + (z - z3)**2)**(7/2)

Vzzz = 3*G*r3*rho*(z - z3)*(3*r**2 - 6*r*r3*cos(lon - lon3) + 3*r3**2 - 2*(z - z3)**2)/(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 + (z - z3)**2)**(7/2)

# 2. Formulas for a vertical cylindrical shell in Table 4

Vcsrrz = pi*G*rho*(-r1**2/(r1**2 + (z - z2)**2)**(3/2) + r1**2/(r1**2 + (z - z1)**2)**(3/2) + r2**2/(r2**2 + (z - z2)**2)**(3/2) - r2**2/(r2**2 + (z - z1)**2)**(3/2))

Vcslonlonz = pi*G*rho*(-r1**2/(r1**2 + (z - z2)**2)**(3/2) + r1**2/(r1**2 + (z - z1)**2)**(3/2) + r2**2/(r2**2 + (z - z2)**2)**(3/2) - r2**2/(r2**2 + (z - z1)**2)**(3/2))

Vcszzz = -2*pi*G*rho*(-r1**2/(r1**2 + (z - z2)**2)**(3/2) + r1**2/(r1**2 + (z - z1)**2)**(3/2) + r2**2/(r2**2 + (z - z2)**2)**(3/2) - r2**2/(r2**2 + (z - z1)**2)**(3/2))

# 3. Formulas for a vertical cylinder in Table 5

Vcrrz = pi*G*R**2*rho/(R**2 + (z - z2)**2)**(3/2) - pi*G*R**2*rho/(R**2 + (z - z1)**2)**(3/2)

Vclonlonz = pi*G*R**2*rho/(R**2 + (z - z2)**2)**(3/2) - pi*G*R**2*rho/(R**2 + (z - z1)**2)**(3/2)

Vczzz = -2*pi*G*R**2*rho/(R**2 + (z - z2)**2)**(3/2) + 2*pi*G*R**2*rho/(R**2 + (z - z1)**2)**(3/2)