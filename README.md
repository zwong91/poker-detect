
**您可以在教育和研究环境中使用本软件。**

**您可以制作本软件的副本，前提是副本仅用于教育和研究目的**

**您可以修改本软件的源代码，前提是修改后的版本也仅用于教育和研究目的，并且您在分发修改后的版本时遵守本许可证的条款。**

**禁止商业用途：** 您不得将本软件用于任何商业或营利性目的。

**责任限制：** 对于因使用本软件而造成的任何直接、间接、偶然、特殊或后果性损害，许可方不承担任何责任，即使许可方已被告知此类损害的可能性。

**非法使用：** 您不得将本软件用于任何非法目的。如果发生此类使用，许可方不承担任何责任。

| Suit      | 中文名称 | 简写 |
|-----------|----------|------|
| Clubs     | 梅花     | c    |
| Diamonds  | 方块     | d    |
| Hearts    | 红桃     | h    |
| Spades    | 黑桃     | s    |

| cls | poker       | 简写 |
|-----|-------------|------|
| 0   | T(10)梅花   | Tc   |
| 1   | T(10)方块   | Td   |
| 2   | T(10)红桃   | Th   |
| 3   | T(10)黑桃   | Ts   |
| 4   | 2梅花       | 2c   |
| 5   | 2方块       | 2d   |
| 6   | 2红桃       | 2h   |
| 7   | 2黑桃       | 2s   |
| 8   | 3梅花       | 3c   |
| 9   | 3方块       | 3d   |
| 10  | 3红桃       | 3h   |
| 11  | 3黑桃       | 3s   |
| 12  | 4梅花       | 4c   |
| 13  | 4方块       | 4d   |
| 14  | 4红桃       | 4h   |
| 15  | 4黑桃       | 4s   |
| 16  | 5梅花       | 5c   |
| 17  | 5方块       | 5d   |
| 18  | 5红桃       | 5h   |
| 19  | 5黑桃       | 5s   |
| 21  | 6方块       | 6d   |
| 22  | 6红桃       | 6h   |
| 23  | 6黑桃       | 6s   |
| 24  | 7梅花       | 7c   |
| 25  | 7方块       | 7d   |
| 26  | 7红桃       | 7h   |
| 27  | 7黑桃       | 7s   |
| 28  | 8梅花       | 8c   |
| 29  | 8方块       | 8d   |
| 30  | 8红桃       | 8h   |
| 31  | 8黑桃       | 8s   |
| 32  | 9梅花       | 9c   |
| 33  | 9方块       | 9d   |
| 34  | 9红桃       | 9h   |
| 35  | 9黑桃       | 9s   |
| 36  | A梅花       | Ac   |
| 37  | A方块       | Ad   |
| 38  | A红桃       | Ah   |
| 39  | A黑桃       | As   |
| 40  | J梅花       | Jc   |
| 41  | J方块       | Jd   |
| 42  | J红桃       | Jh   |
| 43  | J黑桃       | Js   |
| 44  | K梅花       | Kc   |
| 45  | K方块       | Kd   |
| 46  | K红桃       | Kh   |
| 47  | K黑桃       | Ks   |
| 48  | Q梅花       | Qc   |
| 49  | Q方块       | Qd   |
| 50  | Q红桃       | Qh   |
| 51  | Q黑桃       | Qs   |
| 52  | 小王        | SJoker |
| 53  | 大王        | BJoker |

# 数据集在 datasets 目录下的文件夹路径

path: poker.yolo

# 训练集、验证集、测试集相对于 path 的路径（一般不用区分验证集和测试集，统称测试集）

train: train/images
val: val/images
test: test/images

# Default batch_size

batch_size: 16

# 类别信息

nc: 54  # 类别的数量
names:  # 类别的名称列表

- 'Tc'
- 'Td'
- 'Th'
- 'Ts'
- '2c'
- '2d'
- '2h'
- '2s'
- '3c'
- '3d'
- '3h'
- '3s'
- '4c'
- '4d'
- '4h'
- '4s'
- '5c'
- '5d'
- '5h'
- '5s'
- '6c'
- '6d'
- '6h'
- '6s'
- '7c'
- '7d'
- '7h'
- '7s'
- '8c'
- '8d'
- '8h'
- '8s'
- '9c'
- '9d'
- '9h'
- '9s'
- 'Ac'
- 'Ad'
- 'Ah'
- 'As'
- 'Jc'
- 'Jd'
- 'Jh'
- 'Js'
- 'Kc'
- 'Kd'
- 'Kh'
- 'Ks'
- 'Qc'
- 'Qd'
- 'Qh'
- 'Qs'
- 'SJoker'
- 'BJoker'

Install the Git Large File Storage (git-lfs)

```sh
sudo apt-get install git-lfs
git-lfs install
```

To convert any pre-existing files to Git LFS, such as files on other branches or in your prior commit history us the git lfs migrate command

```sh
git lfs migrate import --include="*.wandb"
```

Select the file types to be tracked

```sh
git lfs track "*.wandb"
```

update the gitattributes

```sh
git add .gitattributes
```

Now push to the git commit -m "commit message" git push

```sh
git lfs pull
```
