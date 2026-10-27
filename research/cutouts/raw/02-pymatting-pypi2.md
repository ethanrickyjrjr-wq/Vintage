[Skip to main content](https://pypi.org/project/PyMatting/#content) Switch to mobile version
Security notice: Upgrade certifi, pip, and uv in response to CA certificate incident [See more](https://discuss.python.org/t/information-for-python-users-regarding-emudhra-emsign-ca-certificate-security-incident/109576)
[ ![PyPI](https://pypi.org/static/images/logo-small.0e0855d0.svg) ](https://pypi.org/)
Search PyPI Search
  * [Docs](https://docs.pypi.org/)
  * [Blog](https://blog.pypi.org)
  * [Log in](https://pypi.org/account/login/?next=https%3A%2F%2Fpypi.org%2Fproject%2FPyMatting%2F)
  * [Register](https://pypi.org/account/register/)


  * [Docs](https://docs.pypi.org/)
  * [Blog](https://blog.pypi.org)
  * [Log in](https://pypi.org/account/login/?next=https%3A%2F%2Fpypi.org%2Fproject%2FPyMatting%2F)
  * [Register](https://pypi.org/account/register/)


  * Deutsch 
  * English 
  * español 
  * Esperanto 
  * français 
  * português (Brasil) 
  * Ελληνικά 
  * русский 
  * українська 
  * עברית 
  * 中文 (简体) 
  * 中文 (繁體) 
  * 日本語 
  * 한국어 


Search PyPI Search
# PyMatting 1.1.16
Python package for alpha matting.
pip install PyMatting Copy PIP instructions
  * [ Description  ](https://pypi.org/project/PyMatting/#description)
  * [ Metadata  ](https://pypi.org/project/PyMatting/#metadata)
  * [ Release files  ](https://pypi.org/project/PyMatting/#files)
  * [ Security  ](https://pypi.org/project/PyMatting/#security)
  * [ Release history  ](https://pypi.org/project/PyMatting/#history)


#  [](https://pypi.org/project/PyMatting/#user-content-pymatting-a-python-library-for-alpha-matting)PyMatting: A Python Library for Alpha Matting
[![License: MIT](https://pypi-camo.freetls.fastly.net/77842b88a8c23408316a977512d44ed95db4e988/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f70796d617474696e672f70796d617474696e673f636f6c6f723d627269676874677265656e)](https://opensource.org/licenses/MIT) [![CI](https://pypi-camo.freetls.fastly.net/ded4d33baf230fb6b295652ad75ee9d6b7696b2f/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f70796d617474696e672f70796d617474696e672f2e6769746875622f776f726b666c6f77732f74657374732e796d6c3f6272616e63683d6d6173746572)](https://github.com/pymatting/pymatting/actions?query=workflow%3Atests) [![PyPI](https://pypi-camo.freetls.fastly.net/6e34b3e3062cf78e598eb20b6e9261bc7b1b561b/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f70796d617474696e67)](https://pypi.org/project/PyMatting/) [![JOSS](https://pypi-camo.freetls.fastly.net/e4e7e6f7d4c9627c8a840d830a1d1c357473eb1b/68747470733a2f2f6a6f73732e7468656f6a2e6f72672f7061706572732f39373636636162363562666266303761373063386138333565646433383735612f7374617475732e737667)](https://joss.theoj.org/papers/9766cab65bfbf07a70c8a835edd3875a) [![Documentation](https://pypi-camo.freetls.fastly.net/c893630ef2f360e1d7753442ac3e021d448865ae/68747470733a2f2f70796d617474696e672e6769746875622e696f2f646f63735f6f6e6c696e652e737667)](https://pymatting.github.io/)
We introduce the PyMatting package for Python, which implements various methods to solve the alpha matting problem.
  * **Website and Documentation:** [https://pymatting.github.io/](https://pymatting.github.io)
  * **Benchmarks:** <https://pymatting.github.io/benchmarks.html>


![Lemur](https://pypi-camo.freetls.fastly.net/4aaf600284d8076ca4b5dbda88668700cc60d206/68747470733a2f2f6769746875622e636f6d2f70796d617474696e672f70796d617474696e672f7261772f6d61737465722f646174612f6c656d75722f6c656d75725f61745f7468655f62656163682e706e67)
Given an input image and a hand-drawn trimap (top row), alpha matting estimates the alpha channel of a foreground object which can then be composed onto a different background (bottom row).
PyMatting provides:
  * Alpha matting implementations for: 
    * Closed Form Alpha Matting [[1]](https://pypi.org/project/PyMatting/#user-content-1)
    * Large Kernel Matting [[2]](https://pypi.org/project/PyMatting/#user-content-2)
    * KNN Matting [[3]](https://pypi.org/project/PyMatting/#user-content-3)
    * Learning Based Digital Matting [[4]](https://pypi.org/project/PyMatting/#user-content-4)
    * Random Walk Matting [[5]](https://pypi.org/project/PyMatting/#user-content-5)
    * Shared Sampling Matting [[6]](https://pypi.org/project/PyMatting/#user-content-6)
  * Foreground estimation implementations for: 
    * Closed Form Foreground Estimation [[1]](https://pypi.org/project/PyMatting/#user-content-1)
    * Fast Multi-Level Foreground Estimation (CPU, CUDA and OpenCL) [[7]](https://pypi.org/project/PyMatting/#user-content-7)
  * Fast multithreaded KNN search
  * Preconditioners to accelerate the convergence rate of conjugate gradient descent: 
    * The _incomplete thresholded Cholesky decomposition_ (_Incomplete_ is part of the name. The implementation is quite complete.)
    * The V-Cycle Geometric Multigrid preconditioner
  * Readable code leveraging [NumPy](https://numpy.org/), [SciPy](https://scipy.org/) and [Numba](http://numba.pydata.org/)


##  [](https://pypi.org/project/PyMatting/#user-content-getting-started)Getting Started
###  [](https://pypi.org/project/PyMatting/#user-content-requirements)Requirements
Minimal requirements
  * numpy>=1.16.0
  * pillow>=5.2.0
  * numba>=0.47.0
  * scipy>=1.1.0


Additional requirements for GPU support
  * cupy-cuda90>=6.5.0 or similar
  * pyopencl>=2019.1.2


Requirements to run the tests
  * pytest>=5.3.4


###  [](https://pypi.org/project/PyMatting/#user-content-installation-with-pypi)Installation with PyPI

```
pip3 install pymatting

```

###  [](https://pypi.org/project/PyMatting/#user-content-installation-from-source)Installation from Source

```
git clone https://github.com/pymatting/pymatting
cd pymatting
pip3 install .

```

##  [](https://pypi.org/project/PyMatting/#user-content-example)Example

```
# First import will take a minute due to compilation
from pymatting import cutout

cutout(
    # input image path
    "data/lemur/lemur.png",
    # input trimap path
    "data/lemur/lemur_trimap.png",
    # output cutout path
    "lemur_cutout.png")

```

Alternatively, you can use `pymatting` CLI tool.

```
pymatting data/lemur/lemur.png data/lemur/lemur_trimap.png lemur_cutout.png

```

[More advanced examples](https://pymatting.github.io/examples.html)
##  [](https://pypi.org/project/PyMatting/#user-content-trimap-construction)Trimap Construction
All implemented methods rely on trimaps which roughly classify the image into foreground, background and unknown regions. Trimaps are expected to be `numpy.ndarrays` of type `np.float64` having the same shape as the input image with only one color-channel. Trimap values of 0.0 denote pixels which are 100% background. Similarly, trimap values of 1.0 denote pixels which are 100% foreground. All other values indicate unknown pixels which will be estimated by the algorithm.
##  [](https://pypi.org/project/PyMatting/#user-content-testing)Testing
Run the tests from the main directory:

```
pip3 install -r .[test]
pytest

```

Currently 89% of the code is covered by tests.
##  [](https://pypi.org/project/PyMatting/#user-content-upgrade)Upgrade

```
pip3 install --upgrade pymatting
python3 -c "import pymatting"

```

##  [](https://pypi.org/project/PyMatting/#user-content-gpu-support)GPU-Support
There is [CuPy](https://pymatting.github.io/foreground.html#estimate_foreground_ml_cupy) and [PyOpenCL](https://pymatting.github.io/foreground.html#estimate_foreground_ml_pyopencl) support for foreground estimation.

```
pip3 install -r .[gpu]
pytest tests/test_foreground.py

```

You still need to install proper drivers for GPU support separately.
If you have installed drivers, but CuPy can not find `libnvrtc.so.12`, you might have link to CUDA libraries manually:

```
sudo apt install plocate
# might resolve to something like /home/user/myenv/lib/python3.12/site-packages/nvidia/cuda_nvrtc/lib/
export LD_LIBRARY_PATH="$(dirname $(locate libnvrtc.so.12)):$LD_LIBRARY_PATH"

```

For PyOpenCL, see [docs](https://documen.tician.de/pyopencl/misc.html). You can select computing device by setting `PYOPENCL_CTX` environment variable.
There currently is no GPU support for alpha estimation, only for foreground estimation.
##  [](https://pypi.org/project/PyMatting/#user-content-bug-reports-questions-and-pull-requests)Bug Reports, Questions and Pull-Requests
Please, see [our community guidelines](https://github.com/pymatting/pymatting/blob/master/CONTRIBUTING.md).
##  [](https://pypi.org/project/PyMatting/#user-content-authors)Authors
  * **Thomas Germer**
  * **Tobias Uelwer**
  * **Stefan Conrad**
  * **Stefan Harmeling**


See also the list of [contributors](https://github.com/pymatting/pymatting/contributors) who participated in this project.
##  [](https://pypi.org/project/PyMatting/#user-content-projects-using-pymatting)Projects using PyMatting
  * [Rembg](https://github.com/danielgatis/rembg) - an excellent tool for removing image backgrounds.
  * [PaddleSeg](https://github.com/PaddlePaddle/PaddleSeg) - a library for a wide range of image segmentation tasks.
  * [chaiNNer](https://github.com/chaiNNer-org/chaiNNer) - a node-based image processing GUI.
  * [LSA-Matting](https://github.com/kfeng123/LSA-Matting) - improving deep image matting via local smoothness assumption.
  * [Prickly Gorse Interactive Background Remover](https://github.com/pricklygorse/Interactive-Image-Background-Remover) - a user friendly GUI application for detailed background removal using several models and post-processing features
  * [PyMatting Interactive Tool](https://github.com/pymatting/pymatting-interactive-tool) - background removal with live preview


##  [](https://pypi.org/project/PyMatting/#user-content-license)License
This project is licensed under the MIT License - see the [LICENSE.md](https://pypi.org/project/PyMatting/LICENSE.md) file for details
##  [](https://pypi.org/project/PyMatting/#user-content-citing)Citing
If you found PyMatting to be useful for your work, please consider citing our [paper](https://doi.org/10.21105/joss.02481):

```
@article{Germer2020,
  doi = {10.21105/joss.02481},
  url = {https://doi.org/10.21105/joss.02481},
  year = {2020},
  publisher = {The Open Journal},
  volume = {5},
  number = {54},
  pages = {2481},
  author = {Thomas Germer and Tobias Uelwer and Stefan Conrad and Stefan Harmeling},
  title = {PyMatting: A Python Library for Alpha Matting},
  journal = {Journal of Open Source Software}
}

```

##  [](https://pypi.org/project/PyMatting/#user-content-references)References
[1] Anat Levin, Dani Lischinski, and Yair Weiss. A closed-form solution to natural image matting. IEEE transactions on pattern analysis and machine intelligence, 30(2):228–242, 2007.
[2] Kaiming He, Jian Sun, and Xiaoou Tang. Fast matting using large kernel matting laplacian matrices. In 2010 IEEE Computer Society Conference on Computer Vision and Pattern Recognition, 2165–2172. IEEE, 2010.
[3] Qifeng Chen, Dingzeyu Li, and Chi-Keung Tang. Knn matting. IEEE transactions on pattern analysis and machine intelligence, 35(9):2175–2188, 2013.
[4] Yuanjie Zheng and Chandra Kambhamettu. Learning based digital matting. In 2009 IEEE 12th international conference on computer vision, 889–896. IEEE, 2009.
[5] Leo Grady, Thomas Schiwietz, Shmuel Aharon, and Rüdiger Westermann. Random walks for interactive alpha-matting. In Proceedings of VIIP, volume 2005, 423–429. 2005.
[6] Eduardo S. L. Gastal and Manuel M. Oliveira. "Shared Sampling for Real-Time Alpha Matting". Computer Graphics Forum. Volume 29 (2010), Number 2, Proceedings of Eurographics 2010, pp. 575-584.
[7] Germer, T., Uelwer, T., Conrad, S., & Harmeling, S. (2020). Fast Multi-Level Foreground Estimation. arXiv preprint arXiv:2006.14970.
Lemur image by Mathias Appel from <https://www.flickr.com/photos/mathiasappel/25419442300/> licensed under [CC0 1.0 Universal (CC0 1.0) Public Domain License](https://creativecommons.org/publicdomain/zero/1.0/).
## Project links
  * [ Homepage](https://pymatting.github.io)
  * [ Source](https://github.com/pymatting/pymatting)


## Key dates
PyPI data
Data sourced directly from PyPI's database.
  * **Released:** Sep 8, 2026

Latest release
##  1 maintainer 
PyPI data
Data sourced directly from PyPI's database.
[ ![Avatar for PyMatting from gravatar.com](https://pypi-camo.freetls.fastly.net/d1b06ab6b6656af3d54d1fd9afdcee8b76404405/68747470733a2f2f7365637572652e67726176617461722e636f6d2f6176617461722f62373633333962646563303937393633633862376563313864343763623232323f73697a653d3335) PyMatting ](https://pypi.org/user/PyMatting/)
## Credits
**Author:** The PyMatting Developers
## License
MIT License (MIT)
## Requires
**Python** >=3
## Provides Extra
`gpu` `test`
## Tags
`alpha` `matting`
## Classifiers
  * License 
    * [ OSI Approved :: MIT License ](https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+MIT+License)
  * Operating System 
    * [ OS Independent ](https://pypi.org/search/?c=Operating+System+%3A%3A+OS+Independent)
  * Programming Language 
    * [ Python :: 3 ](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3)


## Metadata
## Project links
  * [ Homepage](https://pymatting.github.io)
  * [ Source](https://github.com/pymatting/pymatting)


## Key dates
PyPI data
Data sourced directly from PyPI's database.
  * **Released:** Sep 8, 2026

Latest release
##  1 maintainer 
PyPI data
Data sourced directly from PyPI's database.
[ ![Avatar for PyMatting from gravatar.com](https://pypi-camo.freetls.fastly.net/d1b06ab6b6656af3d54d1fd9afdcee8b76404405/68747470733a2f2f7365637572652e67726176617461722e636f6d2f6176617461722f62373633333962646563303937393633633862376563313864343763623232323f73697a653d3335) PyMatting ](https://pypi.org/user/PyMatting/)
## Credits
**Author:** The PyMatting Developers
## License
MIT License (MIT)
## Requires
**Python** >=3
## Provides Extra
`gpu` `test`
## Tags
`alpha` `matting`
## Classifiers
  * License 
    * [ OSI Approved :: MIT License ](https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+MIT+License)
  * Operating System 
    * [ OS Independent ](https://pypi.org/search/?c=Operating+System+%3A%3A+OS+Independent)
  * Programming Language 
    * [ Python :: 3 ](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3)


## Release files for PyMatting 1.1.16
For a detailed explanation of source distributions (sdists) and built distributions (wheels), please see the [package formats documentation](https://packaging.python.org/en/latest/discussions/package-formats/#package-formats "External link"). 
###  Source distribution (sdist)   
Source distribution for PyMatting 1.1.16  
| File  | Size  | Uploaded  | Provenance  |   |  
| --- | --- | --- | --- | --- |  
|  [ pymatting-1.1.16.tar.gz](https://files.pythonhosted.org/packages/75/4b/01a653f1ec2a69b1579d9ff47578b41bc432216f1a2b6e57cf37f725a95b/pymatting-1.1.16.tar.gz)  | 45.3 kB  |  Sep 8, 2026  |  Without provenance  |  [Details](https://pypi.org/project/PyMatting/#pymatting-1.1.16.tar.gz)  |  
* * *
###  Built distribution (wheel)   
Table of built distributions (wheels) for PyMatting 1.1.16  
| File  |  Interpreter   |  ABI   |  Platform   |  [Reset](https://pypi.org/project/PyMatting/#files)  |  
| --- | --- | --- | --- | --- |  
|  [ pymatting-1.1.16-py3-none-any.whl](https://files.pythonhosted.org/packages/47/8e/2c00f3615fc906c01f5168d2caedf61811db6259b8d0c9a1b14d7c9af61a/pymatting-1.1.16-py3-none-any.whl) 56.3 kB Sep 8, 2026 Without provenance  |  Python 3   |  none   |  any   |  [Details](https://pypi.org/project/PyMatting/#pymatting-1.1.16-py3-none-any.whl)  |  
* * *
**Total release size:** 101.6 kB 
##  [Release files](https://pypi.org/project/PyMatting/#files) / pymatting-1.1.16.tar.gz   
| Download URL  |  [ pymatting-1.1.16.tar.gz ](https://files.pythonhosted.org/packages/75/4b/01a653f1ec2a69b1579d9ff47578b41bc432216f1a2b6e57cf37f725a95b/pymatting-1.1.16.tar.gz)  |  
| --- | --- |  
| Size  | 45.3 kB  |  
| Tags  |  Source  |  
|  SHA-256 checksum   
[How to use checksums](https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode "External link")  |  `             656e16f07c941b8792c8cd341b49791e74d1949ceae4d8c45fb4e10d3c6e7d77                            __                        `  |  
|  BLAKE2b-256 checksum   
[How to use checksums](https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode "External link")  |  `             754b01a653f1ec2a69b1579d9ff47578b41bc432216f1a2b6e57cf37f725a95b                            __                        `  |  
| Upload date  | Sep 8, 2026  |  
|  Uploaded using Trusted Publishing?   
[What is trusted publishing?](https://docs.pypi.org/trusted-publishers/)  |  No   |  
| Uploaded via  |  `twine/7.0.0 CPython/3.12.3`  |  
##  [Release files](https://pypi.org/project/PyMatting/#files) / pymatting-1.1.16-py3-none-any.whl   
| Download URL  |  [ pymatting-1.1.16-py3-none-any.whl ](https://files.pythonhosted.org/packages/47/8e/2c00f3615fc906c01f5168d2caedf61811db6259b8d0c9a1b14d7c9af61a/pymatting-1.1.16-py3-none-any.whl)  |  
| --- | --- |  
| Size  | 56.3 kB  |  
| Tags  |  Python 3  |  
|  SHA-256 checksum   
[How to use checksums](https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode "External link")  |  `             6ad3f787f90d7720b60e9734c33588cb30f98a66abf7bd772fa499d3a32b466a                            __                        `  |  
|  BLAKE2b-256 checksum   
[How to use checksums](https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode "External link")  |  `             478e2c00f3615fc906c01f5168d2caedf61811db6259b8d0c9a1b14d7c9af61a                            __                        `  |  
| Upload date  | Sep 8, 2026  |  
|  Uploaded using Trusted Publishing?   
[What is trusted publishing?](https://docs.pypi.org/trusted-publishers/)  |  No   |  
| Uploaded via  |  `twine/7.0.0 CPython/3.12.3`  |  
## Security for PyMatting 1.1.16
[Report project as malware](https://pypi.org/project/PyMatting/submit-malware-report/)
### Provenance
**Provenance** describes where a file came from. On PyPI, provenance is shared via **attestations** , which provide a verifiable record of the build or publishing details. [View details, limitations and caveats.](https://docs.pypi.org/using-pypi/package-security/provenance/)
###  No provenance found 
None of the files in this release were uploaded with provenance metadata.
### A note on package security
PyPI is a repository for distributing packages, not a service for auditing them. While third-party security researchers and our staff do their best to detect and remove malicious packages, PyPI cannot guarantee the quality, security or suitability of any given package. 
To learn more about protecting yourself from malicious actors, visit our [package security documentation](https://docs.pypi.org/using-pypi/package-security/introduction/). 
##  Release history [Release notifications](https://docs.pypi.org/api/feeds/#project-releases-feed) | [RSS feed ](https://pypi.org/rss/project/pymatting/releases.xml)
This release
![](https://pypi.org/static/images/blue-cube.572a5bfb.svg)
[1.1.16](https://pypi.org/project/PyMatting/1.1.16/) This release
Sep 8, 2026 [2 release files](https://pypi.org/project/PyMatting/1.1.16/#files) [ No provenance ](https://pypi.org/project/PyMatting/1.1.16/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[1.1.15](https://pypi.org/project/PyMatting/1.1.15/)
Jan 26, 2026 [2 release files](https://pypi.org/project/PyMatting/1.1.15/#files) [ No provenance ](https://pypi.org/project/PyMatting/1.1.15/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[1.1.14](https://pypi.org/project/PyMatting/1.1.14/)
May 16, 2025 [2 release files](https://pypi.org/project/PyMatting/1.1.14/#files) [ No provenance ](https://pypi.org/project/PyMatting/1.1.14/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[1.1.13](https://pypi.org/project/PyMatting/1.1.13/)
Nov 13, 2024 [2 release files](https://pypi.org/project/PyMatting/1.1.13/#files) [ No provenance ](https://pypi.org/project/PyMatting/1.1.13/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[1.1.12](https://pypi.org/project/PyMatting/1.1.12/)
Nov 30, 2023 [2 release files](https://pypi.org/project/PyMatting/1.1.12/#files) [ No provenance ](https://pypi.org/project/PyMatting/1.1.12/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[1.1.11](https://pypi.org/project/PyMatting/1.1.11/)
Nov 8, 2023 [2 release files](https://pypi.org/project/PyMatting/1.1.11/#files) [ No provenance ](https://pypi.org/project/PyMatting/1.1.11/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[1.1.10](https://pypi.org/project/PyMatting/1.1.10/)
Oct 5, 2023 [2 release files](https://pypi.org/project/PyMatting/1.1.10/#files) [ No provenance ](https://pypi.org/project/PyMatting/1.1.10/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[1.1.8](https://pypi.org/project/PyMatting/1.1.8/)
Jun 28, 2022 [2 release files](https://pypi.org/project/PyMatting/1.1.8/#files) [ No provenance ](https://pypi.org/project/PyMatting/1.1.8/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[1.1.7](https://pypi.org/project/PyMatting/1.1.7/)
Jun 9, 2022 [2 release files](https://pypi.org/project/PyMatting/1.1.7/#files) [ No provenance ](https://pypi.org/project/PyMatting/1.1.7/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[1.1.5](https://pypi.org/project/PyMatting/1.1.5/)
Jan 4, 2022 [2 release files](https://pypi.org/project/PyMatting/1.1.5/#files) [ No provenance ](https://pypi.org/project/PyMatting/1.1.5/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[1.1.4](https://pypi.org/project/PyMatting/1.1.4/)
Oct 29, 2021 [2 release files](https://pypi.org/project/PyMatting/1.1.4/#files) [ No provenance ](https://pypi.org/project/PyMatting/1.1.4/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[1.1.3](https://pypi.org/project/PyMatting/1.1.3/)
May 4, 2021 [2 release files](https://pypi.org/project/PyMatting/1.1.3/#files) [ No provenance ](https://pypi.org/project/PyMatting/1.1.3/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[1.1.2](https://pypi.org/project/PyMatting/1.1.2/)
Dec 11, 2020 [2 release files](https://pypi.org/project/PyMatting/1.1.2/#files) [ No provenance ](https://pypi.org/project/PyMatting/1.1.2/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[1.1.1](https://pypi.org/project/PyMatting/1.1.1/)
Oct 29, 2020 [2 release files](https://pypi.org/project/PyMatting/1.1.1/#files) [ No provenance ](https://pypi.org/project/PyMatting/1.1.1/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[1.0.7](https://pypi.org/project/PyMatting/1.0.7/)
Oct 16, 2020 [2 release files](https://pypi.org/project/PyMatting/1.0.7/#files) [ No provenance ](https://pypi.org/project/PyMatting/1.0.7/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[1.0.6](https://pypi.org/project/PyMatting/1.0.6/)
Mar 6, 2020 [2 release files](https://pypi.org/project/PyMatting/1.0.6/#files) [ No provenance ](https://pypi.org/project/PyMatting/1.0.6/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[1.0.5](https://pypi.org/project/PyMatting/1.0.5/)
Feb 17, 2020 [2 release files](https://pypi.org/project/PyMatting/1.0.5/#files) [ No provenance ](https://pypi.org/project/PyMatting/1.0.5/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[1.0.2](https://pypi.org/project/PyMatting/1.0.2/)
Feb 7, 2020 [2 release files](https://pypi.org/project/PyMatting/1.0.2/#files) [ No provenance ](https://pypi.org/project/PyMatting/1.0.2/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[1.0.1](https://pypi.org/project/PyMatting/1.0.1/)
Feb 7, 2020 [2 release files](https://pypi.org/project/PyMatting/1.0.1/#files) [ No provenance ](https://pypi.org/project/PyMatting/1.0.1/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[1.0.0](https://pypi.org/project/PyMatting/1.0.0/)
Jan 29, 2020 [2 release files](https://pypi.org/project/PyMatting/1.0.0/#files) [ No provenance ](https://pypi.org/project/PyMatting/1.0.0/#security)
[ ![](https://pypi.org/static/images/white-cube.2351a86c.svg) PyPI ](https://pypi.org/)
Developed and maintained by the [Python Software Foundation](https://www.python.org/psf/ "External link") and Python community, for the Python community.
[Status: all systems operational](https://status.python.org/ "External link")
[Donate today!](https://donate.pypi.org)
## Help
  * [PyPI documentation](https://docs.pypi.org/)
  * [Getting help](https://docs.pypi.org/about/getting-help/)
  * [Installing packages](https://packaging.python.org/tutorials/installing-packages/ "External link")
  * [Uploading packages](https://packaging.python.org/tutorials/packaging-projects/ "External link")
  * [Packaging user guide](https://packaging.python.org/ "External link")


## About PyPI
  * [PyPI blog](https://blog.pypi.org)
  * [Infrastructure dashboard](https://dtdg.co/pypi "External link")
  * [Statistics](https://pypi.org/stats/)
  * [Logos & trademarks](https://pypi.org/trademarks/)
  * [Our sponsors](https://pypi.org/sponsors/)


## Contributing to PyPI
  * [Bugs and feedback](https://docs.pypi.org/about/contributing/#reporting-bugs)
  * [Contribute on GitHub](https://github.com/pypi/warehouse "External link")
  * [Translate PyPI](https://hosted.weblate.org/projects/pypa/warehouse/ "External link")
  * [Sponsor PyPI](https://pypi.org/sponsors/)
  * [Development credits](https://github.com/pypi/warehouse/graphs/contributors "External link")


## Using PyPI
  * [Terms of Service](https://policies.python.org/pypi.org/Terms-of-Service/ "External link")
  * [Report security issue](https://pypi.org/security/)
  * [Code of conduct](https://policies.python.org/python.org/code-of-conduct/ "External link")
  * [Privacy Notice](https://policies.python.org/pypi.org/Privacy-Notice/ "External link")
  * [Acceptable Use Policy](https://policies.python.org/pypi.org/Acceptable-Use-Policy/ "External link")


Switch to desktop version
[ ![](https://pypi-camo.freetls.fastly.net/0e16ff2846ab7bc04f1e52d760b072c987232f52/68747470733a2f2f73332e6475616c737461636b2e75732d656173742d322e616d617a6f6e6177732e636f6d2f707974686f6e646f746f72672d6173736574732f6d656469612f73706f6e736f725f7765625f6c6f676f732f416e7468726f7069635f6c6f676f5f2d5f536c6174652e706e67) Anthropic, PBC Visionary sponsor ](https://www.anthropic.com/) [ ![](https://pypi-camo.freetls.fastly.net/2056e7cc45e271b6b509980e9ff24b8b6346f2f4/68747470733a2f2f73332e6475616c737461636b2e75732d656173742d322e616d617a6f6e6177732e636f6d2f707974686f6e646f746f72672d6173736574732f6d656469612f73706f6e736f725f7765625f6c6f676f732f626c6f6f6d626572672e706e67) Bloomberg Visionary sponsor ](https://www.techatbloomberg.com/) [ ![](https://pypi-camo.freetls.fastly.net/7e24ecafc35532bbd56c7c91521ea6701110c742/68747470733a2f2f73332e6475616c737461636b2e75732d656173742d322e616d617a6f6e6177732e636f6d2f707974686f6e646f746f72672d6173736574732f6d656469612f73706f6e736f725f7765625f6c6f676f732f6872742e706e67) Hudson River Trading Visionary sponsor ](https://www.hudsonrivertrading.com/careers/) [ ![](https://pypi-camo.freetls.fastly.net/6f7cbf25b7d9ee146661528e012e8fa51d6f3337/68747470733a2f2f73332e6475616c737461636b2e75732d656173742d322e616d617a6f6e6177732e636f6d2f707974686f6e646f746f72672d6173736574732f6d656469612f73706f6e736f725f7765625f6c6f676f732f4d6574615f6c6f636b75705f706f7369746976655f7072696d6172795f5247425f636f70795f68546b493532472e706e67) Meta Visionary sponsor ](https://about.facebook.com/meta/) [ ![](https://pypi-camo.freetls.fastly.net/22baa32a7b36b109ce052634015d878f5d029280/68747470733a2f2f73332e6475616c737461636b2e75732d656173742d322e616d617a6f6e6177732e636f6d2f707974686f6e646f746f72672d6173736574732f6d656469612f73706f6e736f725f7765625f6c6f676f732f6e76696469612e706e67) NVIDIA Visionary sponsor ](https://developer.nvidia.com) [ ![](https://pypi-camo.freetls.fastly.net/34ebcaca9a4316e862f2f7641b12534f0cb81bf1/68747470733a2f2f73332e6475616c737461636b2e75732d656173742d322e616d617a6f6e6177732e636f6d2f707974686f6e646f746f72672d6173736574732f6d656469612f73706f6e736f725f7765625f6c6f676f732f6d6963726f736f66742e706e67) Microsoft Sustainability sponsor ](https://aka.ms/python) [ ![](https://pypi-camo.freetls.fastly.net/237c8773674b9f8beff9f894a07424e3b579cd6a/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f6465706f742d636f6c6f722d6c6f676f2d35567a75416e7a6b2e706e67) Depot Continuous Integration ](https://depot.dev) [ ![](https://pypi-camo.freetls.fastly.net/f0e9bd2edb2aa1c533d61b0d4fda0ee761bef88a/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f6177732d636f6c6f722d6c6f676f2d416c6f43525230612e706e67) AWS Cloud computing and Security Sponsor ](https://aws.amazon.com/) [ ![](https://pypi-camo.freetls.fastly.net/530379bec76c3440bd94a24092f49e27323ad0d7/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f64617461646f672d636f6c6f722d6c6f676f2d71616563774a67722e706e67) Datadog Monitoring ](https://www.datadoghq.com/) [ ![](https://pypi-camo.freetls.fastly.net/9706778018adad6f5bf682f55d7bbc226abe551c/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f666173746c792d636f6c6f722d6c6f676f2d766c6d424c33654c2e706e67) Fastly CDN ](https://www.fastly.com/) [ ![](https://pypi-camo.freetls.fastly.net/522342e78db3080c18697369dde99a0ed7925e86/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f676f6f676c652d636f6c6f722d6c6f676f2d32755437496c54702e706e67) Google Download Analytics ](https://careers.google.com/) [ ![](https://pypi-camo.freetls.fastly.net/f2a422796f8e4d51d60d7030b7973aa1651bd096/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f73656e7472792d636f6c6f722d6c6f676f2d346e306a654878502e706e67) Sentry Error logging ](https://sentry.io/for/python/?utm_source=pypi&utm_medium=paid-community&utm_campaign=python-na-evergreen&utm_content=static-ad-pypi-sponsor-learnmore) [ ![](https://pypi-camo.freetls.fastly.net/b0ba0741ac65afcb01ebb4bbf0634c54b8a15827/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f737461747573706167652d636f6c6f722d6c6f676f2d423232436b746e6b2e706e67) StatusPage Status page ](https://statuspage.io)
  * "PyPI", "Python Package Index", and the blocks logos are registered [trademarks](https://pypi.org/trademarks/) of the [Python Software Foundation](https://www.python.org/psf-landing).
  * © 2026 [Python Software Foundation](https://www.python.org/psf-landing/ "External link")
  * [Site map](https://pypi.org/sitemap/)
  * Deployed from [`68dc61b`](https://github.com/pypi/warehouse/commit/68dc61bfbf31633506f3f03c3a93b34220857cfc "External link")



