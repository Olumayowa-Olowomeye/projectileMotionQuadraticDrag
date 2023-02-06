# projectileMotionQuadraticDrag

## Brief Introduction & Theory
Defines a projectile solver (well-known problem in Newtonian physics) that includes quadratic drag in C++. The 2nd order differential equations (ODEs) defined through the free body diagram are solved using the RK4 (Runge-Kutta 4th Order) numerical scheme. Step sizes are kept constant (no adaptive step-size routine). Simulation parameters together with global contants are defined in the constants.h header file. Please refer to that header file if you want to increase your number of steps or run the simulation in another medium (water for example)

## Assumptions in Physics
It is assumed that the drag acting on the body is fully defined through the quadratic drag formula. It is also assumed that the drag coefficient equals with 0.5. Projectile motions are limited in the XY plane, with +y being orthogonal to the ground and aiming away from it. The only 2 forces considered on the body are its weight and the drag. Any other forces (magneric, etc.) are ingored in the ODEs definition.
## How to Run

## Output Results


## Closing Remarks
