## cp2k提交命令
**cp2k.popt -i file.inp -o file.out**
## cp2k教程
### 一、输入文件介绍
*输入文件 ：inp文件、BASIS_SET、GTH_POTENTIALS*

**Ⅰ** inp文件: 主要输入文件,定义系统和作业参数,BASIS_SET、GTH_POTENTIALS可在 cp2k/data中找到，涵盖大多数常用元素。用户需要为给定的计算生成自己的主输入文件

**Ⅱ** BASIS_SET:包含可用于此计算的基础集的参数的文件CP2K

**Ⅲ** GTH_POTENTIALS:包含可用于此计算的伪可能参数的文件CP2K

#### 1、inp文件
**一般inp文件是使用以下方式书写的：**

**&SECTION**  

KEYWORDS PARAMETER  

***&SUBSECTION***  

KEYWORDS PARAMETER  

***&END SUBSECTION***  

  **&END SECTION**


  **cp2k输入文件的8个Primary section：**

  **Ⅰ** GLOBAL： 用来设置项目名称(PROJECT_NAME)，计算类型打印级别(PRINT_LEVEL)等，其中&RUN_TYPE用来设置整个计算的类型（包括静态计算，几何优化到MD, MC等20多种计算）  

  **Ⅱ**  &FORCE_EVAL 用于设置计算能量的理论，即QM, MM，还是QM/MM，关键词METHOD下面可以设置理论模型；对于选定的模型，下面分别设有&EIP, &EP，&DFT等相应的subsection用于设置相应的参数，模拟体系（cell尺寸，原子坐标，分子top等 ）在&FORCE_EVAL / SUBSYS中设置  

  **Ⅲ**  &MOTION 设置与几何优化(&GEO_OPT)和晶胞优化(&CELL_OPT)相关的原子移动的的参数，如优化算法，收敛标准， MD算法，MC算法，以及NEB搜索鞍点，过渡态等  

  **Ⅳ** &VIBRATIONAL_ANALYSIS 用于设置进行正则模式分析的振动计算参数，如Hessian矩阵的收敛，Intensity的计算等等  

  **Ⅴ** &MULTIPLE_FORCE_EVAL  处理多个FORCE_EVALs  

  **Ⅵ**  &EXT_RESTART  从外部文件开始继续进行指定理论和任务的计算  

  **Ⅶ**  &FARMING  在&JOB%&DIRECTORY和&INPUT_FILE_NAME中包含多个输入文件，进行批量计算  

  **Ⅷ**  &DEBUG和&TEST  用于设置测试任务的参数

#### 2、例子([如何计算能量和力](https://www.cp2k.org/howto:static_calculation))
&GLOBAL
  PROJECT Si_bulk8 #定义项目名称
  RUN_TYPE ENERGY_FORCE #Type of run that you want to perform Geometry optimization
  PRINT_LEVEL LOW
&END GLOBAL

**注：**
1. PROJECT：inp文件名称
2. RUN_TYPE：cp2k做那种计算，包括MC:蒙特卡洛，MD:分子动力学模拟，ENERGY_FORCE：静态能量和力计算
3. PRINT_LEVEL：计算类型打印级别，也就是输出文件的详细程度

<br/>

&FORCE_EVAL

  METHOD Quickstep

  &SUBSYS

    &KIND Si

      ELEMENT   Si

      BASIS_SET DZVP-GTH-PADE

      POTENTIAL GTH-PADE-q4  

    &END KIND

    &CELL

      A     5.430697500    0.000000000    0.000000000

      B     0.000000000    5.430697500    0.000000000

      C     0.000000000    0.000000000    5.430697500  

    &END CELL

    &COORD

      Si    0.000000000    0.000000000    0.000000000

      Si    0.000000000    2.715348700    2.715348700

      Si    2.715348700    2.715348700    0.000000000

      Si    2.715348700    0.000000000    2.715348700

      Si    4.073023100    1.357674400    4.073023100

      Si    1.357674400    1.357674400    1.357674400

      Si    1.357674400    4.073023100    4.073023100

      Si    4.073023100    4.073023100    1.357674400

    &END COORD

  &END SUBSYS

  &DFT

    BASIS_SET_FILE_NAME  BASIS_SET

    POTENTIAL_FILE_NAME  GTH_POTENTIALS

    &QS

      EPS_DEFAULT 1.0E-10

    &END QS

    &MGRID

      NGRIDS 4

      CUTOFF 300

      REL_CUTOFF 60

    &END MGRID

    &XC

      &XC_FUNCTIONAL PADE

      &END XC_FUNCTIONAL

    &END XC

    &SCF

      SCF_GUESS ATOMIC

      EPS_SCF 1.0E-7

      MAX_SCF 300

      &DIAGONALIZATION  ON

        ALGORITHM STANDARD

      &END DIAGONALIZATION

      &MIXING  T

        METHOD BROYDEN_MIXING

        ALPHA 0.4

        NBROYDEN 8

      &END MIXING

    &END SCF

  &END DFT

  &PRINT

    &FORCES ON

    &END FORCES

  &END PRINT

&END FORCE_EVAL

**注：**
1. METHOD：评估原子上的力的方法，QUICKSTEP：Electronic structure methods (DFT, ...)，FIST：Molecular Mechanics，QMMM：Hybrid quantum classical
2. SUBSYS：coordinates, topology, molecules and cell,定义计算中的模拟单元单元和原子的初始坐标，采用的坐标是笛卡尔坐标
- KIND:description of the kind of the atoms 定义元素， ELEMENT ：原子种类
- CELL:定义计算中使用的模拟单元单元格,单位是A，
- COORD：定义原子坐标 格式为<ATOM_KIND> X Y Z
3. DFT：self-consistent Kohn-Sham Density Functional Theory calculation
- BASIS_SET_FILE_NAME 、POTENTIAL_FILE_NAME：设置参数文件
- QS:控制参数，EPS_DEFAULT：设置容差
- MGRID：定义在计算中使用的集成网格应如何设置
- XC：定义了我们要使用的交换相关密度函数
