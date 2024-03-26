from vpython import *

def main():
    G = 6.67408e-11

    #mass of the sun, earth
    m_sun = 1.9891e30
    m_earth = 5.972e24
    m_moon = .076e24

    #scale
    # r_sun = 6.9634e9
    # r_earth = 6.367e6
    # r_moon = 1.74e6

    #not scale
    r_sun = 6.9634e9 * 4
    r_earth = r_sun / 4
    r_moon = 1.74e6


    d_earth = 1.495e11
    d_moon = d_earth + 3.848e8

    #create the objects
    sun = sphere(pos = vector (0,0,0), radius = r_sun, color=color.yellow)
    earth = sphere(pos = vector(d_earth, 0, 0), radius = r_earth, color=color.blue, make_trail = True)
    moon = sphere(pos = vector(d_moon, 0, 0), radius = r_moon, color=color.white, make_trail = False, opacity = 0)
    #scaled visible object
    moonS = sphere(pos = earth.pos + (3 * earth.radius * norm(moon.pos - earth.pos)), radius = earth.radius/2, color=color.white, make_trail = True)


    earth.velocity = vector(0, 3e4, 0)
    moon.velocity = vector(0, 1028, 0) + earth.velocity

    t = 0
    dt = 3600

    while (t < 1e10):
        rate (500)

        earth.pos += earth.velocity * dt
        moon.pos += moon.velocity * dt
        #update scaled moon
        moonS.pos = earth.pos + (3 * earth.radius * norm(moon.pos - earth.pos))
        

        #vectors between bodies
        rSE_vector = earth.pos - sun.pos #tail-head vector between sun and earth
        rME_vector = earth.pos - moon.pos
        rSM_vector = moon.pos - sun.pos   #Moon and Sun
        rEM_vector = moon.pos - earth.pos #Moon and Earth

        #Orbit - Earth
        F_gravSE = -(G * m_sun * m_earth / (mag(rSE_vector)**2)) * norm(rSE_vector)
        F_gravME = -(G * m_moon * m_earth / (mag(rME_vector)**2)) * norm(rME_vector)
        F_net_E = F_gravSE + F_gravME
        earth.velocity += (F_net_E / m_earth) * dt
        
        #Orbit - Moon
        F_gravSM = -(G * m_sun * m_moon / (mag(rSM_vector)**2)) * norm(rSM_vector)
        F_gravEM = -(G * m_earth * m_moon / (mag(rEM_vector)**2)) * norm(rEM_vector)
        F_net_M = F_gravEM + F_gravSM
        moon.velocity += (F_net_M / m_moon) * dt

        t = t + dt


main()