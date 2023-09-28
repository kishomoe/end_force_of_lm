# end_force_of_lm

### Reference

[1] 彭兵,张囡,夏加宽等.**永磁直线电机端部效应力的解析计算**[J].*中国电机工程学报*,2016,36(02):547-553.[DOI:10.13334/j.0258-8013.pcsee.2016.02.028](http://ntps.epri.sgcc.com.cn/djgcxb/CN/10.13334/j.0258-8013.pcsee.2016.02.028).

$$
F_{DF}=F_{end}+F_{slot}
$$

Detent force of linear motor (LM) is composed of end force ($F_{end}$) and cogging force ($F_{slot}$) . Detent force is easily to be obtained by finite element method (FEM) . End force can be calculated by subtracting cogging force from detent force. So,  end force can be obtained using slotless model.

## 1. Slotless model ($F_{DF}$)

![Untitled.png](https://s2.loli.net/2023/09/28/lS8IznB7epiGcWR.png)

FEM result of detent force is as follows,

![Untitled _1_.png](https://s2.loli.net/2023/09/28/PL9KUgrwX2kjZfS.png)

## 2. Infinitely long right end ($F_l$)

![Untitled _2_.png](https://s2.loli.net/2023/09/28/g7uF8stTecShoKz.png)

FEM result of left end force is as follows,

![Untitled _3_.png](https://s2.loli.net/2023/09/28/z8FsNdqekRW7c4j.png)

## 3. Infinitely long left end ($F_r$)

![Untitled _4_.png](https://s2.loli.net/2023/09/28/jmu6MwaD4UqZOFN.png)

FEM result of right end force is as follows,

![Untitled _5_.png](https://s2.loli.net/2023/09/28/m1sbiSuMv5aPCc7.png)

## 4. force synthesis

Combine $F_l$ and $F_r$ into $F_{l+r}$ , and compare with $F_{DF}$ .

![Figure_1.png](https://s2.loli.net/2023/09/28/L8UmKyvgV3JheY2.png)

