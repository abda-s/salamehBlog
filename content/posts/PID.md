---
title: 
description: 
date: 2025-04-09
tags: 
draft: "true"
---
pid is the most common control methods in control systems

this is the standard feedback control architecture

![Image Description](/images/Pasted%20image%2020250409062703.png)

the plant will produce some output signal (y)

we will take the plant signal (y) and match it with the input signal (r)

if the two signals don't match we will take the difference between these two and here is our error signal (e)

now the controller will look at the error signal (e) and compute a control signal (u) witch is applied to the plant


now lets think of what is the simplest thing that we can do?

we can take the error and run it throu a gain of some value lets call it gain k
![Image Description](/images/Pasted%20image%2020250409062649.png)

now lets think what is the control law??

$$u(t)=Ke(t)$$
this is referred to as proportional control the **P** in **proportional** is the same **P** in the **PID** 

this is nothing but take the error and multiplying it by a static gain K to compute your control u 
and what PID is, it's extending on this and making it better, now we have one term what if we have multiple terms not just one?

now lets start adding extra terms to our control law 
![Image Description](/images/Pasted%20image%2020250409062601.png)
 $$u(t)= K_p * e(t) + K_i \int_0^t{e(t)} + K_d * \frac{de(t)}{dt}$$
- $K_p * e(t)$  (Proportional)
- $K_i \int_0^t{e(t)}$ (Integral)
- $K_d * \frac{de(t)}{dt}$ (Derivation)

the PID controller is quite simple when the error gets to the controller the it splits into these three terms

you take the error multiply it by $K_p$ and that gives you the proportional component of control $u_p(t)$, there is there's also an integral component of control $u_i(t)$ which you get by basically integrating the error and then multiplying by $K_i$ or you can flip them around right from our block diagram, there is a linear system you can actually it doesn't matter if the Ki comes before or after the integral right, same thing for the derivative right you can basically switch this around it can be $K_D$ times $S$ or $S$ times $K_D$ it doesn't

yes this seems simple but in a lot of ways it can be shit, but for now lets assume every thing is easy beasy and let's continue 

let's examine each one of the term in isolation to get a better feel of what each one of them does and what they do and how they behave 

## Proportional Control
why don't we now start with just the proportional control let's conceder it by it self 
 ![Image Description](/images/Pasted%20image%2020250410154931.png)
at the beginning we said this is the simplest control that you will have so lets understand it 

let's look at the error signal going in and what the control signal coming out might be

and again the only output signal is the $u_p(t)$ 
![Image Description](/images/Pasted%20image%2020250410162758.png)
as u can see in the error graph we have zero error and at some point we have step input, plant can't respond instantaneously 

the error signal is going to jump up to point A

the proportional control as we can see when the error is **zero** the output is gonna be also zero i don't care what gain u have if the error is zero

but when the step happens we jump up instantaneously to $A * K_p$  

this is what's nice about a proportional control it respond instantaneously the gain $K_p$ is just a multiplication of the error that happens right away there is no dynamics associated with it

the proportional controller is gonna freak out a little bit it realizes there is a large error so it apply a large control signal, and u have to make sure that u put the signal of the control in the right orientation to push back the the output to make the error smaller to make it zero 

at the time we start to respond the error will start going down 

now lets see the what happens to the control signal $u_p(t)$ it's going to mirror the error signal 

there is something interesting going to happen, the error will be smaller and smaller at some point in real systems we might get stuck and there might be some steady state error (S.S error) why does this happen, when the error goes down also the control signal goes down, so the control is getting weaker and weaker and weaker and your applying less control every time to the plant

let's say we are controlling a motor to get to a certain angel each time the error is smaller, so does the voltage applied to the motor and at some point if we apply a small enough voltage the motor wont work any more.

## Integral Control

![Image Description](/images/Pasted%20image%2020250413212833.png)
now let's just look at $K_i$ and ignore $K_p$ and $K_d$, let's remember what this integrator control does is given by the equation  $K_i \int_0^t{e(t)}$ as we see all we have to do is integrate the error and multiply it by some number $K_p$ 

again the error is zero and you gave it a step input 

so what is the integrator is gonna do here??
![Image Description](/images/Pasted%20image%2020250413214953.png)
at first the integrator is doin nothing zero but when the step happens something is gonna happen, let's ask our self what is that something?

let's go ahead and see the time $X_1$, let's say the error signal does any thing for example this thing where is have some small slop 
now we gotta ask our selfs what is the control signal at this time $X_1$ the way you get that control signal is to integrate the error from the time of the step function until $X_1$ witch is just the area under the curve (with the color green), it's how much error the integrator has accumulated

because there isn't that much time the area isn't that large, yes we have a large height but the width is just small you multiply by $K_i$ you will have a small control signal 

now lets push thru time a little bit more with the time $X_2$, you can see that the total time under the curve is is larger, so the control signal keeps pushing harder 

 let's say the error keeps going down until the point $X_3$ at this time, the integrator has accumulated all this green area so now the $u_i(t)$ is quit   large at $X_3$ 

the error at point $X_3$ is zero this is what we want, we want to say to the system just stop we are ok, if the system is intelligent enough it would just stop this is what we want 

but when you think about it the integrator has accumulated and it's like it has some inertia so the system error is going to over shoot it will start going down as we see after $X_3$ it's gonna over shoot the system now what we have it negative area in the red color   

so the control signal is gonna go down but it's still positive as we see after the time $X_3$, what happened is we over shot but the integrator is still pushing in the same direction it's not pushing as hard as it used to but it's still pushing in the same direction

this is gonna get worse before it get's better and at some point we have to accumulate a net deference between the positive and negative area of the error signal

what is gonna happen is that it's eventually it's gonna get us zero steady state error and that's the nice benefit of this control  

we are gonna get to the steady state error only with the integrator controller and only with it, and does this with the exchange of the areas positive and negative and this is why it is coupled with other components to try to get rid of some of these oscillations    

let's talk a little bit more about the claim we made that the integrator will for sure make the SS error zero 

we are gonna explain it in a paradoxical sense 

![Image Description](/images/Pasted%20image%2020250413215100.png)

let's say we have this new error signal, and let's say we have a steady state error let's say that some how we have a non-zero steady state error 

what does the integrator $u_i(t)$ is gonna look like, according to the things we said before we are just integrating the area under the error carve you can see it in the color green 

the control signal will be increasing cuz we only have green positive area so it's going up 

so now think about this if we have a non-zero steady state error the area under the curve is gonna become unbounded it's gonna go to infinity there for the control signal is also gonna go to infinity so there is something very wrong with this system if you have an integrator in it and it keeps pushing harder and harder and harder eventually it have to be able to move the system towards the reference signal

this is the paradox you can't have non-zero steady state because that leads to an unbounded infinite control signal, because if this control signal became large enough it has to eventually be able to move the signal y back to the reference 

the reason of adding the integrator is to get rid of the steady state error

## Derivation Control

this is the last term we are gonna look at, you think we are gonna ignore the proportional and integral term but not quite, the derivation term cant be on it's own don't worry we are gonna explain it now

but for now we are cinda ignoring the proportional and integral terms but actually we aren't, cuz the derivtive control cant operate by it self 
![Image Description](/images/Pasted%20image%2020250413220903.png)

now let's look how the $u_d(t)$ signal looks like

![Image Description](/images/Pasted%20image%2020250413225647.png)

ok again same thing let's assume this step in the error signal, now what is the derivative doing, the derivative  $K_d * \frac{de(t)}{dt}$ is looking at the slope of the error plot and then multiplying it by $K_d$ 

when we look at the time before $X_1$ the error is zero so the $u_d(t)$ will be big fat zero now at the point $X_1$ when we introduced the step we have discontinuity because the slop at point $X_1$ is infinite it just jump from zero to something not zero  instantaneously so the derivative control will have some spike at the point $X_1$ you are gonna get a giant number now maybe the proportional or the integral control is gonna start driving the error signal down after the point $X_1$ 

now i can start looking at the slope at point P1 it's small as you look at point P2 the slope is a little bit steeper and at point P3 it's even more steeper so you get a a higher signal at the control signal 

what is happening is that the $u_d(t)$ is looking at the slope of the error signal to compute what's going to do 

another thing that is interesting to mention here is the steady state behavior, maybe there is zero steady state error maybe there is none-zero steady state error i don't care all i care about is that it's at steady state, what's the slope here? the slope is zero so at any steady state the $u_d(t)$ is zero 

so at the steady state the derivative does nothing 

this control comes to play when there is dynamics 

let's see the dashed error slope is has zero steady state error and this is what we want, we want the error signal to go back to zero 

the signal is flat so the derivative controller is doing nothing so the $u_d(t) = 0$ 
now let's take the IGNORE things away 
![Image Description](/images/Pasted%20image%2020250413230346.png)

now we can talk about all of the terms together cuz that's what a PID controller is when got interplay between all of these components 
we already talked about the $u_p(t)$ idea if you have zero steady state error you have zero error so there for the $u_p(t) = 0$ 

when every thing is perfect the integrator is the only thing that is not zero it is the only thing that is contributing to the controller   

this is the core idea of the PID controller 

IMPORTANT: watch this [vid](https://youtu.be/_VzHpLjKeZ8?si=g_60MByeGy_GCVaE&t=1840) at minute 30:40 to see the practical demonstration of the PID system  
## Reference
- https://www.youtube.com/watch?v=_VzHpLjKeZ8&t=49s

