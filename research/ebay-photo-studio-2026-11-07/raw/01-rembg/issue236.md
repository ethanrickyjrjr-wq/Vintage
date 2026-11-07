<!-- source: https://github.com/danielgatis/rembg/issues/236, fetched 2026-11-07, http 200, rendered with Playwright -->
                                                          Tweaking to improve results · Issue #236 · danielgatis/rembg · GitHub                                             

[Skip to content](#start-of-content)            

## Navigation Menu

[](/)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Fdanielgatis%2Frembg%2Fissues%2F236)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Fdanielgatis%2Frembg%2Fissues%2F236)

[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Fvoltron%2Fissues_fragments%2Fissue_layout&source=header-repo&source_repo=danielgatis%2Frembg)

Appearance settings

You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert

                 

## Repository navigation

                                                                                                                    [](/danielgatis/rembg)

# Tweaking to improve results #236

[New issue](/login?return_to=https://github.com/danielgatis/rembg/issues/236)

Copy link

[New issue](/login?return_to=https://github.com/danielgatis/rembg/issues/236)

Copy link

Closed

Closed

[Tweaking to improve results](/danielgatis/rembg/issues/236#top)#236

Copy link

## Description

[![@bullmoose20](https://avatars.githubusercontent.com/u/12549033?u=93300476b28e11b4e733ac98c99c5dd353447d66&v=4&size=48)](https://github.com/bullmoose20)

[bullmoose20](https://github.com/bullmoose20)

opened [on May 28, 2022](https://github.com/danielgatis/rembg/issues/236#issue-1251462968)

Issue body actions

If we see anomalies when removing backgrounds, are there tweaks we can make? I am mostly trying to remove backgrounds on people headshots and noticed that sometimes a shoulder or everything below the neck disappears...

## Activity

1.  ### bullmoose20 commented on May 31, 2022
    
    [![@bullmoose20](https://avatars.githubusercontent.com/u/12549033?u=93300476b28e11b4e733ac98c99c5dd353447d66&v=4&size=48)](/bullmoose20)
    
    [bullmoose20](/bullmoose20)
    
    [on May 31, 2022](https://github.com/danielgatis/rembg/issues/236#issuecomment-1142144556)
    
    Author
    
    More actions
    
    Before:  
    [![Josh Gad](https://user-images.githubusercontent.com/12549033/171183293-cc15e671-b1b1-40d2-bb69-41aa42dd89e1.jpg)](https://user-images.githubusercontent.com/12549033/171183293-cc15e671-b1b1-40d2-bb69-41aa42dd89e1.jpg)  
    [![Karl Urban](https://user-images.githubusercontent.com/12549033/171183294-f0b91c1a-ac9b-43de-96e8-e101674028e8.jpg)](https://user-images.githubusercontent.com/12549033/171183294-f0b91c1a-ac9b-43de-96e8-e101674028e8.jpg)
    
    After (using rembg i):  
    [![Josh Gad](https://user-images.githubusercontent.com/12549033/171183488-321a6546-c51f-4011-9ce6-a5bd4fac8a1f.png)](https://user-images.githubusercontent.com/12549033/171183488-321a6546-c51f-4011-9ce6-a5bd4fac8a1f.png)  
    [![Karl Urban](https://user-images.githubusercontent.com/12549033/171183493-10b8ca29-46bc-41dd-9497-28a37ab601e1.png)](https://user-images.githubusercontent.com/12549033/171183493-10b8ca29-46bc-41dd-9497-28a37ab601e1.png)
    
    After (using rembg i a -ae):  
    [![Josh Gad-ae](https://user-images.githubusercontent.com/12549033/171186128-f5a59073-8ac5-45b6-bfa4-358f9cf7f5df.png)](https://user-images.githubusercontent.com/12549033/171186128-f5a59073-8ac5-45b6-bfa4-358f9cf7f5df.png)  
    [![Karl Urban-ae](https://user-images.githubusercontent.com/12549033/171186133-db6567f4-088a-453f-ae61-a48653de5c40.png)](https://user-images.githubusercontent.com/12549033/171186133-db6567f4-088a-453f-ae61-a48653de5c40.png)
    
2.  ### bullmoose20 commented on May 31, 2022
    
    [![@bullmoose20](https://avatars.githubusercontent.com/u/12549033?u=93300476b28e11b4e733ac98c99c5dd353447d66&v=4&size=48)](/bullmoose20)
    
    [bullmoose20](/bullmoose20)
    
    [on May 31, 2022](https://github.com/danielgatis/rembg/issues/236#issuecomment-1142150257)
    
    Author
    
    More actions
    
    Additionally, maybe there is a way for me to specify this somehow?  
    u2net\_cloth\_seg ([download](https://drive.google.com/uc?id=15rKbQSXQzrKCQurUjZFg8HqzZad8bcyz), [source](https://github.com/levindabhi/cloth-segmentation)): A pre-trained model for Cloths Parsing from human portrait. Here clothes are parsed into 3 category: Upper body, Lower body and Full body.
    
    And I think almost all are "Upper body"
    
3.  ### bullmoose20 commented on May 31, 2022
    
    [![@bullmoose20](https://avatars.githubusercontent.com/u/12549033?u=93300476b28e11b4e733ac98c99c5dd353447d66&v=4&size=48)](/bullmoose20)
    
    [bullmoose20](/bullmoose20)
    
    [on May 31, 2022](https://github.com/danielgatis/rembg/issues/236#issuecomment-1142178621)
    
    Author
    
    More actions
    
    rembg i -m u2net\_human\_seg
    
    \--help does not show the -m option  
    README.md does not specify that there is a -m option... I stumbled on this...
    
4.  ### bullmoose20 commented on Jun 7, 2022
    
    [![@bullmoose20](https://avatars.githubusercontent.com/u/12549033?u=93300476b28e11b4e733ac98c99c5dd353447d66&v=4&size=48)](/bullmoose20)
    
    [bullmoose20](/bullmoose20)
    
    [on Jun 7, 2022](https://github.com/danielgatis/rembg/issues/236#issuecomment-1148913257)
    
    Author
    
    More actions
    
    While this is a better option and I get better results, I would still like to know how I can contribute to the model to improve it. I have about 200 people headshots before and after background removal and would like to know how I can contribute to the community?
    
5.  ### ArielMAJ commented on Jun 10, 2022
    
    [![@ArielMAJ](https://avatars.githubusercontent.com/u/69123486?u=06b53d4db324eb4642638e32f5cce64819194624&v=4&size=48)](/ArielMAJ)
    
    [ArielMAJ](/ArielMAJ)
    
    [on Jun 10, 2022](https://github.com/danielgatis/rembg/issues/236#issuecomment-1151909586)
    
    More actions
    
    I ran into this same thing and u2net\_human\_seg helped too.
    
    As for improving upon the model, I'm pretty sure you should be able to train your own model (or train u2net\_human\_seg with your own images) and use it. Pretty sure it isn't an easy task either. GL!
    
6.  ### alcinopitchprint commented on Jun 29, 2022
    
    [![@alcinopitchprint](https://avatars.githubusercontent.com/u/68546445?v=4&size=48)](/alcinopitchprint)
    
    [alcinopitchprint](/alcinopitchprint)
    
    [on Jun 29, 2022](https://github.com/danielgatis/rembg/issues/236#issuecomment-1170022481)
    
    More actions
    
    The training process is explained here by [@endh1337](https://github.com/endh1337) , [#193 (comment)](https://github.com/danielgatis/rembg/issues/193#issuecomment-1055534289)
    
    Reacted by Ariel Menezes and Daniel Gatis
    
    Reacted by Dominik Hoffmann
    
7.  [![](https://avatars.githubusercontent.com/u/7380?s=64&u=11bfe344ea77d1e8ba6c14611cdf40beb11bc249&v=4)danielgatis](/danielgatis)
    
    closed this as [completed](/danielgatis/rembg/issues?q=is%3Aissue%20state%3Aclosed%20archived%3Afalse%20reason%3Acompleted)[on Jul 6, 2022](https://github.com/danielgatis/rembg/issues/236#event-6944582789)
    

[Sign up for free](/signup?return_to=https://github.com/danielgatis/rembg/issues/236) **to join this conversation on GitHub.** Already have an account? [Sign in to comment](/login?return_to=https://github.com/danielgatis/rembg/issues/236)

## Metadata

## Metadata

### Assignees

No one assigned

### Labels

No labels

No labels

### Projects

No projects

### Milestone

No milestone

### Relationships

None yet

### Development

No branches or pull requests

## Issue actions

-

You can’t perform that action at this time.
