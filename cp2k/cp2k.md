
## cp2k教程

### cp2k提交命令
**cp2k.popt -i file.inp -o file.out**

### 一、输入文件介绍

**Ⅰ** input文件: 主要输入文件,定义系统和作业参数,BASIS_SET、GTH_POTENTIALS可在 cp2k/data中找到，涵盖大多数常用元素。用户需要为给定的计算生成自己的主输入文件

**Ⅱ** 基础集文件及赝势文件

**Ⅲ** 拓扑结构文件（xyz、cif）

### input文件框架

![DMH2.png](http://ww1.sinaimg.cn/mw690/007nrJjbly1gk1xam0w4yj30my0ait96.jpg)

  **8个Primary section：**

  **Ⅰ** GLOBAL： 用来设置项目名称(PROJECT_NAME)，计算类型打印级别(PRINT_LEVEL)等，其中&RUN_TYPE用来设置整个计算的类型（包括静态计算，几何优化到MD, MC等20多种计算）  

  **Ⅱ**  &FORCE_EVAL 用于设置计算能量的理论，即QM, MM，还是QM/MM，关键词METHOD下面可以设置理论模型；对于选定的模型，下面分别设有&EIP, &EP，&DFT等相应的subsection用于设置相应的参数，模拟体系（cell尺寸，原子坐标，分子top等 ）在&FORCE_EVAL / SUBSYS中设置  

  **Ⅲ**  &MOTION 设置与几何优化(&GEO_OPT)和晶胞优化(&CELL_OPT)相关的原子移动的的参数，如优化算法，收敛标准， MD算法，MC算法，以及NEB搜索鞍点，过渡态等  

  **Ⅳ** &VIBRATIONAL_ANALYSIS 用于设置进行正则模式分析的振动计算参数，如Hessian矩阵的收敛，Intensity的计算等等  

  **Ⅴ** &MULTIPLE_FORCE_EVAL  处理多个FORCE_EVALs  

  **Ⅵ**  &EXT_RESTART  从外部文件开始继续进行指定理论和任务的计算  

  **Ⅶ**  &FARMING  在&JOB%&DIRECTORY和&INPUT_FILE_NAME中包含多个输入文件，进行批量计算  

  **Ⅷ**  &DEBUG和&TEST  用于设置测试任务的参数

**1) GLOBAL**
```
&GLOBAL
   PROJECT 项目名称
   RUN_TYPE 任务类型
   PRINT_LEVEL 输出级别控制
&END GLOBAL
```
**2) FORCE_EVAL**
```
& FORCE_EVAL
  METHOD Quickstep
  &DFT 核心部分
    BASIS_SET_FILE_NAME 基础集文件
    POTENTIAL_FILE_NAME 赝势文件，可在cp2k/data中获取
    &MGRID
      CUTOFF  CUTOFF越大，越有效描述波函数信息，CUTOFF值取决于体系中元素种类
      NGRIDS  使用的多重网格数
      REL_CUTOFF  默认值是40Ry,设置为60Ry精度就足够了
    &END MGRID
    &QS 设置Quickstep框架所需的参数
    &END QS
    &SCF 定义scf自洽过程的相关参数
      EPS_SCF 精度
      SCF_GUESS
      MAX_SCF 最大迭代次数
    &END SCF
    &XC  计算交换关联项所需的参数，解薛定谔方程时，有些能量是可以具体算出，但是有些能量是通过近似算出，对于不能得到准确的结果就归类于交换关联项中
    &END XC
  &END DFT
  &SUBSYS  子系统：坐标，拓扑结构，分子和晶胞
    &CELL
    &END CELL
    &COORD
    &END COORD
    &KIND 元素信息，包括基础文件和赝势文件
    &END KIND
  &END SUBSYS
&END  FORCE_EVAL
```
### 输出文件分析
