# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 17:14:13 2021
You are a physics teacher preparing for the upcoming semester.
You want to provide your students with some functions that will help them calculate some fundamental physical properties.
@author: Sarp
"""

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
def f_to_c(f_temp):
  c_temp=(f_temp-32)*5/9
  return c_temp
print('F to c:',f_to_c(100))
def c_to_f(c_temp):
  f_temp=(c_temp)*9/5+32
  return f_temp
c0_in_fahrenheit=c_to_f(0)
print('C to f:',c0_in_fahrenheit)
def get_force(mass,acceleration):
  return mass*acceleration
train_force=get_force(train_mass,train_acceleration)
print('The GE train supplies', train_force,' Newtons of force')
def get_energy(mass,c=3*10**8):
  return mass*c**2
bomb_energy=get_energy(bomb_mass)
print('A', bomb_mass, 'kg bomb supplies', bomb_energy, 'Joules.')
def get_work(mass,acceleration,distance):
  return get_force(mass,acceleration)*distance
train_work=get_work(train_mass,train_acceleration,train_distance)
print('The GE train does ', train_work,' of work over', train_distance,'meters.')