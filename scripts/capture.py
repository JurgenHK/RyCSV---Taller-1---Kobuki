#!/usr/bin/python3.8

from pynput import keyboard

class logger:

    def __init__(self):
        self.v = 0
        self.w = 0
        self.multiplier_lineal = 1
        self.multiplier_angular = 1

        # Collect events until released
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release) 
        self.listener.start()

    def on_press(self, key):
        #if pressed in self.commands:
        #print('{0} pressed'.format(key))
        self.command(str(key))
        #self.compute_speed()

    def on_release(self, key):
        #print('{0} release'.format(key))
        self.stop()
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    def compute_speed(self):
        phi_1 = self.v - (self.w/2)
        phi_2 = self.v + (self.w/2)
        return phi_1, phi_2

    def command(self, case):
        if case == 'Key.up':
            return self.forwards()
        if case == 'Key.down':
            return self.backwards()
        if case == 'Key.left':
            return self.left()
        if case == 'Key.right':
            return self.right()
        if case == "'p'":
            return self.stop()
        if case == "'s'":
            return self.stop_keyboard()
        if case == "'+'":
            return self.increment()
        if case == "'-'":
            return self.decrement()

    def forwards(self):
        #print("Case Forward")
        self.v = 1*self.multiplier_lineal
        self.w = 0*self.multiplier_angular
    
    def backwards(self):
        #print("Case Back")
        self.v = -1*self.multiplier_lineal
        self.w = 0*self.multiplier_angular

    def left(self):
        #print("Case Left")
        self.v = 0*self.multiplier_lineal
        self.w = 1*self.multiplier_angular

    def right(self):
        #print("Case Right")
        self.v = 0*self.multiplier_lineal
        self.w = -1*self.multiplier_angular
    
    def stop(self):
        #print("Case Stop")
        self.v = 0
        self.w = 0

    def increment(self):
        print("Case Increment")
        self.multiplier_lineal += 0.1 if self.multiplier_lineal < 1 else 0
        self.multiplier_angular += 2.0 if self.multiplier_angular < 180 else 0
         

    def decrement(self):
        print("Case Increment")
        self.multiplier_lineal -= 0.5 if self.multiplier_lineal > 0 else 0
        self.multiplier_angular -= 2.0 if self.multiplier_angular > -0 else 0

    def get_targets(self):
        return self.v,self.w

    def stop_keyboard(self):
        self.stop()
        self.listener.stop()






