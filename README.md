# LAMI

## Overview
The folders are divided into the following three:
- `./src` contains two executable files for LAMI
    - `./src/LAMI_Y.exe` for Y channel inputs.
    - `./src/LAMI_G.exe` for grayscale inputs.
- `./weights` contains all the interpolated weights you need to run the executable files. **(Do **NOT** modify its content or path!!! It would cause abnormal performance.)**
- `./img` contains datasets, current processed input images, and outputs (results).
    - `./img/datasets` includes 3 datasets with 8 different manification ratios.
        - `Set14_Y` has 12 Y channel images in each ratios.
        - `Set14_G` has 2 grayscale images in each ratios.
        - `B100` has 100 Y channel images in each ratios.
    - `./img/input` is where you only need to modified. By selecting specific datasets and magnification ratios from `./img/datasets/`, you can simply overwrite the `./img/input/HR` and `./img/input/LR`.
        - `HR` contains high resolution golden images.
        - `LR` contains low resolution input images.
    - `./img/output` contains corresponding results.

## Environment
- C++ >= 17
- OpenCV C++ == 4.3.0
  
## How To Test
1. Choose the desired magnification ratios and dataset path from `./img/datasets/`. (Take `./img/datasets/Set14_Y/2X/` for example.)
2. Overwrite all the folders under `./img/input` with `./{the selected path}/HR` and `./{the selected path}/LR`.
3. Run the executable file in `./src`. **(If you are using Set14_G for input, run `./src/LAMI_G.exe`. Otherwise, run `./src/LAMI_Y.exe`)**
4. The average runtime and PSNR per image will be displayed on the terminal and the testing results will be saved in the `./img/output`.
