## Name
reflect — calculate the reflection direction for an incident vector
## Declaration  
|  `genType **reflect**(`  | genType I,   |  
| --- | --- |  
|   | genType N`)`;  |  
|  `genDType **reflect**(`  | genDType I,   |  
| --- | --- |  
|   | genDType N`)`;  |  
## Parameters 

_`I` _ 
    
Specifies the incident vector.  

_`N` _ 
    
Specifies the normal vector. 
## Description
For a given incident vector _`I`_and surface normal _`N`_`reflect` returns the reflection direction calculated as `_`I`_- 2.0 *`dot`(_`N`_,_`I`_) *_`N`_`.
_`N`_should be normalized in order to achieve the desired result.
## Version Support  
|   |  **OpenGL Shading Language Version**  |  
| --- | --- |  
|  **Function Name**  |  **1.10**  |  **1.20**  |  **1.30**  |  **1.40**  |  **1.50**  |  **3.30**  |  **4.00**  |  **4.10**  |  **4.20**  |  **4.30**  |  **4.40**  |  **4.50**  |  **4.60**  |  
| reflect (genType)  | ✔  | ✔  | ✔  | ✔  | ✔  | ✔  | ✔  | ✔  | ✔  | ✔  | ✔  | ✔  | ✔  |  
| reflect (genDType)  | -  | -  | -  | -  | -  | -  | ✔  | ✔  | ✔  | ✔  | ✔  | ✔  | ✔  |  
## See Also
[dot](https://registry.khronos.org/OpenGL-Refpages/gl4/html/dot.xhtml), [refract](https://registry.khronos.org/OpenGL-Refpages/gl4/html/refract.xhtml)
## Copyright
Copyright © 2011-2014 Khronos Group. This material may be distributed subject to the terms and conditions set forth in the Open Publication License, v 1.0, 8 June 1999. <https://opencontent.org/openpub/>. 

