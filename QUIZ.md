
## Question 1:
```
There is a fair coin (one side heads, one side tails) and an unfair coin (both sides tails). You pick one at random, flip it 5 times, and observe that it comes up as tails all five times. What is the chance that you are flipping the unfair coin?
```

**Notations:**
    B: baised_coin \
    F: fair_coin \
    H: heads \
    T: tails \
    5T: five tails 

**Given:**    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;P(B) = P(F) = 1/2  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Because      P(T / F) = 1/2 = 0.5   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;,therefore   P(5T / F) = (1 / 2)^5 = 0.03125 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Because     P(T / B) = 1   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;,therefore   P(5T / B) = 1

**Objective:**

    P(B / 5T) = ?

**As per the Baye's rule:** \
        P(B / 5T) =  [P(5T / B) * P(B)] / [P(5T / B) * P(B) + P(5T / F) * P(F)] \
i.e.    P(B / 5T) =  [1 * 0.5] / [1 * 0.5 + 0.03125 * 0.5] \
        P(B / 5T) =  0.5 / 0.515625 \
        P(B / 5T) = 0.9696969696969697 \
        P(B / 5T) ~ 0.97

Therefore, there is 97 % that the coin is baised one.

---

## Question 2:
```
Say we have X ~ Uniform(0, 1) and Y ~ Uniform(0, 1). What is the expected value of the minimum of X and Y?
```

---
