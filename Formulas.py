# 1. Integral kernels of formulas for a vertical cylindrical prism in Table 7

V = G*r3*rho/sqrt(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 + (z - z3)**2)

Vr = -G*r3*rho*(r - r3*cos(lon - lon3))/(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 + (z - z3)**2)**(3/2)

Vlon = -G*r3**2*rho*sin(lon - lon3)/(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 + (z - z3)**2)**(3/2)

Vz = -G*r3*rho*(z - z3)/(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 + (z - z3)**2)**(3/2)

Vrr = G*r3*rho*(4*r**2 - 8*r*r3*cos(lon - lon3) + 3*r3**2*cos(2*lon - 2*lon3) + r3**2 - 2*(z - z3)**2)/(2*(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 + (z - z3)**2)**(5/2))

Vrlon = 3*G*r3**2*rho*(r - r3*cos(lon - lon3))*sin(lon - lon3)/(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 + (z - z3)**2)**(5/2)

Vrz = 3*G*r3*rho*(r - r3*cos(lon - lon3))*(z - z3)/(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 + (z - z3)**2)**(5/2)

Vlonlon = G*r3*rho*(-2*r**2 + 4*r*r3*cos(lon - lon3) - 3*r3**2*cos(2*lon - 2*lon3) + r3**2 - 2*(z - z3)**2)/(2*(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 + (z - z3)**2)**(5/2))

Vlonz = 3*G*r3**2*rho*(z - z3)*sin(lon - lon3)/(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 + (z - z3)**2)**(5/2)

Vzz = -G*r3*rho*(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 - 2*(z - z3)**2)/(r**2 - 2*r*r3*cos(lon - lon3) + r3**2 + (z - z3)**2)**(5/2)

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

# 2. Formulas for a vertical cylindrical shell in Table 8

Vcs = pi*G*rho*(-r1**2*log((-z + z2 + sqrt(r1**2 + (z - z2)**2))/(-z + z1 + sqrt(r1**2 + (z - z1)**2))) + r2**2*log((-z + z2 + sqrt(r2**2 + (z - z2)**2))/(-z + z1 + sqrt(r2**2 + (z - z1)**2))) - (z - z1)*(sqrt(r1**2 + (z - z1)**2) - sqrt(r2**2 + (z - z1)**2)) - (z - z2)*(-sqrt(r1**2 + (z - z2)**2) + sqrt(r2**2 + (z - z2)**2)))

Vcsz = -2*pi*G*rho*(sqrt(r1**2 + (z - z1)**2) - sqrt(r1**2 + (z - z2)**2) - sqrt(r2**2 + (z - z1)**2) + sqrt(r2**2 + (z - z2)**2))

Vcsrr = pi*G*rho*((z - z2)/sqrt(r2**2 + (z - z2)**2) - (z - z1)/sqrt(r2**2 + (z - z1)**2) - (z - z2)/sqrt(r1**2 + (z - z2)**2) + (z - z1)/sqrt(r1**2 + (z - z1)**2))

Vcslonlon = pi*G*rho*((z - z2)/sqrt(r2**2 + (z - z2)**2) - (z - z1)/sqrt(r2**2 + (z - z1)**2) - (z - z2)/sqrt(r1**2 + (z - z2)**2) + (z - z1)/sqrt(r1**2 + (z - z1)**2))

Vcszz = -2*pi*G*rho*((z - z2)/sqrt(r2**2 + (z - z2)**2) - (z - z1)/sqrt(r2**2 + (z - z1)**2) - (z - z2)/sqrt(r1**2 + (z - z2)**2) + (z - z1)/sqrt(r1**2 + (z - z1)**2))

Vcsrrz = pi*G*rho*(-r1**2/(r1**2 + (z - z2)**2)**(3/2) + r1**2/(r1**2 + (z - z1)**2)**(3/2) + r2**2/(r2**2 + (z - z2)**2)**(3/2) - r2**2/(r2**2 + (z - z1)**2)**(3/2))

Vcslonlonz = pi*G*rho*(-r1**2/(r1**2 + (z - z2)**2)**(3/2) + r1**2/(r1**2 + (z - z1)**2)**(3/2) + r2**2/(r2**2 + (z - z2)**2)**(3/2) - r2**2/(r2**2 + (z - z1)**2)**(3/2))

Vcszzz = -2*pi*G*rho*(-r1**2/(r1**2 + (z - z2)**2)**(3/2) + r1**2/(r1**2 + (z - z1)**2)**(3/2) + r2**2/(r2**2 + (z - z2)**2)**(3/2) - r2**2/(r2**2 + (z - z1)**2)**(3/2))

# 3. Formulas for a vertical cylinder in Tables 10, 11, and 12

Vc = pi*G*rho*(-R**2*log(-z + z1 + sqrt(R**2 + (z - z1)**2)) + R**2*log(-z + z2 + sqrt(R**2 + (z - z2)**2)) + (z - z1)*(sqrt(R**2 + (z - z1)**2) - Abs(z - z1)) - (z - z2)*(sqrt(R**2 + (z - z2)**2) - Abs(z - z2)))

Vcz = 2*pi*G*rho*(sqrt(R**2 + (z - z1)**2) - sqrt(R**2 + (z - z2)**2) - Abs(z - z1) + Abs(z - z2))

Vcrr = pi*G*rho*(z - z2)/sqrt(R**2 + (z - z2)**2) + pi*G*rho*(-z + z1)/sqrt(R**2 + (z - z1)**2)

Vclonlon = pi*G*rho*(z - z2)/sqrt(R**2 + (z - z2)**2) + pi*G*rho*(-z + z1)/sqrt(R**2 + (z - z1)**2)

VczzOutside = 2*pi*G*rho*(-z + z2)/sqrt(R**2 + (z - z2)**2) + 2*pi*G*rho*(z - z1)/sqrt(R**2 + (z - z1)**2)

VczzInside = -4*pi*G*rho + 2*pi*G*rho*(-z + z2)/sqrt(R**2 + (z - z2)**2) + 2*pi*G*rho*(z - z1)/sqrt(R**2 + (z - z1)**2)

Vcrrz = pi*G*R**2*rho/(R**2 + (z - z2)**2)**(3/2) - pi*G*R**2*rho/(R**2 + (z - z1)**2)**(3/2)

Vclonlonz = pi*G*R**2*rho/(R**2 + (z - z2)**2)**(3/2) - pi*G*R**2*rho/(R**2 + (z - z1)**2)**(3/2)

Vczzz = -2*pi*G*R**2*rho/(R**2 + (z - z2)**2)**(3/2) + 2*pi*G*R**2*rho/(R**2 + (z - z1)**2)**(3/2)