# Pong project by Suyash Gautam

import random
import simplegui


# Initialize variables
br = 12
bv = [random.randrange(2,4), -random.randrange(1,3)]
h=600
w=1000
bp = [w/2,h/2] 
pw = 15
ph = 120
hpw = pw/2
hph = ph/2
p1pos = float(h/2)
p2pos = float(h/2)
pad1v = float(0)
pad2v = float(0)
score1 = 0
score2 = 0




def spawn_ball(right):
    global bv, bp
    bp = [w/2,h/2]
    
    if right:
        bv = [random.randrange(3,5), -random.randrange(2,4)]
    else:
        bv = [-random.randrange(3,5), -random.randrange(2,4)]

def new_game():
    global p1pos, p2pos, pad1v, pad2v
    bp = [w/2, h/2]
    global score1, score2
    score1 = 0 
    score2 = 0    
    p1pos = float(h/2)
    p2pos = float(h/2)
    pad1v = 0.0
    pad2v = 0.0
    spawn_ball(True) # will spawn to the right

def draw(canvas):
    global bv, bp, p1pos, p2pos, score1, score2
    # Update ball position
    bp[0] = bp[0] + bv[0]
    bp[1] = bp[1] + bv[1]
    canvas.draw_circle(bp, br, 10, "red", "White")
    # write collision rules
   
    # collide and reflect of the bottom size of the canvas
    if bp[1] <= br:
        bv[1] *= -1.02
    # collide and reflect from the top side
    if bp[1] >= (h - br):
        bv[1] *= -1.02
        
    #collision from the left pad
    # if it hits the left gutter
    if bp[0] <= (br + pw):
         # if it hits the pad on the left gutter
        if (p1pos - hph <= bp[1] <= p1pos + hph):
            bv[0] *= -1.1
            bv[1] *= 1.1
        else:
            score2 += 1
            spawn_ball(True)
    # if it hits the right pad
    elif bp[0] >= (w - pw - br) :
            if (p2pos - hph <= bp[1] <= p2pos + hph):
                bv[0] *= -1.1
                bv[1] *= 1.1
            else:
                score1 += 1
                spawn_ball(False)
    #Drawing Pad 1 and 2
    canvas.draw_polygon([(0, p1pos - hph), (pw, p1pos - hph), (pw, p1pos + hph), (0, p1pos + hph)], 1, "White", "White")
    canvas.draw_polygon([(w - pw, p2pos - hph), (w, p2pos - hph), (w, p2pos + hph), (w - pw, p2pos + hph)], 1, "White", "White")
    
    #Keeping the pads on the screen
    if p1pos + pad1v >= hph and p1pos + pad1v <= (h-hph):
        p1pos = p1pos + pad1v
    if p2pos + pad2v >= hph and p2pos + pad2v <= (h-hph):
        p2pos = p2pos + pad2v
    # drawing gutters
    canvas.draw_line([w / 2, 0],[w / 2, h], 4, "White")	#midline
    canvas.draw_line([pw, 0],[pw, h], 4, "White")	#left gutter
    canvas.draw_line([w - pw, 0],[w - pw, h], 4, "White")	#right gutter
    canvas.draw_text(str(score1), [100, 100], 52, "White")
    canvas.draw_text(str(score2), [900, 100], 52, "White")
 
    

# Moving paddle 1
def keydown(key):
    global pad1v, pad2v
    padacc = 8
    if key == simplegui.KEY_MAP["w"]:
        pad1v = pad1v - padacc
    elif key == simplegui.KEY_MAP["s"]:
        pad1v = pad1v + padacc
    elif key == simplegui.KEY_MAP["up"]:
        pad2v = pad2v - padacc    
    elif key == simplegui.KEY_MAP["down"]:
        pad2v = pad2v + padacc    
        
# Moving paddle 1
def keyup(key):
    global pad1v, pad2v
    padacc = 5
    if key == simplegui.KEY_MAP["w"]:
        pad1v = 0
    elif key == simplegui.KEY_MAP["s"]:
        pad1v = 0
    elif key == simplegui.KEY_MAP["up"]:
        pad2v = 0
    elif key == simplegui.KEY_MAP["down"]:
        pad2v = 0
    
frame = simplegui.create_frame("Pong by Suyash", w, h)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game)


frame.start()
new_game()    
    
