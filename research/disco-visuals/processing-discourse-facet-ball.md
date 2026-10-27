[ Skip to last reply ](https://discourse.processing.org/t/is-it-possible-to-have-the-reflect-of-light-of-facet-ball-disco-ball/32532/3) [ Skip to top ](https://discourse.processing.org/t/is-it-possible-to-have-the-reflect-of-light-of-facet-ball-disco-ball/32532/1)
[ Skip to main content ](https://discourse.processing.org/t/is-it-possible-to-have-the-reflect-of-light-of-facet-ball-disco-ball/32532#main-container)
[ ![Processing Community Forum](https://canada1.discourse-cdn.com/flex036/uploads/processingfoundation1/original/3X/6/d/6d1aa58a1166fbd482b924fd547c339b346e7e0d.png) ](https://discourse.processing.org/)
Sign Up Log In
  * ​ 
  * ​ 


#  [ Is it possible to have the reflect of light of facet ball? (Disco ball) ](https://discourse.processing.org/t/is-it-possible-to-have-the-reflect-of-light-of-facet-ball-disco-ball/32532)
[Processing](https://discourse.processing.org/c/processing/6)[Coding Questions](https://discourse.processing.org/c/processing/processing-questions/15)
You have selected **0** posts.
[ select all ](https://discourse.processing.org/t/is-it-possible-to-have-the-reflect-of-light-of-facet-ball-disco-ball/32532)
[ cancel selecting ](https://discourse.processing.org/t/is-it-possible-to-have-the-reflect-of-light-of-facet-ball-disco-ball/32532)
[ Sep 2021  ](https://discourse.processing.org/t/is-it-possible-to-have-the-reflect-of-light-of-facet-ball-disco-ball/32532/1 "Jump to the first post")
1 / 3 
Sep 2021 
[ Oct 2021 ](https://discourse.processing.org/t/is-it-possible-to-have-the-reflect-of-light-of-facet-ball-disco-ball/32532/3)
##  post by bking on Sep 30, 2021 
[ ![](https://avatars.discourse-cdn.com/v4/letter/b/dc4da7/48.png) ](https://discourse.processing.org/u/bking)
[ bking  ](https://discourse.processing.org/u/bking)
2
[ Sep 2021 ](https://discourse.processing.org/t/is-it-possible-to-have-the-reflect-of-light-of-facet-ball-disco-ball/32532 "Post date")
Hello,  
I made a program with two balls which returns the light coming from different place thanks to the mouse.  
I would like to change these balls into a mirror ball (like in clubs) and have the rays of light returned by the mirror ball.  
Thanks for your ideas.

```




/**
 * Spot. 
 * 
 * Move the mouse the change the position and concentation
 * of a blue spot light. 
 */
 
int concentration = 600; // Try values 1 -> 10000
float move=0.00001;
float x;
void setup() {
  size(640, 360, P3D);
  noStroke();
    colorMode(RGB, 1);
  fill(0.9);
  sphereDetail(60);
}

void draw() {
  background(0); 
 
  
  // Orange light on the upper-right of the sphere
  spotLight(204, 153, 0, 360, 160, 600, 0, 0, -1, PI/2, 600); 
     float s = mouseX / float(width);
  // Light the bottom of the sphere
  s=0;
  directionalLight(s*51+51, 102, 126, 0, -1, 0);
  
  // Moving spotlight that follows the mouse
  spotLight(102, 153, 204,mouseX , mouseY, 600, 0, 0, -1, PI/2, 600); 
  
  
  float d = mouseX / float(width);
    directionalLight(0.8, 0.8, 0.8, d, 0, -1);
     lightSpecular(1, 1, 1);
  translate(width/2, height/2, 0); 
  move+=0.01;
  x= 100*cos(move);
  print (x);
  
  translate(30+x, 200, -500);
  
  sphere(120); 
  spotLight(102, 153, 204, 300, mouseY, 600, 0, 0, -1, PI/2, 600); 
   translate(30+7*x, -200, 0); 
   
  sphere(120); 
}

```

  

​ 
​ 
473 views 
[ ![](https://yyz2.discourse-cdn.com/flex036/user_avatar/discourse.processing.org/micuat/48/19407_2.png) ](https://discourse.processing.org/u/micuat "micuat")
[ ![](https://avatars.discourse-cdn.com/v4/letter/b/dc4da7/48.png) ](https://discourse.processing.org/u/bking "bking")
[ ![](https://yyz2.discourse-cdn.com/flex036/user_avatar/discourse.processing.org/jb4x/48/789_2.png) ](https://discourse.processing.org/u/jb4x "jb4x")
8 days later 
##  post by micuat on Oct 8, 2021 
[ ![](https://yyz2.discourse-cdn.com/flex036/user_avatar/discourse.processing.org/micuat/48/19407_2.png) ](https://discourse.processing.org/u/micuat)
[ micuat  ](https://discourse.processing.org/u/micuat)
[ Oct 2021 ](https://discourse.processing.org/t/is-it-possible-to-have-the-reflect-of-light-of-facet-ball-disco-ball/32532/2 "Post date")
Unfortunately, it’s actually very difficult. To get an idea in 2D, Dan made some videos about it
![](https://img.youtube.com/vi/TOEi6T2mtHo/maxresdefault.jpg)
[ Coding Challenge #145: 2D Raycasting ](https://www.youtube.com/watch?v=TOEi6T2mtHo "Coding Challenge #145: 2D Raycasting")
If you want to do it in 3D in real time, you need to work a lot on shaders (GLSL). And just to give you a tip, Unity, for example, has built in support for [reflection](https://docs.unity3d.com/Manual/class-ReflectionProbe.html) - but it’s not bouncing off the light, and it’s about rendering the mirror surface.  
[ ![](https://docs.unity3d.com/uploads/Main/ReflectionProbeScene.jpg) ](https://docs.unity3d.com/uploads/Main/ReflectionProbeScene.jpg)
What I would suggest is to play around with Dan’s example - if you are going for photorealism, surely it’s easier with Unity/Blender/etc but I think the fun part of Processing is to do something “wrong” and make fun stuff ![:slight_smile:](https://emoji.discourse-cdn.com/google_classic/slight_smile.png?v=12)
  

​ 
​ 
##  post by jb4x on Oct 8, 2021 
Reply
  

###  Related topics   
Topic list, column headers with buttons are sortable.  
|  Topic   |  Replies   |  Views   |  Activity   |  
| --- | --- | --- | --- |  
|  [How to make a mirror ball? like in a nightclub](https://discourse.processing.org/t/how-to-make-a-mirror-ball-like-in-a-nightclub/32667) [Coding Questions](https://discourse.processing.org/c/processing/processing-questions/15)  |  [ 5 ](https://discourse.processing.org/t/how-to-make-a-mirror-ball-like-in-a-nightclub/32667/1)  |  498  |  [Oct 2021](https://discourse.processing.org/t/how-to-make-a-mirror-ball-like-in-a-nightclub/32667/6)  |  
|  [Light reflection](https://discourse.processing.org/t/light-reflection/33177) [Coding Questions](https://discourse.processing.org/c/processing/processing-questions/15)  |  [ 3 ](https://discourse.processing.org/t/light-reflection/33177/1)  |  350  |  [Oct 2021](https://discourse.processing.org/t/light-reflection/33177/4)  |  
|  [How to create a 3D geometry with faceted reflection of light (sphere)](https://discourse.processing.org/t/how-to-create-a-3d-geometry-with-faceted-reflection-of-light-sphere/40932) [Coding Questions](https://discourse.processing.org/c/p5js/p5js-questions/18)  |  [ 7 ](https://discourse.processing.org/t/how-to-create-a-3d-geometry-with-faceted-reflection-of-light-sphere/40932/1)  |  366  |  [Feb 2023](https://discourse.processing.org/t/how-to-create-a-3d-geometry-with-faceted-reflection-of-light-sphere/40932/8)  |  
|  [Interactive 3D balls. Is this even possible in Processing?](https://discourse.processing.org/t/interactive-3d-balls-is-this-even-possible-in-processing/39056) [Coding Questions](https://discourse.processing.org/c/p5js/p5js-questions/18)
  * [homework](https://discourse.processing.org/tag/homework/1)

 |  [ 14 ](https://discourse.processing.org/t/interactive-3d-balls-is-this-even-possible-in-processing/39056/1)  |  655  |  [Oct 2022](https://discourse.processing.org/t/interactive-3d-balls-is-this-even-possible-in-processing/39056/15)  |  
|  [Making a light inside the room](https://discourse.processing.org/t/making-a-light-inside-the-room/21164) [Coding Questions](https://discourse.processing.org/c/processing/processing-questions/15)
  * [homework](https://discourse.processing.org/tag/homework/1)

 |  [ 14 ](https://discourse.processing.org/t/making-a-light-inside-the-room/21164/1)  |  879  |  [Jun 2020](https://discourse.processing.org/t/making-a-light-inside-the-room/21164/18)  |

