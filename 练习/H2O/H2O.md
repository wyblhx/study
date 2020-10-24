## H2O的计算
```flow
op=>operation: cp2k和deepmd的联和使用-H2O
sub1=>subroutine: cp2k计算水分子的能量和力
sub2=>subroutine: deepdata处理数据
sub3=>subroutine: deepmd-kit训练数据
e=>end: 结束
op->sub1->sub2->sub3
```

## 一、cp2k计算水分子的能量和力

### 流程图

![H2O的能量和力的计算.jpg](http://ww1.sinaimg.cn/large/007nrJjbgy1gjzkuny8mkj3169135q77.jpg)

### 注意：
FORCE_EVAL模块的书写顺序一定要按下图所示，否则使用dpddata数据时会报错，AssertionError: cannot find coords
![QQ图片20201024200458.png](http://ww1.sinaimg.cn/large/007nrJjbgy1gk0qwo5da9j30g80azmzj.jpg)

### 水分子模型
![water.png](http://ww1.sinaimg.cn/large/007nrJjbgy1gjzlwronzuj310c0jct91.jpg)
### 代码

```
#用来设置项目名称(PROJECT_NAME)，计算类型打印级别(PRINT_LEVEL)等，其中&RUN_TYPE用来设置整个计算的类型（包括静态计算，几何优化到MD, MC等20多种计算）
&GLOBAL
 PROJECT water #项目文件名称
 RUN_TYPE ENERGY_FORCE #任务类型:计算能量和力
 PRINT_LEVEL LOW
&END GLOBAL


#用于设置计算能量的理论，即QM, MM，还是QM/MM，关键词METHOD下面可以设置理论模型
&FORCE_EVAL

	METHOD  Quickstep #计算方式,别名为QS

  &DFT
      #基础集文件名
      BASIS_SET_FILE_NAME  EMSL_BASIS_SETS
      #赝势文件名
      POTENTIAL_FILE_NAME  POTENTIAL

      #设置Quickstep所需要的参数
      &QS
        METHOD GAPW #计算电子结构采用的方法
        EPS_DEFAULT 1.0E-10 #能量校正参数
      &END QS

      #泊松方程
      &POISSON
        PERIODIC NONE #是否应用周期性边界、或者是将周期性边界条件应用的方向
        POISSON_SOLVER MT #求解泊松方程的方式
      &END

      #自洽场（SCF）
      &SCF
        EPS_SCF 1.0E-6 #收敛精度
        SCF_GUESS ATOMIC #Change the initial guess for the wavefunction
        MAX_SCF 10 #SCF优化迭代的最大次数
      &END SCF

      #网格信息-multigrid information
      &MGRID
        CUTOFF 250
        REL_CUTOFF 50
      &END MGRID

      #Parameters needed for the calculation of the eXchange and Correlation potential
      &XC
        &XC_FUNCTIONAL PBE
          #PBE质子条件式,又称质子平衡方程，用PBE表示
          &PBE
            SCALE_X 0.75
            SCALE_C 1.0
          &END PBE
        &END XC_FUNCTIONAL

        #哈特里—福克方程,又称为HF方程，是一个应用变分法计算多电子体系波内函数的方程
        &HF
          &SCREENING
            EPS_SCHWARZ 1.0E-10
          &END SCREENING
          &MEMORY
            MAX_MEMORY  5
          &END MEMORY
          FRACTION 0.25  #Hartree-Fock占总能量的比例
        &END HF

      &END XC

  &END DFT

	&SUBSYS

		#设定盒子大小
		&CELL
      ABC 6.0 6.0 6.0
      PERIODIC NONE #设定边界条件，是否为周期性边界
		&END CELL

		#读取坐标文件
		&TOPOLOGY
   		COORD_FILE_FORMAT xyz
   		COORD_FILE_NAME water.xyz
		&END TOPOLOGY

		#定义元素 H O
   	&KIND H
    	BASIS_SET  6-31Gxx #基础集
    	POTENTIAL  ALL #赝势
   	&END KIND
   	&KIND O
    	BASIS_SET  6-31Gxx
    	POTENTIAL  ALL
   	&END KIND

	&END SUBSYS

	#输出
	&PRINT
    &FORCES ON
    &END FORCES
  &END PRINT

&END FORCE_EVAL
```

### dpdata处理数据

**相关代码**

```python
# 导入相关模块
import dpdata

cp2k_output = dpdata.LabeledSystem('water.out', fmt = 'cp2k/output')

#打印相关信息
print(cp2k_output['atom_names'])
print(cp2k_output['atom_numbs'])
print(cp2k_output['atom_types'])
print(cp2k_output['cells'])
print(cp2k_output['coords'])
print(cp2k_output['energies'])
print(cp2k_output['forces'])

# no virial
cp2k_output.to_deepmd_raw('dpmd_raw')
cp2k_output.to_deepmd_npy('dpmd_npy')
```

**运行后结果**
![QQ图片20201024204839.png](http://ww1.sinaimg.cn/mw690/007nrJjbgy1gk0rpqfljaj30hh09m0tt.jpg)
